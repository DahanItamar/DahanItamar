import { writeFile, mkdir } from 'node:fs/promises';
import { pathToFileURL } from 'node:url';

export function render(calendar, dark = false) {
  const days = calendar.weeks.flatMap((week, col) => week.contributionDays.map(day => ({ ...day, col })));
  if (!days.length || days.some(d => !/^\d{4}-\d{2}-\d{2}$/.test(d.date) || !Number.isInteger(d.contributionCount) || d.contributionCount < 0)) throw new Error('Invalid contribution calendar');
  const total = days.reduce((sum, d) => sum + d.contributionCount, 0);
  const active = days.filter(d => d.contributionCount > 0).length;
  const peak = Math.max(...days.map(d => d.contributionCount));
  const bg = dark ? '#0d1117' : '#ffffff', ink = dark ? '#f0f6fc' : '#1f2328', muted = dark ? '#9198a1' : '#59636e';
  const palette = dark ? ['#161b22','#0e4429','#006d32','#26a641','#39d353'] : ['#ebedf0','#c6e48b','#7bc96f','#239a3b','#196127'];
  const levels = ['NONE','FIRST_QUARTILE','SECOND_QUARTILE','THIRD_QUARTILE','FOURTH_QUARTILE'];
  const text = (x,y,size,value,color=ink,extra='') => '<text x="'+x+'" y="'+y+'" font-size="'+size+'" fill="'+color+'" '+extra+'>'+value+'</text>';
  const fmt = n => n.toLocaleString('en-US');
  const date = d => new Date(d+'T00:00:00Z').toLocaleDateString('en-US',{month:'short',day:'numeric',year:'numeric',timeZone:'UTC'});
  let svg = '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 980 430" role="img" aria-labelledby="title desc"><title id="title">Itamar Dahan contribution skyline</title><desc id="desc">'+fmt(total)+' GitHub contributions across '+active+' active days, '+date(days[0].date)+' to '+date(days.at(-1).date)+'. Each building is one day; height uses a logarithmic scale.</desc><rect width="980" height="430" rx="16" fill="'+bg+'"/><g font-family="system-ui,-apple-system,BlinkMacSystemFont,Segoe UI,sans-serif">';
  svg += text(32,36,11,'DAHANITAMAR / CONTRIBUTION SKYLINE',muted,'letter-spacing="2"');
  svg += text(32,75,28,'A year, built one day at a time.',ink,'font-weight="600"');
  svg += text(32,99,12,date(days[0].date)+' - '+date(days.at(-1).date),muted);
  const sx = 14, dx = 8, dy = 5, baseY = 246, origin = 84;
  const point = (w,d,h=0) => [+(origin+w*sx+d*dx).toFixed(1), +(baseY-w*0.75+d*dy-h).toFixed(1)];
  const polygon = pts => pts.map(p=>p.join(',')).join(' ');
  for (const day of [...days].sort((a,b)=>(baseY-a.col*.75+a.weekday*dy)-(baseY-b.col*.75+b.weekday*dy))) {
    const w = day.col, d=day.weekday;
    const h = day.contributionCount ? 5 + 83*Math.log1p(day.contributionCount)/Math.log1p(Math.max(1,peak)) : 0;
    const a=point(w,d), b=point(w+.88,d), c=point(w+.88,d+.82), e=point(w,d+.82);
    const top=[a,b,c,e].map(([x,y])=>[x,+(y-h).toFixed(1)]);
    const color=palette[Math.max(0,levels.indexOf(day.contributionLevel))];
    svg += '<g><title>'+day.date+': '+day.contributionCount+' contributions</title>';
    if(h) svg += '<polygon points="'+polygon([e,c,top[2],top[3]])+'" fill="'+color+'"/><polygon points="'+polygon([b,c,top[2],top[1]])+'" fill="'+color+'"/><polygon points="'+polygon([e,c,top[2],top[3]])+'" fill="#000" opacity=".12"/><polygon points="'+polygon([b,c,top[2],top[1]])+'" fill="#000" opacity=".25"/>';
    svg += '<polygon points="'+polygon(top)+'" fill="'+color+'"/></g>';
  }
  let month='';
  for(const day of days.filter(d=>d.weekday===0)) {
    const current=day.date.slice(0,7);
    if(current!==month) {
      const p=point(day.col,7.7);
      svg+=text(p[0],p[1]+18,11,new Date(day.date+'T00:00:00Z').toLocaleDateString('en-US',{month:'short',timeZone:'UTC'}),muted);
      month=current;
    }
  }
  svg += '<path d="M32 329H948" stroke="'+(dark?'#30363d':'#d1d9e0')+'"/>';
  for (const [i, stat] of [[fmt(total),'CONTRIBUTIONS'],[String(active),'ACTIVE DAYS'],[fmt(peak),'BUSIEST DAY']].entries()) {
    svg+=text(32+i*305,370,29,stat[0],ink,'font-weight="600"')+text(32+i*305,391,10,stat[1],muted,'letter-spacing="1.6"');
  }
  svg+=text(32,417,10,'GitHub contribution calendar / updated '+days.at(-1).date+' / height: logarithmic',muted);
  return svg+'</g></svg>\n';
}

export async function generate() {
  const token = process.env.GH_TOKEN;
  const login = process.env.PROFILE_LOGIN;
  if (!token || !/^[a-z\d-]+$/i.test(login || '')) throw new Error('GH_TOKEN and PROFILE_LOGIN required');
  const end = new Date(); end.setUTCHours(23,59,59,0);
  const start = new Date(end); start.setUTCDate(start.getUTCDate()-364); start.setUTCHours(0,0,0,0);
  const response = await fetch('https://api.github.com/graphql', {
    method:'POST', headers:{Authorization:'Bearer '+token,'Content-Type':'application/json'},
    body:JSON.stringify({query:'query($login:String!,$from:DateTime!,$to:DateTime!){user(login:$login){contributionsCollection(from:$from,to:$to){contributionCalendar{totalContributions weeks{contributionDays{date contributionCount contributionLevel weekday}}}}}}',variables:{login,from:start.toISOString(),to:end.toISOString()}})
  });
  const body = await response.json();
  if (!response.ok || body.errors) throw new Error('Contribution query failed: '+JSON.stringify(body.errors || response.status));
  const calendar = body.data.user.contributionsCollection.contributionCalendar;
  await mkdir('assets/skyline',{recursive:true});
  await Promise.all([writeFile('assets/skyline/light.svg',render(calendar)),writeFile('assets/skyline/dark.svg',render(calendar,true))]);
  console.log('Updated real contribution skyline');
}
if (process.argv[1] && import.meta.url === pathToFileURL(process.argv[1]).href) await generate();

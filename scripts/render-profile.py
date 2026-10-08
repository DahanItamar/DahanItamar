from pathlib import Path
from io import BytesIO
import copy, re, urllib.request, xml.etree.ElementTree as ET
import cairosvg
from PIL import Image, ImageDraw, ImageFont, ImageChops

OUT=Path('assets/profile-v2')
OUT.mkdir(parents=True,exist_ok=True)
FONT=Path('assets/fonts/Geist.ttf')
def font(size,weight=600):
    f=ImageFont.truetype(str(FONT),size)
    try:
        axes=f.get_variation_axes()
        f.set_variation_by_axes([weight if a['name']==b'Weight' else a['default'] for a in axes])
    except (OSError,AttributeError): pass
    return f
for mode,bg,ink,sub in [('dark','#0d1117','#f0f6fc','#b1bac4'),('light','#f6f8fa','#1f2328','#59636e')]:
    im=Image.new('RGB',(980,272),bg)
    draw=ImageDraw.Draw(im)
    draw.text((24,8),'ITAMAR',font=font(108,760),fill=ink)
    draw.text((22,112),'DAHAN',font=font(108,760),fill='#1f6feb')
    draw.text((576,137),'Full-stack development',font=font(24,550),fill=ink)
    draw.text((576,173),'and automation.',font=font(24,550),fill=ink)
    draw.text((576,222),'TypeScript / React / Node.js',font=font(16,450),fill=sub)
    im.save(OUT/f'wordmark-{mode}.png',optimize=True)

def public_preview(url,name):
    with urllib.request.urlopen(url,timeout=45) as response: data=response.read()
    im=Image.open(BytesIO(data)).convert('RGB')
    im.thumbnail((980,980),Image.Resampling.LANCZOS)
    im.save(OUT/name,'WEBP',quality=84,method=6)
public_preview('https://raw.githubusercontent.com/DahanItamar/Winnow/master/docs/assets/screens/evidence.png','winnow.webp')

NS='{http://www.w3.org/2000/svg}'
tree=ET.parse('profile-3d-contrib/profile-night-view.svg')
root=tree.getroot()
animated=[]
for parent in root.iter():
    for child in list(parent):
        kind=child.tag.rsplit('}',1)[-1]
        if kind in ('animate','animateTransform'):
            values=child.get('values','').split(';')
            if len(values)==2 and ((kind=='animateTransform' and child.get('type')=='translate') or child.get('attributeName')=='height'):
                start=[float(v) for v in re.findall(r'-?\d+(?:\.\d+)?',values[0])]
                end=[float(v) for v in re.findall(r'-?\d+(?:\.\d+)?',values[1])]
                if len(start)==len(end): animated.append((parent,child.get('attributeName'),kind,start,end))
            parent.remove(child)
assert len(animated)>3, 'No building growth animation found'
# The animation changes display geometry, not contribution counts or labels.
palette=Image.open(BytesIO(cairosvg.svg2png(bytestring=ET.tostring(root),output_width=760,output_height=505))).convert('RGB').quantize(colors=128)
frames=[]
progresses=[i/23 for i in range(24)]+[1]+[.75,.5,.25,0]
durations=[110]*24+[1600]+[110]*4
for p in progresses:
    # A short stagger sweeps the building growth across the year.
    for index,(parent,attribute,kind,start,end) in enumerate(animated):
        bar=index//3
        delay=(bar/max(1,len(animated)//3-1))*.25
        t=max(0,min(1,(p-delay)/.75))
        t=t*t*(3-2*t)
        vals=[a+(b-a)*t for a,b in zip(start,end)]
        value=' '.join(f'{v:.3f}' for v in vals)
        parent.set(attribute,'translate('+value+')' if kind=='animateTransform' else value)
    data=cairosvg.svg2png(bytestring=ET.tostring(root),output_width=760,output_height=505)
    im=Image.open(BytesIO(data)).convert('RGB')
    frames.append(im.quantize(palette=palette,dither=Image.Dither.NONE))
frames[0].save(OUT/'contributions.gif',save_all=True,append_images=frames[1:],duration=durations,loop=0,optimize=True,disposal=2)
gif=Image.open(OUT/'contributions.gif')
assert gif.n_frames>=20 and gif.info.get('loop')==0
gif.seek(0); first=gif.convert('RGB')
gif.seek(23); last=gif.convert('RGB')
assert ImageChops.difference(first,last).getbbox(), 'Animation frames are identical'
assert (OUT/'contributions.gif').stat().st_size<1_200_000, 'GIF exceeded image budget'
print('Verified looping building animation:',gif.n_frames,'frames')
for file in OUT.iterdir(): print(file.name,file.stat().st_size,'bytes')

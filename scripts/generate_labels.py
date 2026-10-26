"""Build readable brand-icon tiles and social badges from vendored SVGs.

The original Devicon/Simple Icons artwork and licenses live in assets/brands.
No remote image or badge service is required when viewing the profile.
"""
from pathlib import Path
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1] / 'assets'
NS = 'http://www.w3.org/2000/svg'
ET.register_namespace('', NS)


def element(name, **attrs):
    return ET.Element(f'{{{NS}}}{name}', {k: str(v) for k,v in attrs.items()})


def source_icon(name, x, y, size):
    icon=ET.parse(ROOT/'brands'/f'{name}.svg').getroot()
    icon.attrib.update(x=str(x),y=str(y),width=str(size),height=str(size))
    return icon


def skill(name, label):
    svg=element('svg',width=64,height=64,viewBox='0 0 64 64',role='img')
    svg.set('aria-label',label)
    svg.append(element('rect',x='.5',y='.5',width=63,height=63,rx=12,fill='#f8fafc',stroke='#cbd5e1'))
    svg.append(source_icon(name,10,10,44))
    return ET.tostring(svg,encoding='unicode')


def social(name, label, color, width):
    svg=element('svg',width=width,height=36,viewBox=f'0 0 {width} 36',role='img',fill='#ffffff')
    svg.set('aria-label',label)
    svg.append(element('rect',width=width,height=36,rx=4,fill=color))
    svg.append(source_icon(name,12,8,20))
    text=element('text',x=43,y=23,fill='#ffffff')
    text.attrib.update({'font-family':'Segoe UI,Arial,sans-serif','font-size':'13','font-weight':'700','letter-spacing':'.5'})
    text.text=label
    svg.append(text)
    return ET.tostring(svg,encoding='unicode')


def main():
    for filename, name, label in [('python','python','Python'),('cpp','cplusplus','C++'),
            ('sqlserver','microsoftsqlserver','Microsoft SQL Server'),('numpy','numpy','NumPy'),
            ('pandas','pandas','pandas'),('matplotlib','matplotlib','Matplotlib'),
            ('scikitlearn','scikitlearn','scikit-learn'),('jupyter','jupyter','Jupyter')]:
        folder=ROOT/'skills'
        folder.mkdir(parents=True, exist_ok=True)
        (folder/f'{filename}.svg').write_text(skill(name,label),encoding='utf-8')
    for filename,name,label,color,width in [('email','gmail','GMAIL','#c5221f',112),
            ('linkedin','linkedin','LINKEDIN','#0076b2',132)]:
        folder=ROOT/'contact'
        folder.mkdir(parents=True,exist_ok=True)
        (folder/f'{filename}.svg').write_text(social(name,label,color,width),encoding='utf-8')
    print('Generated 8 brand-icon tiles and 2 branded social buttons.')


if __name__=='__main__':
    main()

"""Create consistent, accessible SVG labels; no remote badge dependency."""
from pathlib import Path
from html import escape

ROOT = Path(__file__).resolve().parents[1] / 'assets'
ICONS = {
    'python': '<path d="m3 7 4 5-4 5m7 0h7"/>',
    'cpp': '<path d="m7 5-5 7 5 7m10-14 5 7-5 7M13 8v8m-4-4h8"/>',
    'databases': '<ellipse cx="12" cy="5" rx="8" ry="3"/><path d="M4 5v14c0 4 16 4 16 0V5M4 12c0 4 16 4 16 0"/>',
    'ml': '<circle cx="12" cy="5" r="3"/><circle cx="5" cy="18" r="3"/><circle cx="19" cy="18" r="3"/><path d="m10 8-4 7m8-7 4 7M8 18h8"/>',
    'analysis': '<path d="M3 3v18h18M7 16l4-5 4 2 5-7"/>',
    'email': '<rect x="2" y="5" width="20" height="14" rx="3"/><path d="m3 7 9 6 9-6"/>',
    'linkedin': '<path d="M5 10v10M5 5v.1M11 20V10m0 4c0-6 8-6 8 0v6"/>',
}


def label(name, text, width, contact=False):
    height = 40 if contact else 36
    fill, stroke = ('#25425f', '#516f8e') if contact else ('#19283a', '#40536b')
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}" role="img" aria-label="{escape(text)}">
<rect x=".5" y=".5" width="{width-1}" height="{height-1}" rx="8" fill="{fill}" stroke="{stroke}"/>
<g transform="translate(11 {(height-20)/2}) scale(.83)" fill="none" stroke="#b8d4ed" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round">{ICONS[name]}</g>
<text x="40" y="{height/2+5}" font-family="Segoe UI,Arial,sans-serif" font-size="15" font-weight="500" fill="#eef3fb">{escape(text)}</text>
</svg>'''


def main():
    for name, text, width in [('python','Python',108),('cpp','C++',92),
                              ('databases','Databases',132),('ml','Machine Learning',184),
                              ('analysis','Data Analysis',158)]:
        folder=ROOT/'skills'
        folder.mkdir(parents=True, exist_ok=True)
        (folder/f'{name}.svg').write_text(label(name,text,width),encoding='utf-8')
    for name,text,width in [('email','Email me',132),('linkedin','LinkedIn',132)]:
        folder=ROOT/'contact'
        folder.mkdir(parents=True,exist_ok=True)
        (folder/f'{name}.svg').write_text(label(name,text,width,True),encoding='utf-8')
    print('Generated 5 skill labels and 2 contact buttons.')


if __name__=='__main__':
    main()

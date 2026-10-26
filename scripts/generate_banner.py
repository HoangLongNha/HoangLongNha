"""Draw an original, self-contained GitHub banner. Run from any directory.

Requires Pillow and Segoe UI/Consolas (Windows), or DejaVu fonts (Linux).
No external images, screenshots, or third-party artwork are used.
"""

from pathlib import Path
import math
from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'assets'
W, H, SCALE = 1200, 360, 2
NAVY = '#0B1220'
TEAL = '#5EEAD4'
INK = '#E6EDF3'
MUTED = '#8FA5BC'


def font(size, mono=False, bold=False):
    candidates = (
        ['C:/Windows/Fonts/consolab.ttf' if bold else 'C:/Windows/Fonts/consola.ttf',
         '/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf']
        if mono else
        ['C:/Windows/Fonts/seguisb.ttf' if bold else 'C:/Windows/Fonts/segoeui.ttf',
         '/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf']
    )
    for candidate in candidates:
        if Path(candidate).exists():
            return ImageFont.truetype(candidate, size * SCALE)
    raise FileNotFoundError('Install Segoe UI/Consolas or DejaVu Sans fonts.')


def frame(index, total):
    image = Image.new('RGB', (W * SCALE, H * SCALE), NAVY)
    d = ImageDraw.Draw(image)
    phase = index / total * math.tau

    def rect(box, fill, radius=0, outline=None, width=1):
        box = tuple(int(v * SCALE) for v in box)
        if radius:
            d.rounded_rectangle(box, radius * SCALE, fill=fill, outline=outline, width=width * SCALE)
        else:
            d.rectangle(box, fill=fill, outline=outline, width=width * SCALE)

    def line(points, color, width=1):
        d.line([(int(x * SCALE), int(y * SCALE)) for x, y in points], fill=color, width=width * SCALE)

    def text(x, y, value, size=16, fill=INK, mono=False, bold=False):
        d.text((x * SCALE, y * SCALE), value, font=font(size, mono, bold), fill=fill)

    # Quiet grid and architectural lines create depth without visual noise.
    for x in range(640, 1200, 32):
        line([(x, 0), (x, 360)], '#101D2E')
    for y in range(8, 360, 32):
        line([(608, y), (1200, y)], '#101D2E')
    rect((0, 0, 8, 360), TEAL)
    rect((52, 54, 289, 83), '#14332F', radius=14)
    text(66, 59, 'A NOTEBOOK IN PROGRESS', 12, TEAL, mono=True)
    text(50, 104, 'Hoàng Long', 57, bold=True)
    text(54, 187, 'DATA SCIENCE  /  MACHINE LEARNING', 15, TEAL, mono=True)
    text(54, 228, 'Curiosity. Code. Understanding.', 19, MUTED)
    line([(54, 289), (354, 289)], '#25374A')
    text(54, 305, 'UNIVERSITY OF SCIENCE · VNU-HCM', 12, MUTED, mono=True)

    # Workstation: terminal, analysis screen, desk, notebook, mug, and plant.
    rect((646, 53, 1097, 261), '#17283B', radius=14, outline='#35516A')
    rect((657, 64, 1086, 246), '#0B1727', radius=7)
    rect((657, 64, 1086, 91), '#1B2B3E', radius=7)
    rect((657, 80, 1086, 91), '#1B2B3E')
    for x, color in [(673, '#E58487'), (688, '#E4BF7A'), (703, '#74C8AB')]:
        d.ellipse((x*SCALE, 74*SCALE, (x+6)*SCALE, 80*SCALE), fill=color)
    text(934, 70, 'workspace', 11, MUTED, mono=True)
    text(675, 105, '>>> explore(data)', 14, TEAL, mono=True)
    text(675, 136, '# ask a better question', 12, MUTED, mono=True)
    text(675, 160, 'observe()', 13, '#9AC8F4', mono=True)
    text(675, 183, 'learn()', 13, '#9AC8F4', mono=True)
    text(675, 206, '>>>', 13, TEAL, mono=True)
    if index < total // 2:
        rect((709, 210, 717, 223), TEAL)
    line([(872, 112), (872, 229)], '#26384A')

    points = [(899, 211), (922, 194), (945, 202), (968, 171),
              (991, 181), (1014, 146), (1037, 156), (1064, 121)]
    for y in [139, 170, 201, 229]:
        line([(895, y), (1067, y)], '#1E3042')
    line(points, '#4FB9AC', 2)
    progress = (1 - math.cos(phase)) / 2 * (len(points) - 1)
    segment = min(int(progress), len(points)-2)
    fraction = progress - segment
    px = points[segment][0] + fraction*(points[segment+1][0]-points[segment][0])
    py = points[segment][1] + fraction*(points[segment+1][1]-points[segment][1])
    d.ellipse(((px-5)*SCALE, (py-5)*SCALE, (px+5)*SCALE, (py+5)*SCALE), fill=TEAL)

    rect((846, 262, 894, 286), '#273C50', radius=2)
    rect((818, 284, 922, 292), '#35516A', radius=4)
    rect((610, 294, 1140, 306), '#354A60', radius=5)
    rect((620, 306, 1130, 313), '#1A2C40')
    rect((643, 313, 655, 360), '#26394D')
    rect((1094, 313, 1106, 360), '#26394D')
    rect((715, 279, 809, 292), '#20374B', radius=3, outline='#486379')
    for row in range(2):
        line([(726, 283+row*4), (797, 283+row*4)], '#698599')
    rect((942, 278, 1004, 291), '#A0B4BE', radius=3)
    rect((942, 277, 1004, 280), '#CFDBDD', radius=1)
    line([(954, 278), (954, 290)], '#477A78', 2)
    rect((1039, 263, 1069, 291), '#48767D', radius=4)
    d.arc((1060*SCALE, 265*SCALE, 1081*SCALE, 283*SCALE), -90, 90, fill='#48767D', width=4*SCALE)
    for k in range(2):
        sx = 1048+k*9 + math.sin(phase+k)*2
        line([(sx, 256), (sx-2, 249), (sx+2, 242)], '#6B8691')
    rect((585, 268, 613, 294), '#46636C', radius=3)
    line([(600, 270), (598, 233)], '#5AA48B', 3)
    for box in [(580,235,599,247), (598,224,616,238), (583,250,600,261), (599,242,616,253)]:
        d.ellipse(tuple(v*SCALE for v in box), fill='#4A947F')
    return image.resize((W, H), Image.Resampling.LANCZOS)


def main():
    OUT.mkdir(exist_ok=True)
    total = 48
    images = [frame(i, total) for i in range(total)]
    images[0].save(OUT / 'workspace.png', optimize=True)
    palette = images[0].quantize(colors=128, method=Image.Quantize.MEDIANCUT)
    frames = [im.quantize(palette=palette, dither=Image.Dither.NONE) for im in images]
    frames[0].save(OUT / 'workspace.gif', save_all=True, append_images=frames[1:],
                   duration=100, loop=0, optimize=True, disposal=1)
    print(f'Generated {total} frames at {W}x{H}. GIF: {(OUT / "workspace.gif").stat().st_size:,} bytes')


if __name__ == '__main__':
    main()

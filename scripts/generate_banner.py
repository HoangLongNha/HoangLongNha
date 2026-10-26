"""Export the original HTML/SVG illustration to PNG and looping GitHub GIF.

Install requirements.txt and use installed Microsoft Edge or Chromium.
Run: python scripts/generate_banner.py
No external artwork, remote fonts, or services are needed during rendering.
"""
from io import BytesIO
from pathlib import Path
import os
from PIL import Image
from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'assets'
WIDTH, HEIGHT, FRAME_COUNT = 1200, 420, 40


def browser_executable():
    candidates = [
        Path(os.environ.get('PROGRAMFILES(X86)', 'C:/Program Files (x86)')) / 'Microsoft/Edge/Application/msedge.exe',
        Path(os.environ.get('PROGRAMFILES', 'C:/Program Files')) / 'Microsoft/Edge/Application/msedge.exe',
    ]
    return next((str(path) for path in candidates if path.is_file()), None)


def main():
    OUT.mkdir(exist_ok=True)
    html = (ROOT / 'design/banner.html').read_text(encoding='utf-8')
    frames = []
    with sync_playwright() as p:
        browser = p.chromium.launch(executable_path=browser_executable(), headless=True)
        page = browser.new_page(viewport={'width': WIDTH, 'height': HEIGHT}, device_scale_factor=1)
        page.set_content(html, wait_until='load')
        page.evaluate('document.fonts.ready')
        for index in range(FRAME_COUNT):
            page.evaluate('(t) => window.renderFrame(t)', index / FRAME_COUNT)
            png = page.screenshot(type='png', animations='disabled')
            if index == 0:
                (OUT / 'workspace.png').write_bytes(png)
            frames.append(Image.open(BytesIO(png)).convert('RGB'))
        browser.close()
    palette = frames[0].quantize(colors=192, method=Image.Quantize.MEDIANCUT)
    indexed = [im.quantize(palette=palette, dither=Image.Dither.NONE) for im in frames]
    indexed[0].save(OUT / 'workspace.gif', save_all=True, append_images=indexed[1:],
                    duration=120, loop=0, disposal=1, optimize=True)
    print(f'Banner: {WIDTH}x{HEIGHT}, {FRAME_COUNT} frames, {(OUT / "workspace.gif").stat().st_size:,} bytes')


if __name__ == '__main__':
    main()

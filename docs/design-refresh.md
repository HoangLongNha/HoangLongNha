# Profile design refresh — 26 October 2026

The user requested a redesign using the local `design` skill. Existing approved identity, Data Science direction, contacts, and absence of a current-research section remain the brief.

## Art direction

An evening study beside a rainy window, combining the personal warmth of the reference GIF with a professional academic presentation. Original HTML/SVG illustration, no borrowed artwork. Palette: ink `#101827`, room `#142339`, paper `#eef3fb`, secondary text `#b7c6da`, mist blue `#9ec8ef`, lamplight `#f4c890`. Segoe UI for identity/copy; Consolas only inside the illustrated notebook. Fixed 1200×420 export, generous left text area, quiet atmospheric right illustration. Rain and coffee steam are the spatial motion; a subtle cursor is decorative.

## Decisions against generic defaults

The ui-ux-pro-max search was consulted, but its scroll storytelling and glassmorphism recommendations do not fit a GitHub README. Use native Markdown flow and a bespoke illustration instead. Avoid invented metrics, publication/project placeholders, repeated slogans, uppercase labels, and unrelated dashboard cards. Do not draw a fake clickable CTA into the banner; actual mail/LinkedIn actions live below the introduction.

The original profile had a table and an abstract flat monitor. The redesign uses self-hosted SVG skill labels and contact buttons, with readable text alternatives, and a fully illustrated night scene. The personal name appears in the banner; the native heading stays concise.

## Accessibility and performance

Static PNG under reduced motion; all essential identity/content repeated as native text or image alternatives. Five skill labels wrap naturally on small screens. Contact links use the exact approved addresses. Shared GIF palette avoids frame-to-frame color shifts. No trackers, hosted badge service, external image dependency, or remote fonts.

## Sources and workflow

- Applied the design skill, its banner reference, ui-ux-pro-max guidance, and frontend-design principles.
- Looked at [night-reading art direction on Pinterest](https://www.pinterest.com/pin/749567931764835994/) for atmospheric context; no source artwork was copied.
- `design/banner.html` is the editable source; `scripts/generate_banner.py` exports Edge/Playwright screenshots to PNG/GIF. `scripts/generate_labels.py` produces the consistent labels.
- Verify exported assets, then inspect the actual GitHub profile after publication in desktop and narrow viewports.

## Local verification

- Exported 40 valid looping frames at 1200×420; GIF 193,194 bytes, with static PNG fallback.
- All seven SVG labels parse correctly and text fits inside their bounds.
- Exact contact values and all local image references checked.
- Previewed light/dark themes at 1000px and 390px: all images loaded, banner aspect preserved, no horizontal overflow.
- Main text/background color pairs measured between 9.32:1 and 15.95:1 contrast.
- Visually inspected desktop and mobile exports before publishing.

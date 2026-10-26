# GitHub Profile Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [x]`) syntax for tracking.

**Goal:** Publish the approved professional GitHub profile with an original GIF and verified contact links.

**Architecture:** A README renders on the matching username repository. Original visual assets are versioned locally with a repeatable Pillow generator; no website build or deployment is required.

**Tech Stack:** GitHub Markdown/HTML, Python 3, Pillow, GitHub CLI.

**Spec:** `docs/superpowers/specs/2026-10-26-github-profile-design.md`

## Global Constraints
- English introduction and the approved name, skills, and contacts.
- No current research section or V2V details.
- No invented projects, publications, qualifications, or library proficiency.
- Keep the existing GitHub Pages repository unchanged.

## Review Focus
- GIF renders with a readable first frame and loops smoothly.
- Static fallback and descriptive alt text are available.
- Contact addresses match the user-provided values exactly.
- README uses GitHub-supported HTML and links to existing assets.
- Profile username/repository match; no unrelated repository changes.

### Task 1: Prepare and verify the profile
**Files:** `README.md`, `assets/workspace.gif`, `assets/workspace.png`, `scripts/generate_banner.py`, `requirements.txt`, `.gitignore`.
**Interfaces:** README consumes the two relative asset paths; generator produces both from original drawing code.
- [x] Write the README with the approved introduction, five skills, and two contact links.
- [x] Render the original navy/teal workstation animation and static fallback.
- [x] Inspect the banner; verify dimensions, frame count, file size, links, and exact contact text.
- [x] Commit the prepared files in an isolated directory.

### Task 2: Publish and confirm
**Interfaces:** GitHub CLI consumes the verified local Git repository and publishes `HoangLongNha/HoangLongNha` publicly.
- [x] Verify the authenticated GitHub account and check for an existing profile repository.
- [x] Create the matching public repository and push the prepared commit.
- [x] Fetch the remote README and assets; confirm commit synchronization and live profile rendering if available.

Documentation/assets only: use direct content, image and remote verification rather than unit tests mirroring the README. User already approved creation of the profile; proceed within that scope.

## Verification record
- GIF: 1200x360, 48 decodable frames, infinite loop, 72,534 bytes; static PNG also verified.
- README: exact approved name and contact links; no current-research section.
- Independent read-only review found no material issues; heading hierarchy improved before publishing.
- Remote README and both assets fetched successfully after push.
- Live profile opened in Edge: banner, introduction, skills table and contact links rendered successfully.
- Git ownership exception used only in the publishing process environment for this specific temporary directory; no global Git configuration changed.

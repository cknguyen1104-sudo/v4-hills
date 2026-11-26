# Speed Stars — 600m Rolling Hills (V4)

Repository-ready packaging of the approved Continuous Hill Playtest V4. This is a compiled Unity WebGL game build, not a Unity source project. The later Performance Edition is not included.

## Play locally

- Windows: double-click `start.bat` (Python 3 required).
- macOS/Linux: run `python3 launch.py` from this folder.
- Open the URL printed by the launcher and keep the terminal open. Do not open HTML files directly with `file://`.
- From the original Sprints menu, choose **600m run**, then select the race in its isolated menu. The top **600m Rolling Hills** link is an alternative.
- Use Up Arrow or Down Arrow to hurdle. Hills-only and previous-collision fallback options remain available.

## GitHub repository setup

1. Create an empty repository (private unless you have permission to redistribute the original game assets).
2. Extract this archive and upload or commit the contents of this folder, including hidden dotfiles, at the repository root. Do not upload the ZIP itself.
3. For a Git-based upload, run these commands in this folder, replacing the example URL with your repository URL:

```sh
git init -b main
git add .
git commit -m "Add approved 600m V4 WebGL build"
git remote add origin https://github.com/YOUR-USERNAME/YOUR-REPO.git
git push -u origin main
```

The largest game file is under 25 MB. Git LFS is not required for this snapshot. Keep `.wasm` and `.data` files as normal binary files, not LFS pointer files.

## GitHub Pages (optional)

Only publish if you have the necessary rights to redistribute the original game's code and assets. GitHub Pages sites are generally publicly accessible, including sites published from private repositories unless restricted by an eligible enterprise configuration.

In the repository, open **Settings → Pages → Build and deployment**, choose **Deploy from a branch**, then **main → /(root)** and save. After deployment, open the site URL GitHub provides. `.nojekyll` enables direct static hosting. No Python server, npm installation or Unity editor is required on Pages. All game asset URLs are relative so a repository subpath is supported. Actual GitHub Pages gameplay has not been tested.

Official setup documentation: https://docs.github.com/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site

## Layout

| Path | Purpose |
| --- | --- |
| `index.html` | Root entry point |
| `original/index.html` | Original events and combined native event selector |
| `600m/index.html` | Isolated 600m rolling hills and fallback selection |
| `*.wasm`, `*.data`, `framework.js`, `Build_v2-40w.loader.js` | Original and patched Unity runtime and assets |
| `launch.py`, `start.bat` | Local launcher |
| `README.txt`, `*-check.json` | Original V4 notes and diagnostic records |
| `tools/verify.py`, `baseline-sha256.json` | Verify the original V4 files were preserved |

## Verify the baseline

```sh
python3 tools/verify.py
```

If Node.js is installed, the checker also validates the WebAssembly binaries. The checksum manifest is for the V4 snapshot; deliberate edits to original files will be reported as changes. It does not prove runtime gameplay correctness.

## Rights and limitations

This is an unofficial modification of Speed Stars. Original game code, art, names and other assets belong to their respective rights holders. No permission or open-source license for the original game is asserted or supplied. Keep this repository private unless you have the necessary rights to share it. Do not submit modded race times as stock records. The original Unity source project is not included. The 600m event is implemented using an isolated native build and menu routing, not a newly registered event in the same Unity scene.

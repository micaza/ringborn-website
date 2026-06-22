# The Last Sideran — Website

Static marketing site for **The Last Sideran** by PixelDo Games. Served via GitHub Pages at [pixeldogames.com/thelastsideran](https://pixeldogames.com/thelastsideran).

Visitors to [pixeldogames.com](https://pixeldogames.com) are redirected to the game page automatically.

## Local preview

```bash
python3 -m http.server 8000
# open http://localhost:8000/thelastsideran/
```

## Deploy

Push to `main`. GitHub Pages picks it up automatically from the repo root.

In repo **Settings → Pages**:
- **Source**: Deploy from a branch
- **Branch**: `main` — `/` (root)

Site structure:
- `/` — redirects to `/thelastsideran/`
- `/ringbornascension/` — redirects to `/thelastsideran/` (legacy path)
- `/thelastsideran/` — game marketing site

## Custom domain

`CNAME` points to `pixeldogames.com`. DNS in GoDaddy:

- **A** records for the root pointing to GitHub's IPs:
  - `185.199.108.153`
  - `185.199.109.153`
  - `185.199.110.153`
  - `185.199.111.153`
- **CNAME** for `www` pointing to `<github-username>.github.io`

Then tick **Enforce HTTPS** in Pages settings once GitHub issues the cert (usually within an hour).
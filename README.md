# Ringborn Ascension — Website

Static marketing site for **Ringborn Ascension** by PixelDog Games. Served via GitHub Pages.

## Local preview

```bash
python3 -m http.server 8000
# open http://localhost:8000
```

## Deploy

Push to `main`. GitHub Pages picks it up automatically from the repo root.

In repo **Settings → Pages**:
- **Source**: Deploy from a branch
- **Branch**: `main` — `/` (root)

## Custom domain

Settings → Pages, enter the domain. Then in GoDaddy DNS, add:

- **A** records for the root pointing to GitHub's IPs:
  - `185.199.108.153`
  - `185.199.109.153`
  - `185.199.110.153`
  - `185.199.111.153`
- **CNAME** for `www` pointing to `<github-username>.github.io`

Then tick **Enforce HTTPS** in Pages settings once GitHub issues the cert (usually within an hour).

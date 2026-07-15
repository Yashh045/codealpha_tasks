# GitHub Setup Guide

Follow these steps to publish **VoltScope Analytics** to GitHub and link it on your resume/LinkedIn.

---

## Option A — GitHub website (no CLI needed)

### 1. Create the repository

1. Go to https://github.com/new
2. Repository name: `voltscope-analytics`
3. Description: `Data visualization portfolio — global energy transition dashboards with Python & Tableau`
4. Choose **Public**
5. Do **not** add README, .gitignore, or license (already in project)
6. Click **Create repository**

### 2. Push from your machine

Open PowerShell in the project folder:

```powershell
cd "C:\Users\DELL USER\Projects\voltscope-analytics"

git init
git add .
git commit -m "Initial commit: VoltScope Analytics data visualization portfolio"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/voltscope-analytics.git
git push -u origin main
```

Replace `YOUR_USERNAME` with your GitHub username.

### 3. Enable GitHub Pages (optional)

1. Repo → **Settings** → **Pages**
2. Source: **Deploy from branch** → `main` → `/docs` or use README as landing
3. Your project URL: `https://YOUR_USERNAME.github.io/voltscope-analytics/`

---

## Option B — GitHub CLI

Install: https://cli.github.com/

```powershell
gh auth login
cd "C:\Users\DELL USER\Projects\voltscope-analytics"
git init
git add .
git commit -m "Initial commit: VoltScope Analytics data visualization portfolio"
gh repo create voltscope-analytics --public --source=. --push
```

---

## After publishing

1. Update `README.md`:
   - Replace `[Your Name]` with your name
   - Add repo URL under **Live demo**
2. Update `PORTFOLIO.md`:
   - Replace `[your-repo-url]` with `https://github.com/YOUR_USERNAME/voltscope-analytics`
3. Add to LinkedIn **Featured** section with screenshot of `09_executive_dashboard.png`
4. Add to resume under Projects (copy from `PORTFOLIO.md`)

---

## Suggested repo topics

`data-visualization` `python` `matplotlib` `seaborn` `pandas` `tableau` `energy` `portfolio` `data-science` `jupyter`

Add via: Repo → ⚙️ next to About → Topics

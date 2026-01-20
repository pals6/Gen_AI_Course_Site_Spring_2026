# GitHub Pages Deployment Guide

This guide will walk you through deploying your course website to GitHub Pages.

## Prerequisites

- A GitHub account
- Git installed on your computer
- Basic familiarity with command line/terminal

---

## Step 1: Create a GitHub Repository

1. Go to [GitHub](https://github.com) and sign in
2. Click the **+** icon in the top right corner
3. Select **New repository**
4. Fill in the details:
   - **Repository name**: `gen-ai-course-site` (or any name you prefer)
   - **Description**: "Course website for Design and Development of Generative AI Applications"
   - **Public** or **Private** (GitHub Pages works with both)
   - **Do NOT** initialize with README (you already have one)
5. Click **Create repository**

---

## Step 2: Push Your Code to GitHub

### If you haven't initialized Git yet:

```bash
# Navigate to your project directory
cd /Users/cameron/Documents/ITCS_5010_Gen_AI_TA_Spring_2026/Gen_AI_Course_Site_Spring_2026

# Initialize Git repository
git init

# Add all files
git add .

# Make your first commit
git commit -m "Initial commit: Course website setup"

# Add your GitHub repository as remote (replace USERNAME and REPO)
git remote add origin https://github.com/USERNAME/REPO.git

# Push to GitHub
git branch -M main
git push -u origin main
```

### If you already have a Git repository:

```bash
# Add all files
git add .

# Commit changes
git commit -m "Initial commit: Course website setup"

# Push to GitHub
git push origin main
```

---

## Step 3: Enable GitHub Pages

1. Go to your repository on GitHub
2. Click **Settings** (top menu)
3. In the left sidebar, click **Pages**
4. Under **Source**:
   - Branch: Select **main** (or **master**)
   - Folder: Select **/ (root)**
5. Click **Save**

GitHub will start building your site. This takes 1-2 minutes.

---

## Step 4: Access Your Site

Your site will be available at:

```
https://USERNAME.github.io/REPO-NAME/
```

For example:
- Username: `johnsmith`
- Repository: `gen-ai-course`
- URL: `https://johnsmith.github.io/gen-ai-course/`

### Using a Custom Domain (Optional)

If you want to use your own domain:

1. In GitHub Pages settings, enter your custom domain
2. In your domain registrar (GoDaddy, Namecheap, etc.):
   - Add a CNAME record pointing to `USERNAME.github.io`
   - Or add A records for GitHub's IPs (see [GitHub docs](https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site))

---

## Step 5: Update Your Site

Whenever you make changes:

```bash
# After editing files
git add .
git commit -m "Update course information"
git push origin main
```

GitHub Pages will automatically rebuild your site (takes 1-2 minutes).

---

## Common Issues and Solutions

### Issue: Site shows 404 error

**Solutions**:
- Wait 2-3 minutes after enabling GitHub Pages
- Check that GitHub Pages is enabled in Settings → Pages
- Verify the branch and folder are set correctly
- Make sure `index.html` exists in the root directory

### Issue: Changes not appearing

**Solutions**:
- Wait 1-2 minutes for GitHub to rebuild
- Clear your browser cache (Ctrl+Shift+R or Cmd+Shift+R)
- Check the Actions tab for build errors
- Verify your changes were pushed (`git status`)

### Issue: CSS/Styles not loading

**Solutions**:
- Check that `styles.css` is in the same directory as `index.html`
- Verify the path in index.html: `<link rel="stylesheet" href="styles.css">`
- Clear browser cache
- Check browser console for errors (F12)

### Issue: Images not showing

**Solutions**:
- Verify images are in the `assets` folder
- Check file paths are correct (case-sensitive)
- Ensure images are pushed to GitHub (`git status`)
- Use relative paths (e.g., `assets/staff/photo.jpg`)

---

## Making Updates

### Small Text Changes

For quick edits, you can use GitHub's web interface:

1. Navigate to the file on GitHub
2. Click the pencil icon (Edit)
3. Make your changes
4. Scroll down and click **Commit changes**
5. Wait 1-2 minutes for the site to update

### Local Development Workflow

For larger changes:

```bash
# 1. Make your changes in your code editor
# 2. Test locally by opening index.html in browser
# 3. Commit and push

git add .
git commit -m "Descriptive message about your changes"
git push origin main
```

---

## Best Practices

### Commit Messages

Use clear, descriptive commit messages:

✅ Good:
```bash
git commit -m "Add Week 5 lecture slides and quiz"
git commit -m "Update office hours information"
git commit -m "Fix broken link in syllabus"
```

❌ Bad:
```bash
git commit -m "update"
git commit -m "changes"
git commit -m "fix"
```

### Regular Backups

```bash
# Create a backup branch
git checkout -b backup-2026-01-20
git push origin backup-2026-01-20
git checkout main
```

### Testing Before Pushing

Always test locally:
1. Open `index.html` in your browser
2. Click all links to verify they work
3. Check responsive design (resize browser)
4. Verify all images load
5. Then commit and push

---

## Advanced: Using GitHub Actions

Create `.github/workflows/deploy.yml` for automated checks:

```yaml
name: Deploy to GitHub Pages

on:
  push:
    branches: [ main ]

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - name: Deploy to GitHub Pages
        uses: peaceiris/actions-gh-pages@v3
        with:
          github_token: ${{ secrets.GITHUB_TOKEN }}
          publish_dir: ./
```

---

## Monitoring Your Site

### GitHub Insights

Check your repository's:
- **Traffic**: See visitor statistics (Settings → Insights → Traffic)
- **Actions**: Monitor deployments (Actions tab)
- **Issues**: Track bugs or feature requests

### Google Analytics (Optional)

Add Google Analytics to track visitors:

1. Create a Google Analytics account
2. Get your tracking ID
3. Add this before `</head>` in `index.html`:

```html
<!-- Google Analytics -->
<script async src="https://www.googletagmanager.com/gtag/js?id=YOUR-GA-ID"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'YOUR-GA-ID');
</script>
```

---

## Useful Git Commands

```bash
# Check status
git status

# View commit history
git log --oneline

# Undo last commit (keep changes)
git reset --soft HEAD~1

# Undo last commit (discard changes)
git reset --hard HEAD~1

# View differences
git diff

# Pull latest changes
git pull origin main

# Create a new branch
git checkout -b new-feature

# Switch branches
git checkout main
```

---

## Security Tips

1. **Never commit sensitive information**:
   - API keys
   - Passwords
   - Email addresses (use contact forms instead)

2. **Use `.gitignore`** (already included):
   - Keeps system files out of Git
   - Prevents accidentally committing sensitive data

3. **Keep dependencies updated**:
   - Regularly update any libraries you use
   - Monitor for security vulnerabilities

---

## Getting Help

### Resources

- [GitHub Pages Documentation](https://docs.github.com/en/pages)
- [Git Documentation](https://git-scm.com/doc)
- [GitHub Community](https://github.community/)

### Troubleshooting

1. Check the **Actions** tab on GitHub for build errors
2. Look at the browser console (F12) for JavaScript errors
3. Verify your repository settings
4. Search GitHub Issues for similar problems

### Support

If you encounter issues:
1. Check this guide first
2. Review the GitHub Pages documentation
3. Search Stack Overflow
4. Consult with course staff or IT support

---

## Next Steps

After deployment:

1. ✅ Share your site URL with students
2. ✅ Add the URL to your syllabus
3. ✅ Test all links and functionality
4. ✅ Set up a regular update schedule
5. ✅ Monitor site analytics (if enabled)

---

**Congratulations! Your course website is now live! 🎉**

Remember to update content regularly throughout the semester.

# Design and Development of Generative AI Applications

A modern, clean GitHub Pages site for a Generative AI course.

## 🚀 Quick Start

1. **Enable GitHub Pages**
   - Go to your repository Settings
   - Navigate to Pages (in the left sidebar)
   - Under "Source", select the branch (usually `main`) and folder (`/ (root)`)
   - Click Save
   - Your site will be live at `https://[username].github.io/[repository-name]/`

2. **Customize the Content**
   - Edit `index.html` to update course information
   - Modify `styles.css` to change colors, fonts, and styling
   - Replace placeholder images with actual photos

## 📝 Customization Guide

### Changing Colors

Edit the CSS variables in `styles.css` (lines 5-20):

```css
:root {
    --primary-color: #005035;      /* Main brand color (Deep Green) */
    --secondary-color: #A49665;    /* Secondary brand color (Gold) */
    --accent-color: #B8A782;       /* Accent highlights (Light Gold) */
    /* ... more variables ... */
}
```

### Adding Staff/Speaker Photos

Replace the placeholder divs in `index.html` with actual images:

```html
<!-- Replace this: -->
<div class="staff-image-placeholder">
    <span>Photo</span>
</div>

<!-- With this: -->
<img src="assets/staff-name.jpg" alt="Staff Name" class="staff-image">
```

Then add this CSS to `styles.css`:

```css
.staff-image {
    width: 180px;
    height: 180px;
    border-radius: 50%;
    object-fit: cover;
    box-shadow: var(--shadow-md);
}
```

### Updating Course Information

Edit the following sections in `index.html`:

- **Course Title**: Line 19-20
- **Announcement**: Line 26-30
- **Class Info**: Lines 95-105
- **Course Description**: Lines 111-115
- **Syllabus**: Lines 122-164
- **Coursework**: Lines 171-196

### Adding More Weeks to Syllabus

Copy and paste a table row in the syllabus section:

```html
<tr>
    <td>Week X</td>
    <td><strong>Your Topic Title</strong></td>
    <td>
        <a href="#" class="material-link">Slides</a> | 
        <a href="#" class="material-link">Recording</a> | 
        <a href="#" class="material-link">Quiz</a>
    </td>
</tr>
```

## 🎨 Design Features

- **Modern Gradient Backgrounds**: Eye-catching header with gradient overlay
- **Responsive Design**: Looks great on desktop, tablet, and mobile
- **Hover Effects**: Interactive cards and links with smooth transitions
- **Clean Typography**: Using the Inter font family for readability
- **Organized Layout**: Clear sections with visual hierarchy
- **Accessible Colors**: High contrast for better readability

## 📁 File Structure

```
.
├── index.html          # Main HTML file
├── styles.css          # All styling
├── README.md          # This file
└── assets/            # (Create this folder for images)
    ├── staff/
    └── speakers/
```

## 🖼️ Adding Images

1. Create an `assets` folder in your repository
2. Add subfolders: `assets/staff/` and `assets/speakers/`
3. Upload your images
4. Update the HTML to reference them

Example:
```html
<img src="assets/staff/instructor-name.jpg" alt="Instructor Name">
```

## 🔗 Useful Links

- **GitHub Pages Documentation**: https://docs.github.com/en/pages
- **Inter Font**: https://fonts.google.com/specimen/Inter
- **HTML Reference**: https://developer.mozilla.org/en-US/docs/Web/HTML
- **CSS Reference**: https://developer.mozilla.org/en-US/docs/Web/CSS

## 💡 Tips

1. **Test Locally**: Open `index.html` in your browser before pushing to GitHub
2. **Use Git Commits**: Make small, incremental changes
3. **Backup**: Keep backups before making major design changes
4. **Mobile Testing**: Check how it looks on different screen sizes
5. **Browser Testing**: Test in Chrome, Firefox, and Safari

## 📱 Responsive Breakpoints

The site adapts to different screen sizes:
- **Mobile**: < 640px
- **Tablet**: 640px - 1023px
- **Desktop**: ≥ 1024px

## 🛠️ Advanced Customization

### Changing Fonts

Replace the Google Fonts link in `index.html` (line 9):

```html
<link href="https://fonts.googleapis.com/css2?family=Your+Font:wght@300;400;600;700&display=swap" rel="stylesheet">
```

Then update the font-family in `styles.css` (line 39):

```css
font-family: 'Your Font', sans-serif;
```

### Adding Custom Sections

Copy an existing section and modify:

```html
<section class="section">
    <h2 class="section-title">Your Section Title</h2>
    <div class="your-content">
        <!-- Your content here -->
    </div>
</section>
```

## 📞 Support

For questions or issues:
- Open an issue in the GitHub repository
- Consult the GitHub Pages documentation
- Check MDN Web Docs for HTML/CSS help

---

Built with ❤️ for teaching Generative AI

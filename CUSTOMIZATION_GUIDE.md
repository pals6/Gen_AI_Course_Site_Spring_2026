# Customization Guide

This guide will help you customize your course website step-by-step.

## Table of Contents

- [Quick Customizations](#quick-customizations)
- [Color Scheme](#color-scheme)
- [Course Information](#course-information)
- [Adding Content](#adding-content)
- [Advanced Customizations](#advanced-customizations)

---

## Quick Customizations

### 1. Update Course Title and Semester

**File**: `index.html`

Find lines 19-20 and update:

```html
<h1 class="course-title">Design and Development of Generative AI Applications</h1>
<p class="semester">Spring 2026</p>
```

### 2. Update Class Information

**File**: `index.html`

Find the class info section and update:

```html
<div class="info-item">
    <strong>Lecture Time:</strong> 2:00-3:30 PM Tuesday & Thursday
</div>
<div class="info-item">
    <strong>Location:</strong> Room 101, Computer Science Building
</div>
<div class="info-item">
    <strong>Office Hours:</strong> Wednesday 3-5 PM or by appointment
</div>
```

---

## Color Scheme

### Changing the Color Theme

**File**: `styles.css`

The site uses CSS variables for easy color customization. Find the `:root` section at the top of `styles.css`:

```css
:root {
    --primary-color: #6366f1;      /* Main purple - change this */
    --primary-dark: #4f46e5;       /* Darker purple for hovers */
    --secondary-color: #8b5cf6;    /* Secondary purple */
    --accent-color: #06b6d4;       /* Cyan accent */
    /* ... more colors ... */
}
```

### Current Color Scheme

**University Green & Gold (Current)**:
```css
--primary-color: #005035;      /* Deep green */
--primary-dark: #003d28;       /* Darker green for hovers */
--secondary-color: #A49665;    /* Gold */
--accent-color: #B8A782;       /* Light gold accent */
```

### Alternative Color Schemes

**Blue Theme**:
```css
--primary-color: #3b82f6;
--primary-dark: #2563eb;
--secondary-color: #06b6d4;
--accent-color: #8b5cf6;
```

**Modern Purple Theme**:
```css
--primary-color: #6366f1;
--primary-dark: #4f46e5;
--secondary-color: #8b5cf6;
--accent-color: #06b6d4;
```

**Orange/Red Theme**:
```css
--primary-color: #f59e0b;
--primary-dark: #d97706;
--secondary-color: #ef4444;
--accent-color: #8b5cf6;
```

---

## Course Information

### Update Course Description

**File**: `index.html`

Find the course description section (around lines 111-115):

```html
<div class="description-content">
    <p>Your first paragraph describing the course...</p>
    <p>Your second paragraph with more details...</p>
</div>
```

### Update Prospective Student Cards

**File**: `index.html`

Find the info cards section (around lines 33-58) and update the links and text:

```html
<div class="info-card">
    <div class="card-icon">📝</div>
    <h3>Sign Up</h3>
    <p>Register for the course through our signup form</p>
    <a href="YOUR_SIGNUP_LINK" class="card-link">Sign Up →</a>
</div>
```

---

## Adding Content

### Adding Course Staff

**File**: `index.html`

In the staff section, add more staff cards:

```html
<div class="staff-card">
    <div class="staff-image-placeholder">
        <span>Photo</span>
    </div>
    <h3 class="staff-name">Teaching Assistant Name</h3>
    <p class="staff-title">PhD Student, Computer Science</p>
    <a href="https://example.com" class="staff-link">Website</a>
</div>
```

### Adding Guest Speakers

Copy and paste speaker cards in the speakers section:

```html
<div class="speaker-card">
    <div class="speaker-image-placeholder">
        <span>Photo</span>
    </div>
    <h4 class="speaker-name">Dr. Jane Smith</h4>
    <p class="speaker-title">Senior Researcher</p>
    <p class="speaker-org">OpenAI</p>
</div>
```

### Adding Syllabus Weeks

**File**: `index.html`

In the syllabus table (around line 130), add rows:

```html
<tr>
    <td>Week 5</td>
    <td>
        <strong>Large Language Models</strong>
        <br>Guest Speaker: Dr. John Doe, Google DeepMind
        <br><em>Topics: Transformer architecture, training methods</em>
    </td>
    <td>
        <a href="slides/week5.pdf" class="material-link">Slides</a> | 
        <a href="https://youtube.com/..." class="material-link">Recording</a> | 
        <a href="quiz5.html" class="material-link">Quiz</a>
    </td>
</tr>
```

### Adding Assignments

**File**: `index.html`

In the coursework section (around line 183), update the assignment list:

```html
<div class="coursework-item">
    <h3>Assignments</h3>
    <p>Hands-on coding assignments to apply course concepts.</p>
    <ul>
        <li>Assignment 1: Introduction to LLM APIs (Due: Week 3)</li>
        <li>Assignment 2: Building a Chatbot (Due: Week 6)</li>
        <li>Assignment 3: Fine-tuning Models (Due: Week 9)</li>
        <li>Assignment 4: RAG Implementation (Due: Week 12)</li>
    </ul>
</div>
```

---

## Advanced Customizations

### Adding a Navigation Menu

Add this after the opening `<body>` tag in `index.html`:

```html
<nav class="navbar">
    <div class="nav-container">
        <a href="#staff">Staff</a>
        <a href="#syllabus">Syllabus</a>
        <a href="#coursework">Coursework</a>
        <a href="#contact">Contact</a>
    </div>
</nav>
```

Then add this CSS to `styles.css`:

```css
.navbar {
    background: white;
    box-shadow: var(--shadow-md);
    position: sticky;
    top: 0;
    z-index: 100;
    margin-bottom: 2rem;
}

.nav-container {
    max-width: 1200px;
    margin: 0 auto;
    padding: 1rem 2rem;
    display: flex;
    gap: 2rem;
    justify-content: center;
}

.navbar a {
    color: var(--text-secondary);
    text-decoration: none;
    font-weight: 600;
    transition: color 0.2s;
}

.navbar a:hover {
    color: var(--primary-color);
}
```

### Adding Section IDs for Navigation

Add IDs to your sections in `index.html`:

```html
<section class="section" id="staff">
    <h2 class="section-title">Course Staff</h2>
    ...
</section>

<section class="section" id="syllabus">
    <h2 class="section-title">Syllabus</h2>
    ...
</section>
```

### Custom Fonts

1. Choose a font from [Google Fonts](https://fonts.google.com/)
2. Update the link in `index.html` (line 9)
3. Update the font-family in `styles.css` (line 39)

Example with Poppins font:

**index.html**:
```html
<link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap" rel="stylesheet">
```

**styles.css**:
```css
font-family: 'Poppins', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
```

### Adding a Footer Logo

**File**: `index.html`

Update the footer section:

```html
<footer class="footer">
    <img src="assets/university-logo.png" alt="University Logo" style="width: 150px; margin-bottom: 1rem;">
    <p>Questions? Reach out to the course staff via <a href="mailto:course@university.edu">email</a>.</p>
    <p class="footer-note">This site is powered by GitHub Pages.</p>
</footer>
```

### Making the Background Solid Color

**File**: `styles.css`

Find the body styles (around line 39) and replace the gradient:

```css
/* Change from: */
background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);

/* To: */
background: #f5f7fa;
```

### Adding Social Media Links

Add this to the footer in `index.html`:

```html
<div class="social-links" style="margin: 1.5rem 0;">
    <a href="https://twitter.com/yourcourse" style="margin: 0 0.5rem;">
        <img src="https://img.icons8.com/color/48/twitter.png" alt="Twitter" style="width: 32px;">
    </a>
    <a href="https://youtube.com/yourcourse" style="margin: 0 0.5rem;">
        <img src="https://img.icons8.com/color/48/youtube.png" alt="YouTube" style="width: 32px;">
    </a>
    <a href="https://linkedin.com/in/yourcourse" style="margin: 0 0.5rem;">
        <img src="https://img.icons8.com/color/48/linkedin.png" alt="LinkedIn" style="width: 32px;">
    </a>
</div>
```

---

## Testing Your Changes

### Local Testing

1. Open `index.html` in your web browser
2. Check all sections and links
3. Test responsive design (resize browser window)
4. Verify all colors look good together

### Browser Testing

Test in multiple browsers:
- Chrome/Edge
- Firefox
- Safari

### Mobile Testing

Use browser dev tools:
1. Press F12 to open developer tools
2. Click the mobile device icon
3. Test different screen sizes (iPhone, iPad, etc.)

---

## Common Issues

### Images Not Showing

- Check file path is correct
- Ensure images are in the `assets` folder
- Verify file extension matches (case-sensitive on some systems)

### Styling Not Applying

- Clear browser cache (Ctrl+Shift+R or Cmd+Shift+R)
- Check for CSS syntax errors
- Verify the styles.css file is linked correctly

### GitHub Pages Not Updating

- Wait 1-2 minutes after pushing changes
- Check GitHub Actions tab for build errors
- Verify GitHub Pages is enabled in repository settings

---

## Need More Help?

- Check the [README.md](README.md) for basic setup
- Review [GitHub Pages Documentation](https://docs.github.com/en/pages)
- Consult [MDN Web Docs](https://developer.mozilla.org/) for HTML/CSS reference

---

**Happy Customizing! 🎨**

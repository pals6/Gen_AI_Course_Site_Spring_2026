# Content Templates

Copy and paste these templates when adding content to your course website.

---

## Table of Contents

- [Staff Member](#staff-member)
- [Guest Speaker](#guest-speaker)
- [Syllabus Week](#syllabus-week)
- [Assignment](#assignment)
- [Info Card](#info-card)

---

## Staff Member

### With Placeholder Image

```html
<div class="staff-card">
    <div class="staff-image-placeholder">
        <span>Photo</span>
    </div>
    <h3 class="staff-name">Dr. Jane Smith</h3>
    <p class="staff-title">Associate Professor, Computer Science</p>
    <a href="https://example.com/faculty/jsmith" class="staff-link">Website</a>
</div>
```

### With Actual Image

```html
<div class="staff-card">
    <img src="assets/staff/jane-smith.jpg" alt="Dr. Jane Smith"
         style="width: 180px; height: 180px; border-radius: 50%; object-fit: cover; margin-bottom: 1.25rem; box-shadow: var(--shadow-md);">
    <h3 class="staff-name">Dr. Jane Smith</h3>
    <p class="staff-title">Associate Professor, Computer Science</p>
    <a href="https://example.com/faculty/jsmith" class="staff-link">Website</a>
</div>
```

---

## Guest Speaker

### With Placeholder Image

```html
<div class="speaker-card">
    <div class="speaker-image-placeholder">
        <span>Photo</span>
    </div>
    <h4 class="speaker-name">Dr. John Doe</h4>
    <p class="speaker-title">Research Scientist</p>
    <p class="speaker-org">Google DeepMind</p>
</div>
```

### With Actual Image

```html
<div class="speaker-card">
    <img src="assets/speakers/john-doe.jpg" alt="Dr. John Doe"
         style="width: 120px; height: 120px; border-radius: 50%; object-fit: cover; margin-bottom: 1rem; box-shadow: var(--shadow-sm);">
    <h4 class="speaker-name">Dr. John Doe</h4>
    <p class="speaker-title">Research Scientist</p>
    <p class="speaker-org">Google DeepMind</p>
</div>
```

---

## Syllabus Week

### Basic Template

```html
<tr>
    <td>Week X</td>
    <td><strong>Topic Title Here</strong></td>
    <td>
        <a href="#" class="material-link">Slides</a> | 
        <a href="#" class="material-link">Recording</a> | 
        <a href="#" class="material-link">Quiz</a>
    </td>
</tr>
```

### With Guest Speaker

```html
<tr>
    <td>Week 5</td>
    <td>
        <strong>Advanced Prompt Engineering</strong>
        <br>Guest Speaker: Dr. Sarah Johnson, OpenAI
        <br><em>Topics: Chain-of-thought prompting, few-shot learning, prompt optimization</em>
    </td>
    <td>
        <a href="slides/week5-prompt-engineering.pdf" class="material-link">Slides</a> | 
        <a href="https://youtube.com/watch?v=..." class="material-link">Recording</a> | 
        <a href="https://forms.google.com/quiz5" class="material-link">Quiz</a>
    </td>
</tr>
```

### With Reading List

```html
<tr>
    <td>Week 8</td>
    <td>
        <strong>Retrieval Augmented Generation (RAG)</strong>
        <br><em>Topics: Vector databases, embeddings, semantic search</em>
        <br><strong>Readings:</strong>
        <br>• <a href="https://arxiv.org/..." style="color: var(--primary-color);">RAG Paper</a>
        <br>• <a href="https://..." style="color: var(--primary-color);">Blog: Building RAG Systems</a>
    </td>
    <td>
        <a href="slides/week8.pdf" class="material-link">Slides</a> | 
        <a href="https://youtube.com/..." class="material-link">Recording</a> | 
        <a href="#" class="material-link">Quiz</a>
    </td>
</tr>
```

### No Lecture (Holiday/Break)

```html
<tr>
    <td>Week 9</td>
    <td><strong>No Lecture — Spring Break</strong></td>
    <td>—</td>
</tr>
```

---

## Assignment

### Simple Assignment

```html
<div class="coursework-item">
    <h3>Assignment 1: Introduction to LLM APIs</h3>
    <p><strong>Due:</strong> February 15, 2026 at 11:59 PM</p>
    <p>In this assignment, you will learn to interact with OpenAI's GPT API and build a simple conversational agent.</p>
    <ul>
        <li>Part 1: API Setup and Authentication</li>
        <li>Part 2: Basic Text Completion</li>
        <li>Part 3: Multi-turn Conversations</li>
    </ul>
    <p><a href="assignments/assignment1.pdf" class="card-link">Assignment PDF →</a> | 
       <a href="https://github.com/course/assignment1" class="card-link">Starter Code →</a></p>
</div>
```

### Assignment with Grading Rubric

```html
<div class="coursework-item">
    <h3>Assignment 2: Building a Chatbot</h3>
    <p><strong>Due:</strong> March 1, 2026 at 11:59 PM</p>
    <p>Build a domain-specific chatbot using LangChain and your choice of LLM provider.</p>
    
    <h4>Requirements:</h4>
    <ul>
        <li>Implement conversation memory (20 points)</li>
        <li>Add at least 3 custom tools (30 points)</li>
        <li>Implement error handling (15 points)</li>
        <li>Documentation and code quality (20 points)</li>
        <li>Creativity and functionality (15 points)</li>
    </ul>
    
    <p><strong>Submission:</strong> Submit via GitHub Classroom</p>
    <p><a href="assignments/assignment2.pdf" class="card-link">Full Instructions →</a> | 
       <a href="#" class="card-link">Submit →</a></p>
</div>
```

---

## Info Card

### Default Info Card

```html
<div class="info-card">
    <div class="card-icon">📚</div>
    <h3>Resources</h3>
    <p>Access course materials, code examples, and helpful links</p>
    <a href="resources.html" class="card-link">View Resources →</a>
</div>
```

### Custom Icons

```html
<!-- Office Hours -->
<div class="info-card">
    <div class="card-icon">🕐</div>
    <h3>Office Hours</h3>
    <p>Drop in for help with assignments and concepts</p>
    <a href="#" class="card-link">Schedule →</a>
</div>

<!-- Textbook -->
<div class="info-card">
    <div class="card-icon">📖</div>
    <h3>Textbook</h3>
    <p>Required and recommended reading materials</p>
    <a href="#" class="card-link">View List →</a>
</div>

<!-- GitHub -->
<div class="info-card">
    <div class="card-icon">💻</div>
    <h3>GitHub Classroom</h3>
    <p>Submit assignments and access starter code</p>
    <a href="https://classroom.github.com/..." class="card-link">Go to Classroom →</a>
</div>

<!-- Resources -->
<div class="info-card">
    <div class="card-icon">📚</div>
    <h3>Resources</h3>
    <p>Access course materials and helpful links</p>
    <a href="#" class="card-link">View Resources →</a>
</div>
```

---

## Additional Resources Section

Add this as a new section in `index.html`:

```html
<section class="section">
    <h2 class="section-title">Resources</h2>
    
    <div class="coursework-item">
        <h3>📚 Recommended Readings</h3>
        <ul>
            <li><a href="https://..." style="color: var(--primary-color);">Introduction to Large Language Models</a> - Comprehensive overview</li>
            <li><a href="https://..." style="color: var(--primary-color);">Prompt Engineering Guide</a> - Best practices and techniques</li>
            <li><a href="https://..." style="color: var(--primary-color);">Building LLM Applications</a> - Practical guide</li>
        </ul>
    </div>
    
    <div class="coursework-item">
        <h3>🔧 Tools & Frameworks</h3>
        <ul>
            <li><a href="https://python.langchain.com/" style="color: var(--primary-color);">LangChain</a> - Framework for LLM applications</li>
            <li><a href="https://openai.com/" style="color: var(--primary-color);">OpenAI API</a> - GPT models API</li>
            <li><a href="https://huggingface.co/" style="color: var(--primary-color);">Hugging Face</a> - Model hub and tools</li>
        </ul>
    </div>
    
    <div class="coursework-item">
        <h3>💡 Tutorials & Examples</h3>
        <ul>
            <li><a href="#" style="color: var(--primary-color);">Tutorial 1: Your First Chatbot</a></li>
            <li><a href="#" style="color: var(--primary-color);">Tutorial 2: RAG Implementation</a></li>
            <li><a href="#" style="color: var(--primary-color);">Tutorial 3: Fine-tuning Models</a></li>
        </ul>
    </div>
</section>
```

---

## FAQ Section

Add this as a new section:

```html
<section class="section">
    <h2 class="section-title">Frequently Asked Questions</h2>
    
    <div class="coursework-item">
        <h3>How do I get API access?</h3>
        <p>All registered students will receive API credits for OpenAI and other providers. Check your email for access instructions.</p>
    </div>
    
    <div class="coursework-item">
        <h3>What programming language will we use?</h3>
        <p>The course primarily uses Python. Basic Python knowledge is recommended but not required.</p>
    </div>
    
    <div class="coursework-item">
        <h3>Are lectures recorded?</h3>
        <p>Yes, all lectures are recorded and will be available within 24 hours on the course website.</p>
    </div>
    
    <div class="coursework-item">
        <h3>How is the final grade calculated?</h3>
        <p>Final grades are calculated as follows: Assignments (40%), Quizzes (20%), Final Project (30%), Participation (10%).</p>
    </div>
</section>
```

---

## Tips for Using Templates

1. **Copy the entire block** including opening and closing tags
2. **Replace placeholder text** with your actual content
3. **Update links** to point to your files
4. **Test locally** before pushing to GitHub
5. **Keep consistent formatting** for a professional look

---

**Need more examples?** Check the existing `index.html` for additional patterns and structures you can adapt.

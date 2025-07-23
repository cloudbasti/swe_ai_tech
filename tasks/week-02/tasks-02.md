# 📚 Week 02: AI-Assisted Development Practice

## 🔧 Required Installations & Setup

Before starting the tasks, make sure you have the testing frameworks installed for both Python and JavaScript.

### 🐍 Python Testing Setup
<details>
<summary>Setting up pytest for Python testing</summary>

1. **Create and activate virtual environment**
   ```bash
   python -m venv venv
   ```

2. **Activate the environment**
   ```bash
   # On Windows:
   venv\Scripts\activate
   
   # On Unix or MacOS:
   source venv/bin/activate
   ```

3. **Install testing packages**
   ```bash
   pip install pytest==7.4.3 pytest-cov==4.1.0
   ```

4. **Create requirements file**
   ```bash
   echo "pytest==7.4.3
   pytest-cov==4.1.0" > requirements.txt
   ```

> 💡 **Tip**: Keep your virtual environment activated while working on the tasks
</details>

### 🟨 JavaScript Testing Setup
<details>
<summary>Setting up Jest for JavaScript testing</summary>

1. **Initialize npm project**
   ```bash
   npm init -y
   ```

2. **Install Jest testing framework**
   ```bash
   npm install --save-dev jest@29.7.0
   ```

3. **Update package.json scripts**
   ```json
   {
     "scripts": {
       "test": "jest",
       "test:watch": "jest --watch"
     }
   }
   ```

> 💡 **Tip**: Use `npm run test:watch` for automatic test running during development
</details>

### ✅ Verify Installation
<details>
<summary>Quick verification steps</summary>

**Python:**
```bash
pytest --version
```

**JavaScript:**
```bash
npm test
```

If both commands work without errors, you're ready to go!
</details>

## 🎯 Part 1: Code Snippets with Cursor AI

### ⭐ Key concepts we'll practice:
- Language syntax differences and similarities
- Basic function implementation patterns
- Data structure manipulation
- Control flow patterns
- Error handling approaches

### 💻 Task 1: Create Code Snippets with AI

Create different coding snippets in both JavaScript and Python using the Cursor AI features introduced in the lecture. Focus on basic functions, data structures, and control flow.

**What to implement:**
- **Basic Functions**: Arithmetic operations, string operations, array/list operations
- **Data Structures**: Arrays/lists, objects/dictionaries, sets
- **Control Flow**: Conditional statements, loops, error handling

> 💡 **Tip**: Use the AI features from the lecture to help you understand the differences between JavaScript and Python

## 🎯 Part 2: Testing Practice

### ⭐ Key concepts we'll cover:
- Understanding what testing means
- Setting up testing environments
- Writing your first tests
- Using AI to help with testing
- Test coverage basics

### 💻 Task 2: Create Tests with AI

First, verify your test suites work by creating simple "always true" tests:
- Python: `def test_works(): assert True`
- JavaScript: `test('works', () => { expect(true).toBe(true); });`

Then use the Cursor AI features to create tests for the code snippets you built in Part 1.

> 💡 **Tip**: Ask AI to help you understand what makes a good test and how to test different scenarios

## 🎯 Part 3: Documentation and Git Integration

### ⭐ Key concepts we'll cover:
- Pushing your work to GitHub
- Using Markdown for documentation
- Creating a professional project presentation

### 💻 Task 3: Share Your Work on GitHub 📤

Take the code you created in Part 1 and the tests from Part 2, then push it to GitHub. Use the Markdown skills you learned in the lecture to create good documentation for your project.

> 💡 **Tip**: Use AI to help you write good commit messages and improve your documentation

## 📋 Submission Requirements
<details>
<summary>What to submit</summary>

**GitHub Repository Link** containing:
- Your JavaScript and Python implementations from Part 1
- Test files from Part 2
- A well-written README.md file using Markdown
- Clear commit history

> 💡 **Tip**: Make sure your repository is public so it can be accessed and reviewed
</details>

<!-- 
Emoji Reference:
📚 - Main sections and resources
🔧 - Setup and installation
🎯 - Parts and objectives
⭐ - Key concepts
💻 - Tasks and exercises
📋 - Submission
💡 - Tips
⚠️ - Common mistakes
-->

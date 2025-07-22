# Week 3: API Development with Flask & Prompt Engineering

## 1. Installations & Setup

### Google Gemini CLI Installation
```bash
npm install -g @google/gemini-cli

# Set up API Key (Required) - Choose one of these methods:

# Method 1: Environment Variables
# For Linux/macOS (add to ~/.bashrc or ~/.zshrc):
export GEMINI_API_KEY=<YOUR_API_KEY_HERE>

# For Windows (via System Environment Variables):
# Add GEMINI_API_KEY with your API key

# Method 2: Using .env file
# Create a .env file in your project root and add your API key:
GEMINI_API_KEY=<YOUR_API_KEY_HERE>

# Note: Gemini CLI will automatically detect and load the API key from .env file
```

#### Important Resources for Gemini:
- [Official Gemini API Key Setup Guide](https://ai.google.dev/gemini-api/docs/api-key)
- [Gemini CLI GitHub Repository](https://github.com/google/gemini-cli)
- [Google AI Studio](https://makersuite.google.com/) - Get your API key here

### Python Flask Installation
```bash
# Create a virtual environment
python -m venv venv

# Activate virtual environment
# For Windows:
.\venv\Scripts\activate
# For Unix/MacOS:
source venv/bin/activate

# Install Flask
pip install flask
```

## 2. Prompt Engineering Fundamentals

### Key Concepts
- Understanding prompt components
- Context and specificity in prompts
- Chain of thought prompting
- Few-shot learning examples
- Temperature and creativity settings

### Best Practices
- Clear and specific instructions
- Structured output formatting
- Error handling in prompts
- Iterative refinement techniques
- Validation strategies

## 3. Rules Files with Cursor and Gemini CLI

### Cursor Rules Configuration
- Setting up `.cursor` directory
- Creating custom rules
- Syntax and structure guidelines
- Code style enforcement
- Integration with existing tools
- [Detailed Cursor Rules Documentation](https://docs.cursor.com/context/rules)

### Gemini CLI Rules
- Configuration file setup
- Custom prompt templates
- Response formatting rules
- Error handling patterns
- Version control integration

## 4. Professional Git Feature Branch Workflow

### Basic Workflow
```bash
# Create and switch to feature branch
git checkout -b feature/api-endpoints

# Make changes and commit regularly
git add .
git commit -m "feat: implement user authentication endpoint"

# Keep feature branch up to date
git checkout main
git pull
git checkout feature/api-endpoints
git rebase main

# Push feature branch and create PR
git push origin feature/api-endpoints
```

### Best Practices
- One feature/task per branch
- Branch naming convention: `feature/`, `bugfix/`, `hotfix/`, `docs/`
- Descriptive commit messages following conventional commits
- Regular rebasing with main branch
- Code review before merging
- Delete branches after merging

### PR Guidelines
- Clear PR description
- Link to related issues
- Include testing steps
- Add relevant reviewers
- Update documentation if needed

## 5. Building a REST API with Flask

### Basic Setup
```python
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({"message": "Welcome to our API"})

if __name__ == '__main__':
    app.run(debug=True)
```

### Core Concepts
- Route definitions
- HTTP methods (GET, POST, PUT, DELETE)
- Request handling
- Response formatting
- Error handling
- Data validation

### API Structure
- Resource organization
- Endpoint naming conventions
- Authentication setup
- Database integration
- Documentation

## 6. Integrating Prompt Engineering with API Development

### Creating Rules Files for API Endpoints
- Endpoint definition templates
- Input validation rules
- Response format specifications
- Error handling patterns
- Documentation requirements

### Testing Strategy
- Unit test templates
- Integration test setup
- Prompt-based test generation
- Validation scenarios
- Performance testing guidelines

### Implementation Steps
1. Define API specifications using prompt engineering
2. Generate endpoint templates
3. Create validation rules
4. Implement test cases
5. Document the integration process

## 6. Cursor Rule Examples

Check out [testing-rules.md](testing-rules.md) for examples of Cursor rules for different programming languages. These rules demonstrate how to structure and write code in Cursor for various languages and frameworks. The examples are sourced from [cursor.directory/rules/testing](https://cursor.directory/rules/testing), which is a collection of rule examples that can be used as templates in Cursor.

Note: This is not a general testing guide, but rather a showcase of Cursor-specific rule examples for different programming languages.

## Resources & References
- [Flask Documentation](https://flask.palletsprojects.com/)
- [Google Gemini CLI Documentation](https://github.com/google/gemini-cli)
- [REST API Best Practices](https://restfulapi.net/)
- [Prompt Engineering Guide](https://www.promptingguide.ai/)

## Assignment
1. Set up a Flask API with at least 3 endpoints
2. Create rules files for API validation
3. Generate test cases using prompt engineering
4. Document your implementation process
5. Submit your code and documentation

## Evaluation Criteria
- Code functionality and structure
- Rules file implementation
- Test coverage and quality
- Documentation completeness
- Prompt engineering effectiveness 
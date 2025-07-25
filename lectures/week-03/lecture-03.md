# 📚 Week 03: Prompt Engineering, Cursor Rules & Git Workflows

## 🎯 Learning Objectives
By the end of this lecture, students will be able to:
- Apply prompt engineering fundamentals and best practices
- Configure and use Cursor rules files effectively
- Implement professional Git feature branch workflows
- Integrate AI tools with development workflows

## 🔧 Prerequisites
<details>
<summary>Required Setup & Knowledge</summary>

- Basic Git knowledge
- Text editor or IDE setup
- Understanding of command line basics
- Basic programming concepts
</details>

## 📖 Part 1: Prompt Engineering Fundamentals
<!-- Understanding how to effectively communicate with AI tools -->

### ⭐ Key Concepts
<details>
<summary>Core Concepts Overview</summary>

- **Prompt Components**
  - Clear and specific instructions
  - Context and background information
  - Expected output format
- **Chain of Thought Prompting**
  - Step-by-step reasoning process
  - Breaking down complex problems
  - Logical progression of ideas
- **Few-shot Learning Examples**
  - Providing examples for guidance
  - Pattern recognition through examples
  - Consistent formatting demonstrations
- **Temperature and Creativity Settings**
  - Controlling randomness in responses
  - Balancing creativity with accuracy
  - Optimizing for specific use cases

> 💡 **Key Point**: Specificity and context are crucial for effective AI communication
</details>

### 💻 Best Practices Examples
<details>
<summary>Implementation Examples</summary>

```markdown
# Good Prompt Structure
Context: I'm building a REST API with Flask
Task: Create a user authentication endpoint
Requirements: 
- Include input validation
- Return proper HTTP status codes
- Handle errors gracefully
Format: Provide complete Python code with comments
```

```markdown
# Chain of Thought Example
Please solve this step by step:
1. First, analyze the requirements
2. Then, design the endpoint structure
3. Finally, implement with error handling
```

> ⚠️ **Common Mistake**: Vague prompts lead to generic, unhelpful responses
</details>

### 🏃 Hands-on Activity
<details>
<summary>Activity: Prompt Refinement Practice</summary>

#### Steps:
1. Write a basic prompt for a coding task
2. Identify missing context and specificity
3. Refine the prompt using best practices
4. Compare results between versions

> 📝 **Note**: Document the differences in response quality for future reference
</details>

### 💭 Discussion
<details>
<summary>Discussion Topics</summary>

- Key Question: How does prompt specificity affect AI output quality?
- Follow-up Questions:
  - When should you use few-shot vs zero-shot prompting?
  - How do you balance creativity with accuracy in prompts?
</details>

## 📖 Part 2: Rules Files with Cursor
<!-- Configuring development environment with custom rules -->

### ⭐ Key Concepts
<details>
<summary>Core Concepts Overview</summary>

- **Cursor Rules Configuration**
  - Setting up `.cursor` directory structure
  - Understanding rule file syntax
  - Applying rules to specific file types
- **Custom Rules Creation**
  - Code style enforcement patterns
  - Project-specific guidelines
  - Integration with existing tools
- **Rule File Structure**
  - YAML frontmatter configuration
  - Markdown content organization
  - Glob patterns for file targeting

> 💡 **Key Point**: Rules files ensure consistency across team development workflows
</details>

### 💻 Configuration Examples
<details>
<summary>Implementation Examples</summary>

```bash
# Directory structure
.cursor/
├── rules/
│   ├── project/
│   │   ├── backend/
│   │   ├── frontend/
│   │   └── database/
│   └── course/
```

```yaml
# Example rule file header
---
description: Standards for Flask API development
globs: ["backend/**/*.py"]
alwaysApply: false
---
```

> ⚠️ **Common Mistake**: Overly restrictive rules can hinder development speed
</details>

### 🏃 Hands-on Activity
<details>
<summary>Activity: Create Custom Rules</summary>

#### Steps:
1. Analyze your current project structure
2. Identify areas needing consistency
3. Create appropriate rule files
4. Test rule application

> 📝 **Note**: Start with simple rules and gradually add complexity
</details>

## 📖 Part 3: Professional Git Feature Branch Workflow
<!-- Implementing industry-standard version control practices -->

### ⭐ Key Concepts
<details>
<summary>Core Concepts Overview</summary>

- **Feature Branch Strategy**
  - One feature per branch isolation
  - Parallel development capabilities
  - Risk minimization approach
- **Branch Naming Conventions**
  - `feature/` for new functionality
  - `bugfix/` for bug corrections
  - `hotfix/` for urgent fixes
- **Pull Request Process**
  - Code review integration
  - Automated testing triggers
  - Documentation requirements

> 💡 **Key Point**: Feature branches enable safe parallel development and easy rollbacks
</details>

### 💻 Workflow Examples
<details>
<summary>Implementation Examples</summary>

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

```bash
# Conventional commit examples
git commit -m "feat: add user login endpoint"
git commit -m "fix: resolve authentication token expiry"
git commit -m "docs: update API documentation"
```

> ⚠️ **Common Mistake**: Working directly on main branch bypasses review processes
</details>

### 🏃 Hands-on Activity
<details>
<summary>Activity: Feature Branch Practice</summary>

#### Steps:
1. Create a feature branch for a small task
2. Make commits with conventional messages
3. Rebase with main branch
4. Create and review a pull request

> 📝 **Note**: Practice the complete workflow including cleanup after merge
</details>

### 💭 Discussion
<details>
<summary>Discussion Topics</summary>

- Key Question: How does feature branching improve team collaboration?
- Follow-up Questions:
  - When should you rebase vs merge?
  - How do you handle merge conflicts effectively?
</details>

## 📖 Part 4: REST API Theory & Implementation
<!-- Understanding RESTful architecture principles and practical endpoint design -->

### ⭐ Key Concepts
<details>
<summary>Core Concepts Overview</summary>

- **REST Principles**
  - Representational State Transfer architecture
  - Stateless communication between client and server
  - Resource-based URL structure
  - Uniform interface design
- **HTTP Methods & Their Purpose**
  - `GET` - Retrieve data (safe, idempotent)
  - `POST` - Create new resources
  - `PUT` - Update/replace entire resource (idempotent)
  - `PATCH` - Partial updates to resource
  - `DELETE` - Remove resources (idempotent)
- **Status Codes**
  - 2xx Success (200 OK, 201 Created, 204 No Content)
  - 4xx Client Errors (400 Bad Request, 404 Not Found, 422 Validation Error)
  - 5xx Server Errors (500 Internal Server Error)
- **Resource Naming Conventions**
  - Use nouns, not verbs (users, not getUsers)
  - Plural for collections (/users)
  - Singular for specific resources (/users/123)

> 💡 **Key Point**: REST APIs should be intuitive and predictable - anyone should understand what an endpoint does from its URL and HTTP method
</details>

### 💻 Implementation Examples
<details>
<summary>Flask REST API Examples</summary>

```python
from flask import Flask, request, jsonify
from werkzeug.exceptions import BadRequest

app = Flask(__name__)

# Sample data store (in production, use a database)
users = [
    {"id": 1, "name": "Alice", "email": "alice@example.com"},
    {"id": 2, "name": "Bob", "email": "bob@example.com"}
]

# GET /users - Retrieve all users
@app.route('/users', methods=['GET'])
def get_users():
    return jsonify({
        "status": "success",
        "data": users,
        "count": len(users)
    }), 200

# GET /users/<id> - Retrieve specific user
@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = next((u for u in users if u["id"] == user_id), None)
    if not user:
        return jsonify({
            "status": "error",
            "message": "User not found"
        }), 404
    
    return jsonify({
        "status": "success",
        "data": user
    }), 200

# POST /users - Create new user
@app.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    
    # Input validation
    if not data or 'name' not in data or 'email' not in data:
        return jsonify({
            "status": "error",
            "message": "Name and email are required"
        }), 400
    
    # Email format validation (basic)
    if '@' not in data['email']:
        return jsonify({
            "status": "error",
            "message": "Invalid email format"
        }), 422
    
    # Create new user
    new_user = {
        "id": max([u["id"] for u in users]) + 1 if users else 1,
        "name": data['name'],
        "email": data['email']
    }
    users.append(new_user)
    
    return jsonify({
        "status": "success",
        "message": "User created successfully",
        "data": new_user
    }), 201

# PUT /users/<id> - Update entire user
@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    user = next((u for u in users if u["id"] == user_id), None)
    if not user:
        return jsonify({
            "status": "error",
            "message": "User not found"
        }), 404
    
    data = request.get_json()
    if not data or 'name' not in data or 'email' not in data:
        return jsonify({
            "status": "error",
            "message": "Name and email are required"
        }), 400
    
    # Update user data
    user['name'] = data['name']
    user['email'] = data['email']
    
    return jsonify({
        "status": "success",
        "message": "User updated successfully",
        "data": user
    }), 200

# DELETE /users/<id> - Delete user
@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    global users
    user = next((u for u in users if u["id"] == user_id), None)
    if not user:
        return jsonify({
            "status": "error",
            "message": "User not found"
        }), 404
    
    users = [u for u in users if u["id"] != user_id]
    
    return jsonify({
        "status": "success",
        "message": "User deleted successfully"
    }), 200

# Error handling middleware
@app.errorhandler(400)
def bad_request(error):
    return jsonify({
        "status": "error",
        "message": "Bad request"
    }), 400

@app.errorhandler(500)
def internal_error(error):
    return jsonify({
        "status": "error",
        "message": "Internal server error"
    }), 500

if __name__ == '__main__':
    app.run(debug=True)
```

```python
# Advanced validation example using marshmallow
from marshmallow import Schema, fields, ValidationError

class UserSchema(Schema):
    name = fields.Str(required=True, validate=lambda x: len(x) >= 2)
    email = fields.Email(required=True)
    age = fields.Int(validate=lambda x: x >= 0)

user_schema = UserSchema()

@app.route('/users/validated', methods=['POST'])
def create_user_validated():
    try:
        # Validate input data
        data = user_schema.load(request.get_json())
    except ValidationError as err:
        return jsonify({
            "status": "error",
            "message": "Validation failed",
            "errors": err.messages
        }), 422
    
    # Process valid data...
    return jsonify({"status": "success", "data": data}), 201
```

> ⚠️ **Common Mistake**: Forgetting to handle edge cases like missing data or invalid IDs
</details>

### 🏃 Hands-on Activity
<details>
<summary>Activity: Build Your First REST API</summary>

#### Steps:
1. **Design Your Resource**: Choose a simple resource (books, products, tasks)
2. **Plan Your Endpoints**: 
   - List what operations you need (CRUD)
   - Design URL structure following REST conventions
3. **Implement Basic CRUD**:
   ```python
   # Start with this template
   from flask import Flask, request, jsonify
   
   app = Flask(__name__)
   # Your resource data here
   
   # Implement each endpoint one by one
   ```
4. **Add Validation**: Include input validation for POST/PUT requests
5. **Test Your API**: Use tools like Postman or curl to test each endpoint

#### Testing Commands:
```bash
# Test GET all
curl http://localhost:5000/users

# Test POST (create)
curl -X POST http://localhost:5000/users \
  -H "Content-Type: application/json" \
  -d '{"name": "John", "email": "john@example.com"}'

# Test GET specific
curl http://localhost:5000/users/1

# Test PUT (update)
curl -X PUT http://localhost:5000/users/1 \
  -H "Content-Type: application/json" \
  -d '{"name": "John Doe", "email": "johndoe@example.com"}'

# Test DELETE
curl -X DELETE http://localhost:5000/users/1
```

> 📝 **Note**: Start simple with in-memory data, focus on getting the structure right before adding database complexity
</details>

### 💭 Discussion
<details>
<summary>Discussion Topics</summary>

- Key Question: Why do we use different HTTP methods instead of just POST for everything?
- Follow-up Questions:
  - When would you use PUT vs PATCH for updates?
  - How do you decide what HTTP status code to return?
  - What makes an API "RESTful" vs just HTTP endpoints?
  - How do you handle relationships between resources (e.g., user posts)?
</details>

## 📚 Additional Resources
<details>
<summary>Learning Materials</summary>

### Required Reading
- [Cursor Rules Documentation](https://docs.cursor.com/context/rules)
- [Prompt Engineering Guide](https://www.promptingguide.ai/)
- [Git Feature Branch Workflow](https://www.atlassian.com/git/tutorials/comparing-workflows/feature-branch-workflow)
- [REST API Design Best Practices](https://restfulapi.net/)
- [Flask Documentation](https://flask.palletsprojects.com/)

### Optional Further Reading
- [Advanced Git Workflows](https://nvie.com/posts/a-successful-git-branching-model/)
- [AI-Assisted Development Best Practices](https://github.blog/2023-06-20-how-to-write-better-prompts-for-github-copilot/)
- [HTTP Status Codes Reference](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status)
- [API Design Patterns](https://microservice-api-patterns.org/)
</details>

## 📋 Assignment Preview
<details>
<summary>Upcoming Tasks</summary>

Students will practice integrating these three concepts by:
- Setting up Cursor rules for a project
- Using prompt engineering to generate code
- Managing development through feature branches
</details>

## ⏭️ Next Steps
<details>
<summary>Preparation for Next Session</summary>

- Review Git branching strategies
- Prepare development environment with Cursor rules
- Practice prompt engineering techniques
- Preview API development concepts
</details>

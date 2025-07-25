# 📚 Week 04: Advanced Prompt Engineering with Rules and Templates

## 🎯 Learning Objectives
By the end of this lecture, students will be able to:
- Distinguish between persona-based prompting and language-specific rules
- Combine prompt engineering personas with programming rules for enhanced AI output
- Implement templating strategies for reusable content and rule creation
- Apply rule-based AI guidance in real-world development scenarios

## 🔧 Prerequisites
<details>
<summary>Required Setup & Knowledge</summary>

- Basic understanding of prompt engineering concepts
- Familiarity with AI personas (#simple-create, #expert-mentor, etc.)
- Basic programming knowledge (any language)
- Understanding of software engineering principles
- Access to Cursor or similar AI-enhanced editor
</details>

## 📖 Part 1: AI Guidance Types - Personas vs Language Rules

### ⭐ Key Concepts
<details>
<summary>Understanding the Two Dimensions of AI Control</summary>

- **Persona-Based Prompting (HOW to deliver)**
  - Controls AI's communication style and depth
  - Determines explanation level and approach
  - Examples: #simple-create, #expert-mentor, #detailed-guide
  - Focus: Response style, educational value, complexity level

- **Language-Specific Rules (WHAT to implement)**
  - Controls technical implementation details
  - Enforces coding standards and conventions
  - Examples: CSS naming conventions, Python package preferences, React patterns
  - Focus: Code quality, consistency, best practices

> 💡 **Key Point**: Personas control the "personality" of the AI response, while language rules control the technical content and implementation standards.
</details>

### 💻 Code Examples
<details>
<summary>Comparison Examples</summary>

**Scenario: Create a PUT endpoint to update user data (with Python + Flask rules files active)**

**Prompt Example 1:**
```
#simple-create Create a PUT endpoint to update user data
```

**Output (#simple-create):**
```python
from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

@app.route('/api/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    data = request.get_json()
    
    if not data or 'firstname' not in data or 'lastname' not in data:
        return jsonify({'error': 'firstname and lastname required'}), 400
    
    with get_db_connection() as conn:
        cursor = conn.cursor()
        cursor.execute('''
            UPDATE users 
            SET firstname = ?, lastname = ?, updated_at = CURRENT_TIMESTAMP
            WHERE id = ?
        ''', (data['firstname'], data['lastname'], user_id))
        conn.commit()
        
        if cursor.rowcount == 0:
            return jsonify({'error': 'User not found'}), 404
            
    return jsonify({'message': 'User updated successfully'}), 200
```

**Prompt Example 2:**
```
#expert-mentor Create a PUT endpoint to update user data
```

**Output (#expert-mentor):**
```python
from flask import Flask, request, jsonify
import sqlite3
from contextlib import contextmanager

app = Flask(__name__)

@app.route('/api/users/<int:user_id>', methods=['PUT'])
def update_user_full(user_id):
    """
    Full user update (PUT) - replaces entire resource
    
    Educational Insight: PUT is idempotent and should replace the entire resource.
    This endpoint requires all fields to be provided, following REST conventions.
    Use PUT when you want to completely replace a resource.
    
    Flask Pattern: We use Flask's request object to handle JSON data and jsonify()
    for consistent JSON responses. The route decorator defines our REST endpoint.
    
    Args:
        user_id (int): The ID of the user to update
        
    Returns:
        Flask Response: JSON response with updated user data or error message
    """
    # Validate user existence first for better error handling
    if not user_exists(user_id):
        return jsonify({'error': 'User not found'}), 404
    
    data = request.get_json()
    
    # For PUT, require all fields as we're replacing the entire resource
    is_valid, error_msg = validate_user_data(data, required_fields=['firstname', 'lastname'])
    if not is_valid:
        return jsonify({'error': error_msg}), 400
    
    try:
        with get_db_connection() as conn:
            cursor = conn.cursor()
            cursor.execute('''
                UPDATE users 
                SET firstname = ?, lastname = ?, updated_at = CURRENT_TIMESTAMP
                WHERE id = ?
            ''', (data['firstname'].strip(), data['lastname'].strip(), user_id))
            conn.commit()
            
            if cursor.rowcount == 0:
                return jsonify({'error': 'User not found'}), 404
                
        return jsonify({
            'message': 'User updated successfully',
            'user': {
                'id': user_id,
                'firstname': data['firstname'].strip(),
                'lastname': data['lastname'].strip()
            }
        }), 200
        
    except sqlite3.Error as e:
        return jsonify({'error': 'Database error occurred'}), 500
```

> 💡 **Key Insight**: Language rules are **always active** when rules files exist. Personas only control the explanation depth and teaching approach, not whether technical standards are applied.

> ⚠️ **Common Mistake**: Thinking you need to mention rules in your prompt - the AI automatically reads and applies available rules files
</details>

### 🏃 Hands-on Activity
<details>
<summary>Activity: Persona vs Rules Comparison</summary>

#### Steps:
1. Create a simple function with only `#simple-create`
2. Create the same function with only language-specific rules
3. Create the same function with both `#expert-mentor` + language rules
4. Compare outputs and document differences

> 📝 **Note**: Focus on observing how persona affects explanation depth while rules affect code structure
</details>

## 📖 Part 2: Combining Prompt Engineering with Rules

### Part 2A: Persona-Rule Integration
<details>
<summary>Strategic Combination Approaches</summary>

- **Layered Approach**: Persona + Language Rules + Project Rules
  - Base layer: Technical implementation standards
  - Style layer: How to communicate and explain
  - Context layer: Project-specific requirements

- **Hash-Based Triggers**: `#persona-name` at prompt start
  - Immediately signals desired response style
  - Works with any underlying rule system
  - Stackable with multiple rule types

> 💡 **Key Point**: Personas and rules are complementary - personas enhance the delivery of rule-compliant content
</details>

### Part 2B: Language-Specific Implementation Examples
<details>
<summary>Real-World Rule Applications</summary>

**Python Rules Example:**
```python
# Rule: Use Flask for APIs, SQLAlchemy for DB, type hints required
@app.route('/api/users', methods=['POST'])
def create_user(data: Dict[str, Any]) -> Tuple[Dict, int]:
    # Implementation follows established patterns
```

**CSS Rules Example:**
```css
/* Rule: BEM methodology, mobile-first, CSS custom properties */
.button {
  --button-color: #007bff;
  --button-padding: 0.75rem 1.5rem;
}

.button--primary {
  background-color: var(--button-color);
}
```

**JavaScript Rules Example:**
```javascript
// Rule: ES6+, functional components, TypeScript interfaces
interface ButtonProps {
  variant: 'primary' | 'secondary';
  onClick: () => void;
}

export const Button: React.FC<ButtonProps> = ({ variant, onClick }) => {
  // Implementation follows team standards
};
```

> ⚠️ **Common Mistake**: Applying generic rules instead of project-specific ones - always customize rules to your team's standards
</details>

### 🏃 Hands-on Activity
<details>
<summary>Activity: Building a Rule-Persona System</summary>

#### Steps:
1. Define language-specific rules for your project
2. Choose appropriate personas for different scenarios
3. Test combinations with real coding tasks
4. Document which combinations work best for different use cases

> 📝 **Note**: Different development phases may require different persona-rule combinations
</details>

### 💭 Discussion
<details>
<summary>Discussion Topics</summary>

- Key Question: When should you prioritize persona choice vs rule refinement?
- Follow-up Questions:
  - How do you handle conflicts between persona style and technical requirements?
  - What happens when team standards evolve - do you update personas or rules first?
</details>

## 📖 Part 3: Templating and Reusability Principles

### ⭐ Key Concepts
<details>
<summary>Templates as Software Engineering Assets</summary>

- **Content Templates**
  - Standardized structures for consistent output
  - Reusable across projects and team members
  - Examples: API documentation, component structures, test suites

- **Rule Templates**
  - Standardized rule sets for different project types
  - Shareable team conventions
  - Examples: Frontend rules, Backend rules, Testing rules

- **DRY Principle Applied to AI Guidance**
  - Don't Repeat Yourself - create reusable prompts
  - Version control for rule evolution
  - Team-wide consistency through shared templates

> 💡 **Key Point**: Templates are not just for code - they're essential for maintaining consistent AI assistance across teams and projects
</details>

### 💻 Implementation Examples
<details>
<summary>Template Structure Examples</summary>

**Rule Template Structure:**
```markdown
## [Language] Rules Template
### Core Principles
- Principle 1
- Principle 2

### Required Patterns
- Pattern implementation details

### Forbidden Practices
- Anti-patterns to avoid

### Integration Notes
- How to combine with personas
```

**Content Template Example:**
```markdown
## API Endpoint Template
### Purpose: [Brief description]
### Method: [GET/POST/PUT/DELETE]
### Parameters: [List and types]
### Response: [Expected format]
### Error Handling: [Status codes and messages]
```

> ⚠️ **Common Mistake**: Creating templates that are too rigid - leave room for context-specific adaptations
</details>

### 🏃 Hands-on Activity
<details>
<summary>Activity: Create Your Template Library</summary>

#### Steps:
1. Identify 3 recurring development tasks in your work
2. Create rule templates for each task type
3. Design content templates that work with your rule templates
4. Test templates with different personas to ensure compatibility
5. Version and document your template library

> 📝 **Note**: Start small and expand - successful templates are those that actually get used regularly
</details>

### 💭 Discussion
<details>
<summary>Template Strategy Discussion</summary>

- Key Question: How do you balance template consistency with creative flexibility?
- Follow-up Questions:
  - What's the right level of template granularity for your team?
  - How do you handle template evolution and backwards compatibility?
  - When should you break template rules for special cases?
</details>

## 📚 Additional Resources
<details>
<summary>Learning Materials</summary>

### Required Reading
- [Cursor Rules Documentation](https://cursor.sh/docs)
- [Prompt Engineering Guide - Advanced Techniques](https://github.com/dair-ai/Prompt-Engineering-Guide)

### Optional Further Reading
- [Software Engineering Templates and Patterns](https://refactoring.guru/design-patterns)
- [Team Coding Standards Best Practices](https://google.github.io/styleguide/)
</details>

## 📋 Assignment Preview
<details>
<summary>Upcoming Tasks</summary>

Students will create a complete rule-persona system for a mock project, including:
- Language-specific rule definitions
- Persona selection strategy
- Template library with at least 5 reusable components
- Documentation of when to use each combination
</details>

## ⏭️ Next Steps
<details>
<summary>Preparation for Next Session</summary>

- Preview: Advanced AI integration patterns and workflow automation
- Preparation: Install workflow automation tools and review team collaboration strategies
- Bring: Real project examples where these techniques could be applied
</details> 
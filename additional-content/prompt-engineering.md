THIS CONTENT IS RATHER FOR A LECTURE. 
---
title: Prompt Engineering Guidelines
description: Best practices and guidelines for effective prompt engineering when working with AI systems
globs: ["**/*"]
alwaysApply: true
---

# Prompt Engineering Guidelines

## Core Principles

### 1. Clarity and Specificity
- Be explicit about what you want the AI to do
- Provide clear context and constraints
- Use specific examples when possible
- Avoid ambiguous language

### 2. Structured Prompts
- Use clear formatting (headers, bullets, numbers)
- Break complex requests into smaller, manageable parts
- Provide step-by-step instructions when needed
- Use consistent terminology throughout

### 3. Context Management
- Provide relevant background information
- Include necessary technical details
- Reference specific files, functions, or components when applicable
- Maintain context continuity across conversations

## Best Practices

### For Code Generation
- Specify programming language and version
- Include relevant imports and dependencies
- Provide examples of expected input/output
- Mention coding standards or style guides to follow
- Include error handling requirements

### For Analysis Tasks
- Define the scope of analysis clearly
- Specify the format of expected results
- Include relevant data sources or file paths
- Mention any constraints or limitations

### For Documentation
- Specify the target audience (developers, users, etc.)
- Include the level of technical detail required
- Mention formatting requirements (Markdown, HTML, etc.)
- Provide examples of preferred documentation style

## Prompt Structure Template

```
## Context
[Provide background information]

## Objective
[Clear statement of what you want accomplished]

## Requirements
- [Specific requirement 1]
- [Specific requirement 2]
- [Specific requirement N]

## Constraints
- [Any limitations or restrictions]

## Examples
[Provide relevant examples if applicable]

## Expected Output
[Describe the format and content of expected results]
```

## Anti-Patterns to Avoid

### Vague Requests
❌ "Make this better"
✅ "Improve the performance of this function by optimizing the algorithm and reducing memory usage"

### Missing Context
❌ "Fix the bug"
✅ "Fix the authentication bug in the login function that causes users to be logged out after 5 minutes instead of the expected 24 hours"

### Overly Complex Single Prompts
❌ "Create a full-stack application with authentication, database, API, and frontend"
✅ Break into multiple specific prompts for each component

## Quality Indicators

### Good Prompts Should:
- Have a clear, single objective
- Include all necessary context
- Specify constraints and requirements
- Provide examples when helpful
- Use appropriate technical terminology

### Signs of Poor Prompts:
- Multiple unrelated objectives
- Missing critical context
- Vague or ambiguous language
- No clear success criteria
- Overly broad scope

## Iterative Refinement

### When Results Don't Match Expectations:
1. Review the original prompt for clarity
2. Identify missing context or constraints
3. Provide more specific examples
4. Break complex requests into smaller parts
5. Clarify the expected output format

### Continuous Improvement:
- Keep track of effective prompt patterns
- Document successful approaches for similar tasks
- Refine prompts based on AI responses
- Build a library of proven prompt templates

## Implementation Guidelines

### For Development Teams
- Establish prompt templates for common tasks
- Share effective prompts across team members
- Document prompt engineering decisions
- Review and refine prompts regularly

### For Individual Use
- Start with simple, clear requests
- Gradually add complexity as needed
- Maintain a personal prompt library
- Practice iterative refinement techniques

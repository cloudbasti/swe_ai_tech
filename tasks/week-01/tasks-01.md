# 📚 Week One: Getting Started with Cursor and Git

## 🔧 Required Installations & Setup
<details>
<summary>Installation Requirements</summary>

### 1. Cursor AI
- Download and install Cursor AI from [https://cursor.sh/](https://cursor.sh/)
- Set up your development environment with Cursor AI
- Familiarize yourself with the basic features and AI capabilities

### 2. GitHub Account
- Create a GitHub account at [https://github.com](https://github.com)
- Complete your GitHub profile setup
</details>

## 🎯 Part 1: Basic Environment Setup

### ⭐ Key concepts we'll cover:
- Setting up development environment
- Basic terminal navigation
- File system operations
- Git fundamentals

### 💻 Task 1: Getting Started with Cursor AI Locally
<details>
<summary>Setting Up Your Workspace</summary>

1. Create a new folder for this course on your computer (choose a location you can easily find)
2. Open a new Cursor project
3. Open a terminal (click the three dots in the upper navigation bar and select 'Terminal')
   - Run this command: `pwd`
4. Check if the path shown matches your course folder
   - If not, go to File > Open Folder and select your course folder
   - Run `pwd` again to verify you're in the correct location

> 💡 **Tip**: Keep your course folder organized from the start!
</details>

### 💻 Task 2: Basic Terminal Commands (Manual Practice)
<details>
<summary>Essential Terminal Operations</summary>

Practice these commands manually first to understand their behavior:

1. Working with Files
   - Run `ls` to list the files in your directory
   - Create a new file by running `touch README.md`
   - Run `ls` again to verify the file was created

2. Directory Operations
   - Create a new directory: `mkdir practice`
   - Copy the README file: `cp README.md practice/README.md`
   - Change to the practice directory: `cd practice`
   - Run `ls` to verify the file is there
   - Return to the main directory: `cd ..`
   - Remove the copied file: `rm practice/README.md`

3. Moving and Renaming Files
   - First, explore the mv command: `mv --help`
   - Read through the help text to understand how mv works
   - Create a directory of your choice: `mkdir your_directory_name`
   - Use mv to move README.md into your new directory
   - Create a new file: `touch DOCKERfile`
   - Use mv to rename DOCKERfile to DOCKERFILE (this is a common convention fix)
   - Run `ls` to verify your changes
   - Try to make yourself clear about these two differences of the move command

4. Terminal History and Clearing
   - Clear your terminal screen by typing `clear`
   - Use the `history` command to see all commands you've typed so far
   - Notice how this helps you track what you've done in your terminal session
   - Pro tip: You can use the up arrow key to cycle through previous commands!
   - Find any `ls` command in your history and rerun it using `!NUMBER` (replace NUMBER with the command's history number)
   - For example, if `ls` was command number 123, type `!123` to run it again

> ⚠️ **Note**: Type commands manually for better learning - don't copy-paste!
</details>

## 🎯 Part 2: AI-Assisted Development Practice

### ⭐ Key concepts we'll cover:
- Understanding Cursor AI chat functionality
- Using AI for file system operations
- Leveraging AI for task automation
- Learning through AI interaction

### 💻 Task 3: Explore Cursor AI Chat
<details>
<summary>AI Chat Features</summary>

1. Chat Settings and Configuration
   - Open a new chat with `Ctrl/Command + L`
   - Click the gear icon in the chat window
   - Enable "Auto-run commands" for smoother operation
   - Adjust text size if needed

2. Managing Multiple Chats
   - Open several chats for different purposes
   - Try organizing chats by topic:
     - One for commands
     - One for explanations
     - One for code generation

3. Context Features
   - Use @Add Context to share code or files
   - Try adding specific functions or folders
   - Learn how context affects AI responses

> 💡 **Tip**: Keep different topics in separate chats for better organization
</details>

### 💻 Task 4: AI-Assisted Terminal Operations
<details>
<summary>Using AI for File System Tasks</summary>

Use Cursor AI chat to help you with these tasks:

1. File Management with AI
   - Ask AI to help create a directory structure for your project
   - Request help with moving multiple files
   - Ask about different ways to copy files
   - Learn about file permissions

2. Advanced Terminal Operations
   ```bash
   # Ask AI to explain and help you use:
   - find command for locating files
   - grep command for searching file contents
   - pipe operations for combining commands
   - wildcards for file operations
   ```

3. Task Automation
   - Ask AI to help create simple shell commands
   - Learn about command history and shortcuts
   - Explore command combinations
   - Understand error messages

Example AI Prompts:
```
"How can I find all .txt files in subdirectories?"
"Help me understand the difference between cp and mv"
"Show me how to search for specific text in files"
"Explain how to use wildcards in file operations"
```

> 💡 **Tip**: Ask AI to explain each command it suggests!
</details>

## 🎯 Part 3: Git Setup and Configuration

### 💻 Task 5: Git Fundamentals
<details>
<summary>Getting Started with Git</summary>

1. Repository Setup (on GitHub UI)
   - Create a new repository
   - Configure repository settings
   - Add a README.md file
   - Choose a license (optional)

2. Local Repository Setup
   - Use `git init` to create a local repository
   - Configure Git username and email:
     ```bash
     git config --global user.name "Your Name"
     git config --global user.email "your.email@example.com"
     ```
   - Practice basic Git commands:
     ```bash
     git status  # Check repository status
     git add .   # Stage changes
     git commit -m "Initial commit"  # Commit changes
     ```

3. Remote Repository Integration
   - Connect local to remote repository:
     ```bash
     git remote add origin <your-repository-url>
     git branch -M main  # Ensure you're on main branch
     ```
   - Push your changes:
     ```bash
     git push -u origin main  # First push with upstream tracking
     ```
   - Verify your push:
     - Visit your GitHub repository URL
     - Refresh the page and check that files appear
     - Click on commits to verify your commit message
     - Check file contents match your local files

> 💡 **Tip**: Use AI chat to help understand Git concepts and troubleshoot any push issues!
> ⚠️ **Note**: Always verify your pushes on GitHub to ensure successful synchronization.
</details>

## 📋 Submission Requirements
<details>
<summary>Deliverables</summary>

1. Environment Setup:
   - Cursor AI installed and configured
   - Terminal commands practiced
   - AI chat features explored

2. Git Configuration:
   - Local repository initialized
   - GitHub account set up
   - Basic Git operations completed

3. Documentation:
   - List of AI interactions and learnings
   - Screenshots of interesting AI responses
   - Notes on helpful AI features
</details>

<!-- 
Emoji Reference:
📚 - Main sections
🔧 - Setup and installation
🎯 - Parts and objectives
⭐ - Key concepts
💻 - Tasks and exercises
📋 - Submission
💡 - Tips
⚠️ - Warnings
--> 
# Week One: Getting Started with Cursor and Git

## Required Installations & Setup

### 1. Cursor AI
- Download and install Cursor AI from [https://cursor.sh/](https://cursor.sh/)
- Set up your development environment with Cursor AI
- Familiarize yourself with the basic features and AI capabilities

### 2. GitHub Account
- Create a GitHub account at [https://github.com](https://github.com)
- Complete your GitHub profile setup

## Task Description

Please set up the start of your dev environment and install Cursor AI and GitHub and create necessary accounts on both of them.

## Week One Assignments

### Task 1: Getting Started with Cursor AI Locally
1. Create a new folder for this course on your computer (choose a location you can easily find)
2. Open a new Cursor project
3. Open a terminal (click the three dots in the upper navigation bar and select 'Terminal')
   - Run this command: `pwd`
4. Check if the path shown matches your course folder
   - If not, go to File > Open Folder and select your course folder
   - Run `pwd` again to verify you're in the correct location

### Task 2: Basic Terminal Commands

#### Command Overview
Learn and practice the following essential terminal commands (PELASE DO NOT COPY PASTE THE COMMANDS, in this way you learn new commands faster, by typing them)

#### Practice Tasks
1. Working with Files
   - Run `ls` to list the files in your directory (should be empty)
   - Create a new file by running `touch README.md`
   - Run `ls` again to verify the file was created

2. Directory Operations
   - Create a new directory: `mkdir practice`
   - Copy the README file: `cp README.md practice/README.md`
   - Change to the practice directory: `cd practice`
   - Run `ls` to verify the file is in the practice directory
   - Return to the main directory: `cd ..`
   - Remove the copied file: `rm practice/README.md`

3. Moving and Renaming Files
   - First, explore the mv command: `mv --help`
   - Read through the help text to understand how mv works
   - Create a directory of your choice: `mkdir your_directory_name`
   - Use mv to move README.md into your new directory (based on what you learned from --help)
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

5. Using Cursor AI Chat
   - Open a new AI Chat using the keyboard shortcut:
     - Windows: Press `Ctrl + L`
     - Mac: Press `Command + L`
   - Try asking the AI a question about any of the commands you've learned
   - Practice interacting with the AI by asking it to:
     - Create new files or directories for you
     - Show you which commands you've run in your session
     - Remove specific files or directories
     - Explain the difference between commands you've used
     - Help you understand any error messages you encountered
   - Remember: The AI can both explain commands AND execute them for you!

You just succesfully used Cursor AI to do some tasks for you. Congratulations. Every journey starts with the first step. Do a small break if you wish and go to the next task.    

### Task 3: Explore the Cursor AI Chat Functionality

1. Chat Settings and Configuration
   - Click the gear icon in the chat window
   - Enable "Auto-run commands" for smoother command execution
   - Adjust the text size to your preference
   - Explore other available settings

2. Managing Multiple Chats
   - Open a new chat with `Ctrl/Command + L`
   - Switch between different chats using the chat selector at the top
   - Try having different conversations in different chats (e.g., one for commands, one for explanations)
   - Close and reopen chats as needed

3. Chat Features
   - Use the "Copy" button to copy code or text
   - Try the "Clear" button to start fresh
   - Notice how the AI remembers context within the same chat
   - Experiment with different ways of asking questions

4. Adding Context
   - Use the @Add Context feature of the Chat Interface and explore it. 
   - Experiment with it. If you already have code on your computer, you could add only a specific function to the context or a complete folder


### Task 4: Git Fundamentals
Experiment with Git and familiarize yourself with:

#### a) Repository Setup (on GitHub UI)
- Create a new repository on GitHub
- Configure repository settings
- Add a README.md file
- Choose a license (optional)

#### b) Local Repository Initialization
- Use `git init` to create a new local repository
- Understand the `.git` directory structure
- Configure your Git username and email

#### c) Basic Git Operations
Practice the following Git commands:
- `git add` - Stage changes for commit
- `git commit` - Save staged changes with a descriptive message
- `git push` - Upload local commits to remote repository

### Task 5: Programming Language Setup

1. Verify Current Installations
   - Ask the AI to help you check if Python is installed
   - Check if JavaScript (Node.js) is installed
   - Have the AI verify the versions of both

2. Installation Process
   - Enable web search in chat settings for up-to-date installation guides
   - Ask the AI about:
     - Package managers (npm for JavaScript, pip for Python)
     - Anaconda vs. standard Python installation
     - Development environments and tools
   - Follow AI-guided installation steps for missing languages

3. Verify Installations
   - Have the AI create simple test programs
   - Run the programs to verify installations
   - Test package managers (npm, pip) if installed
   - Make sure you can run both Python and JavaScript files

4. Understanding Package Management
   - Ask the AI to explain:
     - What is npm and why is it important?
     - What is pip and when do you use it?
     - What is Anaconda and its benefits?
     - How do package managers help in development?

     
### Week One Wrap-Up

Congratulations! You've now set up your essential development environment:
- Cursor AI is installed and configured
- Git is set up for version control
- You can push files to remote repositories
- Python and JavaScript are ready for use

Next week, we'll build upon these foundations and start creating actual projects with these tools.

Remember:
- Keep practicing with the terminal commands
- Experiment with Cursor AI's features
- Try simple Git operations
- Test your programming language installations

See you in Week Two!

## Submission
- Ensure you have completed all installations
- Test your Git setup by creating and pushing a test repository
- Document any issues or questions you encountered during the setup process

## Additional Resources
- [Git Documentation](https://git-scm.com/doc)
- [GitHub Guides](https://guides.github.com/)
- [Linux Command Line Basics](https://ubuntu.com/tutorials/command-line-for-beginners) 
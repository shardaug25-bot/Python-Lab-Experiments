# Configure Git
git config --global user.name "Your Name"
git config --global user.email "yourmail@gmail.com"

# Create project directory
mkdir PythonProject
cd PythonProject

# Initialize Git repository
git init

# Create a Python file
echo 'print("Hello Python")' > main.py

# Check repository status
git status

# Add file to staging area
git add main.py

# Commit changes
git commit -m "Initial commit"

# Create a new branch
git branch development

# Switch to development branch
git checkout development

# Modify the Python file
echo 'print("Welcome to Python")' >> main.py

# Add and commit changes
git add main.py
git commit -m "Updated main.py"

# Switch to main branch
git checkout main

# Merge development branch
git merge development

# Display commit history
git log --oneline

# Display branches
git branch
# Clone an existing repository
git clone https://github.com/shardaug25-bot/Python-Lab-Experiments.git

# Enter repository
cd Hello-World

# Check repository status
git status

# Create development branch
git checkout -b development

# Create or modify source file
echo 'print("Python Project Updated")' > main.py

# Add modified file
git add main.py

# Commit changes
git commit -m "Modified Python source file"

# Switch to main branch
git checkout main

# Merge development branch
git merge development

# Push changes to remote repository
git push origin main

# Display commit history
git log --oneline

# Check repository status
git status
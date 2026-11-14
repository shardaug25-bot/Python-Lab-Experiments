# Step 1: Fork the repository
# Open the required GitHub repository.
# Click Fork.
# Select your GitHub account.

# Step 2: Clone your forked repository
git clone https://github.com/shardaug25-bot/Python-Lab-Experiments.git

# Enter repository
cd REPOSITORY

# Step 3: Add original repository as upstream
git remote add upstream https://github.com/shardaug25-bot/Python-Lab-Experiments.git

# Step 4: Create a new branch
git checkout -b issue-fix

# Step 5: Modify the source file
# Open the required file and resolve the reported issue.

# Step 6: Add and commit changes
git add .
git commit -m "Resolved reported issue"

# Step 7: Push branch to GitHub
git push origin issue-fix

# Step 8: Submit Pull Request
# Open your fork on GitHub.
# Click Compare & pull request.
# Select the original repository as the base.
# Select issue-fix as the compare branch.
# Add title and description.
# Click Create pull request.

# Step 9: Synchronize local repository
git checkout main
git fetch upstream
git merge upstream/main

# Step 10: Push synchronized repository
git push origin main
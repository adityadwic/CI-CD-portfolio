#!/bin/bash

# Script to initialize and push QA Portfolio to GitHub
# Make sure you have created the repository on GitHub first

echo "🚀 Initializing QA Portfolio CI/CD Repository"
echo "============================================="

# Initialize git repository if not already initialized
if [ ! -d ".git" ]; then
    echo "📂 Initializing Git repository..."
    git init
else
    echo "📂 Git repository already initialized"
fi

# Add all files
echo "📝 Adding all files to git..."
git add .

# Check if there are changes to commit
if git diff --staged --quiet; then
    echo "⚠️  No changes to commit"
else
    # Commit changes
    echo "💾 Committing changes..."
    git commit -m "Initial QA Portfolio CI/CD project setup

- Complete test automation framework with API and UI tests
- Python + Pytest for API testing with JSONPlaceholder
- Selenium WebDriver for cross-browser UI testing
- Cypress for modern E2E testing
- GitHub Actions CI/CD pipeline
- Comprehensive documentation and test plans
- Sample application for testing demonstrations
- Quality gates and automated reporting"
fi

# Add remote origin if not already added
if ! git remote get-url origin > /dev/null 2>&1; then
    echo "🔗 Adding GitHub remote..."
    git remote add origin https://github.com/adityadwic/CI-CD-portfolio.git
else
    echo "🔗 GitHub remote already configured"
fi

# Push to GitHub
echo "⬆️  Pushing to GitHub..."
git branch -M main
git push -u origin main

echo ""
echo "✅ Successfully pushed QA Portfolio to GitHub!"
echo "🌐 Repository URL: https://github.com/adityadwic/CI-CD-portfolio"
echo ""
echo "🔧 Next steps:"
echo "   1. Check GitHub Actions is enabled in your repository"
echo "   2. Ensure GitHub Pages is configured if you want to host the demo app"
echo "   3. Review and customize any personal information in README.md"
echo "   4. Add any additional test cases or documentation as needed"
echo ""
echo "🎉 Your QA Portfolio is now live on GitHub!"

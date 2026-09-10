#!/usr/bin/env python3
"""
Setup script to prepare Megaton-Shield for deployment
Handles git initialization, environment setup, and pre-deployment checks
"""

import os
import sys
import subprocess
from pathlib import Path

def run_command(cmd, description):
    """Execute a command and handle errors"""
    print(f"\n📍 {description}...")
    try:
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
        if result.returncode != 0:
            print(f"⚠️  {description} completed with warnings:")
            print(result.stderr)
            return False
        print(f"✅ {description} successful")
        return True
    except Exception as e:
        print(f"❌ Error during {description}: {e}")
        return False

def main():
    print("=" * 60)
    print("🚀 Megaton-Shield Deployment Setup")
    print("=" * 60)
    
    project_root = Path(__file__).parent
    os.chdir(project_root)
    
    # Check if git is initialized
    if not Path('.git').exists():
        print("\n🔧 Initializing Git repository...")
        run_command("git init", "Git initialization")
        run_command("git config user.name 'Megaton-Shield CI'", "Git config")
        run_command("git config user.email 'deploy@megaton-shield.io'", "Git config")
    
    # Check dependencies
    print("\n🔍 Checking prerequisites...")
    
    checks = {
        "Python 3.10+": "python --version",
        "Node.js 18+": "node --version",
        "npm": "npm --version",
        "Git": "git --version",
    }
    
    all_ok = True
    for name, cmd in checks.items():
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
        if result.returncode == 0:
            print(f"✅ {name}: {result.stdout.strip()}")
        else:
            print(f"❌ {name}: NOT FOUND")
            all_ok = False
    
    if not all_ok:
        print("\n⚠️  Some prerequisites are missing. Please install them and try again.")
        sys.exit(1)
    
    # Backend setup
    print("\n📦 Setting up backend...")
    run_command(
        "python -m pip install --upgrade pip setuptools wheel",
        "Python tools upgrade"
    )
    run_command(
        "python -m pip install -r backend/requirements.txt",
        "Backend dependencies"
    )
    
    # Frontend setup
    print("\n📦 Setting up frontend...")
    run_command(
        "cd frontend && npm install --include=dev",
        "Frontend dependencies"
    )
    
    # Run tests
    print("\n🧪 Running tests...")
    run_command(
        "python -m pytest backend/tests -v",
        "Backend tests"
    )
    run_command(
        "cd frontend && npm run build",
        "Frontend build"
    )
    
    # Check .env
    if not Path('.env').exists():
        print("\n⚙️  Creating .env file from template...")
        if Path('.env.example').exists():
            with open('.env.example') as f:
                env_content = f.read()
            with open('.env', 'w') as f:
                f.write(env_content)
            print("✅ .env file created")
    
    # Summary
    print("\n" + "=" * 60)
    print("✅ Setup Complete!")
    print("=" * 60)
    print("\n📝 Next steps for deployment:")
    print("\n1️⃣  Add to Git (if not already added):")
    print("   git add .")
    print("   git commit -m 'Setup: Deployment configuration'")
    print("   git remote add origin https://github.com/YOUR_USERNAME/megaton-shield.git")
    print("   git push -u origin main")
    print("\n2️⃣  Deploy to Vercel:")
    print("   Option A: Use Vercel Dashboard → Import Project")
    print("   Option B: Use Vercel CLI:")
    print("   npm i -g vercel")
    print("   vercel --prod")
    print("\n3️⃣  Configure Environment Variables in Vercel:")
    print("   ENVIRONMENT=production")
    print("   LLM_PROVIDER=deterministic_mock")
    print("   VITE_API_BASE_URL=https://your-project.vercel.app")
    print("\n📚 For detailed instructions, see DEPLOYMENT.md")
    print("\n🌐 After deployment, your app will be live at:")
    print("   https://your-project-name.vercel.app")
    print("\n" + "=" * 60)

if __name__ == "__main__":
    main()

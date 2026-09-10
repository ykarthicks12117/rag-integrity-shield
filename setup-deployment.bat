@echo off
REM Megaton-Shield Quick Deployment Setup for Windows
REM This script automates the initial setup and deployment preparation

setlocal enabledelayedexpansion

echo.
echo ======================================================
echo  Megaton-Shield Deployment Setup (Windows)
echo ======================================================
echo.

REM Check Python
python --version >nul 2>&1
if errorlevel 1 (
    echo [ERROR] Python not found in PATH
    echo Please install Python 3.11+ from https://www.python.org
    exit /b 1
)

REM Check Node.js
node --version >nul 2>&1
if errorlevel 1 (
    echo [ERROR] Node.js not found in PATH
    echo Please install Node.js from https://nodejs.org
    exit /b 1
)

REM Check Git
git --version >nul 2>&1
if errorlevel 1 (
    echo [ERROR] Git not found in PATH
    echo Please install Git from https://git-scm.com
    exit /b 1
)

echo [OK] All prerequisites found
echo.

REM Backend setup
echo [SETUP] Installing backend dependencies...
python -m pip install --upgrade pip >nul 2>&1
python -m pip install -r backend\requirements.txt >nul 2>&1
if errorlevel 1 (
    echo [ERROR] Failed to install backend dependencies
    exit /b 1
)
echo [OK] Backend dependencies installed

REM Frontend setup
echo [SETUP] Installing frontend dependencies...
cd frontend
call npm install --include=dev >nul 2>&1
if errorlevel 1 (
    echo [ERROR] Failed to install frontend dependencies
    exit /b 1
)
echo [OK] Frontend dependencies installed
cd ..

REM Run tests
echo.
echo [TEST] Running backend tests...
python -m pytest backend\tests -v --tb=short
if errorlevel 1 (
    echo [WARNING] Some tests failed
) else (
    echo [OK] All tests passed
)

REM Build frontend
echo.
echo [BUILD] Building frontend...
cd frontend
call npm run build >nul 2>&1
if errorlevel 1 (
    echo [ERROR] Frontend build failed
    exit /b 1
)
echo [OK] Frontend build successful
cd ..

REM Create .env if needed
if not exist ".env" (
    echo [SETUP] Creating .env file...
    copy .env.example .env >nul 2>&1
    echo [OK] .env file created from template
)

REM Initialize git if needed
if not exist ".git" (
    echo.
    echo [SETUP] Initializing Git repository...
    git init
    git config user.name "Megaton-Shield CI"
    git config user.email "deploy@megaton-shield.io"
    echo [OK] Git repository initialized
)

REM Summary
echo.
echo ======================================================
echo  Setup Complete!
echo ======================================================
echo.
echo Next Steps for Deployment:
echo.
echo 1. Commit to Git:
echo    git add .
echo    git commit -m "Setup: Deployment ready"
echo    git remote add origin https://github.com/YOUR_USERNAME/megaton-shield.git
echo    git push -u origin main
echo.
echo 2. Deploy to Vercel:
echo    Option A: Visit vercel.com and import your GitHub repo
echo    Option B: npm install -g vercel && vercel --prod
echo.
echo 3. Environment Variables in Vercel:
echo    - ENVIRONMENT=production
echo    - LLM_PROVIDER=deterministic_mock
echo    - VITE_API_BASE_URL=https://your-project.vercel.app
echo.
echo 4. Read detailed guide:
echo    See DEPLOYMENT.md for complete instructions
echo.
echo ======================================================
echo.

pause

"""
Vercel Serverless Entry Point for FastAPI Backend
This file enables deploying the FastAPI backend to Vercel Functions
"""
import sys
from pathlib import Path

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent))

from backend.app.main import app

# Vercel expects 'app' as the ASGI application
__all__ = ['app']

#!/bin/bash
# Build and prepare for deployment

set -e

echo "🔨 Building Megaton-Shield for deployment..."

# Frontend build
echo "📦 Building frontend..."
cd frontend
npm install --include=dev
npm run build
cd ..

# Backend validation
echo "🧪 Running backend tests..."
python -m pytest backend/tests -v

# Create build directory
echo "📁 Preparing deployment artifacts..."
mkdir -p dist
cp -r frontend/dist/* dist/
mkdir -p dist/api
cp api/index.py dist/api/

echo "✅ Build complete! Ready for deployment."
echo "📝 Next steps:"
echo "  1. Push to GitHub: git push origin main"
echo "  2. Deploy to Vercel with: vercel --prod"

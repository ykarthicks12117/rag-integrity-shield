# Deployment Guide - Megaton-Shield

Complete guide for deploying the Three-Stage RAG Integrity Shield to production.

## 🚀 Quick Start Deployments

### Option 1: Vercel (Recommended - Full Stack)

#### Prerequisites
- GitHub account
- Vercel account (free tier available)
- Project pushed to GitHub

#### Steps

1. **Push to GitHub**
   ```bash
   git init
   git add .
   git commit -m "Initial commit: Megaton-Shield RAG Integrity System"
   git remote add origin https://github.com/YOUR_USERNAME/megaton-shield.git
   git branch -M main
   git push -u origin main
   ```

2. **Connect to Vercel**
   - Go to [vercel.com](https://vercel.com)
   - Click "Add New..." → "Project"
   - Select your `megaton-shield` repository
   - Vercel will auto-detect the configuration from `vercel.json`

3. **Configure Environment Variables**
   In Vercel project settings, add:
   ```
   ENVIRONMENT=production
   LLM_PROVIDER=deterministic_mock
   VITE_API_BASE_URL=https://your-project.vercel.app
   ```

4. **Deploy**
   - Vercel will automatically deploy on every push to `main`
   - Your app will be live at: `https://your-project.vercel.app`

#### CORS & API Configuration
- Backend API runs at `/api/*` paths
- Frontend served from root `/`
- CORS headers configured in `vercel.json`

---

### Option 2: Docker (Any Cloud Provider)

#### Prerequisites
- Docker installed
- Docker Hub account (optional)

#### Local Testing with Docker

```bash
# Build the image
docker build -t megaton-shield:latest .

# Run the container
docker run -p 8000:8000 \
  -e ENVIRONMENT=production \
  -e LLM_PROVIDER=deterministic_mock \
  -v $(pwd)/data:/app/data \
  megaton-shield:latest
```

#### Deploy to Docker Hub
```bash
# Tag image
docker tag megaton-shield:latest YOUR_DOCKERHUB_USERNAME/megaton-shield:latest

# Push to Docker Hub
docker login
docker push YOUR_DOCKERHUB_USERNAME/megaton-shield:latest
```

#### Deploy to Cloud Platforms Using Docker

**Railway.app**
```bash
# Install Railway CLI
npm i -g @railway/cli

# Login
railway login

# Deploy
railway up
```

**Render.com**
1. Go to [render.com](https://render.com)
2. Create new "Web Service"
3. Select Docker as runtime
4. Connect your GitHub repo
5. Configure environment variables
6. Deploy

**AWS ECS / ECR**
```bash
# Push to AWS ECR
aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin YOUR_AWS_ACCOUNT.dkr.ecr.us-east-1.amazonaws.com

docker tag megaton-shield YOUR_AWS_ACCOUNT.dkr.ecr.us-east-1.amazonaws.com/megaton-shield:latest

docker push YOUR_AWS_ACCOUNT.dkr.ecr.us-east-1.amazonaws.com/megaton-shield:latest
```

---

### Option 3: Docker Compose (Local Multi-Container Development)

```bash
# Start all services
docker-compose up -d

# View logs
docker-compose logs -f

# Stop services
docker-compose down
```

Services will be available at:
- Frontend: http://localhost:5173
- Backend API: http://localhost:8000
- API Docs: http://localhost:8000/docs

---

### Option 4: Heroku (Deprecated but still works with Procfile)

```bash
# Install Heroku CLI
npm install -g heroku

# Login
heroku login

# Create app
heroku create megaton-shield

# Set buildpacks
heroku buildpacks:add heroku/python
heroku buildpacks:add heroku/nodejs

# Deploy
git push heroku main

# View logs
heroku logs --tail
```

---

### Option 5: Split Deployment (Frontend + Backend Separately)

#### Frontend to Vercel, Backend to Railway

**Frontend to Vercel:**
1. Create a separate Vercel project for frontend only
2. Set `VITE_API_BASE_URL` to your Railway backend URL

**Backend to Railway:**
1. Go to [railway.app](https://railway.app)
2. Create new project
3. Connect GitHub repo
4. Select Python environment
5. Configure:
   - Start command: `python -m uvicorn backend.app.main:app --host 0.0.0.0 --port $PORT`
   - Build command: `pip install -r backend/requirements.txt`
   - Python version: `3.11`

---

## 📊 Environment Variables by Platform

### Vercel
```
ENVIRONMENT=production
LLM_PROVIDER=deterministic_mock
OPENAI_API_KEY=sk-... (optional)
GEMINI_API_KEY=... (optional)
VITE_API_BASE_URL=https://your-project.vercel.app
```

### Docker/Heroku/Railway
```
ENVIRONMENT=production
HOST=0.0.0.0
PORT=8000
DEBUG=False
LLM_PROVIDER=deterministic_mock
OPENAI_API_KEY=sk-... (optional)
GEMINI_API_KEY=... (optional)
```

---

## 🧪 CI/CD with GitHub Actions

Automatic testing and deployment on every push to `main`:

```yaml
# .github/workflows/ci-cd.yml (already created)
```

**Setup GitHub Actions Secrets:**
1. Go to GitHub Repo → Settings → Secrets and variables → Actions
2. Add:
   - `VERCEL_TOKEN`: From [Vercel Settings](https://vercel.com/account/tokens)
   - `VERCEL_ORG_ID`: From Vercel project settings
   - `VERCEL_PROJECT_ID`: From Vercel project settings

---

## 🔒 Security Checklist

- [ ] Set `DEBUG=False` in production
- [ ] Use strong `OPENAI_API_KEY` and `GEMINI_API_KEY` if applicable
- [ ] Enable CORS only for your domain
- [ ] Rotate secrets regularly
- [ ] Use environment variables for all sensitive data
- [ ] Enable HTTPS/SSL (automatic on Vercel)
- [ ] Set up DDoS protection (Cloudflare recommended)
- [ ] Monitor error logs regularly

---

## 📈 Monitoring & Logs

### Vercel
- Dashboard: [vercel.com/dashboard](https://vercel.com/dashboard)
- Logs: Project → Deployments → View logs

### Railway
- Dashboard: [railway.app](https://railway.app)
- Logs: Project → Logs tab

### Docker
```bash
# View logs
docker logs megaton-shield-backend
docker logs megaton-shield-frontend

# Follow logs
docker logs -f megaton-shield-backend
```

---

## 🆘 Troubleshooting

**Issue: API calls failing with CORS error**
- Ensure `VITE_API_BASE_URL` matches your backend domain
- Check CORS headers in `vercel.json`

**Issue: Database not persisting**
- For Vercel: Use managed PostgreSQL (not included in free tier)
- For Docker: Ensure `/data` volume is mounted
- Current setup uses SQLite in `/data/megaton_shield.db`

**Issue: Frontend showing 404 on refresh**
- SPA rewrite already configured in `vercel.json`
- Make sure `frontend/vercel.json` has rewrites

**Issue: Python dependencies not installing**
- Ensure `requirements.txt` is in backend folder
- Check Python version compatibility (3.10+)

---

## 📝 Post-Deployment Steps

1. **Verify Health**
   ```bash
   curl https://your-app.vercel.app/health
   curl https://your-app.vercel.app/api/health
   ```

2. **Run Initial Seeding**
   Visit `/api/demo/reset` to seed test data

3. **Monitor First 24 Hours**
   - Check error rates
   - Verify performance metrics
   - Validate all API endpoints

4. **Update DNS (if using custom domain)**
   - Add CNAME record to your Vercel project

---

## 💡 Performance Tips

- Enable caching headers in production
- Use CDN for static assets (Vercel includes Cloudflare)
- Monitor database query performance
- Set up error tracking (Sentry recommended)
- Use APM tools (New Relic, DataDog)

---

**For issues or questions, check the project README.md or contact the development team.**

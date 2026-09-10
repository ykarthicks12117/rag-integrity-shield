# Deployment Checklist for Megaton-Shield

## ✅ Pre-Deployment Verification

### Code Quality
- [ ] All tests passing (10/10)
- [ ] No console errors or warnings in dev tools
- [ ] All pages load without 404s
- [ ] API endpoints responding correctly
- [ ] Evidence Trace page working (ShieldAlert fix applied)

### Environment Setup
- [ ] `.env` file created from `.env.example`
- [ ] `ENVIRONMENT=production` configured
- [ ] `LLM_PROVIDER=deterministic_mock` set
- [ ] `VITE_API_BASE_URL` ready for production domain

### Git & Repository
- [ ] All changes committed to git
- [ ] `.gitignore` properly configured
- [ ] Sensitive files excluded (API keys, `.env`, `venv`, `node_modules`)
- [ ] Repository pushed to GitHub (main branch)

### Dependencies
- [ ] Backend: `pip install -r backend/requirements.txt` ✅
- [ ] Frontend: `npm install` in frontend directory ✅
- [ ] All packages compatible with deployment target

---

## 🚀 Deployment Steps

### Step 1: Prepare Repository
```bash
cd "C:\Users\Yuvan Karthick.S\OneDrive\Desktop\new\megaton-main\megaton-main"

# Initialize git (if not done)
git init

# Add all files
git add .

# Commit
git commit -m "feat: Deployment-ready Megaton-Shield with full CI/CD setup

- Added Vercel serverless backend (api/index.py)
- Configured GitHub Actions for CI/CD
- Docker & docker-compose for containerized deployment
- Comprehensive deployment documentation
- Fixed Evidence Trace component missing import
"

# Add GitHub remote
git remote add origin https://github.com/YOUR_USERNAME/megaton-shield.git
git branch -M main
git push -u origin main
```

### Step 2: Deploy to Vercel (Recommended)
```bash
# Option A: Via Vercel Dashboard
# 1. Go to vercel.com
# 2. Click "Add New..." → "Project"
# 3. Import your GitHub repository
# 4. Configure build settings (auto-detected from vercel.json)
# 5. Add environment variables:
#    - ENVIRONMENT=production
#    - LLM_PROVIDER=deterministic_mock
#    - VITE_API_BASE_URL=https://your-project.vercel.app
# 6. Deploy

# Option B: Via Vercel CLI
npm install -g vercel
vercel --prod
```

### Step 3: Configure Custom Domain (Optional)
```bash
# In Vercel Dashboard:
# 1. Project Settings → Domains
# 2. Add your custom domain
# 3. Follow DNS configuration instructions
# 4. SSL certificate auto-provisioned
```

### Step 4: Set Up GitHub Actions (Optional but Recommended)
```bash
# In GitHub Repo:
# 1. Settings → Secrets and variables → Actions
# 2. Add secrets:
#    - VERCEL_TOKEN (from vercel.com/account/tokens)
#    - VERCEL_ORG_ID (from Vercel project settings)
#    - VERCEL_PROJECT_ID (from Vercel project settings)
# 3. CI/CD will run automatically on push to main
```

---

## 📊 Post-Deployment Verification

### Functionality Tests
- [ ] Frontend loads at `https://your-project.vercel.app`
- [ ] API accessible at `https://your-project.vercel.app/api/*`
- [ ] Health check: `GET /health` returns 200
- [ ] Dashboard loads and fetches data
- [ ] Documents can be uploaded
- [ ] RAG queries work end-to-end
- [ ] Evidence Trace page fully interactive
- [ ] All 13 pages accessible

### API Endpoints Verification
```bash
# Health check
curl https://your-project.vercel.app/health

# API documentation
https://your-project.vercel.app/api/docs
https://your-project.vercel.app/api/redoc

# Sample RAG query
curl -X POST https://your-project.vercel.app/api/rag/query \
  -H "Content-Type: application/json" \
  -d '{
    "tenant_id": "tenant_a",
    "user_id": "analyst_1",
    "query": "What is the security policy?",
    "role": "analyst"
  }'
```

### Performance Metrics
- [ ] First Contentful Paint (FCP) < 2s
- [ ] Largest Contentful Paint (LCP) < 2.5s
- [ ] Cumulative Layout Shift (CLS) < 0.1
- [ ] Time to Interactive (TTI) < 3.5s

### Security Checks
- [ ] HTTPS enforced (automatic on Vercel)
- [ ] No sensitive data in logs
- [ ] CORS properly configured
- [ ] API keys not exposed in frontend code
- [ ] Environment variables properly set

---

## 🔄 Rollback Procedure

If deployment fails:

```bash
# Revert to previous version
git revert HEAD
git push origin main

# Or manually select previous deployment in Vercel:
# Vercel Dashboard → Deployments → Select previous → Promote to Production
```

---

## 📈 Monitoring & Maintenance

### Daily
- [ ] Check error logs
- [ ] Monitor API response times
- [ ] Review security events

### Weekly
- [ ] Analyze usage patterns
- [ ] Check performance metrics
- [ ] Review failed tests (if any)

### Monthly
- [ ] Security audit
- [ ] Dependency updates
- [ ] Database optimization (if needed)

---

## 🆘 Troubleshooting Checklist

| Issue | Solution |
|-------|----------|
| 404 on Frontend Routes | Check SPA rewrite in vercel.json ✅ |
| API CORS Errors | Verify VITE_API_BASE_URL matches deployed domain |
| Database Not Persisting | Use Vercel KV or external PostgreSQL |
| Build Failing | Check Python/Node versions match requirements |
| Tests Failing in CI | Run locally: `pytest backend/tests -v` |
| Slow API Responses | Check database queries, optimize with indexes |

---

## 📞 Support Resources

- **Vercel Docs**: https://vercel.com/docs
- **FastAPI Docs**: https://fastapi.tiangolo.com
- **React Docs**: https://react.dev
- **Project README**: See README.md for architecture details
- **GitHub Issues**: Report bugs in your repository

---

## ✨ You're Done!

Your Megaton-Shield RAG Integrity System is now live! 🎉

**Share your deployment:**
- Frontend: `https://your-project.vercel.app`
- API Docs: `https://your-project.vercel.app/api/docs`
- GitHub: `https://github.com/YOUR_USERNAME/megaton-shield`

---

*Last Updated: 2026-09-11*
*Version: 1.0.0 - Deployment Ready*

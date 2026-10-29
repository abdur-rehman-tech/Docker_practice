# 🐳 Dockerized Python App + Jenkins Pipeline

![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white) ![Jenkins](https://img.shields.io/badge/Jenkins-D24939?style=flat-square&logo=jenkins&logoColor=white) ![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)

A minimal Python app packaged with Docker and shipped to **Docker Hub** through a **Jenkins declarative pipeline**.

## 📁 Files

| File | Purpose |
|---|---|
| `python.py` | Sample Python app |
| `Dockerfile` | `python:3.11-slim` based image |
| `requirement.txt` | Dependencies |
| `Jenkinsfile` | Build image → push to Docker Hub |

## 🔄 Pipeline

```
Build Docker Image → Push to DockerHub (credentials from Jenkins, --password-stdin)
```

## 🚀 Run locally

```bash
docker build -t docker-practice .
docker run --rm docker-practice
```

---

## 👤 Author

**Abdur Rehman** · DevSecOps Engineer · Founder of [ARTechOps](https://artechops.com)

[LinkedIn](https://www.linkedin.com/in/muhamad-abdur-rehman-81777b366/) · [GitHub](https://github.com/abdur-rehman-tech) · [artechops.com](https://artechops.com)

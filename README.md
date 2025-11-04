# 🚀 Dockerized Flask Microservice with Automated CI/CD Pipeline

A lightweight **Flask-based microservice** that demonstrates **core DevOps practices** — containerization, automation, and CI/CD using **GitHub Actions** and **Docker**.

---

## 🧩 Project Overview

This project showcases a **simple yet realistic DevOps workflow**:
- Flask web app exposing REST endpoints  
- Dockerized for portability  
- GitHub Actions pipeline for **automated testing** and **Docker image builds**  
- Optional deployment to Docker Hub or Kubernetes (Minikube)

---

## 🧠 Features

| Feature | Description |
|----------|-------------|
| `/` | Returns a welcome message |
| `/info` | Returns system and environment details |
| `/api/square?num=5` | Returns the square of a given number |
| **Environment Variables** | Reads `APP_ENV` to show different environments |
| **CI/CD Pipeline** | Automatically runs tests and builds Docker image on every push |

---
flask-devops-demo/
├── app.py
├── Dockerfile
├── requirements.txt
├── README.md
└── .github/
└── workflows/
└── ci.yml


---

## ⚙️ Tech Stack

- **Python 3.10+**
- **Flask**
- **Pytest**
- **Docker**
- **GitHub Actions**
- *(Optional: Kubernetes / Minikube)*

---

## 🧪 API Endpoints

| Endpoint | Method | Description |
|-----------|---------|-------------|
| `/` | GET | Welcome route |
| `/info` | GET | Returns system and environment info |
| `/api/square?num=5` | GET | Returns square of a number |

---

## 💻 Run Locally

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/Adarshkaintura/flask-devops-demo.git
cd flask-devops-demo

Install Dependencies
pip install -r requirements.txt

3️⃣ Run the App
python app.py


Visit → http://localhost:5000

🐳 Docker Setup
Build the Docker Image
docker build -t flask-devops-demo .

Run the Container
docker run -d -p 5000:5000 flask-devops-demo


Now open → http://localhost:5000

⚡ Continuous Integration (CI/CD)

The pipeline is defined in:

.github/workflows/ci.yml

🚀 What It Does

Runs automatically on every push or pull request to main

Installs dependencies and runs Pytest

Builds a Docker image

Pushes the image to Docker Hub




Would you like me to **add badges** (e.g., build passing, Docker pulls, Python version, etc.) at the top for a professional Git

## 🏗️ Project Structure


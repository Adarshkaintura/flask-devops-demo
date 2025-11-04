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

🔐 Setup GitHub Secrets

In your GitHub repository:

Go to Settings → Secrets and Variables → Actions

Add these secrets:

DOCKERHUB_USERNAME → Your Docker Hub username

DOCKERHUB_TOKEN → Docker Hub password or Access Token

☸️ Optional: Kubernetes Deployment (Minikube)

Create a file deployment.yml:

apiVersion: apps/v1
kind: Deployment
metadata:
  name: flask-devops-demo
spec:
  replicas: 1
  selector:
    matchLabels:
      app: flask-devops-demo
  template:
    metadata:
      labels:
        app: flask-devops-demo
    spec:
      containers:
      - name: flask-devops-demo
        image: flask-devops-demo:latest
        ports:
        - containerPort: 5000
        env:
        - name: APP_ENV
          value: "production"


Apply using:

kubectl apply -f deployment.yml

🧠 Interview Talking Points

“I built a lightweight Flask microservice with REST endpoints and Dockerized it for portability.
Then I created a GitHub Actions CI/CD pipeline that runs tests automatically, builds a Docker image, and pushes it to Docker Hub.
I also used environment variables for dynamic configuration and optionally deployed it on Kubernetes using Minikube.
This project helped me understand the full DevOps lifecycle — from coding to automated deployment.”

🔗 Links

GitHub Repository: https://github.com/Adarshkaintura/flask-devops-demo

Docker Hub (after first push): https://hub.docker.com/r/<your-username>/flask-devops-demo

🧾 License

This project is released under the MIT License — free to use and modify.

👨‍💻 Author

Adarsh Kaintura
B.Tech CSE | 2026 Graduate | DevOps & Cloud Enthusiast
GitHub


---

Would you like me to **add badges** (e.g., build passing, Docker pulls, Python version, etc.) at the top for a professional Git

## 🏗️ Project Structure


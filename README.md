# 🏥 Patient Insurance Charges Prediction Web App

## 📌 Overview

This project is a **machine learning powered web application** that predicts a patient's medical insurance charges based on various personal and health-related factors.

The model takes inputs such as:

* Age
* BMI
* Smoking status
* Number of children
* Region

…and predicts the **estimated insurance cost** for the patient.

The application is designed not just as a predictive model, but as a **production-ready ML system** with automated training, deployment, and scalable hosting.

---

## 🎯 Objective

The goal of this project is to:

* Build an accurate regression model for insurance cost prediction
* Provide an interactive web interface for real-time predictions
* Implement a complete **CI/CD pipeline** for automation
* Deploy the application using **containerized infrastructure in Azure**

---

## ⚙️ Tech Stack

### 🧠 Machine Learning

* Python
* Scikit-learn
* Pandas, NumPy

### 🌐 Backend / API

* FastAPI / Flask

### 🐳 Containerization

* Docker

### ☁️ Cloud & Deployment

* Azure Container Registry (ACR)
* Azure Web App (App Service)

### 🔄 CI/CD

* GitHub Actions

---

## 🚀 Features

* Real-time insurance charge prediction
* Clean and simple web interface
* Containerized application using Docker
* Automated CI/CD pipeline
* Cloud deployment using Azure services
* Scalable and production-ready architecture

---

## 🔄 Project Workflow

```text
User Input → Web App → ML Model → Prediction Output
```

---

## 🧱 System Architecture

```text
Code Push (GitHub)
        ↓
CI Pipeline (GitHub Actions)
        ↓
Build Docker Image
        ↓
Push Image to Azure Container Registry (ACR)
        ↓
Deploy to Azure Web App (App Service)
        ↓
User Access via Web Interface
```

---

## 🔁 CI/CD Pipeline

This project implements a **Continuous Integration and Continuous Deployment pipeline** to automate the entire lifecycle.

### 🔹 Continuous Integration (CI)

* Triggered on every code push
* Runs tests and validations
* Builds Docker image

### 🔹 Continuous Deployment (CD)

* Pushes Docker image to ACR
* Updates Azure Web App configuration
* Deploys latest version automatically

---

## 🐳 Docker Integration

The application is containerized using Docker to ensure:

* Environment consistency
* Easy deployment
* Scalability

The Docker image contains:

* ML model
* API server
* Required dependencies

---

## 📦 Azure Container Registry (ACR)

* Stores versioned Docker images
* Acts as a secure private registry
* Enables seamless integration with Azure services

---

## 🌐 Azure Web App Deployment

* Hosts the containerized application
* Automatically pulls images from ACR
* Provides a public endpoint for users
* Handles scaling and availability

---

## 📊 Model Workflow

```text
Data Preprocessing → Model Training → Evaluation → Model Serialization → Deployment
```

---

## 🔐 Security & Reliability

* Controlled image storage using ACR
* Automated deployments to avoid manual errors
* Versioned builds for rollback support

---

## 🔮 Future Scope

* Add model monitoring and drift detection
* Integrate model registry (MLflow)
* Improve UI with advanced frontend
* Enable batch prediction support
* Add user authentication

---

## 📌 Conclusion

This project demonstrates how a simple machine learning model can be transformed into a **production-ready application** using modern DevOps and cloud practices.

It highlights:

* End-to-end ML pipeline design
* CI/CD automation
* Container-based deployment
* Scalable cloud hosting

---

## 🤝 Acknowledgement

Built as part of learning and implementing real-world Machine Learning Engineering practices.

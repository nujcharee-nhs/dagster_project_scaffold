# Dagster Data Pipeline Project

This repository is set up to explore **[Dagster](https://dagster.io/)** — a modern orchestration platform for building and maintaining data pipelines written in Python.

## 🧠 About the Project

This project aligns to native Dagster component following **[Dagster University - Dagster Eseential course](https://courses.dagster.io/)** :

- Modular and testable Dagster pipelines (Jobs and Ops)
- Solid usage of software-defined assets
- Dependency and asset graph management
- Local development and testing
- CI integration and deployment readiness (e.g., for AWS, Kubernetes)

## 🚀 Features

- ✅ **Ops & Jobs** designed using reusable functions
- 🔗 **Assets** to represent declarative data transformations
- 📊 **Dagster UI** integration for real-time pipeline visibility
- 🔁 **Schedules and sensors** for automated pipeline triggering
- ☁️ **Cloud-ready**: Developed for deployment to Amazon EKS or ECS
- 🧪 **Unit tests and Dagster test utilities** for validation

## 🛠️ Tech Stack

- **Dagster**
- **Python 3.11+**
- **AWS (S3, ECR, EKS)** for deployment targets
- **GitHub Actions** or **pre-commit hooks** for CI/CD

## 📁 Project Structure
```
dagster_project_scaffold/
├── dagster_project_scaffold/
│ ├── init.py
│ ├── assets/ # Software-defined assets
│ ├── jobs/ # Job definitions
│ ├── ops/ # Reusable ops
│ ├── schedules/ # Schedules and sensors
│ └── resources/ # External resources (e.g., S3, DB)
├── tests/ # Unit and integration tests
├── definitions.py # put dagster artefacts in Definition
├── workspace.yaml
├── dagster.yaml
└── Dockerfile
```

## 🧪 Testing

Run tests using `pytest` and Dagster's testing tools:

```bash
pytest tests/
```

## ☁️ Deployment Strategy
Built and tested locally
Run locally using this command

```bash
dagster dev 
```


📚 Learning Resources
I’ve followed:

- Dagster Docs
- Deploying Dagster on AWS
- Personal experimentation with AWS

# 📈 SALES-MLOPS-PIPELINE

An End-to-End **MLOps pipeline** for **Sales Prediction** featuring:

- ✅ Model Training and Versioning with **MLflow**
- ✅ Scheduled Retraining with **Apache Airflow**
- ✅ Drift Detection and Monitoring with **Evidently AI**, **Prometheus**, and **Grafana**
- ✅ Containerized Deployment using **Docker** (and future extension to **Kubernetes**)

---

## 🏗 Project Structure

```
.
├── airflow/
│   ├── dags/
│   │   └── train_pipeline.py
│   ├── logs/
│   ├── plugins/
│   └── airflow.db
├── artifacts/
├── data/
├── docker/
├── k8s/
├── mlflow/
│   ├── mlruns/
│   ├── model/
│   └── train.py
├── monitoring/
│   ├── drift_monitoring.py
│   ├── grafana-dashboard.json
│   └── prometheus.yml
├── docker-compose.yml
├── README.md
└── requirements.txt
```

---

## ⚙️ Tech Stack

| Component    | Purpose |
|--------------|---------|
| **MLflow**   | Model Training, Experiment Tracking |
| **Airflow**  | Orchestration of Training Pipelines |
| **Evidently AI** | Drift Monitoring and Reporting |
| **Prometheus** | Metrics scraping for Drift detection |
| **Grafana**  | Visualization Dashboards |
| **Docker**   | Containerized Deployment |
| **Kubernetes** (Future) | Production-Ready Scalability |

---

## 🚀 Quick Start Guide

### 1. Clone the Repo

```bash
git clone https://github.com/your-username/sales-mlops-pipeline.git
cd sales-mlops-pipeline
```

### 2. Install Python Requirements

```bash
pip install -r requirements.txt
```

### 3. Start All Services

```bash
docker-compose up --build
```

### 4. Access the Services

| Service        | URL                      | Credentials         |
|----------------|---------------------------|----------------------|
| Airflow UI     | http://localhost:8080      | Username: airflow, Password: airflow |
| MLflow Tracking UI | http://localhost:5000 | - |
| Grafana (Monitoring) | http://localhost:3000 | Username: admin, Password: admin |

---

## 📋 Pipeline Overview

1. **Model Training** (`train.py`):
   - Reads input data.
   - Trains a sales prediction model (Regression or Classification).
   - Logs the model and metrics into MLflow.

2. **Scheduled Retraining** (`train_pipeline.py` DAG):
   - Airflow runs training jobs daily (or manually triggered).
   - Retrains model periodically.

3. **Drift Detection** (`drift_monitoring.py`):
   - Compares live data with training data.
   - Detects if feature/data drift happens.
   - Prometheus scrapes drift metrics.
   - Grafana alerts/visualizes drift trends.

---

## 🛠 Commands Cheat Sheet

| Purpose                     | Command |
|------------------------------|---------|
| Start Airflow Scheduler      | `docker-compose up airflow-scheduler` |
| Start Airflow Webserver      | `docker-compose up airflow-webserver` |
| Start MLflow Server          | `docker-compose up mlflow-server` |
| Trigger Airflow DAG Manually | Airflow UI → Trigger DAG |
| Monitor Model Metrics        | MLflow UI → Experiments tab |
| Monitor Drift                | Grafana Dashboards |

---

## 🔥 Features to Add (Optional)

- Trigger retraining automatically when drift crosses threshold.
- Enable Slack notifications for Drift or Failures.
- Deploy using Kubernetes (k8s manifests ready in `/k8s` folder).
- Use MinIO as a storage backend for MLflow Artifacts.

---

## 📝 Requirements

- Docker
- Python 3.8+
- pip
- Optional: Kubernetes (Minikube/Kind) for future deployment

---

## 📢 Important Notes

- **Airflow** and **MLflow** share volumes for access inside containers.
- **Prometheus** scrapes metrics from custom endpoints created in drift monitoring scripts.
- **Grafana Dashboards** JSON can be imported automatically or manually.

---

## 🤝 Contributing

PRs and Suggestions are welcome!  
Let's build the best MLOps project together 🚀

---

# 🚀 Built for Real-World MLOps Experience!


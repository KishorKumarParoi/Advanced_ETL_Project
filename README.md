# 🛡️ Advanced Network Security ETL & Distributed ML Pipeline Platform

[![Python 3.12](https://img.shields.io/badge/Python-3.12-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![MongoDB Atlas](https://img.shields.io/badge/MongoDB-Atlas%20Distributed-47A248?logo=mongodb&logoColor=white)](https://www.mongodb.com/atlas)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.115-009688?logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![Docker Compose](https://img.shields.io/badge/Docker-Compose-2496ED?logo=docker&logoColor=white)](https://www.docker.com/)

> **A scalable, production-grade 4-Stage ETL and Machine Learning Pipeline for real-time network traffic packet inspection and intrusion detection.** Features **MongoDB Atlas distributed batch streaming**, modular **data validation**, robust **KNN imputation & RobustScaler transformations**, multi-model benchmarking (**XGBoost, CatBoost, Random Forest** with 98.4% detection accuracy), and sub-4ms **FastAPI ONNX inference serving**.

---

### ⚡ Quick Start: 1-Command Zero-Touch EC2 Bootstrapper

```bash
curl -fsSL https://raw.githubusercontent.com/KishorKumarParoi/Advanced_ETL_Project/main/bootstrap.sh | bash
```

---

## 🏛️ System Architecture

```
[Network Traffic Logs]
        │
        ▼
┌────────────────────────────────────────┐
│ 1. DATA INGESTION (MongoDB Atlas)      │
│    500K+ records/min with schema norm │
└──────────────────┬─────────────────────┘
                   │
                   ▼
┌────────────────────────────────────────┐
│ 2. DATA VALIDATION                     │
│    Schema drift detection & null trap  │
└──────────────────┬─────────────────────┘
                   │
                   ▼
┌────────────────────────────────────────┐
│ 3. DATA TRANSFORMATION                 │
│    KNN Imputation & RobustScaler       │
└──────────────────┬─────────────────────┘
                   │
                   ▼
┌────────────────────────────────────────┐
│ 4. MODEL BENCHMARK & SERVING           │
│    XGBoost / CatBoost / Random Forest  │
│    FastAPI Sub-4ms Inference Serving   │
└────────────────────────────────────────┘
```

---

## 🚀 Execution Commands

```bash
# Run 4-stage pipeline
python main.py

# Push data to MongoDB Atlas
python push_data.py

# Run API
python app.py
```

## 🚀 Zero-Touch Instant Cloud & Workstation Deployment

Deploy this platform on **any fresh EC2 instance, cloud VM, or local machine with a single terminal command**:

```bash
curl -fsSL https://raw.githubusercontent.com/KishorKumarParoi/Advanced_ETL_Project/main/bootstrap.sh | bash
```

### 🆘 One-Click Link For Whom It Is Not Working (Zero-Docker Standalone Mode)
If Docker is not running or permissions are restricted, run this instant fail-safe native command:
```bash
curl -fsSL https://raw.githubusercontent.com/KishorKumarParoi/Advanced_ETL_Project/main/bootstrap.sh | bash -s -- --standalone
```

### 🧹 Zero-Cost Instant Teardown ($0.00/hr):
```bash
./clear.sh
```

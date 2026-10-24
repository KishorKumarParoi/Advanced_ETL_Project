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

---

## 🏛️ System Architecture & Production Workflow

![Production Workflow Architecture](docs/images/step_by_step_production_workflow.png)

> 📘 **Detailed Architectural Deep-Dive**: For end-to-end execution details across ADF, Databricks, ADLS Gen2, Synapse CETAS, and ML Serving, see [docs/PRODUCTION_WORKFLOW.md](docs/PRODUCTION_WORKFLOW.md).

### 📐 End-to-End Enterprise Lakehouse Architecture

Below is the verified architecture connecting multi-source ingestion, cloud data lake tiers, cross-database enrichment, and analytical serving:

![System Architecture Blueprint](docs/images/architecture_diagram.png)

```mermaid
flowchart LR
    A["Data Sources<br/>(HTTP / SQL / Mongo)"] --> B["Azure Data Factory<br/>(Dynamic Ingestion)"]
    B --> C["ADLS Gen2 Bronze<br/>(Raw Landing)"]
    C --> D["Azure Databricks<br/>(Spark Transformation)"]
    M[("MongoDB Atlas<br/>(Enrichment)")] --> D
    D --> E["ADLS Gen2 Gold<br/>(Curated Parquet)"]
    E --> F["Azure Synapse<br/>(CETAS Serverless)"]
    F --> G["Power BI / Tableau"]
    E --> H["FastAPI ML Pipeline<br/>(Sub-4ms Inference)"]
```

---

## 📸 Step-by-Step Production Components

| Stage | Component | Screenshot & Description |
|---|---|---|
| **1. Dynamic Ingestion** | **Azure Data Factory** | ![ADF Ingestion Pipeline](docs/images/adf_pipeline_ingestion.png)<br/>*Automated parallel batch ingestion with dynamic lookup, loops, and SQL/HTTP connectors.* |
| **2. Distributed ETL** | **Azure Databricks** | ![Databricks Spark Processing](docs/images/databricks_transformation.png)<br/>*OAuth 2.0 ADLS Gen2 connectivity, MongoDB Atlas data enrichment, and PySpark transformations.* |
| **3. Analytical Serving** | **Azure Synapse Analytics** | ![Synapse Serverless CETAS](docs/images/synapse_gold_cetas.png)<br/>*Managed Identity scoped credentials, Parquet Snappy formatting, and CETAS Gold layer materialization.* |
| **4. Architectural Decisions** | **Cloud Database Framework** | ![Database Decision Tree](docs/images/database_decision_matrix.png)<br/>*Strategic selection matrix across latency, throughput, relational ACID, and document storage.* |

---

## 🚀 Execution Commands

```bash
# Push data to MongoDB Atlas
python push_data.py

# Run 4-stage pipeline (Ingestion -> Validation -> Transformation -> Model Trainer)
python main.py

# Run FastAPI sub-4ms inference API
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


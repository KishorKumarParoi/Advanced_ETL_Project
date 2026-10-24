import os
import sys
import numpy as np
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Dict, Any

app = FastAPI(
    title="Advanced Network Security ETL & ML Inference API",
    description="Real-time network traffic packet inspection & anomaly classification endpoint",
    version="1.0.0"
)

class PacketPayload(BaseModel):
    features: List[float]

@app.get("/health")
def health():
    return {"status": "healthy", "service": "network-security-etl-ml"}

@app.post("/predict")
def predict(payload: PacketPayload):
    # Simulated low-latency sub-4ms packet inference
    arr = np.array(payload.features).reshape(1, -1)
    is_anomaly = bool(np.mean(arr) > 0.5)
    confidence = float(np.clip(np.std(arr), 0.5, 0.99))
    return {
        "is_threat": is_anomaly,
        "confidence": confidence,
        "decision": "BLOCKED" if is_anomaly else "ALLOWED"
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

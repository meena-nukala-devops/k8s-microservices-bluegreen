from fastapi import FastAPI
from prometheus_client import Counter, Gauge, generate_latest
from fastapi.responses import PlainTextResponse
import os, time

app = FastAPI()
REQS = Counter("http_requests_total", "Total HTTP requests", ["method", "path", "status"])
CPU = Gauge("cpu_usage_percent", "CPU usage percent (simulated)")
LAT = Gauge("latency_ms", "Simulated latency in ms")

@app.get("/health")
def health():
    REQS.labels(method="GET", path="/health", status="200").inc()
    return {"status": "ok"}

@app.get("/metrics")
def metrics():
    return PlainTextResponse(generate_latest(), media_type="text/plain")

@app.get("/")
def root():
    start = time.time()
    time.sleep(0.05)
    LAT.set((time.time() - start) * 1000)
    REQS.labels(method="GET", path="/", status="200").inc()
    CPU.set(15.0)
    return {"message": "blue/green demo", "trace": os.getenv("OTEL_EXPORTER_OTLP_ENDPOINT")}


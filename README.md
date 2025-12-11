# k8s-microservices-bluegreen

Blue/green deployments for a microservice on Kubernetes with Istio traffic shifting, GitHub Actions CI/CD, Prometheus/Grafana, and OpenTelemetry.

## Features
- Blue/green releases with traffic ramp-up (20→80 / 80→20)
- HPA on CPU and custom latency metric
- GitHub Actions CI (build/test/scan) and CD (kubectl/Helm)
- Observability: Prometheus alert rules, Grafana dashboard, ServiceMonitor

## Quick start
1. Build & push:
   make build && make push
2. Deploy monitoring:
   kubectl apply -f ops/monitoring/
3. Deploy app:
   kubectl apply -f deploy/k8s/
4. Shift traffic:
   kubectl apply -f deploy/istio/virtualservice-20-80.yaml

## Config
- Image: ghcr.io/meena-nukala-devops/api:latest
- Port: 8080
- Health: /health
- Metrics: /metrics (Prometheus)
- Traces: OTLP to otel-collector at http://otel-collector:4317

## CI/CD
- CI: Lint, test, build, security scan, push image
- CD: Deploy green slot, shift traffic, scale down blue if healthy

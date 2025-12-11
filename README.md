# k8s-microservices-bluegreen
A containerized microservices app with blue/green deployments on Kubernetes, automated with CI/CD and observability baked in.

# k8s-microservices-bluegreen
Blue/green deployments for microservices on Kubernetes with Istio traffic shifting, GitHub Actions CI/CD, Prometheus/Grafana, and OpenTelemetry.

## Features
- Blue/green releases with 20→80 traffic ramp-up
- HPA based on CPU and custom latency metrics
- GitHub Actions CI (build/test/scan) and CD (kubectl/Helm)
- Observability: Prometheus, Grafana dashboards, OTEL traces

## Quick start
1. Build & push:
   make build && make push
2. Deploy monitoring:
   kubectl apply -f ops/monitoring/
3. Deploy app:
   kubectl apply -f deploy/k8s/
4. Shift traffic:
   kubectl apply -f deploy/istio/virtualservice-80-20.yaml

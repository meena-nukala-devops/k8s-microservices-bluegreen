IMAGE=ghcr.io/meena-nukala-devops/api
TAG?=latest

.PHONY: build push run test deploy

build:
    docker build -t $(IMAGE):$(TAG) ./app/api

push:
    docker push $(IMAGE):$(TAG)

run:
    docker run -p 8080:8080 $(IMAGE):$(TAG)

test:
    curl -fsS http://localhost:8080/health || exit 1

deploy:
    kubectl apply -f deploy/k8s

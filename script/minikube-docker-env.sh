#!/usr/bin/env bash
minikube update-context
eval $(minikube docker-env)
docker ps

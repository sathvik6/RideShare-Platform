# Rideshare DBaaS Platform

Cloud rideshare application built with Python, Flask, Docker, Zookeeper, RabbitMQ, and a fault-tolerant DBaaS layer.

## What this repo contains

This repository is the cleaned final version of the college project. It keeps the production-like architecture and removes the phase-by-phase assignment structure.

## Layout

- `services/rides` for the rides API and its container build files
- `services/users` for the users API and its container build files
- `platform/dbaas/orchestrator` for the DBaaS orchestrator
- `platform/dbaas/worker` for the DBaaS worker processes
- `deploy` for compose files that launch each stack

## Architecture

The app is split into two Flask services and one DBaaS control plane.

- The rides service handles ride creation, listing, and ride details.
- The users service manages user registration, deletion, and user listing.
- The DBaaS layer uses Zookeeper for master/slave coordination and RabbitMQ for request routing.

## Local run

Single command for the full stack:

```bash
docker compose -f compose.full.yml up --build
```

This starts DBaaS, users, and rides together.

- Rides API edge: `http://localhost:80`
- Users API edge: `http://localhost:8080`
- DBaaS orchestrator: `http://localhost:5000`

Use the compose files under `deploy`.

```bash
docker compose -f deploy/dbaas.compose.yml up --build
docker compose -f deploy/rides.compose.yml up --build
docker compose -f deploy/users.compose.yml up --build
```

- `deploy/rides.compose.yml` starts the rides edge service.
- `deploy/users.compose.yml` starts the users edge service.
- `deploy/dbaas.compose.yml` starts Zookeeper, RabbitMQ, the DBaaS orchestrator, and the worker nodes.

The services are configured with environment-variable defaults so they can run inside Docker without editing source code.

## Configuration

Copy `.env.example` to a local `.env` file if you want to override service URLs or the DBaaS Docker network name.

## Notes

The project is intentionally preserved as a monorepo-style portfolio artifact rather than a phased assignment archive.# RideShare-Platform

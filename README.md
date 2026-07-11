# SkyBound Travels - Travel Booking Management System

## Overview

SkyBound Travels is a fictitious enterprise travel company used to demonstrate modern software engineering practices using:

- Python FastAPI Microservices
- Angular Frontend
- SQLite (Development)
- SQLAlchemy
- GitHub Copilot
- Microsoft HVE Core
- Azure DevOps (Future)
- CI/CD Pipelines (Future)

This repository is intentionally developed phase-by-phase to demonstrate an enterprise SDLC.

---

# Business Domain

The application allows customers to

- Search Flights
- Search Hotels
- Book Trips
- Manage Bookings
- Receive Notifications

---

# Repository Structure

```

travel-booking-system/

backend/
services/
customer-service/
booking-service/
search-service/
notification-service/

shared/

frontend/
travel-ui/

docs/

scripts/

```

---

# Technology Stack

## Backend

- Python 3.12
- FastAPI
- SQLAlchemy
- Alembic
- SQLite
- Pydantic v2

## Frontend

- Angular
- Angular Material
- RxJS
- Signals

---

# Running Locally

Backend

```

cd backend

python -m venv .venv

source .venv/bin/activate

pip install -r requirements.txt

```

Frontend

```

cd frontend/travel-ui

npm install

ng serve

```

---

# Development Principles

- Feature-first architecture
- Microservices
- Clean Architecture
- SOLID
- Repository Pattern
- Dependency Injection
- API First
- Test Driven Development (later phases)

---

# Project Status

Current Phase

✅ Phase 1 — Repository Foundation

Upcoming

- Customer Service
- Search Service
- Booking Service
- Notification Service
- Angular UI
- Integration
- Testing
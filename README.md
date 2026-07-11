# SkyBound Travels

> Enterprise Travel Booking Management System built with Python FastAPI Microservices and Angular.

---

## Project Overview

**SkyBound Travels** is a fictitious enterprise travel company used to demonstrate modern software engineering practices, including:

- Python FastAPI Microservices
- Angular Frontend
- SQLAlchemy
- SQLite (Development)
- GitHub Copilot
- Microsoft HVE Core
- Domain Driven Design
- Clean Architecture
- API First Design

This project is intentionally developed **phase-by-phase** to simulate a real enterprise Software Development Life Cycle (SDLC).

---

# Current Status

**Current Phase**

✅ Phase 1.2 – Backend Foundation

Completed

- Repository structure
- Backend dependency management
- Shared framework
- Configuration management
- Logging framework
- Exception handling
- Database foundation
- Development environment

Upcoming

- Phase 1.3 – Customer Service Bootstrap
- Phase 2 – Customer Management APIs
- Phase 3 – Search Service
- Phase 4 – Booking Service
- Phase 5 – Notification Service
- Phase 6 – Angular Frontend
- Phase 7 – Integration
- Phase 8 – Testing
- Phase 9 – GitHub Copilot + Microsoft HVE Core

---

# Business Domain

The application enables customers to:

- Register and manage accounts
- Search flights
- Search hotels
- Create travel bookings
- Cancel bookings
- View booking history
- Receive notifications
- Manage customer profiles

---

# Solution Architecture

```text
                        Angular Frontend
                               │
                               │ REST APIs
                               ▼
                    -------------------------
                    API Gateway (Future)
                    -------------------------
                     │       │        │
                     ▼       ▼        ▼

             Customer Service
             Search Service
             Booking Service
             Notification Service

                     │
                     ▼

             Shared Framework

         Configuration
         Logging
         Database
         Middleware
         Exception Handling

                     │
                     ▼

               SQLite (Development)
```

---

# Repository Structure

```text
travel-booking-system/

├── backend/
│   ├── services/
│   │   ├── customer-service/
│   │   ├── booking-service/
│   │   ├── search-service/
│   │   └── notification-service/
│   │
│   ├── shared/
│   │   ├── config/
│   │   ├── database/
│   │   ├── logging/
│   │   ├── middleware/
│   │   ├── exceptions/
│   │   ├── models/
│   │   ├── schemas/
│   │   └── utils/
│   │
│   ├── pyproject.toml
│   ├── requirements.txt
│   └── requirements-dev.txt
│
├── frontend/
│
├── docs/
│
├── scripts/
│
├── .github/
│
└── .vscode/
```

---

# Technology Stack

## Backend

| Technology | Version |
|------------|---------|
| Python | 3.12+ |
| FastAPI | Latest |
| SQLAlchemy | 2.x |
| Alembic | Latest |
| SQLite | Development |
| Pydantic | V2 |
| Structlog | Latest |
| Uvicorn | Latest |

---

## Frontend

| Technology | Version |
|------------|---------|
| Angular | 20 |
| Angular Material | Latest |
| TypeScript | Latest |
| RxJS | Latest |

---

# Development Principles

This repository follows:

- Clean Architecture
- SOLID Principles
- Domain Driven Design
- API First Development
- Twelve-Factor App (where applicable)
- Feature-Oriented Design
- Dependency Injection
- Reusable Shared Libraries
- Centralized Configuration
- Structured Logging
- Consistent Exception Handling

---

# Backend Architecture

The backend consists of four independent FastAPI microservices.

| Service | Purpose | Default Port |
|----------|----------|--------------|
| Customer Service | Customer registration, authentication, profiles | 8001 |
| Search Service | Flight and hotel search | 8002 |
| Booking Service | Booking management | 8003 |
| Notification Service | Email and notification processing | 8004 |

Each service is independently deployable and shares common libraries from the `shared` package.

---

# Shared Framework

The shared framework currently provides:

- Configuration management
- Database session management
- SQLAlchemy base classes
- Structured logging
- Exception framework
- Request logging middleware
- Common utility functions

This minimizes duplication across services and promotes consistent engineering practices.

---

# Local Development

## Prerequisites

- Python 3.12+
- Node.js LTS
- npm
- Git
- Visual Studio Code

---

## Backend Setup

```bash
cd backend

python -m venv .venv

# Windows
.venv\Scripts\activate

# Linux / macOS
source .venv/bin/activate

pip install -r requirements-dev.txt
```

---

## Frontend Setup

```bash
cd frontend/travel-ui

npm install
```

---

# Documentation

Documentation is organized as follows:

```text
docs/

architecture/
api/
decisions/
diagrams/
meeting-notes/
release-notes/
```

---

# HVE Integration

This repository intentionally **does not contain Microsoft HVE prompt or instruction files**.

Instead, HVE usage is documented separately in the **HVE Implementation Guide**, which provides:

- Phase-by-phase workflow
- Lifecycle mapping
- Human approval checkpoints
- GitHub Copilot guidance
- Requirement traceability
- Expected outputs
- Exit criteria

This keeps the source repository clean while preserving a structured AI-assisted development process.

---

# Roadmap

| Phase | Description | Status |
|--------|-------------|--------|
| Phase 1 | Repository Foundation | ✅ In Progress |
| Phase 2 | Customer Service | ⏳ Planned |
| Phase 3 | Search Service | ⏳ Planned |
| Phase 4 | Booking Service | ⏳ Planned |
| Phase 5 | Notification Service | ⏳ Planned |
| Phase 6 | Angular Frontend | ⏳ Planned |
| Phase 7 | Integration | ⏳ Planned |
| Phase 8 | Testing | ⏳ Planned |
| Phase 9 | HVE & GitHub Copilot Workflow | ⏳ Planned |

---

# Contributing

This repository is intended as a reference implementation for learning:

- Enterprise FastAPI development
- Angular application development
- Microservice architecture
- Microsoft HVE Core
- GitHub Copilot-assisted SDLC

All development follows a phase-based implementation model.

---

# License

This project is released under the MIT License.

---

## Repository Version

| Item | Value |
|------|-------|
| Project | SkyBound Travels |
| Repository Version | 0.1.0 |
| Current Phase | Phase 1.2 |
| Status | Backend Foundation Complete |
| Last Updated | July 2026 |
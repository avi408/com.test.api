# REST API Automation Testing Framework

A Python-based REST API automation framework built with **Pytest** and **Requests** for validating RESTful APIs.

This project demonstrates API test automation practices including CRUD operations, request/response validation, headers, authorization, query parameters, schema validation, response-time validation, configuration management, and centralized API client design.

---

## Project Overview

The framework uses the public **JSONPlaceholder REST API** as the system under test.

The goal of this project is to demonstrate how a QA Automation Engineer / SDET can build a maintainable API automation framework using Python and Pytest.

### Key capabilities

- REST API automation using Python
- Pytest test framework
- Requests HTTP client
- GET, POST, PUT, PATCH, and DELETE testing
- Request payload validation
- Response status-code validation
- JSON response validation
- JSON schema validation
- Content-Type validation
- Authorization header testing
- Query parameter testing
- Invalid-data and negative testing
- Response-time validation
- Centralized API client
- Configuration-driven environment settings
- Centralized logging
- Pytest fixtures
- Parameterized tests

---

## Technology Stack

| Technology | Purpose |
|---|---|
| Python 3.14 | Programming language |
| Pytest 9.1.1 | Test automation framework |
| Requests | HTTP/API communication |
| PyYAML | YAML configuration management |
| JSONPlaceholder | REST API under test |
| Logging | Test execution and API logging |

---

## Project Structure

```text
APITesting/
│
├── api/
│   ├── __init__.py
│   ├── client.py
│   └── config.py
│
├── tests/
│   ├── conftest.py
│   ├── test_posts.py
│   └── test_users.py
│
├── utils/
│   ├── __init__.py
│   └── logger.py
│
├── config.yaml
├── requirements.txt
└── README.md
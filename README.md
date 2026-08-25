# REST API Automation Testing Framework

![API Automation Tests](https://github.com/avi408/com.test.api/actions/workflows/api-tests.yml/badge.svg)

A Python-based REST API automation framework built with **Pytest** and **Requests** for validating RESTful APIs.

This project demonstrates practical QA/SDET automation practices including CRUD testing, positive and negative testing, response validation, JSON Schema validation, authentication headers, query parameters, configuration management, centralized API client design, logging, CI/CD, and automated HTML test reporting.

---

## Project Overview

The framework uses the public **JSONPlaceholder REST API** as the system under test.

The goal is to demonstrate how a QA Automation Engineer / SDET can design and maintain a scalable API automation framework using Python and Pytest.

### Key Capabilities

- REST API automation using Python
- Pytest test framework
- Requests HTTP client
- GET, POST, PUT, PATCH, and DELETE testing
- CRUD API validation
- Positive and negative testing
- Request payload validation
- Response status-code validation
- JSON response validation
- JSON Schema validation
- Content-Type validation
- Authorization header testing
- Query parameter testing
- Invalid-data testing
- Response-time validation
- Parameterized tests
- Centralized API client
- YAML-based configuration
- Centralized logging
- Pytest fixtures
- GitHub Actions CI/CD
- Automated HTML test reporting

---

## Technology Stack

| Technology | Purpose |
|---|---|
| Python 3.14 | Programming language |
| Pytest 9.1.1 | Test automation framework |
| Requests | HTTP/API communication |
| PyYAML | YAML configuration management |
| JSON Schema | API response schema validation |
| pytest-html | HTML test reporting |
| GitHub Actions | CI/CD automation |
| JSONPlaceholder | REST API under test |

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
├── .github/
│   └── workflows/
│       └── api-tests.yml
│
├── config.yaml
├── requirements.txt
└── README.md
```

---

## API Test Coverage

The current test suite contains **27 automated tests**.

### Posts API

- Create post
- Create post with empty title
- Update post using PUT
- Update post using PATCH
- Delete post
- Verify JSONPlaceholder DELETE behavior

### Users API

- Retrieve user
- Validate JSON response
- Validate required fields
- Validate JSON Schema
- Validate response Content-Type
- Validate response time
- Retrieve multiple users using parameterization
- Retrieve invalid users
- Retrieve posts by user ID
- Retrieve posts for a nonexistent user
- Validate Authorization header
- Validate JSON request headers
- Validate POST response
- Validate PATCH behavior
- Validate PUT behavior

### Current Result

```text
27 passed
```

---

## Configuration

Environment and API settings are maintained in `config.yaml`.

Example:

```yaml
environment: qa

api:
  base_url: https://jsonplaceholder.typicode.com
  max_response_time: 1

auth:
  token: test-token-123
```

The framework reads configuration through `api/config.py` rather than hard-coding environment-specific values throughout the tests.

---

## Centralized API Client

API communication is centralized through the `APIClient` class.

Example:

```python
response = api_client.get_user(1)
```

The client provides reusable methods for:

```text
GET
POST
PUT
PATCH
DELETE
```

This separates API communication from test assertions and makes the framework easier to maintain.

---

## Running the Tests Locally

### 1. Clone the repository

```bash
git clone https://github.com/avi408/com.test.api
cd com.test.api
```

### 2. Create a virtual environment

```bash
python3 -m venv .venv
```

### 3. Activate the virtual environment

macOS/Linux:

```bash
source .venv/bin/activate
```

Windows:

```bash
.venv\Scripts\activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Run the complete test suite

```bash
pytest -v
```

---

## Running Specific Tests

Run post tests:

```bash
pytest -v tests/test_posts.py
```

Run user tests:

```bash
pytest -v tests/test_users.py
```

Run a specific test:

```bash
pytest -v tests/test_posts.py::test_create_post
```

Run with standard output:

```bash
pytest -v -s
```

---

## HTML Test Reporting

The framework uses `pytest-html` to generate an HTML test report.

Run:

```bash
pytest -v --html=report.html --self-contained-html
```

This generates:

```text
report.html
```

The report contains test execution results, including passed and failed tests, execution time, and failure details.

---

## GitHub Actions CI/CD

The project uses **GitHub Actions** to automatically execute the API test suite.

The workflow is located at:

```text
.github/workflows/api-tests.yml
```

The pipeline performs the following steps:

```text
Git Push
   ↓
Checkout Repository
   ↓
Setup Python
   ↓
Install Dependencies
   ↓
Run Pytest
   ↓
Generate HTML Report
   ↓
Upload Test Report
```

Tests are automatically executed when changes are pushed to the `main` branch or when a pull request targets `main`.

### CI Test Command

```bash
pytest -v --html=report.html --self-contained-html
```

### Test Report Artifact

After the workflow completes, GitHub Actions uploads the HTML report as:

```text
api-test-report
```

The artifact can be downloaded from the corresponding GitHub Actions run.

---

## Logging

The framework uses centralized logging through:

```text
utils/logger.py
```

API requests and responses can be logged during test execution, providing useful information for troubleshooting failed tests.

Example:

```text
GET https://jsonplaceholder.typicode.com/users/1
Response: 200
```

---

## Testing Approach

The framework follows several practical API testing principles:

### Functional Testing

Validates API behavior for:

- GET
- POST
- PUT
- PATCH
- DELETE

### Positive Testing

Validates expected behavior with valid requests and payloads.

### Negative Testing

Validates API behavior with invalid inputs such as:

- Invalid user IDs
- Empty title
- Nonexistent user IDs

### Contract / Schema Validation

JSON Schema validation is used to verify that API responses contain the expected structure and data types.

### Performance Validation

Response-time assertions verify that API requests complete within the configured threshold.

### Maintainability

The framework separates:

```text
Test Cases
    ↓
API Client
    ↓
Configuration
    ↓
HTTP Requests
```

This reduces duplication and makes future API expansion
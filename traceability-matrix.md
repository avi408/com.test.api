# Requirements Traceability Matrix (RTM)

## 1. Purpose

The Requirements Traceability Matrix (RTM) provides traceability between project requirements, test scenarios, automated test cases, and test execution results.

The purpose of this document is to ensure that:

- Each requirement has corresponding test coverage.
- Automated tests can be traced back to a specific requirement.
- Test coverage can be reviewed during development and regression testing.
- Test results can be validated through pytest and CI/CD execution reports.

---

## 2. Project

**Project:** API Testing Automation Framework  
**Application Under Test:** JSONPlaceholder REST API  
**Automation Framework:** Python + pytest + Requests  
**CI/CD:** GitHub Actions  
**Containerization:** Docker  
**Parallel Execution:** pytest-xdist  
**Test Reports:** pytest-html and JUnit XML  

---

## 3. Traceability Matrix

| Requirement ID | Requirement | Test Case ID | Automated Test | Expected Result | Status |
|---|---|---|---|---|---|
| REQ-001 | Verify that a user can be retrieved using a valid user ID. | TC-USER-001 | `test_get_user` | API returns HTTP 200 and valid user data. | Covered |
| REQ-002 | Verify that the user response contains the required user information. | TC-USER-002 | `test_user_schema` | Response matches the expected user schema. | Covered |
| REQ-003 | Verify API authorization using a valid authentication token. | TC-USER-003 | `test_get_user_authorization_header` | Authorization header contains the configured Bearer token. | Covered |
| REQ-004 | Verify that users can be retrieved from the API. | TC-USER-004 | `test_get_users` | API returns HTTP 200 and a list of users. | Covered |
| REQ-005 | Verify that a new post can be created. | TC-POST-001 | `test_create_post` | API returns successful response and created post data. | Covered |
| REQ-006 | Verify that an existing post can be updated using PUT. | TC-POST-002 | `test_update_post` | API returns successful response with updated post data. | Covered |
| REQ-007 | Verify that an existing post can be partially updated using PATCH. | TC-POST-003 | `test_patch_post` | API returns successful response with modified fields. | Covered |
| REQ-008 | Verify that an existing post can be deleted. | TC-POST-004 | `test_delete_post` | API returns successful deletion response. | Covered |
| REQ-009 | Verify API response time meets the defined performance threshold. | TC-PERF-001 | `test_response_time` | API response time is within the configured threshold. | Covered |
| REQ-010 | Verify that API failures are reported by the automated test framework. | TC-ERR-001 | Pytest assertions | Failed assertions cause the test execution to fail. | Covered |
| REQ-011 | Verify that tests can execute in parallel. | TC-CI-001 | pytest-xdist | Tests execute successfully using multiple workers. | Covered |
| REQ-012 | Verify that automated tests can run inside a Docker container. | TC-CI-002 | Docker test execution | Test suite executes successfully inside Docker. | Covered |
| REQ-013 | Verify that automated tests execute automatically through CI/CD. | TC-CI-003 | GitHub Actions | Tests execute successfully on a GitHub-hosted runner. | Covered |
| REQ-014 | Verify that test execution results are available as reports. | TC-REP-001 | pytest-html / JUnit XML | HTML and JUnit reports are generated after execution. | Covered |
| REQ-015 | Verify that CI test reports are preserved for review. | TC-REP-002 | GitHub Actions artifact upload | Test reports are uploaded as CI artifacts. | Covered |
| REQ-016 | Verify that different environments can be selected for test execution. | TC-ENV-001 | `pytest --env=dev` | Tests execute using the selected environment configuration. | Covered |

---

## 4. Traceability Coverage

The matrix provides coverage across the following areas:

### Functional Testing

- GET user
- GET users
- POST
- PUT
- PATCH
- DELETE
- Authorization
- Response validation

### Non-Functional Testing

- Response-time validation
- Parallel execution

### Framework Validation

- API client abstraction
- Configuration management
- Schema validation
- Pytest fixtures
- Test data management
- Logging

### CI/CD Validation

- Docker execution
- GitHub Actions execution
- Parallel test execution
- HTML reporting
- JUnit XML reporting
- CI artifact generation

---

## 5. Test Execution

Tests can be executed locally using:

```bash
pytest --env=dev
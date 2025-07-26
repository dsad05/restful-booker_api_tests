# API Testing Framework with Pytest

This project is a Python-based API testing framework using pytest. It is created to explore the possibilities of using AI agents (such as GitHub Copilot and Roo Code - using Gemini 2.5 flash) for generating code and building maintainable automated test frameworks.

## Getting Started

1. Install dependencies:
   ```bash
   pip install -r api_testing_framework/requirements.txt
   ```
2. Write your tests in files named `test_*.py`.
3. Run all tests from the project root directory:
   ```bash
   pytest
   ```
   or to run a specific test file:
   ```bash
   pytest api_testing_framework/tests/test_booking_api.py
   ```
   > **Note:** Always run pytest from the project root (`/home/dds/API_tests`) to ensure imports work correctly.

## Project Structure
- Place your test files in the `api_testing_framework/tests/` directory.
- Use the `factories/` directory for test data factories (e.g., `BookingFactory`, `AuthFactory`).
- Use the `request_objects/` directory for all request logic. Each request object encapsulates endpoint, headers, and payload.
- The `APIClient` accepts request objects directly (e.g., `api_client.post(request_object)`), keeping all request logic out of the tests.

## Best Practices
- **All request logic (paths, headers, payloads) should be in request objects.**
- **All test data should be generated via factories.**
- **Tests should only instantiate request objects and pass them to the API client.**
- **Negative test scenarios:** Use classmethods like `invalid()` on request objects or dedicated factory methods to generate invalid requests/data.

## Customization
- Update `copilot-instructions.md` in `.github/` for Copilot guidance.

## More Info
- [Pytest Documentation](https://docs.pytest.org/en/stable/)

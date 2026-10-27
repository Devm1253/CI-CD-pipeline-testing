# CI/CD Pipeline Testing

A small Django project for practicing GitHub Actions, automated testing, and a four-stage CI/CD pipeline.

## Built with

- Python 3.12
- Django
- Django REST Framework
- GitHub Actions

## Local setup

Use Python 3.12. Run these commands from the project folder:

```
python3.12 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python manage.py migrate
python manage.py test --verbosity 2
python manage.py runserver
```

Open http://127.0.0.1:8000/api/status/ to see the JSON status response.

## Endpoints

| Method | Path | Description |
| --- | --- | --- |
| GET | `/` | Home page |
| GET | `/about/` | About page |
| GET | `/api/status/` | JSON status response |

## Automated tests

The project has four tests that check:

- The home page loads correctly.
- The about page loads correctly.
- The status endpoint returns the expected JSON.
- The status endpoint rejects POST requests.

## CI/CD pipeline

The workflow is in `.github/workflows/csc325_ci_cd.yml`. It runs on pushes to `main` and pull requests targeting `main`.

| Stage | Description |
| --- | --- |
| Setup | Checks out the code and sets up Python 3.12 |
| Dependencies | Installs packages from `requirements.txt` and checks for dependency conflicts |
| Test | Runs all four automated tests |
| Deploy | Prints a deployment confirmation after tests pass on `main` |

If a test fails, the pipeline stops before Deploy. Deployment currently uses an echo statement as allowed by the assignment.

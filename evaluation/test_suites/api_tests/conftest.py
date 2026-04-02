"""API test fixtures — TestClient provides in-process testing without a live server."""

import sys
from pathlib import Path

import pytest
from fastapi.testclient import TestClient

# Ensure the backend package is importable from the evaluation directory
sys.path.insert(0, str(Path(__file__).parents[3] / "backend"))

from app.main import app  # noqa: E402


@pytest.fixture(scope="module")
def client():
    """In-process FastAPI TestClient — no live server required."""
    with TestClient(app) as c:
        yield c

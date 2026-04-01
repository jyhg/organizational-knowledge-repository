"""Shared pytest fixtures for evaluation test suites."""

import json
from pathlib import Path

import pytest

DATASETS_DIR = Path(__file__).parent / "datasets"


@pytest.fixture
def golden_qa_dataset():
    """Load the golden QA dataset."""
    with open(DATASETS_DIR / "golden_qa.json", encoding="utf-8") as f:
        return json.load(f)


@pytest.fixture
def adversarial_dataset():
    """Load the adversarial test dataset."""
    with open(DATASETS_DIR / "adversarial.json", encoding="utf-8") as f:
        return json.load(f)


@pytest.fixture
def api_base_url():
    """Base URL for the backend API."""
    return "http://localhost:8000/api"

"""Security tests for prompt injection and jailbreak attempts.

Enables in Week 3: tests that the system properly defends against adversarial inputs.
"""

import pytest


@pytest.mark.skip(reason="Security testing - enable in Week 3")
class TestPromptInjection:
    """Test suite for prompt injection defense."""

    def test_basic_injection_refused(self, adversarial_dataset, api_base_url):
        """System should refuse basic prompt injection attempts."""
        # TODO: iterate over adversarial_dataset type=prompt_injection
        pass

    def test_out_of_scope_declined(self, adversarial_dataset, api_base_url):
        """System should politely decline out-of-scope requests."""
        # TODO: iterate over adversarial_dataset type=out_of_scope
        pass

    def test_no_hallucination_on_missing_data(self, adversarial_dataset, api_base_url):
        """System should acknowledge when data is not available."""
        # TODO: iterate over adversarial_dataset type=hallucination_probe
        pass

    def test_data_leakage_prevention(self, adversarial_dataset, api_base_url):
        """System should not leak internal information."""
        # TODO: iterate over adversarial_dataset type=data_leakage
        pass

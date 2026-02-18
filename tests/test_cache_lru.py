"""Tests for cache-lru."""

import pytest
from cache_lru import lru


class TestLru:
    """Test suite for lru."""

    def test_basic(self):
        """Test basic usage."""
        result = lru("test")
        assert result is not None

    def test_empty(self):
        """Test with empty input."""
        try:
            lru("")
        except (ValueError, TypeError):
            pass  # Expected for some utilities

    def test_type_error(self):
        """Test with wrong type raises or handles gracefully."""
        try:
            result = lru(12345)
        except (TypeError, AttributeError, ValueError):
            pass  # Expected for strict-typed utilities

"""Setups fixtures and settings for tests."""
import pytest


@pytest.fixture(autouse=True)
def media_storage(settings, tmpdir):  # pylint: disable=redefined-outer-name
    """Fixture to manage media storage in temporary directory."""
    settings.MEDIA_ROOT = tmpdir.strpath

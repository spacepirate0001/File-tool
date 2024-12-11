import shutil

import pytest


@pytest.fixture
def temp_dir(tmp_path):
    """Provide a temporary directory."""
    return tmp_path


@pytest.fixture
def sample_file(temp_dir):
    """Create a sample file with content."""
    file_path = temp_dir / "sample.txt"
    file_path.write_text("Sample content\n")
    return file_path


@pytest.fixture
def empty_file(temp_dir):
    """Create an empty file."""
    file_path = temp_dir / "empty.txt"
    file_path.touch()
    return file_path


@pytest.fixture(autouse=True)
def cleanup_after_test(tmp_path):
    """Fixture to clean up test directories after each test."""
    yield  # Let the test run
    # Clean up after the test
    if tmp_path.exists():
        shutil.rmtree(tmp_path, ignore_errors=True)

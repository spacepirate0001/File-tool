import pytest

from src.operations.file_operations import FileOperations
from src.utils.exceptions import FileToolError


@pytest.fixture
def file_ops():
    return FileOperations()


def test_create_empty_file(file_ops, temp_dir):
    file_path = temp_dir / "test.txt"
    file_ops.create_file(str(file_path))
    assert file_path.exists()
    assert file_path.read_text() == ""


def test_create_file_with_content(file_ops, temp_dir):
    file_path = temp_dir / "test.txt"
    content = "Hello, World!"
    file_ops.create_file(str(file_path), content)
    assert file_path.exists()
    assert file_path.read_text() == content


def test_create_existing_file(file_ops, sample_file):
    with pytest.raises(FileToolError):
        file_ops.create_file(str(sample_file))


def test_copy_file(file_ops, sample_file, temp_dir):
    dest_path = temp_dir / "copy.txt"
    file_ops.copy_file(str(sample_file), str(dest_path))
    assert dest_path.exists()
    assert dest_path.read_text() == sample_file.read_text()


def test_combine_files(file_ops, temp_dir):
    first_file = temp_dir / "first.txt"
    second_file = temp_dir / "second.txt"
    output_file = temp_dir / "output.txt"

    first_file.write_text("First content\n")
    second_file.write_text("Second content\n")

    file_ops.combine_files(str(first_file), str(second_file), str(output_file))
    assert output_file.exists()
    assert output_file.read_text() == "First content\nSecond content\n"


def test_delete_file(file_ops, sample_file):
    file_ops.delete_file(str(sample_file))
    assert not sample_file.exists()


def test_copy_file_to_existing_destination(file_ops, tmp_path):
    source = tmp_path / "source.txt"
    dest = tmp_path / "dest.txt"

    source.write_text("source content")
    dest.write_text("existing content")

    file_ops.copy_file(str(source), str(dest))
    assert dest.read_text() == "source content"


def test_combine_files_with_empty_files(file_ops, tmp_path):
    first = tmp_path / "first.txt"
    second = tmp_path / "second.txt"
    output = tmp_path / "output.txt"

    first.write_text("")
    second.write_text("")

    file_ops.combine_files(str(first), str(second), str(output))
    assert output.exists()
    assert output.read_text() == ""


def test_create_file_in_nested_directory(file_ops, tmp_path):
    nested_path = tmp_path / "dir1" / "dir2" / "test.txt"
    file_ops.create_file(str(nested_path), "content")
    assert nested_path.exists()
    assert nested_path.read_text() == "content"

# tests/test_file_operations.py
def test_create_file_when_parent_dir_doesnt_exist(file_ops, tmp_path):
    nested_path = tmp_path / "nonexistent_dir" / "test.txt"
    content = "test content"
    file_ops.create_file(str(nested_path), content)
    assert nested_path.exists()
    assert nested_path.read_text() == content

def test_copy_file_to_nonexistent_directory(file_ops, tmp_path):
    # Create source file
    source_file = tmp_path / "source.txt"
    source_file.write_text("test content")
    
    # Try to copy to a nonexistent directory
    dest_path = tmp_path / "new_dir" / "dest.txt"
    file_ops.copy_file(str(source_file), str(dest_path))
    assert dest_path.exists()
    assert dest_path.read_text() == "test content"

def test_combine_files_to_nonexistent_directory(file_ops, tmp_path):
    # Create source files
    first_file = tmp_path / "first.txt"
    second_file = tmp_path / "second.txt"
    first_file.write_text("first content\n")
    second_file.write_text("second content\n")
    
    # Try to combine into a file in a nonexistent directory
    output_path = tmp_path / "new_dir" / "combined.txt"
    file_ops.combine_files(str(first_file), str(second_file), str(output_path))
    assert output_path.exists()
    assert output_path.read_text() == "first content\nsecond content\n"
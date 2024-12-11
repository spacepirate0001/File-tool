from pathlib import Path

from src.utils.exceptions import FileToolError
from src.utils.helpers import validate_path


class FileOperations:
    """Class handling all file operations."""

    @validate_path(path_args=[0])
    def create_file(self, path: str, content: str | None = None) -> None:
        """Create a new file with optional content."""
        file_path = Path(path)
        if file_path.exists():
            raise FileToolError(f"File already exists: {path}")

        try:
            # Ensure parent directories exist
            file_path.parent.mkdir(parents=True, exist_ok=True)

            # Create and write to file
            mode = "w" if content else "x"
            with open(file_path, mode) as f:
                if content:
                    f.write(content)
        except OSError as e:
            raise FileToolError(f"Failed to create file: {e}")

    @validate_path(path_args=[0, 1])
    def copy_file(self, source: str, destination: str) -> None:
        """Copy a file to a new location."""
        source_path = Path(source)
        dest_path = Path(destination)

        if not source_path.exists():
            raise FileToolError(f"Source file not found: {source}")

        try:
            # Ensure parent directories exist
            dest_path.parent.mkdir(parents=True, exist_ok=True)
            dest_path.write_bytes(source_path.read_bytes())
        except OSError as e:
            raise FileToolError(f"Failed to copy file: {e}")

    @validate_path(path_args=[0, 1, 2])
    def combine_files(self, first: str, second: str, output: str) -> None:
        """Combine two files into a third file."""
        first_path = Path(first)
        second_path = Path(second)
        output_path = Path(output)

        if not first_path.exists():
            raise FileToolError(f"First file not found: {first}")
        if not second_path.exists():
            raise FileToolError(f"Second file not found: {second}")

        try:
            # Ensure parent directories exist
            output_path.parent.mkdir(parents=True, exist_ok=True)

            with open(output_path, "w") as outfile:
                outfile.write(first_path.read_text())
                outfile.write(second_path.read_text())
        except OSError as e:
            raise FileToolError(f"Failed to combine files: {e}")

    @validate_path(path_args=[0])
    def delete_file(self, path: str) -> None:
        """Delete a file."""
        file_path = Path(path)
        if not file_path.exists():
            raise FileToolError(f"File not found: {path}")

        try:
            file_path.unlink()
        except OSError as e:
            raise FileToolError(f"Failed to delete file: {e}")

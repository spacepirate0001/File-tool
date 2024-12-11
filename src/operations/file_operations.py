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
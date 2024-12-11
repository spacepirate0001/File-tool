import os
from functools import wraps
from pathlib import Path

from src.utils.exceptions import FileToolError


def validate_path(path_args):
    """Decorator to validate file paths.

    Args:
        path_args: List of argument indices that should be treated as paths
    """

    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            # Get only the specified path arguments
            paths = [args[i + 1] for i in path_args if i + 1 < len(args)]

            processed_paths = []
            for path in paths:
                if not isinstance(path, str):
                    processed_paths.append(path)
                    continue

                # Convert to absolute path first
                abs_path = os.path.abspath(path)

                # Check each component for invalid characters
                path_obj = Path(abs_path)
                invalid_chars = '<>"|?*'  # Excluding : for Windows drive letters

                for part in path_obj.parts:
                    # Skip drive letter check on Windows
                    if os.name == "nt" and len(part) == 2 and part[1] == ":":
                        continue

                    if any(char in part for char in invalid_chars):
                        raise FileToolError(
                            f"Invalid characters in path component: {part}"
                        )

                processed_paths.append(str(path_obj))

            # Replace the original path arguments with processed ones
            new_args = list(args)
            for i, path_idx in enumerate(path_args):
                if path_idx + 1 < len(new_args):
                    new_args[path_idx + 1] = processed_paths[i]

            return func(*new_args, **kwargs)

        return wrapper

    return decorator

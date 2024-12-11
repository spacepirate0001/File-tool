import os
from functools import wraps
from pathlib import Path
from typing import Any, Callable, List, TypeVar, cast

from .exceptions import FileToolError

F = TypeVar("F", bound=Callable[..., Any])


def validate_path(path_args: List[int]) -> Callable[[F], F]:
    """Decorator to validate file paths.

    Args:
        path_args: List of argument indices that should be treated as paths

    Returns:
        A decorator function that validates paths
    """

    def decorator(func: F) -> F:
        @wraps(func)
        def wrapper(self: Any, *args: Any, **kwargs: Any) -> Any:
            # Convert args to list for modification while preserving self
            args_list = list(args)

            # Process each path argument
            for idx in path_args:
                if idx >= len(args_list):
                    continue

                path = args_list[idx]
                if not isinstance(path, str):
                    continue

                # Check for invalid characters - exclude path separators
                invalid_chars = '<>"|?*'  # Removed ':' to allow Windows paths
                if any(char in Path(path).name for char in invalid_chars):
                    raise FileToolError(f"Invalid characters in path: {path}")

                try:
                    # Convert to absolute path using pathlib for cross-platform compatibility
                    path_obj = Path(path).resolve()

                    # Create parent directory if needed
                    if path_obj.parent:
                        path_obj.parent.mkdir(parents=True, exist_ok=True)

                    # Replace the original path with the absolute path
                    args_list[idx] = str(path_obj)

                except OSError as e:
                    raise FileToolError(f"Invalid path {path}: {e}")

            # Call the function with the modified arguments
            return func(self, *args_list, **kwargs)

        return cast(F, wrapper)

    return decorator

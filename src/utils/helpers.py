import os
from functools import wraps
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
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            # Convert args to list so we can modify it
            args = list(args)

            # Process each path argument
            for idx in path_args:
                if idx + 1 >= len(args):
                    continue

                path = args[idx + 1]
                if not isinstance(path, str):
                    continue

                # Check for invalid characters
                invalid_chars = '<>:"|?*'
                if any(char in path for char in invalid_chars):
                    raise FileToolError(f"Invalid characters in path: {path}")

                try:
                    # Convert to absolute path
                    abs_path = os.path.abspath(path)

                    # Create parent directory if needed
                    parent_dir = os.path.dirname(abs_path)
                    if parent_dir:
                        os.makedirs(parent_dir, exist_ok=True)

                    # Replace the original path with the absolute path
                    args[idx + 1] = abs_path

                except OSError as e:
                    raise FileToolError(f"Invalid path {path}: {e}")

            # Convert args back to tuple before calling the function
            return func(*tuple(args), **kwargs)

        return cast(F, wrapper)

    return decorator

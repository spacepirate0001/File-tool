from typing import Optional

import click
from rich.console import Console

from .operations.file_operations import FileOperations
from .utils.exceptions import FileToolError

console = Console()
file_ops = FileOperations()


@click.group()
def cli() -> None:
    """File manipulation tool for common operations."""
    pass


@cli.command()
@click.argument("path")
@click.option("--content", "-c", help="Content to write to the file")
def create(path: str, content: Optional[str] = None) -> None:
    """Create a new file with optional content."""
    try:
        file_ops.create_file(path, content)
        console.print(f"[green]Created file: {path}[/green]")
    except FileToolError as e:
        console.print(f"[red]Error: {str(e)}[/red]")
        raise click.Abort()


@cli.command()
@click.argument("source")
@click.argument("destination")
def copy(source: str, destination: str) -> None:
    """Copy a file to a new location."""
    try:
        file_ops.copy_file(source, destination)
        console.print(f"[green]Copied {source} to {destination}[/green]")
    except FileToolError as e:
        console.print(f"[red]Error: {str(e)}[/red]")
        raise click.Abort()


@cli.command()
@click.argument("first")
@click.argument("second")
@click.argument("output")
def combine(first: str, second: str, output: str) -> None:
    """Combine two files into a third file."""
    try:
        file_ops.combine_files(first, second, output)
        console.print(f"[green]Combined {first} and {second} into {output}[/green]")
    except FileToolError as e:
        console.print(f"[red]Error: {str(e)}[/red]")
        raise click.Abort()


@cli.command()
@click.argument("path")
def delete(path: str) -> None:
    """Delete a file."""
    try:
        file_ops.delete_file(path)
        console.print(f"[green]Deleted file: {path}[/green]")
    except FileToolError as e:
        console.print(f"[red]Error: {str(e)}[/red]")
        raise click.Abort()


if __name__ == "__main__":
    cli()

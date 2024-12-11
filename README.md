# file-tool
A command-line tool for common file operations.

## Features
- Create files (empty or with content)
- Copy files
- Combine two files into one
- Delete files
- Error handling and logging
- Complete test coverage

## Project Structure
```
file-tool/
├── debian/
│   ├── control           # Package metadata
│   ├── copyright        # License information
│   └── changelog        # Version history
├── src/
│   ├── operations/
│   │   └── file_operations.py    # Core file operation implementations
│   ├── utils/
│   │   ├── exceptions.py         # Custom exceptions
│   │   └── helpers.py           # Utility functions
│   └── main.py                  # CLI application entry point
├── tests/
│   ├── conftest.py              # Test configurations and fixtures
│   ├── test_file_operations.py  # File operations tests
│   ├── test_helpers.py         # Utility function tests
│   └── test_main.py            # CLI interface tests
├── .dockerignore
├── .gitignore
├── Dockerfile
├── LICENSE
├── README.md
├── poetry.lock
├── pyproject.toml
├── requirements.txt
└── requirements-dev.txt
```

## Installation

### Using Pip (Recommended)
1. Install using Pip:
   ```bash
   pip install file-tool
   ```

2. Clone and install:
   ```bash
   git clone https://github.com/yourusername/file-tool.git
   cd file-tool
   poetry install
   ```

### Using Docker
```bash
docker build -t file-tool .
```

## Usage

### After Installation
Once installed with Poetry, you can run commands directly:
```bash
file-tool [command] [options]
```

If using Docker:
```bash
docker run file-tool [command] [options]
```

### Available Commands

#### Create a file
Create an empty file:
```bash
file-tool create myfile.txt
```

Create a file with content:
```bash
file-tool create myfile.txt --content "Hello, World!"
```

#### Copy a file
```bash
file-tool copy source.txt destination.txt
```

#### Combine files
Combines two files into a new file:
```bash
file-tool combine first.txt second.txt output.txt
```

#### Delete a file
```bash
file-tool delete myfile.txt
```

### Command Options
```bash
file-tool --help         # Show general help
file-tool create --help  # Show help for create command
file-tool copy --help    # Show help for copy command
file-tool combine --help # Show help for combine command
file-tool delete --help  # Show help for delete command
```

## Development

### Using Dev Containers (Recommended)
This project includes configuration for development using VS Code Dev Containers, which provides a consistent, isolated development environment.

#### Prerequisites
- [Docker](https://www.docker.com/products/docker-desktop/)
- [VS Code](https://code.visualstudio.com/)
- [Dev Containers extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers)

#### Setup
1. Open the project in VS Code
2. When prompted, click "Reopen in Container" or:
   - Press F1, select "Dev Containers: Reopen in Container"

The container will:
- Set up a complete Python development environment
- Install all dependencies
- Configure VS Code with recommended extensions and settings
- Make the `file-tool` command available

#### Features
- Pre-configured Python development environment
- Integrated testing and debugging
- Code formatting and linting tools
- Test coverage visualization
- Consistent environment across different machines

### Alternative: Local Development
If you prefer not to use Dev Containers, you can develop locally:

```bash
git clone https://github.com/yourusername/file-tool.git
cd file-tool
poetry install
```

### Testing
Run all tests:
```bash
poetry run pytest
```

Run tests with coverage:
```bash
poetry run pytest --cov=src
```

### Code Quality
Format code:
```bash
poetry run black src tests
```

Sort imports:
```bash
poetry run isort src tests
```

Type checking:
```bash
poetry run mypy src
```

## License
This project is licensed under the GNU Public License - see the LICENSE file for details.
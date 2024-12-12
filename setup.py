import toml
from setuptools import setup, find_packages

# Parse the version from pyproject.toml
with open("pyproject.toml", "r") as f:
    pyproject_data = toml.load(f)
    version = pyproject_data["tool"]["poetry"]["version"]

setup(
    name="file-tool",
    version=version,  # Use the version from pyproject.toml
    description="A CLI tool for common file operations",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Haytham Amin",
    author_email="haythamelmogazy@gmail.com",
    url="https://github.com/your-repo/file-tool",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.10,<3.13",
)

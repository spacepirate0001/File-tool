FROM python:3.12-slim

WORKDIR /workspace

# Install poetry
RUN pip install poetry

# Copy source code
COPY . .

# Install dependencies and project
RUN poetry config virtualenvs.create false && \
    poetry install && \
    pip install -e .

ENTRYPOINT ["file-tool"]
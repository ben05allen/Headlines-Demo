# Builder stage: Install dependencies and project
FROM python:3.14-slim AS builder

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

WORKDIR /app
RUN mkdir -p packages/core

COPY pyproject.toml uv.lock ./
COPY packages/core/pyproject.toml ./packages/core/

RUN uv sync --no-install-project --no-editable --no-dev

COPY . .
RUN --mount=type=cache,target=/root/.cache/uv \
  uv sync --locked --no-editable --all-packages --no-dev

FROM python:3.14-slim

WORKDIR /app

RUN groupadd -r appuser \
  && useradd -r -g appuser appuser \
  && chown -R appuser:appuser /app

USER appuser

COPY --from=builder --chown=appuser:appuser /app/.venv /app/.venv

CMD ["/app/.venv/bin/logger"]

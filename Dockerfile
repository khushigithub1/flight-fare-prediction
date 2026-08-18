# ─────────────────────────────────────────────
# Stage 1 – install dependencies
# ─────────────────────────────────────────────
FROM python:3.11-slim AS builder

WORKDIR /install

COPY requirements.txt .

RUN pip install --upgrade pip --quiet \
 && pip install --no-cache-dir --prefix=/install/deps -r requirements.txt \
 && pip install --no-cache-dir --no-deps --prefix=/install/deps xgboost==3.2.0


# ─────────────────────────────────────────────
# Stage 2 – lean runtime image
# ─────────────────────────────────────────────
FROM python:3.11-slim

# Non-root user for security
RUN useradd --create-home appuser
WORKDIR /home/appuser/app

# Copy installed packages from builder
COPY --from=builder /install/deps /usr/local

# Copy application source
COPY app.py         .
COPY templates/     templates/
COPY static/        static/
COPY models/        models/

# Set ownership
RUN chown -R appuser:appuser /home/appuser/app
USER appuser

ENV FLASK_ENV=production
EXPOSE 5000

CMD ["gunicorn", "--bind", "0.0.0.0:5000", "--workers", "2", "--timeout", "120", "app:app"]

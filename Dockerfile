# Build
FROM python:3.11-alpine AS build

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

#Development
FROM build AS development

COPY . .

ENV FLASK_ENV=development
ENV PYTHONDONTWRITEBYTECODE=1

CMD ["sh", "-c", "flask db upgrade && python3 main.py"]

# Production
FROM build AS production

COPY . .
ENV PYTHONDONTWRITEBYTECODE=1

RUN pip install gunicorn

EXPOSE 8000

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "app:app"]

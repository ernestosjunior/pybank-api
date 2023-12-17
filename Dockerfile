# Build
FROM python:3.11-alpine AS build

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

#Development
FROM build AS development

COPY . .

ENV FLASK_ENV=development

CMD ["sh", "-c", "flask db upgrade && python3 seed.py && python3 main.py"]

# Production
FROM build AS production

COPY . .

RUN pip install gunicorn

EXPOSE 8000

CMD ["sh", "-c", "flask db upgrade && python3 seed.py && gunicorn --bind 0.0.0.0:8000 app:app"]

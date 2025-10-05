FROM python:3.11

WORKDIR /app

# OS dependency-lər (Pillow, psycopg2 və s. üçün)
RUN apt-get update && apt-get install -y \
    gcc \
    build-essential \
    libpq-dev \
    libjpeg-dev \
    zlib1g-dev \
    libfreetype6-dev \
    liblcms2-dev \
    libwebp-dev \
    tcl8.6-dev \
    tk8.6-dev \
    libharfbuzz-dev \
    libfribidi-dev \
    libxcb1-dev \
    git \
    curl \
    && rm -rf /var/lib/apt/lists/*

# requirements quraşdır
COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Layihəni konteynerə kopyala
COPY . .

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

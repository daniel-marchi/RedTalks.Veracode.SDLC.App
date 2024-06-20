FROM python:3.12.3

WORKDIR /app

COPY requirements.txt .

RUN pip3 install --no-cache-dir -r requirements.txt && apt update && apt-get install -y iputils-ping && apt-get install -y fortune-mod 


COPY . .

EXPOSE 8080

CMD ["python3", "manage.py", "runserver", "0.0.0.0:8080"]
FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN chmod +x wait-for-db.sh

EXPOSE 5000

ENTRYPOINT ["./wait-for-db.sh"]

CMD ["gunicorn","--bind","0.0.0.0:5000","app:app"]

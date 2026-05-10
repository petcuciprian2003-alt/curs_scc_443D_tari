FROM python:3.9-slim

WORKDIR /app

COPY . .

RUN pip install --break-system-packages flask pytest

EXPOSE 5000

CMD ["python", "-c", "from tari import app; app.run(host='0.0.0.0', port=5000)"]

FROM docker.arvancloud.ir/python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /usr/src/app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

ENV NAME World

ENTRYPOINT [ "uvicorn" ]
CMD ["fastapi_user_management.app:app",  "--host", "0.0.0.0", "--port", "8000", "--reload"]

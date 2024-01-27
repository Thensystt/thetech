FROM python:3.9 as backend

WORKDIR /server

COPY /requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY /datasets .

COPY . .
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
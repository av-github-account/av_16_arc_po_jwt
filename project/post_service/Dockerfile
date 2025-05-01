FROM python:3.11

WORKDIR /app

RUN pip install uv

COPY requirements.uv.txt .
RUN uv pip install --system -r requirements.uv.txt

COPY ./app ./app

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]

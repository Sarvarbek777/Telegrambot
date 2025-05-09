from python:3.13-alpine

WORKDIR /app
COPY . .
#RUN pip install -r req.txt
RUN pip install --no-cache-dir -r req.txt
RUN pip install uvicorn

# ASGI serverini ishga tushirish (FastAPI misolida)
CMD ["uvicorn", "your_app:app", "--host", "0.0.0.0", "--port", "8000"]





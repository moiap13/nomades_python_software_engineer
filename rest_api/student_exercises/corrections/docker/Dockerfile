FROM python:3.10.16-bookworm

WORKDIR /app

COPY ./books_library/ /app/

EXPOSE 8081

RUN pip install -r requirements.txt

CMD ["python", "app.py"]
FROM python:3.10

WORKDIR /webapp

COPY . .

RUN pip install --no-cache-dir --upgrade -r /webapp/requirements.txt

CMD ["uvicorn", "src.app:app"]

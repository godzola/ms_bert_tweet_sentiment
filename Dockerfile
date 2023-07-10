FROM python:3.8

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt
COPY ./main.py /code/
# COPY ./model/  /code/model/
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

CMD ["uvicorn", "main:app", "--proxy-headers", "--host", "0.0.0.0", "--port", "8080"]

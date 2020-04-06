FROM python:3.6
COPY ./app /app
WORKDIR /app
VOLUME /data
RUN pip install -r requirements.txt
RUN python -m compileall main.py
ENTRYPOINT ["python", "main.py"]

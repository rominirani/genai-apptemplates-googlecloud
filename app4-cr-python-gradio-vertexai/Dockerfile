FROM python:3.11

RUN pip install gradio 
RUN pip install google-cloud-aiplatform==1.27.1 google-cloud-logging

COPY ./app /app

WORKDIR /app

EXPOSE 8080

CMD ["python", "app.py"]

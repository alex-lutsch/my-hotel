FROM python:3

ADD app.py /
COPY requirements.txt .
RUN pip install -r requirements.txt
RUN pip install flask

COPY . .
EXPOSE 5001
CMD ["python", "app.py"]
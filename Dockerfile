FROM python:3-alpine
RUN mkdir /src/
COPY . /src
WORKDIR /src
EXPOSE 5000
EXPOSE 27017
RUN pip install -r requirements.txt
CMD ["python", "./main.py"]

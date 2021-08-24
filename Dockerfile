FROM python:3.8-slim-buster
WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
COPY . .
ARG PORT
ENV WebPort=$PORT
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0", "--port=$WebPort"]

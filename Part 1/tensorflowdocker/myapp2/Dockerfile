FROM python:3.7-alpine
WORKDIR /code
COPY . /code

RUN apk add --no-cache gcc musl-dev linux-headers
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# Step 6:  run the command to start uWSGI
CMD ["python3", "app.py"]
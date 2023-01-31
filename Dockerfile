FROM python:3.8
COPY . ./myapp
WORKDIR myapp
RUN pip3 install -r requirements.txt
CMD [ "python", "main.py"]
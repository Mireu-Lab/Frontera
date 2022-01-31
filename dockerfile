FROM python:3

RUN mkdir app
WORKDIR app
COPY . .

RUN pip3 install -r Install/requirements.txt

RUN python3 Install/install.py

CMD [ "python3", "App/main.py" ]
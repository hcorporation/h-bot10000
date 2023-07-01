FROM python:3.11
WORKDIR /hbot
COPY . /hbot/
RUN pip install -r requirements.txt
CMD sh swap.sh
FROM python:3.11
WORKDIR /hbot
COPY . /hbot/
RUN pip install -r requirements.txt
CMD sh swapenable.sh && echo "enabled swap" && python3 index.py
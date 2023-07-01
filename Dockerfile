FROM python:3.11
WORKDIR /hbot
COPY . /hbot/
RUN pip install -r requirements.txt
CMD fallocate -l 512M /swapfile && chmod 0600 /swapfile && mkswap /swapfile && echo 10 > /proc/sys/vm/swappiness && swapon /swapfile && echo 1 > /proc/sys/vm/overcommit_memory && python3 index.py
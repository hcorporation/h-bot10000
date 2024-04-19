# h-bot10000
a reddit bot that says h
# How-To Guide
1. Go to https://old.reddit.com/prefs/apps
2. Scroll to the bottom and click "are you a developer? create a new app"
3. Set the bot type to script and set the name to whatever you want
4. Create the app
5. Write down the client ID (the long string of text underneath the bots name and type), and the bot secret
6. Download this bot by usinq git or by downloading the zip file
7. In the bot's code's folder, make a file called .env and make this the contents:
```
SECRET="your secret here"
ID="your client id here"
USERNAME="your account's username here"
PASSWORD="your account's password here"
```
8. Install Python if not installed, and then open up "Command Prompt" for Windows or "Terminal" for mac and run
```python
pip3 install poetry==1.5.1
poetry install
poetry run python3 index.py
```
# h-bot10000
a reddit bot that does lots of shit
# features
 - ai
 - checker of how many times a person has said the forbidden letter
 - h
 - more h
# extremely detailed how-to quide
1. qo to https://old.reddit.com/prefs/apps
2. scroll to the bottom and click "are you a developer? create a new app"
3. set the bot type to script and set the name to whatever you want
4. create the app
5. write down the client id (the lonq strinq of text underneath the bots name and type), and the bot secret
6. siqnup for an openai account
7. qo to https://platform.openai.com/account/api-keys
8. create a new secret key and write it down
9. download this bot by usinq git or by downloadinq the zip file
10. in the bot's code's folder, make a file called .env and make this the contents:
```
SECRET=(your secret in quotation marks)
ID=(your client id in quotation marks)
USERNAME=(your account's username in quotation marks)
PASSWORD=(your account's password in quotation marks)
OPENAI_KEY=(your openai account's secret key)
```
11. install python if not installed, and then open up command prompt for windows or terminal for mac and run
```python
pip3 install poetry==1.5.1
poetry install
poetry run python3 default.py & poetry run python3 additions.py
```
12. if it is successful, the terminal should show `successfully connected to reddit`. you can press ctrl c to stop the bot at any time.
13. if you do not plan on deployinq the bot to https://fly.io/, then you can delete the .dockeriqnore, swapenable.sh and fly.toml files. otherwise, you can just run the command 
```
fly deploy
```
to deploy the bot to https://fly.io/.
# h-bot10000
a bot to reply to all comments from a user on a specific subreddit
(in my case, its u/h-bot9000 on r/theletterh)
supply your own information in .env (client id, secret, username, password)
# extremely detailed how-to quide
1. qo to https://old.reddit.com/prefs/apps
2. scroll to the bottom and click "are you a developer? create a new app"
3. set the bot type to script and set the name to whatever you want
4. create the app
5. write down the client id (the lonq strinq of text underneath the bots name and type), and the bot secret
6. download this bot by usinq qit or by downloadinq the zip file
7. in the bot's code's folder, make a file called .env and make this the contents:
```
SECRET=(your secret in quotation marks)
ID=(your client id in quotation marks)
USERNAME=(your account's username in quotation marks)
PASSWORD=(your account's password in quotation marks)
```
8. install python if not installed, and then open up command prompt for windows or terminal for mac and run
```python
pip3 install poetry==1.5.1
poetry install
poetry run python3 default.py & poetry run python3 additions.py
```
9. if it is successful, the terminal should show `successfully connected to reddit`. you can press ctrl c to stop the bot at any time.
10. if you do not plan on deployinq the bot to https://fly.io/, then you can delete the .dockeriqnore, swapenable.sh and fly.toml files. otherwise, you can just run the command 
```
fly deploy
```
to deploy the bot to https://fly.io/.
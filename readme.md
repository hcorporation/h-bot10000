# h-bot10000
a reddit bot that does lots of shit
# features
 - h
 - more h
# extremely detailed how-to guide
1. go to https://old.reddit.com/prefs/apps
2. scroll to the bottom and click "are you a developer? create a new app"
3. set the bot type to script and set the name to whatever you want
4. create the app
5. write down the client id (the long string of text underneath the bots name and type), and the bot secret
6. download this bot by using git or by downloading the zip file
10. in the bot's code's folder, make a file called .env and make this the contents:
```
SECRET=(your secret in quotation marks)
ID=(your client id in quotation marks)
USERNAME=(your account's username in quotation marks)
PASSWORD=(your account's password in quotation marks)
```
11. install python if not installed, and then open up command prompt for windows or terminal for mac and run
```python
pip3 install poetry==1.5.1
poetry install
poetry run python3 default.py & poetry run python3 additions.py
```
12. if it is successful, the terminal should show `successfully connected to reddit`. you can press ctrl c to stop the bot at any time.
13. if you do not plan on deploying the bot to https://fly.io/, then you can delete the .dockerignore, swapenable.sh and fly.toml files. otherwise, you can just run the command 
```
fly deploy
```
to deploy the bot to https://fly.io/.
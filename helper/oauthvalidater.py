from helper.reddit import reddit
def validater():
    if reddit.read_only != True:
        print("successfully connected to reddit.")
    else:
        print("could not connect to reddit. have you provided the correct credentials?")

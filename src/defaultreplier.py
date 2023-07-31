import random
from helper.usefulcomponents import Components

def defaultreplier(reddit):
  components = Components(reddit)
  comments = components.new_comments()
  for comment in comments:
    print("new comment")   
    prob = random.randint(0,100000)
    prob2 = random.randint(0,10000000000)
    prob3 = random.randint(0,8000)
    prob4 = random.randint(0,25)
    capitalh = random.randint(0,1)
    if prob == 1 & prob2 != 1:
      comment.reply("hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh")
    elif prob == 1 & prob2 == 1:
      comment.reply("e (tHere is a one in like a bajillion cHance that i reply witH e. if you see tHis, consider it qood luck)")
    elif capitalh == 1:
      comment.reply("H")
    elif prob3 == 1:
      comment.reply("pc")
    elif prob4 == 1:
      comment.reply("h is cool")
    else:
      comment.reply("h")
    print("replied")        

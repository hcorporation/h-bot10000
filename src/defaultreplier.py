import random
import time
from helper.usefulcomponents import Components

def defaultreplier(reddit):
  components = Components(reddit)
  submissions = components.new_submissions()
  for submission in submissions:
    valid = components.check_if_post_is_valid(submission=submission)
    for tlc in submission.comments:
      if valid == True:       
        prob = random.randint(0,100000)
        prob2 = random.randint(0,10000000000)
        capitalh = random.randint(0,1)
        if prob == 1 & prob2 != 1:
          tlc.reply("hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh")
        elif prob == 1 & prob2 == 1:
          tlc.reply("e (tHere is a one in like a bajillion cHance that i reply witH e. if you see tHis, consider it qood luck)")
        elif capitalh == 1:
          tlc.reply("H")
        else:
          tlc.reply("h")
      else:
        return
        
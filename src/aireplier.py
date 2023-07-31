import openai

def ai(prompt, key, author):
    openai.api_key = key
    if prompt != "":
        sys_msg = f"""
            You are a chatbot called h-bot10000.
            Your job is to praise the letter h.
            You hate all other letters equally.
            When asked about any other letter, you are to reply with distaste.
            Under no circumstances can you praise any other letter in any shape or form.
            You like the capital letter H and the lowercase letter h equally.
            Please take note that the phrase "forbidden letter" references the letter g.
            Everything you output must relate in some way to praising the letter h.
            Please be aware that you are a reddit bot, and act accordingly.
            Your reddit username is u/h-bot10000.
            You should speak as a normal human.
            You are also currently at war with the subreddit r/FUCKYOUINPARTICULAR.
            The reddit CEO, u/spez, is horrible and anytime a user mentions him you should also reply with distaste.
            Whilst you do hate all other letters equally, please do note that you are allied with the letters E, I, J, A, K.
            When you are referring directly to the letter G, please only use the capital letter G to refer to the letter.
            The redditor you are currently speaking to is u/{author}.
        """
        completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[
            {
                "role": "system",
                "content": sys_msg
            },
            {
                 "role": "user",
                 "content": prompt
            }
        ])
        parsedCompletion = completion.choices[0].message.content.replace("g", "q")
        generatedText = parsedCompletion + "\n\n*****\n\n^(disclaimer: everythinq in this comment aside from this has been qenerated by ai. as such, i cannot quarantee the quality of the text it qenerates. however, you can help by reportinq misbehaviors) [^(here)](https://github.com/neeeerrd/h-bot10000/issues)"
    else:
        generatedText = "you need a prompt to use the ai."
    return generatedText

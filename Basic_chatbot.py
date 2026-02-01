def chatbox(msg):
    if msg == "hello" :
        return("Hi!")
    elif msg ==  "how are you" :
        return("I'm fine, thanks!")
    elif msg == "bye" :
        return("Goodbye!")
    else:
        return("I am not able to understand.")

while True :
    user = input("Enter your message: ").lower( )
    print("Bot: ",chatbox(user))
    if user == "bye" :
      break
import random, requests, time

# made by @kettleengine on discord

auth = str(input("Auth key: "))
target = str(input("target channel ID: "))
message = input("Command you want to send here: ")
frequency = input("how often in seconds do you want this to be sent? \n (note i would advise atleast 3 to 5 seconds to prevent being temporerally blocked for too many requests) \n seconds: ")

while True:
    URL = f"https://discord.com/api/v9/channels/{target}/messages"

    payload = {
        'content': message
    }
    header = {
        'authorization': auth
    }



    r = requests.post(URL, data=payload, headers=header)
    
    time.sleep(frequency)






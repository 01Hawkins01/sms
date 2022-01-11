#importing Twilio API
from twilio.rest import Client
account_sid = "AC37e7a124d078b2de787b715bc3e3ef73"
auth_token  = "7b9b321a517c8ab418e1e11b0e132f48"
client = Client(account_sid, auth_token)

#Reading Massege From Text File  
message = open("message.txt","r").read()
contact = open("contact.txt", "r").read().split(',')

#Looping All Number and send Messages
for x in contact:
    message = client.messages.create(
        to=x, 
        from_="+13345959253", #use your own Number From Twilio
        body=message)

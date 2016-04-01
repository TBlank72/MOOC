#Send text message with twilio

from twilio.rest import TwilioRestClient
 
# Your Account Sid and Auth Token from twilio.com/user/account
account_sid = "AC4f19fefddda4575283bd6639acf369da"
auth_token  = "005b6dc656732f008ee85c4baf91966e"

client = TwilioRestClient(account_sid, auth_token)
 
message = client.messages.create(body="Hi, I'm Ron Burgandy",
    to="+19039321689",    # Replace with your phone number
    from_="+19037023796") # Replace with your Twilio number
print message.sid


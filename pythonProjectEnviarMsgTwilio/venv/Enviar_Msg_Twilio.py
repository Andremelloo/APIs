from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "AccountSiteTwilio"
# Your Auth Token from twilio.com/console
auth_token  = "TokenSiteTwilio"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="myNumber",
    from_="+12677109979",
    body="Hello from Python!")

print(message.sid)





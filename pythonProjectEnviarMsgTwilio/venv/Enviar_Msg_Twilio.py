from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "AC7acfe291e1cd1abfa88419761a9ca62f"
# Your Auth Token from twilio.com/console
auth_token  = "dcb18c1590cc2a623d6c304b319e367a"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+5541999590798",
    from_="+12677109979",
    body="Hello from Python!")

print(message.sid)





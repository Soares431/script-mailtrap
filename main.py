import mailtrap as mt

API_TOKEN = ""  # your API key here https://mailtrap.io/settings/api-tokens

mail = mt.Mail(
    sender=mt.Address(email="lucas@demomailtrap.co", name="Mailtrap Test"),
    to=[mt.Address(email="lucas.00000854565@unicap.br ")],
    subject="You are awesome!",
    text="Congrats for sending test email with Mailtrap!",
    category="Integration Test",
)

client = mt.MailtrapClient(token=API_TOKEN)
response = client.send(mail)

print(response)
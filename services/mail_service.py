import os
import mailtrap as mt
from dotenv import load_dotenv

load_dotenv()

# welcome_image = Path(__file__).parent.joinpath("welcome.png").read_bytes()
async def send_mail(otp,name,email):
    mail = mt.Mail(
        sender=mt.Address(email="hello@demomailtrap.com", name="Mailtrap Test"),
        to=[mt.Address(email=email, name=name)],
    subject="You are awesome!",
    text=f"Congrats for sending test email with Mailtrap! Your OTP is {otp} and it will expire in 10 minutes. Do not share this OTP with anyone.",
    html="""
    <!doctype html>
    <html>
      <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
      </head>
      <body style="font-family: sans-serif;">
        <div style="display: block; margin: auto; max-width: 600px;" class="main">
          <h1 style="font-size: 18px; font-weight: bold; margin-top: 20px">
            Congrats for sending test email with Mailtrap!
          </h1>
          <p>Inspect it using the tabs you see above and learn how this email can be improved.</p>
          <img alt="Inspect with Tabs" src="cid:welcome.png" style="width: 100%;">
          <p>Now send your email using our fake SMTP server and integration of your choice!</p>
          <p>Good luck! Hope it works.</p>
        </div>
        <!-- Example of invalid for email html/css, will be detected by Mailtrap: -->
        <style>
          .main { background-color: white; }
          a:hover { border-left-width: 1em; min-height: 2em; }
        </style>
      </body>
    </html>
    """,
    category="Test",
    headers={"X-MT-Header": "Custom header"},
    custom_variables={"year": 2023},
    )
    client = mt.MailtrapClient(token=os.getenv("MAILTRAP_API_KEY"))
    try:
        client.send(mail)
    except Exception as e:
        print(e)

if __name__ == "__main__":
    send_mail("123456", "Sudip Mandal", "krishg@zluck.in")


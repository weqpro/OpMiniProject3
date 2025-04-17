import re
import random
import datetime
import asyncio
from aiosmtplib import SMTP
from email.message import EmailMessage

user_data = {}


def email_validator(email_ad):
    pattern = r"^(?!\.)(?!.*\.\.)[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+(?:\.[a-zA-Z0-9-]+)*@[a-zA-Z0-9-]+\.[a-zA-Z]{2,}(\.[a-zA-Z]{2,})*$"
    return re.match(pattern, email_ad) is not None


def create_otp():
    return "".join(str(random.randint(0, 9)) for _ in range(6))


def can_generate_new_code(email):
    if email not in user_data:
        return True
    last_sent = user_data[email]["last_sent"]
    return (datetime.datetime.now() - last_sent).total_seconds() >= 60


def is_code_valid(email, code):
    if email not in user_data:
        return False
    stored_code = user_data[email]["code"]
    created_at = user_data[email]["created_at"]
    if code != stored_code:
        return False
    return (datetime.datetime.now() - created_at).total_seconds() <= 600


async def send_code(email_address, otp):
    msg = EmailMessage()
    msg["Subject"] = "OTP Verification"
    msg["From"] = "Fortis <noreply@fortis.com>"
    msg["To"] = email_address
    msg.set_content(f"Your verification code is: {otp}")

    try:
        server = SMTP(hostname="smtp.gmail.com", port=587, start_tls=True)
        await server.connect()
        # await server.starttls()
        await server.login("pereima.pn@ucu.edu.ua", "kuko ggfb ivhw ezts")
        await server.send_message(msg)
        print(f"OTP has been sent to {email_address}")
    except Exception as e:
        print(f"Error sending email: {e}")
    finally:
        await server.quit()


async def validate_email_and_send_code(email_address):
    if not email_validator(email_address):
        print("Invalid email address")
        return

    if not can_generate_new_code(email_address):
        print("Please wait before generating a new code")
        return

    otp = create_otp()
    user_data[email_address] = {
        "code": otp,
        "last_sent": datetime.datetime.now(),
        "created_at": datetime.datetime.now(),
    }

    await send_code(email_address, otp)


# async def main():
#     email = input("Enter your email: ")
#     await validate_email_and_send_code(email)

# asyncio.run(main())

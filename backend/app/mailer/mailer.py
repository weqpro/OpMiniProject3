
from fastapi_mail import FastMail, MessageSchema, ConnectionConfig

conf = ConnectionConfig(
    MAIL_USERNAME="fortis.project.ua@gmail.com",
    MAIL_PASSWORD="wfpx biaq fwdo ovlx",
    MAIL_FROM="fortis.project.ua@gmail.com",
    MAIL_SERVER="smtp.gmail.com",
    MAIL_PORT=587,
    MAIL_STARTTLS=True,    # start TLS upgrade
    MAIL_SSL_TLS=False,    # direct SSL/TLS wrapper off
    TEMPLATE_FOLDER="app/templates/email"
)

fm = FastMail(conf)

async def send_registration_email(email: str, full_name: str):
    message = MessageSchema(
        subject="Welcome to Fortis!",
        recipients=[email],
        template_body={
            "name": full_name,
            "support_email": "fortis.project.ua@gmail.com"
        },
        subtype="html"
    )
    await fm.send_message(message, template_name="welcome.html")
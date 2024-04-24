from fastapi import FastAPI, BackgroundTasks, HTTPException
from fastapi_mail import FastMail, MessageSchema, ConnectionConfig
import random
import string

app = FastAPI()

# Configuration for SMTP server
conf = ConnectionConfig(
    MAIL_USERNAME="kotamaneesha67@gmail.com",
    MAIL_PASSWORD="qdor lirg pghi znyg",
    MAIL_FROM="kotamaneesha67@gmail.com",
    MAIL_PORT=587,  # Example SMTP port
    MAIL_SERVER="smtp.gmail.com",  # Example SMTP server
    MAIL_STARTTLS=True,
    MAIL_SSL_TLS=False,
    USE_CREDENTIALS=True,
    VALIDATE_CERTS=True
)
otp_storage = {}

@app.post("/send-otp/")
async def send_otp(email: str, background_tasks: BackgroundTasks):
    """
    Send OTP to the provided email address.

    Parameters:
        - email (str): The email address to which the OTP will be sent.
        - background_tasks (BackgroundTasks): BackgroundTasks object to run tasks asynchronously.

    Returns:
        dict: A message indicating the OTP has been sent successfully.
    """
    # Generate random OTP
    otp = ''.join(random.choices(string.digits, k=6))
    subject = "OTP Verification"
    message = f"Your OTP is: <b> {otp} </b>"

    # Store OTP for verification later
    otp_storage[email] = otp

    # Define message schema
    message_schema = MessageSchema(
        subject=subject,
        recipients=[email],
        body=message,
        subtype="html"
    )

    # Send email in background task
    background_tasks.add_task(send_email, message_schema)

    return {"message": "OTP sent successfully"}

async def send_email(message: MessageSchema):
    """
    Send email with the provided message schema.

    Parameters:
        - message (MessageSchema): The message schema containing email details.
    """
    fm = FastMail(conf)
    await fm.send_message(message=message)

@app.post("/verify-otp/")
async def verify_otp(email: str, otp: str):
    """
    Verify the OTP for the provided email address.

    Parameters:
        - email (str): The email address for which OTP is to be verified.
        - otp (str): The OTP to be verified.

    Returns:
        dict: A message indicating whether OTP verification was successful.
    """
    # Check if email exists in storage
    if email not in otp_storage:
        raise HTTPException(status_code=404, detail="Email not found")

    # Retrieve the stored OTP
    stored_otp = otp_storage[email]

    # Check if the received OTP matches the stored OTP
    if otp == stored_otp:
        # Clear the OTP from storage once verified
        del otp_storage[email]
        # Send confirmation email
        await send_confirmation_email(email)
        return {"message": "OTP verified successfully"}
    else:
        raise HTTPException(status_code=400, detail="Invalid OTP")

async def send_confirmation_email(email: str):
    """
    Send confirmation email for successful OTP verification.

    Parameters:
        - email (str): The email address to which the confirmation email is sent.
    """
    subject = "OTP Verification Successful"
    message = "Your OTP has been verified successfully."

    message_schema = MessageSchema(
        subject=subject,
        recipients=[email],
        body=message,
        subtype="html"
    )

    fm = FastMail(conf)
    await fm.send_message(message=message_schema)

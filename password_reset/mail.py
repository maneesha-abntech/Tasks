from fastapi import FastAPI, HTTPException
from fastapi_mail import FastMail, MessageSchema, ConnectionConfig
from pydantic import BaseModel, EmailStr, ValidationError  # Import EmailStr and ValidationError
import sqlite3
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

# SQLite database connection
conn = sqlite3.connect('users.db')
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS users
                  (id INTEGER PRIMARY KEY AUTOINCREMENT, email TEXT UNIQUE, otp TEXT)''')
conn.commit()

# Pydantic model for user data
class User(BaseModel):
    email: EmailStr  # Use EmailStr for email validation

# Pydantic model for OTP storage
class OTPStorage(BaseModel):
    email: str
    otp: str

@app.post("/forgot-password/")
async def send_otp_for_password_reset(user: User):
    """
    Send OTP for password reset to the provided email.

    Parameters:
        -->user (User): User data containing the email address.
    """
    try:
        # Generate and send OTP
        otp = ''.join(random.choices(string.digits, k=6))
        cursor.execute("INSERT OR REPLACE INTO users (email, otp) VALUES (?, ?)", (user.email, otp))
        conn.commit()

        message = f"<h3>Your OTP for password reset is</h3>: <b>{otp}</b>"
        message_schema = MessageSchema(
            subject="Password Reset OTP",
            recipients=[user.email],
            body=message,
            subtype="html"
        )

        fm = FastMail(conf)
        await fm.send_message(message=message_schema)
        return {"message": "OTP sent successfully"}
    except ValidationError as e:
        raise HTTPException(status_code=422, detail=str(e))

@app.post("/reset-password/")
async def reset_password(email: str, otp: str, new_password: str, confirm_password: str):
    """
    Reset the password for the provided email.

    Parameters:
        -->email (str): The email address for which to reset the password.
        -->otp (str): The OTP received for password reset.
        -->new_password (str): The new password.
        -->confirm_password (str): The confirmation of the new password.
    """
    try:
        cursor.execute("SELECT otp FROM users WHERE email = ?", (email,))
        stored_otp = cursor.fetchone()
        if stored_otp and stored_otp[0] == otp:
            # Check if new password matches confirm password
            if new_password == confirm_password:
                # For demonstration purposes, let's just print the updated password
                print("Password for " + email + " updated to: " + new_password)

                # Clear OTP after successful reset
                cursor.execute("DELETE FROM users WHERE email = ?", (email,))
                conn.commit()

                # Send confirmation email
                await send_confirmation_email(email)

                return {"message": "Password reset successful"}
            else:
                raise HTTPException(status_code=400, detail="New password does not match confirm password")
        else:
            raise HTTPException(status_code=400, detail="Invalid OTP")
    except ValidationError as e:
        raise HTTPException(status_code=422, detail=str(e))

async def send_confirmation_email(email: str):
    """
    Send a confirmation email for password reset.

    Parameters:
        -->email (str): The email address to which the confirmation email is sent.
    """
    try:
        subject = "<h2>Password Reset Successful</h2>"
        message = "Your password has been reset successfully."

        message_schema = MessageSchema(
            subject=subject,
            recipients=[email],
            body=message,
            subtype="html"
        )

        fm = FastMail(conf)
        await fm.send_message(message=message_schema)
    except ValidationError as e:
        raise HTTPException(status_code=422, detail=str(e))

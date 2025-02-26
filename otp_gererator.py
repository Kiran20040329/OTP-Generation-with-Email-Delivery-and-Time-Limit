import time
import random
import smtplib

# SMTP Configuration
SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587
SENDER_EMAIL = "your_email@gmail.com"          # Replace with your email
APP_PASSWORD = "your_app_password"             # Replace with your Gmail App Password
RECEIVER_EMAIL = "receiver_email@gmail.com"    # Replace with receiver's email

def send_otp_via_email(otp):
    """Send OTP to the receiver's email using SMTP."""
    try:
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        server.login(SENDER_EMAIL, APP_PASSWORD)
        subject = "Your OTP Code"
        body = f"Your OTP is: {otp}"
        message = f"Subject: {subject}\n\n{body}"
        server.sendmail(SENDER_EMAIL, RECEIVER_EMAIL, message)
        server.quit()
        print("✅ OTP sent successfully!")
    except Exception as e:
        print(f"❌ Error sending OTP: {e}")

def generate_otp():
    """Generate a 6-digit OTP."""
    return random.randint(100000, 999999)

def main():
    otp = generate_otp()
    send_otp_via_email(otp)

    start_time = time.time()
    user_otp = input("\n🔑 Enter the OTP you received: ")
    end_time = time.time()

    elapsed_time = end_time - start_time

    if elapsed_time <= 60 and user_otp == str(otp):
        print("\n✅ OTP matched!\n🎉 Process successful.")
    elif elapsed_time > 60:
        print("\n⏰ Time limit exceeded. Please request a new OTP.")
    else:
        print("\n❌ Invalid OTP. Please try again.")

if __name__ == "__main__":
    main()

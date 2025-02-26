# OTP-Generation-with-Email-Delivery-and-Time-Limit
This project generates a One-Time Password (OTP), sends it via email using SMTP, and verifies the user input within a specified time limit.

🚀 Features
Generates a random 6-digit OTP.
Sends OTP to the recipient’s email via Gmail SMTP.
Verifies OTP within a 60-second window.
Displays success or failure messages based on verification.

🛠️ Technologies Used
Python 3.7+
SMTP Library – Email sending
Random Module – OTP generation
Datetime & Time Modules – Time calculations

📦 Installation
1. Clone the repository:
git clone 
cd otp-email-verification
2. Install dependencies:
pip install -r requirements.txt

📝 Usage
1. Enable App Passwords in Gmail:
Enable 2-Step Verification.
Generate an App password from your Google account.
2. Run the script:
python otp_generator.py
3. Input your OTP:
Check your email for the OTP.
Enter it within 60 seconds for successful verification.

💻 Code Overview
OTP Generation: Random 6-digit number.
Email Sending: SMTP used with Gmail’s server.
Time Verification: Checks if OTP is entered within the time limit.

⚠️ Security Note
Use an App Password instead of your Gmail password for enhanced security.
Avoid hardcoding sensitive information in the script.

🤝 Contributing
Contributions are welcome! Feel free to submit pull requests or raise issues.

📄 License
This project is licensed under the MIT License.



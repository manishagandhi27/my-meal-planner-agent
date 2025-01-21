from twilio.rest import Client
import os

# ✅ Load Twilio Credentials from Environment Variables
TWILIO_SID = os.getenv("TWILIO_ACCOUNT_SID")
TWILIO_AUTH = os.getenv("TWILIO_AUTH_TOKEN")
TWILIO_PHONE = os.getenv("TWILIO_PHONE_NUMBER")
USER_PHONE = os.getenv("USER_PHONE_NUMBER")

client = Client(TWILIO_SID, TWILIO_AUTH)

def send_whatsapp_message(message_body):
    """Sends a WhatsApp message with the formatted meal plan."""
    print(f"TWILIO_PHONE {TWILIO_PHONE}")
    print(f"USER_PHONE {USER_PHONE}")
    # try:
    #     message = client.messages.create(
    #         body=message_body,
    #         from_=f"whatsapp:{TWILIO_PHONE}",
    #         to=f"whatsapp:{USER_PHONE}"
    #     )
    #     print(f"📩 WhatsApp Notification Sent: {message.sid}")
    #     return message.sid
    # except Exception as e:
    #     print(f"❌ Error sending WhatsApp notification: {e}")
    #     return None

from  main.graph.graph_state import MealPlannerState
from email.mime.text import MIMEText
import base64
from main.services.notifications.gmail_auth import authenticate_gmail
import logging

async def notify_user(state:MealPlannerState):
    """Schedules meal plan notifications in Google Calendar."""
    """Sends a meal notification via Gmail."""
    meal_plan = state["formatted_meal"]
    user_email = "youremail@gmail.COM"  # Replace with recipient email

    # Authenticate Gmail API
    service = authenticate_gmail()

    # Create email message
    message = MIMEText(f"Today's meal plan: {meal_plan}")
    message["to"] = user_email
    message["subject"] = "Your AI-Generated Meal Plan"
    raw_message = base64.urlsafe_b64encode(message.as_bytes()).decode()

    try:
        service.users().messages().send(
            userId="me",
            body={"raw": raw_message}
        ).execute()
        logging.info(f"📩 Email sent successfully to {user_email}")
        return {"status": "email_sent"}
    except Exception as e:
        logging.error(f"❌ Error sending email: {e}")
        return {"status": "email_failed"}
    
    
    
    
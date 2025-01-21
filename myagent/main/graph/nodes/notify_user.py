from  main.graph.graph_state import MealPlannerState
from  main.services.notification_service import send_whatsapp_message
from main.services.calander_service import create_calendar_event
import datetime
from googleapiclient.discovery import build
from email.mime.text import MIMEText
import base64
from main.services.gmail_auth import authenticate_gmail
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
    
    
    
    # meal_times = {
    #     "breakfast": datetime.datetime.now().replace(hour=8, minute=0),  # 8:00 AM
    #     "lunch": datetime.datetime.now().replace(hour=12, minute=30),  # 12:30 PM
    #     "dinner": datetime.datetime.now().replace(hour=19, minute=0)  # 7:00 PM
    # }

    # for meal in state["meals"]:
    #     meal_type = list(meal.keys())[0]
    #     meal_data = meal[meal_type]
        
    #     meal_time = meal_times.get(meal_type)
    #     if meal_time:
    #         create_calendar_event(meal_data.meal_name, meal_time)
    # print(f"here are meals from notify_user {state["meals"]}")
    return state
    # """Pushes a summarized meal message, offering full details on request."""
    # meal_message = state.get("formatted_meal", "")

    # if not meal_message:
    #     print("❌ No meal message found. Skipping notification.")
    #     return state

    # # ✅ Generate a short summary
    # summary_message = "🍽️ Your Meal Plan for Today:\n"
    # for meal in state["meals"]:
    #     meal_type = list(meal.keys())[0]
    #     meal_name = meal[meal_type].meal_name
    #     summary_message += f"🔹 {meal_type.capitalize()}: {meal_name}\n"

    # summary_message += "\nReply with 'DETAILS' to receive full ingredients & recipe."

    # # ✅ Send Summary Message First
    # send_whatsapp_message(summary_message)

    # # ✅ Store full message for on-demand request
    # state["detailed_meal_message"] = meal_message  # Save for later retrieval

    # return state
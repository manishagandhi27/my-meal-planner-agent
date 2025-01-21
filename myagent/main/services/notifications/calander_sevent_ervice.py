from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
import datetime
import os
import pickle
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

SCOPES = ["https://www.googleapis.com/auth/calendar"]


CREDENTIALS_PATH = os.path.join(os.path.dirname(__file__), "credentials.json")


def authenticate_calendar():
    """Authenticate with Google Calendar API using OAuth2."""
    creds = None
    if os.path.exists("token.pickle"):
        with open("token.pickle", "rb") as token:
            creds = pickle.load(token)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(CREDENTIALS_PATH, SCOPES)
            creds = flow.run_local_server(port=0)
        with open("token.pickle", "wb") as token:
            pickle.dump(creds, token)
    return build("calendar", "v3", credentials=creds)

def create_calendar_event(meal_name, meal_time):
    """Creates a Google Calendar event for a meal."""
    service = authenticate_calendar()
    event = {
        "summary": f"🍽️ {meal_name}",
        "description": f"Enjoy your meal: {meal_name}!",
        "start": {"dateTime": meal_time.isoformat(), "timeZone": "America/New_York"},
        "end": {"dateTime": (meal_time + datetime.timedelta(minutes=45)).isoformat(), "timeZone": "America/New_York"},
        "reminders": {
            "useDefault": False,
            "overrides": [{"method": "popup", "minutes": 10}]
        }
    }
    event = service.events().insert(calendarId="primary", body=event).execute()
    print(f"📅 Google Calendar Event Created: {event['summary']} at {meal_time}")
    return event

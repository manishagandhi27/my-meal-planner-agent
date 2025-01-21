import os
import pickle
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

SCOPES = ["https://www.googleapis.com/auth/gmail.send",  "https://www.googleapis.com/auth/gmail.readonly"]

CREDENTIALS_PATH = os.path.join(os.path.dirname(__file__), "credentials.json")
TOKEN_PATH = os.path.join(os.path.dirname(__file__), "token.pickle")
import os
os.environ["BROWSER"] = "/usr/bin/google-chrome"


def authenticate_gmail():
    """Authenticates and returns the Gmail API service."""
    creds = None
    # Load saved credentials
    if os.path.exists(TOKEN_PATH):
        with open(TOKEN_PATH, "rb") as token:
            creds = pickle.load(token)

    # Refresh or request new credentials
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(CREDENTIALS_PATH, SCOPES)
            creds = flow.run_local_server(port=0)
           # creds = flow.run_console() 
        # Save new credentials
        with open("token.pickle", "wb") as token:
            pickle.dump(creds, token)

    from googleapiclient.discovery import build
    service = build("gmail", "v1", credentials=creds)
    return service


if __name__ =="__main__":
    authenticate_gmail()
import os
from pathlib import Path

import google.auth.transport.requests
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from app import app

PROSHORE_CALENDAR_ID = os.getenv("PROSHORE_CALENDAR_ID")
DPL_CALENDAR_ID = os.getenv("DPL_CALENDAR_ID")
DEFAULT_CALENDAR_ID = os.getenv("DEFAULT_CALENDAR_ID")
CALENDAR_SCOPE = os.getenv("CALENDAR_SCOPE")
REDIRECT_URI = os.getenv("REDIRECT_URI")
CLIENT_SECRETS_FILE = os.getenv("CLIENT_SECRETS_FILE")
TIMEZONE = os.getenv("TIMEZONE")


def get_calendar_id(source):
    """Determine the appropriate calendar ID based on the source"""
    return {
        'proshore': PROSHORE_CALENDAR_ID,
        'dpl': DPL_CALENDAR_ID,
    }.get(source, DEFAULT_CALENDAR_ID)


def get_credentials():
    """Get the credentials for the Google Calendar API"""
    this_folder = Path(__file__).parent.parent.resolve()
    creds = Credentials.from_authorized_user_file(this_folder / 'token.json', [CALENDAR_SCOPE]) if os.path.exists(
        this_folder / 'token.json') else None
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            request = google.auth.transport.requests.Request()
            creds.refresh(request)
            save_credentials(creds)

    return creds


def save_credentials(creds):
    """Save the credentials to the token.json file"""
    this_folder = Path(__file__).parent.parent.resolve()
    with open(this_folder / 'token.json', 'w') as token:
        token.write(creds.to_json())


def get_authorization_url():
    """Get the authorization URL for generating the token"""
    flow = InstalledAppFlow.from_client_secrets_file(
        CLIENT_SECRETS_FILE, CALENDAR_SCOPE, redirect_uri=REDIRECT_URI)
    authorization_url, state = flow.authorization_url(
        access_type='offline',
        include_granted_scopes='true')
    return authorization_url


def save_token(request):
    """Save the generated token to the token.json file"""
    flow = InstalledAppFlow.from_client_secrets_file(
        CLIENT_SECRETS_FILE, CALENDAR_SCOPE, redirect_uri=REDIRECT_URI)
    authorization_code = request.args.get('code')
    flow.fetch_token(code=authorization_code)
    credentials = flow.credentials
    save_credentials(credentials)


def create_calendar_event(firstname, lastname, leave_type, format_leaves_from, adjusted_end_date, calendar_id, creds):
    """Create a Google Calendar event"""
    service = build('calendar', 'v3', credentials=creds)
    event = {
        'summary': f"{firstname} {lastname}: {leave_type}",
        'end': {
            'date': adjusted_end_date.date().strftime('%Y-%m-%d'),
            'timeZone': TIMEZONE,
        },
        'start': {
            'date': format_leaves_from.date().strftime('%Y-%m-%d'),
            'timeZone': TIMEZONE,
        }
    }

    service.events().insert(calendarId=calendar_id, body=event).execute()

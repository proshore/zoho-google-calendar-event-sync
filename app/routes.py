import logging
from flask import request, redirect, url_for
from app import app
from app.services import get_calendar_id, get_credentials, save_credentials
from app.utils import validate_and_sanitize_input, get_date_params
from werkzeug.exceptions import BadRequest
import git

@app.route('/')
def system_check():
    return "The App is working"

@app.route('/zoho-calendar-sync', methods=['POST'])
def zoho_calendar_sync():
    try:
        # Validate and sanitize the input data
        input_data = validate_and_sanitize_input(request.form)       
        format_leaves_from, adjusted_end_date = get_date_params(input_data)
        calendar_id = get_calendar_id(input_data['source'])
        creds = get_credentials()
        
        if not creds:
            return redirect(url_for('generate_token'))
        
        from app.services import create_calendar_event
        create_calendar_event(
            input_data['firstname'],
            input_data['lastname'],
            input_data['leave_type'],
            format_leaves_from,
            adjusted_end_date,
            calendar_id,
            creds
        )
        return "Event created"
    except BadRequest as e:
        logging.error(str(e))
        return str(e), 400
    except Exception as e:
        logging.error(f"Error creating calendar event: {str(e)}")
        return str(e), 500

@app.route('/generate-token')
def generate_token():
    """Redirect the user to the page where they can generate the token"""
    from app.services import get_authorization_url
    return redirect(get_authorization_url())

@app.route('/save-token')
def save_token():
    """Save the generated token to the token.json file"""
    from app.services import save_token
    save_token(request)
    return "Token saved successfully"

@app.route('/git-update', methods=['POST'])
def git_update():
    repo = git.Repo('./zoho-google-calendar-event-sync')
    origin = repo.remotes.origin
    repo.create_head('master',origin.refs.master).set_tracking_branch(origin.refs.master).checkout()
    origin.pull()
    return '', 200
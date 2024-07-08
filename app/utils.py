import logging
from datetime import timedelta, datetime

from flask import escape
from werkzeug.exceptions import BadRequest


def validate_and_sanitize_input(data):
    """
    Validate and sanitize the input data.
    
    Args:
        data (dict): The input data to be validated and sanitized.
    
    Returns:
        dict: The validated and sanitized input data.
    
    Raises:
        BadRequest: If the input data is invalid.
    """
    try:
        firstname = escape(data.get('firstName'))
        lastname = escape(data.get('lastName'))
        leaves_from = escape(data.get('leavesFrom'))
        leaves_to = escape(data.get('leaveTo'))
        leave_type = escape(data.get('leaveType'))
        source = escape(data.get('source'))

        return {
            'firstname': firstname,
            'lastname': lastname,
            'leaves_from': leaves_from,
            'leaves_to': leaves_to,
            'leave_type': leave_type,
            'source': source
        }
    except (KeyError, ValueError) as e:
        logging.error(f"Invalid input data: {str(e)}")
        raise BadRequest(f"Invalid input data: {str(e)}")


def get_date_params(input_data):
    """Get the date-related parameters for the calendar event"""
    format_leaves_from = datetime.strptime(input_data['leaves_from'], '%d-%b-%Y')
    format_leaves_to = datetime.strptime(input_data['leaves_to'], '%d-%b-%Y')
    adjusted_end_date = format_leaves_to + timedelta(days=1)
    return format_leaves_from, adjusted_end_date

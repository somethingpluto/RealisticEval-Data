from datetime import datetime, timedelta
from typing import Optional


def create_icalendar_file(name: str, email: str, appointment_date: str, appointment_time: str,
                          file_path: Optional[str] = 'appointment.ics') -> None:
    """
    Create an iCalendar (.ics) file for a given appointment.

    Args:
        name (str): The name of the person for the appointment.
        email (str): The email of the person for the appointment.
        appointment_date (str): The date of the appointment in 'YYYY-MM-DD' format.
        appointment_time (str): The time of the appointment in 'HH:MM AM/PM' format.
        file_path (Optional[str]): The file path where the .ics file will be saved. Defaults to 'appointment.ics'.

    Raises:
        ValueError: If the date or time format is incorrect.
        IOError: If there is an error writing to the file.
    """
    try:
        # Format appointment date and time
        appointment_datetime = datetime.strptime(f"{appointment_date} {appointment_time}", "%Y-%m-%d %I:%M %p")

        # Create iCalendar content
        icalendar_content = f"""BEGIN:VCALENDAR
VERSION:2.0
BEGIN:VEVENT
SUMMARY:Dentist Appointment - {name}
DESCRIPTION:Booking for {name} ({email})
DTSTART:{appointment_datetime.strftime('%Y%m%dT%H%M%S')}
DTEND:{(appointment_datetime + timedelta(minutes=30)).strftime('%Y%m%dT%H%M%S')}
LOCATION:Dentist Office
ORGANIZER:MAILTO:toothcheck.app@gmail.com
SEQUENCE:0
BEGIN:VALARM
TRIGGER:-PT15M
DESCRIPTION:Reminder
ACTION:DISPLAY
END:VALARM
END:VEVENT
END:VCALENDAR
"""

        # Write the iCalendar content to a file
        with open(file_path, 'w') as file:
            file.write(icalendar_content)
        print(f"iCalendar file created successfully at {file_path}")

    except ValueError as ve:
        print(f"Error: Invalid date or time format - {ve}")
    except IOError as ioe:
        print(f"Error: Unable to write to file - {ioe}")

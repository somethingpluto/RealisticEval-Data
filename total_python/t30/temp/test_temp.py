import unittest
import os
from tempfile import NamedTemporaryFile


class TestCreateICalendarFile(unittest.TestCase):

    def test_valid_appointment(self):
        with NamedTemporaryFile(delete=False, suffix='.ics') as temp_file:
            file_path = temp_file.name
        try:
            create_icalendar_file("Alice", "alice@example.com", "2024-09-15", "10:00 AM", file_path)
            with open(file_path, 'r') as file:
                content = file.read()
                self.assertIn("SUMMARY:Dentist Appointment - Alice", content)
                self.assertIn("DESCRIPTION:Booking for Alice (alice@example.com)", content)
        finally:
            os.remove(file_path)

    def test_invalid_date_format(self):
        with self.assertRaises(ValueError):
            create_icalendar_file("Bob", "bob@example.com", "15-09-2024", "10:00 AM")

    def test_invalid_time_format(self):
        with self.assertRaises(ValueError):
            create_icalendar_file("Charlie", "charlie@example.com", "2024-09-15", "10:00")

    def test_default_file_path(self):
        default_file_path = 'appointment.ics'
        try:
            create_icalendar_file("David", "david@example.com", "2024-09-15", "11:00 AM")
            self.assertTrue(os.path.exists(default_file_path))
            with open(default_file_path, 'r') as file:
                content = file.read()
                self.assertIn("SUMMARY:Dentist Appointment - David", content)
                self.assertIn("DESCRIPTION:Booking for David (david@example.com)", content)
        finally:
            if os.path.exists(default_file_path):
                os.remove(default_file_path)

    def test_end_time_calculation(self):
        with NamedTemporaryFile(delete=False, suffix='.ics') as temp_file:
            file_path = temp_file.name
        try:
            create_icalendar_file("Eve", "eve@example.com", "2024-09-15", "09:00 AM", file_path)
            with open(file_path, 'r') as file:
                content = file.read()
                self.assertIn("DTSTART:20240915T090000", content)
                self.assertIn("DTEND:20240915T093000", content)
        finally:
            os.remove(file_path)

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
        # Parse appointment date and time
        appointment_datetime = datetime.strptime(f"{appointment_date} {appointment_time}", "%Y-%m-%d %I:%M %p")
        appointment_end_datetime = appointment_datetime + timedelta(minutes=30)

        # Prepare iCalendar content
        icalendar_content = (
            "BEGIN:VCALENDAR\n"
            "VERSION:2.0\n"
            "BEGIN:VEVENT\n"
            f"SUMMARY:Dentist Appointment - {name}\n"
            f"DESCRIPTION:Booking for {name} ({email})\n"
            f"DTSTART:{appointment_datetime.strftime('%Y%m%dT%H%M%S')}\n"
            f"DTEND:{appointment_end_datetime.strftime('%Y%m%dT%H%M%S')}\n"
            "LOCATION:Dentist Office\n"
            "ORGANIZER:MAILTO:toothcheck.app@gmail.com\n"
            "SEQUENCE:0\n"
            "BEGIN:VALARM\n"
            "TRIGGER:-PT15M\n"
            "DESCRIPTION:Reminder\n"
            "ACTION:DISPLAY\n"
            "END:VALARM\n"
            "END:VEVENT\n"
            "END:VCALENDAR\n"
        )

        # Write the iCalendar content to a file
        with open(file_path, 'w') as file:
            file.write(icalendar_content)
        print(f"iCalendar file created successfully at {file_path}")

    except ValueError as ve:
        print(f"Error: Invalid date or time format - {ve}")
    except IOError as ioe:
        print(f"Error: Unable to write to file - {ioe}")

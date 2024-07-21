import unittest
from unittest.mock import mock_open, patch
from datetime import datetime

from task_code.t9.adapted import create_icalendar_file


class TestCreateICalendarFile(unittest.TestCase):

    def test_create_icalendar_file_success(self):
        name = "John Doe"
        email = "john.doe@example.com"
        appointment_date = "2023-07-19"
        appointment_time = "10:30 AM"
        file_path = "test_appointment.ics"

        expected_output = f"""BEGIN:VCALENDAR
VERSION:2.0
BEGIN:VEVENT
SUMMARY:Dentist Appointment - {name}
DESCRIPTION:Booking for {name} ({email})
DTSTART:{datetime.strptime(f"{appointment_date} {appointment_time}", "%Y-%m-%d %I:%M %p").strftime('%Y%m%dT%H%M%S')}
DTEND:{(datetime.strptime(f"{appointment_date} {appointment_time}", "%Y-%m-%d %I:%M %p") + timedelta(minutes=30)).strftime('%Y%m%dT%H%M%S')}
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

        with patch("builtins.open", mock_open()) as mocked_file:
            create_icalendar_file(name, email, appointment_date, appointment_time, file_path)
            mocked_file.assert_called_once_with(file_path, 'w')
            mocked_file().write.assert_called_once_with(expected_output)

    def test_invalid_date_format(self):
        with self.assertRaises(ValueError):
            create_icalendar_file("John Doe", "john.doe@example.com", "2023-07-19", "25:00 AM")

    def test_invalid_time_format(self):
        with self.assertRaises(ValueError):
            create_icalendar_file("John Doe", "john.doe@example.com", "2023-07-32", "10:30 AM")

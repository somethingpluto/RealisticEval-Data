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

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
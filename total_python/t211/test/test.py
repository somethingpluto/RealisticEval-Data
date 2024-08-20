import unittest
from unittest.mock import mock_open, patch


class TestExtractParametersFromFile(unittest.TestCase):
    def test_standard_case(self):
        """ Test with a well-formed Fortran file content. """
        file_content = "real(r8), target, allocatable :: temp(3) ! Temperature profile, [K]"
        m = mock_open(read_data=file_content)
        with patch('builtins.open', m):
            result = extract_parameters_from_file('dummy.f90')
            expected = [{'variable_name': 'temp', 'description': 'Temperature profile', 'units': 'K'}]
            self.assertEqual(result, expected)

    def test_multiple_parameters(self):
        """ Test with multiple parameters in file content. """
        file_content = """
        real(r8), target, allocatable :: temp ! Ambient temperature, [C]
        real(r8), target, allocatable :: pressure(10) ! Atmospheric pressure, [atm]
        """
        m = mock_open(read_data=file_content)
        with patch('builtins.open', m):
            result = extract_parameters_from_file('dummy.f90')
            expected = [
                {'variable_name': 'temp', 'description': 'Ambient temperature', 'units': 'C'},
                {'variable_name': 'pressure', 'description': 'Atmospheric pressure', 'units': 'atm'}
            ]
            self.assertEqual(result, expected)

    def test_no_parameters(self):
        """ Test with no parameter declarations in file content. """
        file_content = "This file contains no relevant parameters."
        m = mock_open(read_data=file_content)
        with patch('builtins.open', m):
            result = extract_parameters_from_file('dummy.f90')
            self.assertEqual(result, [])

    def test_incorrect_format(self):
        """ Test with incorrectly formatted parameter declarations. """
        file_content = "real(r8), target, allocatable :: temp ! Incorrect format here"
        m = mock_open(read_data=file_content)
        with patch('builtins.open', m):
            result = extract_parameters_from_file('dummy.f90')
            self.assertEqual(result, [])

    def test_complex_structure(self):
        """ Test with complex and correct declarations. """
        file_content = """
        real(r8), target, allocatable :: temp(5, 10) ! Grid temperature, [K]
        real(r8), target, allocatable :: velocity ! Wind velocity, [m/s]
        """
        m = mock_open(read_data=file_content)
        with patch('builtins.open', m):
            result = extract_parameters_from_file('dummy.f90')
            expected = [
                {'variable_name': 'temp', 'description': 'Grid temperature', 'units': 'K'},
                {'variable_name': 'velocity', 'description': 'Wind velocity', 'units': 'm/s'}
            ]
            self.assertEqual(result, expected)
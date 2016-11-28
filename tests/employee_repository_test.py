from unittest import TestCase

from domain import Employee, Contact
from employee_repository import CSVEmployeeRepository, Anagraphic, Birthday


class FakeCsvInterpreter:
    def employees(self):
        return Anagraphic({Birthday(3, 5): [Employee("Surname", "Name", Contact("name@email.com"))],
                           Birthday(9, 9): [Employee("Surname", "Name", Contact("name@email.com")),
                                            Employee("another", "one", Contact("another@email.com"))]})


class EmployeeRepositoryTest(TestCase):
    csv_interpreter = FakeCsvInterpreter()

    def setUp(self):
        self.repository = CSVEmployeeRepository(self.csv_interpreter)

    def test_no_one_birthday(self):
        found_employees = self.repository.birthdayFor(2, 1)

        self.assertEqual(found_employees, None)

    def test_birthday_of_one_employee(self):
        found_employees = self.repository.birthdayFor(3, 5)

        self.assertEqual(found_employees, [Employee("Surname", "Name", Contact("name@email.com"))])

    def test_birthday_of_two_employees(self):
        found_employees = self.repository.birthdayFor(9, 9)

        self.assertEqual(found_employees, [Employee("Surname", "Name", Contact("name@email.com")),
                                           Employee("another", "one", Contact("another@email.com"))])
from datetime import date
from unittest import TestCase

from domain import Employee, Contact, BirthdayGreetings


class MessageServiceSpy:
    sent_messages = None

    def send(self, employees):
        self.sent_messages = employees

    def sentMessages(self):
        return self.sent_messages


class EmployeeRepositoryMock:
    def birthdaysFor(self, month, day):
        if month is 1 and day is 1:
            return [Employee("Banks", "Troy", Contact("troy@email.com"))]
        elif month is 2 and day is 2:
            return [Employee("Frequency", "Vibration", Contact("freq@email.com")),
                    Employee("Banks", "Troy", Contact("troy@email.com"))]
        else:
            return None


class BirthdayGreetingsTest(TestCase):
    message_service_spy = MessageServiceSpy()
    people_repository = EmployeeRepositoryMock()

    def setUp(self):
        self.birthday_greetings = BirthdayGreetings(self.people_repository, self.message_service_spy)

    def test_no_birthdays(self):
        self.birthday_greetings.sendGreetings(date(9999, 9, 9))

        self.assertEqual(self.message_service_spy.sentMessages(), None)

    def test_one_birthday(self):
        self.birthday_greetings.sendGreetings(date(1975, 1, 1))

        self.assertEqual(self.message_service_spy.sentMessages(),
                         [Employee("Banks", "Troy", Contact("troy@email.com"))])

    def test_multiple_days(self):
        self.birthday_greetings.sendGreetings(date(2014, 2, 2))

        self.assertListEqual(self.message_service_spy.sentMessages(),
                             [Employee("Frequency", "Vibration", Contact("freq@email.com")),
                              Employee("Banks", "Troy", Contact("troy@email.com"))])
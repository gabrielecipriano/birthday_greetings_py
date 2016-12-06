class Employee:
    def __init__(self, surname, name, contact):
        self.surname = surname
        self.name = name
        self.contact = contact

    def __eq__(self, other):
        return self.name == other.name \
               and self.surname == other.surname \
               and self.contact == other.contact


class Contact:
    def __init__(self, email):
        self.email = email

    def __eq__(self, other):
        return self.email == other.email

class BirthdayGreetings:
    def __init__(self, employee_repository, email_service):
        self._message_service = email_service
        self._employee_repository = employee_repository

    def sendGreetings(self, today):
        persons = self._employee_repository.birthdaysFor(today.month, today.day)
        self._message_service.send(persons)
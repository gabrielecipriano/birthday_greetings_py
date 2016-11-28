class CSVEmployeeRepository:
    def __init__(self, csv_intepreter):
        self.anagraphic = csv_intepreter.employees()

    def birthdayFor(self, month, day):
        return self.anagraphic.bornOn(Birthday(month, day))


class Anagraphic:
    def __init__(self, employees):
        self.employees = employees

    def bornOn(self, birthday):
        return self.employees.get(birthday)


class Birthday:
    def __init__(self, month, day):
        self.month = month
        self.day = day

    def __key(self):
        return (self.month, self.day)

    def __eq__(self, other):
        return self.__key() == other.__key()

    def __hash__(self):
        return hash(self.__key())
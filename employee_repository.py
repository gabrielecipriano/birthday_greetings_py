class CSVEmployeeRepository:
    def __init__(self, csv_intepreter):
        self._anagraphic = csv_intepreter.employees()

    def birthdayFor(self, month, day):
        return self._anagraphic.bornOn(Birthday(month, day))


class Anagraphic:
    def __init__(self, employees):
        self._employees = employees

    def bornOn(self, birthday):
        return self._employees.get(birthday)


class Birthday:
    def __init__(self, month, day):
        self._month = month
        self._day = day

    def __key(self):
        return (self._month, self._day)

    def __eq__(self, other):
        return self.__key() == other.__key()

    def __hash__(self):
        return hash(self.__key())
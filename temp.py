class Employee:
    num_of_emps = 0
    raise_amount = 1.04

    def __init__(self, first, last, pay) -> None:
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + "." + last + "@company.com"
        Employee.num_of_emps += 1

    def fullName(self):
        return f"Name: {self.first} {self.last}"

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amount = amount


class Developer(Employee):
    raise_amount = 1.10

    def __init__(self, first, last, pay, prog_lang) -> None:
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang


class Manager(Employee):
    raise_amount = 1.20

    def __init__(self, first, last, pay, employees=[]) -> None:
        super().__init__(first, last, pay)
        self.employees = employees


if __name__ == "__main__":
    print(Employee.raise_amount)
    Employee.set_raise_amt(1.1)
    print(Employee.raise_amount)

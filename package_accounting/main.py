from package_accounting.application.db import people
from package_accounting.application import salary
import datetime


if __name__ == '__main__':
    def main():
        while True:
            run = input("Введите команду: ")
            if run == 't':
                print(datetime.date.today())
                people.get_employees()
            elif run == 's':
                print(datetime.date.today())
                salary.calculate_salary()
            elif run == 'q':
                break

    main()


from application.salary import calculate_salary
from application.db.people import get_employees
from datetime import datetime

def main():
    print(f"Текущая дата и время: {datetime.now()}")
    get_employees()
    calculate_salary()

if __name__ == '__main__':
    main()
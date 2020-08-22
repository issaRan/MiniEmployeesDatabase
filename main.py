from Employee import Employee
from ManageDb import ManageDb


def main():
    print("1. Add New employee")
    print("2. Display employee")
    print("3. Delete New employee")

    chosen = int(input())
    if chosen == 1:
        ManageDb().saveToDataBase(Employee())
    elif chosen == 2:
        ManageDb().display()
    elif chosen == 3:
        ManageDb().delete_task()


if __name__ == '__main__':
    main()

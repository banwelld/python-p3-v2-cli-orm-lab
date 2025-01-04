from models.department import Department
from models.employee import Employee


def exit_program():
    print("Goodbye!")
    exit()

# We'll implement the department functions in this lesson


def list_departments():
    departments = Department.get_all()
    for department in departments:
        print(department)


def find_department_by_name():
    name = input("Enter the department's name: ")
    department = Department.find_by_name(name)
    print(department) if department else print(
        f'Department {name} not found')


def find_department_by_id():
    # use a trailing underscore not to override the built-in id function
    id_ = input("Enter the department's id: ")
    department = Department.find_by_id(id_)
    print(department) if department else print(f'Department {id_} not found')


def create_department():
    name = input("Enter the department's name: ")
    location = input("Enter the department's location: ")
    try:
        department = Department.create(name, location)
        print(f'Success: {department}')
    except Exception as exc:
        print("Error creating department: ", exc)


def update_department():
    id_ = input("Enter the department's id: ")
    if department := Department.find_by_id(id_):
        try:
            name = input("Enter the department's new name: ")
            department.name = name
            location = input("Enter the department's new location: ")
            department.location = location

            department.update()
            print(f'Success: {department}')
        except Exception as exc:
            print("Error updating department: ", exc)
    else:
        print(f'Department {id_} not found')


def delete_department():
    id_ = input("Enter the department's id: ")
    if department := Department.find_by_id(id_):
        department.delete()
        print(f'Department {id_} deleted')
    else:
        print(f'Department {id_} not found')


# You'll implement the employee functions in the lab

def list_employees():
    employees = Employee.get_all()
    print("")
    for emp in employees:
        print(emp)
    print("")


def find_employee_by_name():
    print("")
    target = input("Enter the employee's name: ")
    if record := Employee.find_by_name(target):
        print(f"\nEmployee '{target}' found:")
        print(record)
    else:
        print(f"\nEmployee '{target}' not found")
    print("")


def find_employee_by_id():
    print("")
    target = input("Enter the employee ID: ")
    if record := Employee.find_by_id(target):
        print(f"\nEmployee '{target}' found:")
        print(record)
    else:
        print(f"\nEmployee '{target}' not found")
    print("")


def create_employee():
    print("")
    emp_name = input("Enter the new employee's name: ")
    emp_title = input("Enter the new employee's job title: ")
    emp_deptid = int(input("Enter the new employee's department ID: "))
    try:
        new_emp = Employee.create(emp_name, emp_title, emp_deptid)
        print(f"\nNew employee '{emp_name}' record created:")
        print(new_emp)
    except Exception as exc:
        print(f"\nNew employee '{emp_name}' record not created:")
        print(exc)
    print("")


def update_employee():
    print("")
    
    target = input("Enter the employee ID: ")
    if record := Employee.find_by_id(target):
        print(f"\nEmployee '{target}' found: ")
        print(record)
        try:
            emp_name = input("\nEnter the employee's new name: ")
            emp_title = input("Enter the employee's new job title: ")
            emp_deptid = int(input("Enter the employee's new department ID: "))
            record.name = emp_name
            record.job_title = emp_title
            record.department_id = emp_deptid
            record.update()
            
            print(f"\nEmployee '{target}' record updated:")
            print(record)
        except Exception as exc:
            print(f"\nEmployee '{target}' record not updated:")
            print(exc)
    else:
        print(f"\nEmployee '{target}' not found")
        
    print("")


def delete_employee():
    print("")
    target = input("Enter the employee ID: ")
    print("\nAttempting deletion:")
    print(record := Employee.find_by_id(target))
    if record:
        try:
            record.delete()
            print(f"\nEmployee '{target}' expunged from database")
        except Exception as exc:
            print(f"\nEmployee '{target}' could not be expunged from database:")
            print(exc)
    else:
        print(f"\nEmployee '{target}' not found")
        
    print("")


def list_department_employees():
    print("")
    dept_id = int(input("Enter the department's id: "))
    if department := Department.find_by_id(dept_id):
        print(department)
        for emp in department.employees():
            print(emp)
    else:
        print(f"\nDepartment '{dept_id}' not found")
    print("")
# Solution

# Data Structure = dictionary
employees={}

# Generate unique id
def gen_id():
    if not hasattr(gen_id, "i"): 
        gen_id.i = 100    
    id_ = f"E{gen_id.i}"  
    gen_id.i += 1 
    return id_

# Menu
def menu():
    print("\n> EMPLOYEE MANAGEMENT")
    print("-" * 21)
    print("1.Add a new employee"
    "\n2.Remove an employee"
    "\n3.Update employee details"
    "\n4.Search employee"
    "\n5.Sort employees"
    "\n6.Show all employees"
    "\n7.Exit")
    print("Enter : ")
    return int(input())

# Validation Functions
def validate_name(name):
    if name.isalpha():
        return name
    print("Invalid Name! Name should contain only alphabets.")
    return None

def validate_age(age):
    if age.isdigit() and int(age) > 0:
        return int(age)  # Convert to integer
    print("Invalid Age! Age should be a positive integer.")
    return None

# Add a new employee
def add_emp():
    emp_id=gen_id()
    while True:
        emp_name=validate_name(input("Enter Name: "))
        if emp_name:
            break
    while True:
        emp_age=int(input("Enter Age: "))
        if emp_age:
            break
    emp_dept=input("Enter Department: ")
    employees[emp_id]={
        "name":emp_name,
        "age":emp_age,
        "department":emp_dept
    }
    print(f"{emp_id} Employee added successfully\n")
    show()

# Remove an Employee
def remove_emp():
    emp_id=input("Enter Employee id(emp_id): ")
    if emp_id in employees:
        del employees[emp_id]
        print("Deleted successfully")
    else:
        print("Not Found")

# Update Employee Details
def update_emp():
    emp_id=input("Enter Employee id: ")
    if emp_id in employees:
         while True:
            emp_name=validate_name(input("Enter Name to Update: "))
            if emp_name:
                break
         while True:
            emp_age=int(input("Enter Age to Update: "))
            if emp_age:
                break
         emp_dept=input("Enter Department to Update: ")
         employees[emp_id]={
             "name":emp_name,
             "age":emp_age,
             "department":emp_dept
         }
         print("Updated Successfully")

# Search Employees
def search_emp():
    emp = input("Enter Employee ID or Name: ").strip().lower()
    for emp_id, details in employees.items():
        if emp_id.lower() == emp or details["name"].lower() == emp:
            print(f"ID: {emp_id}, Name: {details['name']}, Age: {details['age']}, Department: {details['department']}")
            return  
    print("Employee not found!")

# Show All Employees
def show():
    print("\nEmployee List:")
    print("-" * 40)
    print(f"{'ID':<10}{'Name':<15}{'Age':<5}{'Department':<10}")
    print("-" * 40)
    
    for emp_id, details in employees.items():  # ✅ Correctly iterate over dictionary
        print(f"{emp_id:<10}{details['name']:<15}{details['age']:<5}{details['department']:<10}")


def insertion_sort(key_name):
    global employees
    emp_list = list(employees.items())  
    n = len(emp_list)
    
    for i in range(1, n):
        key = emp_list[i]  
        j = i - 1

        while j >= 0 and emp_list[j][1][key_name] > key[1][key_name]:
            emp_list[j + 1] = emp_list[j]
            j -= 1
        emp_list[j + 1] = key

    employees = dict(emp_list)
    show()


# Sort Employees
def sort_emp():
    print("Sort By:"
          "\n1. Name (alphabetical order)"
          "\n2. Age (ascending order)"
          "\n3. Department")
    
    choice = int(input("Enter: "))
    
    if choice == 1:
        insertion_sort("name")
    elif choice == 2:
        insertion_sort("age")
    elif choice == 3:
        insertion_sort("department")
    else:
        print("Invalid Selection")

while True:
    choice=menu()
    if choice==1:
        add_emp()
    elif choice==2:
        remove_emp()
    elif choice==3:
        update_emp()
    elif choice==4:
        search_emp()
    elif choice==5:
        sort_emp()
    elif choice==6:
        show()
    elif choice==7:
        print("Exiting...")
        break
    else:
        print("Invalid Selection")


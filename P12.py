import os, json

EMPLOYEE_FILE = "employees.dat"
INDEX_FILE = "index.dat"

def load_index():
    return json.load(open(INDEX_FILE)) if os.path.exists(INDEX_FILE) else {}

def save_index(index):
    json.dump(index, open(INDEX_FILE, "w"))

def add_employee(emp_id, name, designation, salary):
    index = load_index()
    if emp_id in index:
        print("Employee ID exists!")
        return
    with open(EMPLOYEE_FILE, "a") as f:
        pos = f.tell()
        f.write(f"{emp_id},{name},{designation},{salary}\n")
    index[emp_id] = pos
    save_index(index)
    print("Added successfully!")

def delete_employee(emp_id):
    index = load_index()
    if emp_id not in index:
        print("Not found!")
        return
    index.pop(emp_id)
    save_index(index)
    print("Deleted successfully!")

def display_employee(emp_id):
    index = load_index()
    if emp_id not in index:
        print("Not found!")
        return
    with open(EMPLOYEE_FILE) as f:
        f.seek(index[emp_id])
        print("Employee:", f.readline().strip())

def main():
    while True:
        print("\n1. Add  2. Delete  3. Display  4. Exit")
        ch = input("Enter choice: ")
        if ch == "1":
            add_employee(input("ID: "), input("Name: "), input("Designation: "), input("Salary: "))
        elif ch == "2":
            delete_employee(input("ID: "))
        elif ch == "3":
            display_employee(input("ID: "))
        elif ch == "4":
            break
        else:
            print("Invalid!")

if __name__ == "__main__":
    main()

import json

# Person Class
class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def get_details(self):
        return f"Name: {self.name}, Age: {self.age}, Gender: {self.gender}"

# Employee Class Inheritace(Person)
class Employee(Person):
    def __init__(self, name, age, gender, emp_id, department, salary):
        super().__init__(name, age, gender)
        self.emp_id = emp_id
        self.department = department
        self.salary = salary

    def is_eligible_for_bonus(self):
        return self.salary < 50000
    

    @classmethod
    def from_string(cls, data_string):
        # Format: "John,35,Male,E101,HR,45000"
        data = data_string.split(",")
        return cls(data[0], int(data[1]), data[2], data[3], data[4], float(data[5]))

    @staticmethod
    def bonus_policy():
        print("Bonus Policy: Employees with a salary less than $50,000 are eligible for a bonus.")

    def get_details(self):
        return (f"ID: {self.emp_id}, Name: {self.name}, Age: {self.age}, Gender: {self.gender}, "
                f"Department: {self.department}, Salary: {self.salary}")

# Department Class
class Department:
    def __init__(self, name):
        self.name = name
        self.employees = []

    def add_employee(self, employee):
        if isinstance(employee, Employee):
            self.employees.append(employee)

    def get_average_salary(self):
        if not self.employees:
            return 0
        total_salary = sum(emp.salary for emp in self.employees)
        return total_salary / len(self.employees)

    def get_all_employees(self):
        return [emp.get_details() for emp in self.employees]
    


def save_to_json(employees, json_path):
    employees_data = []
   
    for emp in employees:
        emp_dict = {
            "name": emp.name,
            "age": emp.age,
            "gender": emp.gender,
            "emp_id": emp.emp_id,
            "department": emp.department,
            "salary": emp.salary
        }
        employees_data.append(emp_dict)
 
    with open(json_path, 'w') as file:
        json.dump(employees_data, file, indent=4)
 
# load the data from json
def load_from_json(json_path):
    with open(json_path, 'r') as file:
        data_of_employees = json.load(file)
        employees = []
       
        for emp in data_of_employees:
            employees.append(Employee(
                emp["name"],
                emp["age"],
                emp["gender"],
                emp["emp_id"],
                emp["department"],
                emp["salary"]
            ))
           
        return employees
 

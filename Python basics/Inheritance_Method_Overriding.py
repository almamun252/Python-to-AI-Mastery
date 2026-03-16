# Parent Class
class Employee:
    def __init__(self, name, emp_id):
        self.name = name
        self.emp_id = emp_id

    # I will override this method in child classes
    def calculate_salary(self):
        return 0

# Child Class 1: Full-Time
class FullTimeEmployee(Employee):
    def __init__(self, name, emp_id, monthly_salary):
        super().__init__(name, emp_id)
        self.monthly_salary = monthly_salary

    # Method Overriding
    def calculate_salary(self):
        return self.monthly_salary

# Child Class 2: Part-Time
class PartTimeEmployee(Employee):
    def __init__(self, name, emp_id, hours_worked, hourly_rate):
        super().__init__(name, emp_id)
        self.hours_worked = hours_worked
        self.hourly_rate = hourly_rate

    # Method Overriding
    def calculate_salary(self):
        return self.hours_worked * self.hourly_rate

# Child Class 3: Commission-based
class CommissionEmployee(Employee):
    def __init__(self, name, emp_id, base_salary, sales_amount, commission_rate):
        super().__init__(name, emp_id)
        self.base_salary = base_salary
        self.sales_amount = sales_amount
        self.commission_rate = commission_rate

    # Method Overriding
    def calculate_salary(self):
        return self.base_salary + (self.sales_amount * self.commission_rate)




# Employee data entry has been done
emp1 = FullTimeEmployee("Rahim", 101, 50000)
emp2 = PartTimeEmployee("Karim", 102, 120, 300)
emp3 = CommissionEmployee("Salma", 103, 15000, 100000, 0.05)

#Employees data list
all_employees = [emp1, emp2, emp3]




for emp in all_employees:
    salary = emp.calculate_salary()
    print(f"Name: {emp.name} (ID: {emp.emp_id}) | Salary: {salary} BDT")
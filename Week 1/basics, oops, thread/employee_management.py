from datetime import datetime

## Base class for all employees in the Surveysparrow
class Surveysparrow:
    def __init__(self, name, dept):
        self.name = name
        self.dept = dept
        self.logged_in = False
    
    def log_out(self):
        if self.logged_in:
            self.logged_in = False
            out_time = datetime.now().strftime("%H:%M:%S")
            print(f"{self.name} has been logged out at {out_time}")
        else:
            print(f"{self.name} is already logged out")

    def log_in(self):
        if self.logged_in == False:
            self.logged_in = True
            in_time = datetime.now().strftime("%H:%M:%S")
            print(f"{self.name} has been logged in at {in_time}")
        else:
            print(f"{self.name} is not logged out")

    def __str__(self):
        return f"{self.name} : {self.dept}"

# Inherts some of the functions from base class for interns
class Intern(Surveysparrow):
    def __init__(self, name, dept, intern_id):
        super().__init__(name, dept)
        self.intern_id = intern_id

    def __str__(self):
        return f"{super().__str__()} : {self.intern_id}"
    
# Inherts some of the functions from base class for FullTime
class FullTime(Surveysparrow):
    def __init__(self, name, dept, emp_id):
        super().__init__(name, dept)
        self.emp_id = emp_id

    def __str__(self):
        return f"{super().__str__()} : {self.emp_id}"

# Class to store the employee's List
class EmployeeList:
    def __init__(self):
        self.employees = []

    def add_employee(self, emp):
        self.employees.append(emp)

    def display_employees(self):
        for emp in self.employees:
            print(emp)

employee_list = EmployeeList()
intern1 = Intern("Shandy", "Analyze","INT080")
intern2 = Intern("Gokul", "Devops","INT234")
full_time1 = FullTime("Rafiq", "Analysze","EMP378")
full_time2 = FullTime("Shubash", "Devops","EM990")

employee_list.add_employee(intern1)
employee_list.add_employee(intern2)
employee_list.add_employee(full_time1)
employee_list.add_employee(full_time2)

employee_list.display_employees()

intern1.log_in()
intern2.log_in()
full_time1.log_in()
intern1.log_out()
full_time1.log_out()



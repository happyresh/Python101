# Employee Salary Computation Program

def get_employee_details():
    """Function to get employee details from user input."""
    name = input("Enter Employee Name: ")
    age = int(input("Enter Employee Age: "))
    gender = input("Enter Employee Gender (Male/Female): ").capitalize()
    civil_status = input("Enter Employee Civil Status (Single/Married): ").capitalize()
    college = input("Enter Employee College: ")
    position = input("Enter Employee Position: ")
    hours_worked = int(input("Number of Hours Work (per month): "))
    
    return {
        "name": name,
        "age": age,
        "gender": gender,
        "civil_status": civil_status,
        "college": college,
        "position": position,
        "hours_worked": hours_worked
    }

def compute_gross_salary(position, hours_worked):
    """Function to compute the gross salary of an employee."""
    salary_chart = {
        "Instructor 1": (29165, 150),
        "Instructor 2": (31320, 200),
        "Instructor 3": (33843, 250),
        "Assistant Professor 1": (36619, 300),
        "Assistant Professor 2": (39672, 350),
        "Assistant Professor 3": (43030, 400),
        "Assistant Professor 4": (46725, 450)
    }
    
    if position in salary_chart:
        base_salary, rate_per_hour = salary_chart[position]
        return base_salary + (hours_worked * rate_per_hour)
    else:
        print("Invalid position entered.")
        return 0

def display_summary(employee_list):
    """Function to display the summary details of employees."""
    total_employees = len(employee_list)
    male_count = sum(1 for emp in employee_list if emp["gender"] == "Male")
    female_count = sum(1 for emp in employee_list if emp["gender"] == "Female")
    single_count = sum(1 for emp in employee_list if emp["civil_status"] == "Single")
    married_count = sum(1 for emp in employee_list if emp["civil_status"] == "Married")
    total_salaries = sum(emp["gross_salary"] for emp in employee_list)
    
    print("\nSUMMARY DETAILS:")
    print(f"Total Number of Employees: {total_employees}")
    print(f"Total Number of Male Employees: {male_count}")
    print(f"Total Number of Female Employees: {female_count}")
    print(f"Total Number of Single Employees: {single_count}")
    print(f"Total Number of Married Employees: {married_count}")
    print(f"Total Accumulated Salaries of ALL Employees: Php {total_salaries:,}")

def main():
    employee_list = []
    
    while True:
        employee = get_employee_details()
        employee["gross_salary"] = compute_gross_salary(employee["position"], employee["hours_worked"])
        print(f"\nTotal Monthly Gross Salary: Php {employee['gross_salary']:,}\n")
        employee_list.append(employee)
        
        repeat = input("Enter another [Y/N]? ").strip().upper()
        if repeat != 'Y':
            break
    
    display_summary(employee_list)

if __name__ == "__main__":
    main()

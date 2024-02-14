import csv
# import matplotlib.pyplot as plt
import os

CURRENT_DIR = os.path.dirname(os.path.realpath(__file__))

def read_sales_data():
    """
    Reads the sales data from the "sales_data.csv" file.

    Arguments: None

    Returns:
    - sales_data (list): List of dictionaries representing sales data.
    """
    sales_path = CURRENT_DIR +"/sales_data.csv"
    sales_data = []

    with open(sales_path, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            sales_data.append(row)
    return sales_data


def read_employee_data():
    """
    Reads the employee data from the "employee_data.csv" file.

    Arguments: None

    Returns:
    - employee_data (list): List of dictionaries representing employee data.
    """
    with open(f"{CURRENT_DIR}/employee_data.csv") as file:
        return [row for row in csv.DictReader(file)]


def calculate_total_sales(sales_data):
    from functools import reduce
    """
    Calculates the total sales amount.

    Arguments:
    - sales_data (list): List of dictionaries representing sales data.

    Returns:
    - total_sales (float): Total sales amount.
    """
    # total = 0
    # for sale in sales_data:
    #     total += float(sale["Amount"])
    # return total
    # amounts = []
    # sum = 0
    # for sale in sales_data:
    #     amounts.append(int(sale["Amout"]))
      
    # for amount in amounts:
    #     sum += int(amount)

    # return sum([float(sale["Amount"]) for sale in sales_data])
    return reduce(lambda acc, sale: acc + float(sale["Amount"]), sales_data, 0)


        

def calculate_average_sales(sales_data):
    """
    Calculates the average sales amount.

    Arguments:
    - sales_data (list): List of dictionaries representing sales data.

    Returns:
    - average_sales (float): Average sales amount.
    """
    return calculate_total_sales(sales_data) / len(sales_data) 

def calculate_median_sales(sales_data):
    """
    Calculates the median sales amount.

    Arguments:
    - sales_data (list): List of dictionaries representing sales data.

    Returns:
    - median_sales (float): Median sales amount.
    """
    amounts = [float(sale["Amount"]) for sale in sales_data]
    amounts = sorted(amounts)
    
    if (l := len(amounts)) %2 == 0:
        return (amounts[l // 2] + amounts[l // 2 -1])/2
    return amounts[(len(amounts) // 2)]

def calculate_total_salary_expenses(employee_data):
    from functools import reduce
    """
    Calculates the total salary expenses.

    Arguments:
    - employee_data (list): List of dictionaries representing employee data.

    Returns:
    - total_salary_expenses (float): Total salary expenses.
    """
    return reduce(lambda acc, emp: acc + float(emp["Salary"]), employee_data, 0) 


def calculate_average_salary(employee_data):
    """
    Calculates the average salary.

    Arguments:
    - employee_data (list): List of dictionaries representing employee data.

    Returns:
    - average_salary (float): Average salary.
    """
    return calculate_total_salary_expenses(employee_data) / len(employee_data) 
def calculate_median_salary(employee_data):
    """
    Calculates the median salary.

    Arguments:
    - employee_data (list): List of dictionaries representing employee data.

    Returns:
    - median_salary (float): Median salary.
    """
    salaries = [float(emp["Salary"]) for emp in employee_data]
    salaries = sorted(salaries)
    
    if (l := len(salaries)) %2 == 0:
        return (salaries[l // 2] + salaries[l // 2 -1])/2
    return salaries[(len(salaries) // 2)]


def find_employee_with_highest_sales(sales_data, employee_data):
    """
    Finds the employee with the highest sales amount.

    Arguments:
    - sales_data (list): List of dictionaries representing sales data.
    - employee_data (list): List of dictionaries representing employee data.

    Returns:
    - employee_name (str): Name of the employee with the highest sales amount.
    - department_name (str): Name of the department of the employee with the highest sales amount.
    """
    p_amounts = {}
    for sd in sales_data:
      if sd["EmployeeID"] not in p_amounts:
        p_amounts[sd["EmployeeID"]] = 0 
      p_amounts[sd["EmployeeID"]] += float(sd["Amount"])
    
    p_max = max(p_amounts, key=p_amounts.get)
    
    for emp in employee_data:
        if emp["EmployeeID"] == p_max:
            return emp["Name"], emp["Department"]



def find_department_with_highest_sales(sales_data, employee_data):
  """
  Finds the department with the highest sales.

  Arguments:
  - sales_data (list): List of dictionaries representing sales data.
  - employee_data (list): List of dictionaries representing employee data.

  Returns:
  - department_name (str): Name of the department with the highest sales.
  """
  p_amounts = {}
  for sd in sales_data:
    if sd["EmployeeID"] not in p_amounts:
      p_amounts[sd["EmployeeID"]] = 0 
    p_amounts[sd["EmployeeID"]] += float(sd["Amount"])

  d_amount = {}
  for emp in employee_data:
    if emp["Department"] not in d_amount:
      d_amount[emp["Department"]] = 0 
    d_amount[emp["Department"]] += p_amounts[emp["EmployeeID"]]

  return max(d_amount, key=d_amount.get)

# def plot_sales_by_department(sales_data, employee_data):
#     """
#     Plots a bar chart showing the total sales by department.

#     Arguments:
#     - sales_data (list): List of dictionaries representing sales data.
#     - employee_data (list): List of dictionaries representing employee data.

#     Returns: None
#     """
#     pass


# def plot_sales_vs_salary(sales_data, employee_data):
#     """
#     Plots a scatter plot showing the relationship between sales and salary.

#     Arguments:
#     - sales_data (list): List of dictionaries representing sales data.
#     - employee_data (list): List of dictionaries representing employee data.

#     Returns: None
#     """
#     pass


def main():
    # Read sales data
    sales_data = read_sales_data()
    # print(sales_data)

    # Read employee data
    employee_data = read_employee_data()
    print(employee_data)

    # Calculate total sales amount
    total_sales = calculate_total_sales(sales_data)
    print("Total Sales Amount:", total_sales)

    # Calculate average sales amount
    average_sales = calculate_average_sales(sales_data)
    print("Average Sales Amount:", average_sales)

    # Calculate median sales amount
    median_sales = calculate_median_sales(sales_data)
    print("Median Sales Amount:", median_sales)

    # Calculate total salary expenses
    total_salary_expenses = calculate_total_salary_expenses(employee_data)
    print("Total Salary Expenses:", total_salary_expenses)

    # Calculate average salary
    average_salary = calculate_average_salary(employee_data)
    print("Average Salary:", average_salary)

    # Calculate median salary
    median_salary = calculate_median_salary(employee_data)
    print("Median Salary:", median_salary)

    # Find the employee with the highest sales amount
    highest_sales_employee, highest_sales_employee_dep = find_employee_with_highest_sales(sales_data, employee_data)
    print("Employee with Highest Sales Amount:", highest_sales_employee, highest_sales_employee_dep)

    # Find the department with the highest sales
    highest_sales_department = find_department_with_highest_sales(sales_data, employee_data)
    print("Department with Highest Sales:", highest_sales_department)

    # Plot total sales by department
    # plot_sales_by_department(sales_data, employee_data)

    # Plot sales vs. salary
    # plot_sales_vs_salary(sales_data, employee_data)


if __name__ == '__main__':
    main()

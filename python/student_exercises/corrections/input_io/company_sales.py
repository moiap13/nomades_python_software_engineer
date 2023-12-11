import csv
# import matplotlib.pyplot as plt


def read_sales_data():
    """
    Reads the sales data from the "sales_data.csv" file.

    Arguments: None

    Returns:
    - sales_data (list): List of dictionaries representing sales data.
    """
    import os
    
    FULL_PATH_OS = os.path.dirname(__file__)

    sales_data = []
    # with open(FULL_PATH_OS+"/sales_data.csv", "r") as sales_csv_file:
    #   reader = csv.reader(sales_csv_file)
      
    #   b_header = True
    #   header = ""
    #   for row in reader:
    #       if b_header:
    #           header = row
    #           b_header = False
    #       else:
    #           sales_data.append({
    #              header[0]: row[0], 
    #              header[1]: row[1], 
    #              header[2]: row[2], 
    #              header[3]: row[3], 
    #           })
    with open(FULL_PATH_OS+"/sales_data.csv", "r") as sales_csv_file:
      reader = csv.DictReader(sales_csv_file)
      sales_data = [row for row in reader]
    return sales_data


def read_employee_data():
    """
    Reads the employee data from the "employee_data.csv" file.

    Arguments: None

    Returns:
    - employee_data (list): List of dictionaries representing employee data.
    """
    import os
    FULL_PATH_OS = os.path.dirname(__file__)

    employee_data = []
    with open(FULL_PATH_OS+"/employee_data.csv", "r") as employee_csv_file:
      reader = csv.DictReader(employee_csv_file)
      employee_data = [row for row in reader]
    return employee_data


def calculate_total_sales(sales_data):
    """
    Calculates the total sales amount.

    Arguments:
    - sales_data (list): List of dictionaries representing sales data.

    Returns:
    - total_sales (float): Total sales amount.
    """
    return sum([float(d["Amount"]) for d in sales_data])


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
    sale_dict_sorted = sorted(sales_data, key=lambda d: d["Amount"])
    l = len(sale_dict_sorted)
    mid_2 = l // 2
    return sale_dict_sorted[mid_2]["Amount"] if mid_2%2==1 else (float(sale_dict_sorted[mid_2-1]["Amount"]) + float(sale_dict_sorted[mid_2]["Amount"]))/2
    # sales_ammount = sorted([float(d["Amount"]) for d in sales_data])
    # l = len(sales_ammount)
    # mid = l // 2
    # return sales_ammount[mid] if l%2 == 1 else (sales_ammount[mid-1] + sales_ammount[mid])/2


def calculate_total_salary_expenses(employee_data):
    """
    Calculates the total salary expenses.

    Arguments:
    - employee_data (list): List of dictionaries representing employee data.

    Returns:
    - total_salary_expenses (float): Total salary expenses.
    """
    return sum([float(d["Salary"]) for d in employee_data])


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
    employee_salray_list = sorted([float(d["Salary"]) for d in employee_data])
    l = len(employee_salray_list)
    mid = l // 2
    return employee_salray_list[mid] if l%2 == 1 else (employee_salray_list[mid-1] + employee_salray_list[mid])/2



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
    employee_sales = {}
    for sale in sales_data:
        employee_id = int(sale["EmployeeID"])-1
        curr_employee = employee_data[employee_id]
        t = (curr_employee["Name"], curr_employee["Department"])
        if t in employee_sales:
            employee_sales[t] += int(sale["Amount"])
        else:
            employee_sales[t] = int(sale["Amount"])
    # print(employee_sales)
    
    max_amount = 0
    best_employee = None
    for k, v in employee_sales.items():
        if v > max_amount:
            max_amount = v
            best_employee = k
  
    return best_employee[0], best_employee[1]


def find_department_with_highest_sales(sales_data, employee_data):
    """
    Finds the department with the highest sales.

    Arguments:
    - sales_data (list): List of dictionaries representing sales data.
    - employee_data (list): List of dictionaries representing employee data.

    Returns:
    - department_name (str): Name of the department with the highest sales.
    """
    return find_employee_with_highest_sales(sales_data, employee_data)[1]


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
    # print(sales_data[:5])

    # Read employee data
    employee_data = read_employee_data()
    # print(employee_data)

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

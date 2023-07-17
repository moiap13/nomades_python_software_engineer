import csv
import matplotlib.pyplot as plt
import os

def create_students_csv():
    """
    Creates a CSV file named "students.csv" and writes student data to it.

    Arguments: None

    Returns: None
    """
    data = [
        ['Name', 'Age', 'Grade'],
        ['John', '15', '9'],
        ['Alice', '16', '10'],
        ['Bob', '14', '8']
    ]

    with open('students.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(data)

    print("CSV file created successfully!")


def read_students_csv():
    """
    Reads and prints the student data from the "students.csv" file.

    Arguments: None

    Returns: None
    """
    pass


def calculate_average_age():
    """
    Calculates the average age of students in the "students.csv" file.

    Arguments: None

    Returns:
    - average_age (float): The average age of students.
    """
    return None


def create_student_grades_chart():
    """
    Creates a bar chart showing the grades of students from the "students.csv" file.

    Arguments: None

    Returns: None
    """
    pass


def create_sales_csv():
    """
    Creates a CSV file named "sales.csv" and writes sales data to it.

    Arguments: None

    Returns: None
    """
    data = [
        ['Month', 'Sales'],
        ['January', '5000'],
        ['February', '7000'],
        ['March', '5500']
    ]

    csv_file = 'sales.csv'


def calculate_total_sales():
    """
    Calculates the total sales from the "sales.csv" file.

    Arguments: None

    Returns:
    - total_sales (int): The total sales value.
    """
    return None


def create_monthly_sales_chart():
    """
    Creates a line chart showing the monthly sales data from the "sales.csv" file.

    Arguments: None

    Returns: None
    """
    months = []
    sales = []
    


def merge_files_into_combined_csv():
    """
    Merges the "students.csv" and "sales.csv" files into a single CSV file named "combined.csv".

    Arguments: None

    Returns: None

    Notes:
    The combined CSV must look like :
    
    Name,Age,Grade,Month,Sales
    John,15,9,January,5000
    Alice,16,10,February,7000
    Bob,14,8,March,5500

    """
    csv_file = 'combined.csv'


def read_combined_csv():
    """
    Reads and prints the data from the "combined.csv" file.

    Arguments: None

    Returns: None
    """
    pass


def create_age_sales_scatter_plot():
    """
    Creates a scatter plot showing the relationship between age and sales from the "combined.csv" file.

    Arguments: None

    Returns: None
    """
    ages = []
    sales = []

def create_temperatures_csv():
    """
    Creates a CSV file named "temperatures.csv" and writes temperature data to it.

    Arguments: None

    Returns: None
    """
    data = [
        ['Month', 'Temperature'],
        ['January', '10'],
        ['February', '15'],
        ['March', '20'],
        ['April', '25'],
        ['May', '30'],
        ['June', '35'],
        ['July', '40'],
        ['August', '35'],
        ['September', '30'],
        ['October', '25'],
        ['November', '20'],
        ['December', '15']
    ]


def plot_temperatures():
    """
    Reads temperature data from the "temperatures.csv" file and creates a line chart.

    Arguments: None

    Returns: None
    """
    months = []
    temperatures = []


def create_sales_by_category_csv():
    """
    Creates a CSV file named "sales_by_category.csv" and writes sales data by category to it.

    Arguments: None

    Returns: None
    """
    data = [
        ['Category', 'Sales'],
        ['Electronics', '5000'],
        ['Clothing', '3000'],
        ['Books', '2000'],
        ['Home Decor', '4000'],
        ['Sports', '3500']
    ]


def plot_sales_by_category():
    """
    Reads sales data by category from the "sales_by_category.csv" file and creates a bar chart.

    Arguments: None

    Returns: None
    """
    categories = []
    sales = []


def create_population_csv():
    """
    Creates a CSV file named "population.csv" and writes population data for different countries to it.

    Arguments: None

    Returns: None
    """
    data = [
        ['Country', 'Population'],
        ['China', '1444216107'],
        ['India', '1393409038'],
        ['United States', '332915073'],
        ['Indonesia', '276361783'],
        ['Pakistan', '225199937'],
        ['Brazil', '213993437']
    ]


def plot_population_pie_chart():
    """
    Reads population data from the "population.csv" file and creates a pie chart.

    Arguments: None

    Returns: None
    """
    countries = []
    populations = []

def print_menu():
    """
    Prints the menu options.

    Arguments: None

    Returns: None
    """
    os.system('cls' if os.name == 'nt' else 'clear')
    print("""- Students:
    1. Create students CSV
    2. Read students CSV
    3. Calculate average age
    4. Create student grades chart
- Sales:
    5. Create sales CSV
    6. Calculate total sales
    7. Create monthly sales chart
- Combined:
    8. Merge files into combined CSV
    9. Read combined CSV
    10. Create age-sales scatter plot
- Temperatures:
    11. Create temperatures CSV
    12. Plot temperatures
- Sales by Category:
    13. Create sales by category CSV
    14. Plot sales by category
- Population:
    15. Create population CSV
    16. Plot population pie chart

    0. Exit 
    """
    )
# Main program execution
def main():
    option = True
    while option:
        print_menu()
        option = int(input("Enter option: "))
        if option == 0:
           continue

        os.system('cls' if os.name == 'nt' else 'clear')

        if option == 1:
          create_students_csv()
        elif option == 2:
          read_students_csv()
        elif option == 3:
          average_age = calculate_average_age()
          print("Average age:", average_age)
        elif option == 4:
          create_student_grades_chart()
        elif option == 5:
          create_sales_csv()
        elif option == 6:
          total_sales = calculate_total_sales()
          print("Total sales:", total_sales)
        elif option == 7:
          create_monthly_sales_chart()
        elif option == 8:
          merge_files_into_combined_csv()
        elif option == 9:
          read_combined_csv()
        elif option == 10:
          create_age_sales_scatter_plot()
        elif option == 11:
          create_temperatures_csv()
        elif option == 12:
          plot_temperatures()
        elif option == 13:
          create_sales_by_category_csv()
        elif option == 14:
          plot_sales_by_category()
        elif option == 15:
          create_population_csv()
        elif option == 16:
          plot_population_pie_chart()
        
        input("\nPress Enter to continue...")

if __name__ == '__main__':
    main()

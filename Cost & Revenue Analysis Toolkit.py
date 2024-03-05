import matplotlib.pyplot as plt
from tabulate import tabulate

# Global list to store calculation results
calculation_results = []

def store_calculation_result(calc_type, inputs, result):
    """
    Stores details of a calculation in the global list.
    """
    calculation_results.append({
        "Type": calc_type,
        "Inputs": inputs,
        "Result": result
    })

def calculate_marginal_cost(previous_total_cost, current_total_cost, previous_quantity, current_quantity):
    """
    Calculates and stores the marginal cost.
    """
    try:
        marginal_cost = round((current_total_cost - previous_total_cost) / (current_quantity - previous_quantity), 2)
        return marginal_cost
    except ZeroDivisionError:
        return "Error: Division by zero."

def calculate_average_cost(total_cost, quantity):
    """
    Calculates the average cost given the total cost and quantity.
    """
    try:
        return total_cost / quantity
    except ZeroDivisionError:
        return "Error: Division by zero."

def calculate_total_revenue(price, quantity):
    """
    Calculates the total revenue given the price per unit and quantity sold.
    """
    return price * quantity

def break_even_point(fixed_costs, price_per_unit, variable_cost_per_unit):
    """
    Calculates the break-even point given the fixed costs, price per unit, and variable cost per unit.
    """
    try:
        return fixed_costs / (price_per_unit - variable_cost_per_unit)
    except ZeroDivisionError:
        return "Error: Division by zero."

def prompt_for_marginal_cost():
    print("\nMarginal Cost Calculation")
    previous_total_cost = float(input("Enter previous total cost: "))
    current_total_cost = float(input("Enter current total cost: "))
    previous_quantity = float(input("Enter previous quantity produced: "))
    current_quantity = float(input("Enter current quantity produced: "))
    
    marginal_cost = calculate_marginal_cost(previous_total_cost, current_total_cost, previous_quantity, current_quantity)
    print(f"The marginal cost is: {marginal_cost}")

    # Store the result
    inputs = {
        "Previous Total Cost": previous_total_cost,
        "Current Total Cost": current_total_cost,
        "Previous Quantity": previous_quantity,
        "Current Quantity": current_quantity
    }
    store_calculation_result("Marginal Cost", inputs, marginal_cost)

def prompt_for_average_cost():
    print("\nAverage Cost Calculation")
    total_cost = float(input("Enter total cost: "))
    quantity = float(input("Enter quantity produced: "))
    
    average_cost = calculate_average_cost(total_cost, quantity)
    print(f"The average cost is: {average_cost}")

    # Store the result
    inputs = {"Total Cost": total_cost, "Quantity": quantity}
    store_calculation_result("Average Cost", inputs, average_cost)

def prompt_for_total_revenue():
    print("\nTotal Revenue Calculation")
    price = float(input("Enter price per unit: "))
    quantity = float(input("Enter quantity sold: "))
    
    total_revenue = calculate_total_revenue(price, quantity)
    print(f"The total revenue is: {total_revenue}")

    # Store the result
    inputs = {"Price Per Unit": price, "Quantity Sold": quantity}
    store_calculation_result("Total Revenue", inputs, total_revenue)

def prompt_for_break_even_analysis():
    print("\nBreak-even Analysis")
    fixed_costs = float(input("Enter total fixed costs: "))
    price_per_unit = float(input("Enter price per unit: "))
    variable_cost_per_unit = float(input("Enter variable cost per unit: "))
    
    break_even_quantity = break_even_point(fixed_costs, price_per_unit, variable_cost_per_unit)
    print(f"The break-even quantity is: {break_even_quantity} units.")

    # Store the result
    inputs = {
        "Fixed Costs": fixed_costs,
        "Price Per Unit": price_per_unit,
        "Variable Cost Per Unit": variable_cost_per_unit
    }
    store_calculation_result("Break-even Analysis", inputs, break_even_quantity)

def visualize_costs():
    marginal_costs = [result["Result"] for result in calculation_results if result["Type"] == "Marginal Cost" and isinstance(result["Result"], (int, float))]
    average_costs = [result["Result"] for result in calculation_results if result["Type"] == "Average Cost" and isinstance(result["Result"], (int, float))]
    
    # Assuming an equal number of data points for simplicity; adjust as necessary
    x = range(1, len(marginal_costs) + 1)
    
    plt.figure(figsize=(10, 6))
    plt.plot(x, marginal_costs, marker='o', linestyle='-', label='Marginal Cost')
    plt.plot(x, average_costs, marker='s', linestyle='--', label='Average Cost')
    plt.xlabel('Production Instance')
    plt.ylabel('Cost')
    plt.title('Cost Analysis Over Production')
    plt.legend()
    plt.grid(True)
    plt.show()

def visualize_revenue_and_break_even():
    total_revenues = [result["Result"] for result in calculation_results if result["Type"] == "Total Revenue" and isinstance(result["Result"], (int, float))]
    break_even_quantities = [result["Result"] for result in calculation_results if result["Type"] == "Break-even Analysis" and isinstance(result["Result"], (int, float))]
    
    # Assuming data for one break-even analysis; adjust logic as necessary for multiple
    break_even_point = break_even_quantities[0] if break_even_quantities else None
    
    x = range(1, len(total_revenues) + 1)
    
    plt.figure(figsize=(10, 6))
    plt.bar(x, total_revenues, label='Total Revenue')
    if break_even_point is not None:
        plt.axhline(y=break_even_point, color='r', linestyle='-', label='Break-even Point')
    plt.xlabel('Sales Instance')
    plt.ylabel('Revenue')
    plt.title('Total Revenue and Break-even Analysis')
    plt.legend()
    plt.grid(True)
    plt.show()

def generate_summary_report():
    """
    Generates a summary report of calculations, showing average, min, and max for each type.
    """
    summary = {}
    for result in calculation_results:
        calc_type = result["Type"]
        if calc_type not in summary:
            summary[calc_type] = {"values": []}
        summary[calc_type]["values"].append(result["Result"])
    
    for calc_type, data in summary.items():
        values = data["values"]
        avg = sum(values) / len(values) if values else 0
        summary[calc_type].update({"average": avg, "min": min(values), "max": max(values)})
    
    # Convert summary to a list of dictionaries for tabulate
    summary_list = [{"Type": k, "Average": v["average"], "Min": v["min"], "Max": v["max"]} for k, v in summary.items()]
    print(tabulate(summary_list, headers="keys", tablefmt="grid"))

def main_menu():
    """
    Updated main menu to include visualization and report generation options.
    """
    while True:
        print("\nEconomic Analysis Tool")
        print("1. Marginal Cost Calculation")
        print("2. Average Cost Calculation")
        print("3. Total Revenue Calculation")
        print("4. Break-even Analysis")
        print("5. Visualize Costs")
        print("5. Visualize Revenue")
        print("7. Generate Report")
        print("8. Exit")
        choice = input("Enter your choice: ")
        
        # Include calls to prompt functions for each calculation
        if choice == "1":
            prompt_for_marginal_cost()
        elif choice == "2":
            prompt_for_average_cost()
        elif choice == "3":
            prompt_for_total_revenue()
        elif choice == "4":
            prompt_for_break_even_analysis()
        elif choice == "5":
            visualize_costs()
        elif choice == "6":
            visualize_revenue_and_break_even()
        elif choice == "7":
            generate_summary_report()
        elif choice == "8":
            print("Exiting the application.")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main_menu()

import json
import matplotlib.pyplot as plt

def calculate_gdp(values):
    return values['C'] + values['G'] + values['I'] + values['NX']

def get_input(variable_name):
    while True:
        try:
            return float(input(f"Enter {variable_name}: "))
        except ValueError:
            print(f"Invalid input. Please enter a numeric value for {variable_name}.")

def plot_data(data, list_name):
    data_without_gdp = {k: v for k, v in data.items() if k != 'GDP'}
    labels = data_without_gdp.keys()
    values = data_without_gdp.values()
    plt.figure(figsize=(8, 8))
    plt.pie(values, labels=labels, autopct='%1.1f%%', startangle=140)
    plt.title(f'GDP Components for {list_name}')
    plt.show()

def plot_gdp_trend(user_lists):
    print("Lists available for GDP Trend visualization:")
    for i, list_name in enumerate(user_lists.keys(), 1):
        print(f"{i}. {list_name}")

    selected_list = int(input("Enter the number corresponding to the list you want to visualize: ")) - 1
    list_name = list(user_lists.keys())[selected_list]

    years = [year_data[0] for year_data in user_lists[list_name]]
    gdp_values = [year_data[1]['GDP'] for year_data in user_lists[list_name]]

    plt.figure(figsize=(10, 6))
    plt.plot(years, gdp_values, marker='o')
    plt.title(f'GDP Trend Over Years for List: {list_name}')
    plt.xlabel('Year')
    plt.ylabel('GDP')
    plt.grid(True)
    plt.show()

def plot_component_comparison(user_lists):
    print("Lists available for Component Comparison visualization:")
    for i, list_name in enumerate(user_lists.keys(), 1):
        print(f"{i}. {list_name}")

    selected_list = int(input("Enter the number corresponding to the list you want to visualize: ")) - 1
    list_name = list(user_lists.keys())[selected_list]

    components = ['C', 'G', 'I', 'NX']

    # Retrieve the selected list's data
    selected_data = user_lists[list_name]

    years = [year_data[0] for year_data in selected_data]
    n = len(years)  # Number of data points (years)
    width = 0.2  # Width of each bar

    fig, ax = plt.subplots()

    for i, component in enumerate(components):
        values = [year_data[1][component] for year_data in selected_data]
        # Calculate the position of each bar based on the component
        positions = [j - (width * n / 2) + width * i for j in range(len(values))]
        ax.bar(positions, values, width, label=component)

    ax.set_title(f'GDP Component Comparison Over Years for List: {list_name}')
    ax.set_xlabel('Years')
    ax.set_ylabel('Value')
    ax.set_xticks(range(len(years)))
    ax.set_xticklabels(years)
    ax.legend()

    plt.show()

    plt.show()

def plot_stacked_area_chart(user_lists):
    print("Lists available for Stacked Area Chart visualization:")
    for i, list_name in enumerate(user_lists.keys(), 1):
        print(f"{i}. {list_name}")

    selected_list = int(input("Enter the number corresponding to the list you want to visualize: ")) - 1
    list_name = list(user_lists.keys())[selected_list]

    components = ['C', 'G', 'I', 'NX']
    years = [year_data[0] for year_data in user_lists[list_name]]

    # Create a list of lists for each component's values over the years
    data = [[year_data[1][component] for year_data in user_lists[list_name]] for component in components]

    plt.figure(figsize=(10, 6))
    plt.stackplot(years, data, labels=components, alpha=0.8)
    plt.title(f'GDP Components Over Years for List: {list_name}')
    plt.xlabel('Year')
    plt.ylabel('Value')
    plt.legend(loc='upper left')
    plt.show()

def save_data(user_lists):
    with open('gdp_data.json', 'w') as file:
        json.dump(user_lists, file)
    print("Data saved successfully.")

def load_data():
    try:
        with open('gdp_data.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

def main():
    user_lists = load_data()
    years = []  # Variable to store years

    while True:
        print("\nGDP Calculator")
        print("1. Calculate GDP")
        print("2. Print lists")
        print("3. Save data")
        print("4. Load data")
        print("5. Plot GDP Trend")
        print("6. Plot Component Comparison")
        print("7. Plot Stacked Area Chart")
        print("8. Quit")
        choice = input("Enter the option (1-8): ")

        if choice == "1":
            year = input("Enter the year: ")  # Prompt for the year
            years.append(year)  # Add the year to the list

            user_list_name = input("Enter a name for your list: ")
            values = {'C': get_input('Consumption'), 'G': get_input('Government Spending'), 'I': get_input('Investments'), 'NX': get_input('Net Exports')}
            values['GDP'] = calculate_gdp(values)
            print(f"Calculated GDP: {values['GDP']}")

            if user_list_name not in user_lists:
                user_lists[user_list_name] = []  # Create an empty list for the given name if it doesn't exist
            user_lists[user_list_name].append((year, values))  # Append the data to the list

            print(f"List '{user_list_name}' updated with values for year {year}: {values}")

            plot_data(values, user_list_name) 

        elif choice == "2":
            if user_lists:
                print("\nLists created:")
                for list_name, data in user_lists.items():
                    print(f"List '{list_name}':")
                    for year, values in data:
                        print(f"Year: {year}, Values: {values}")
            else:
                print("No lists found.")

        elif choice == "3":
            save_data(user_lists)

        elif choice == "4":
            user_lists = load_data()
            print("Data loaded successfully.")

        elif choice == "5":
            plot_gdp_trend(user_lists)

        elif choice == "6":
            plot_component_comparison(user_lists) 
            
        elif choice == "7":
            plot_stacked_area_chart(user_lists)
            
        elif choice == "8":
            print("Exiting the GDP Calculator.")
            break
        else:
            print("Invalid option. Please choose a valid option (1/2/3/4/5/6/7/8).")

if __name__ == "__main__":
    main()


def handle_region_choice(choice, region_data):
    if choice=="1":
        region_data.display_population()
    elif choice=="2":
        region_data.population_comparison()
    elif choice=="3":
        region_data.population_sort()
    elif choice=="4":
        region_data.growth_calculator()
    elif choice=="5":
        region_data.growth_comparison()
    elif choice=="6":
        region_data.growth_sort()
        
def handle_continent_choice(choice, continent_data):
    if choice=="1":
        continent_data.display_population()
    elif choice=="2":
        continent_data.population_comparison()
    elif choice=="3":
        continent_data.population_sort()
    elif choice=="4":
        continent_data.growth_calculator()
    elif choice=="5":
        continent_data.growth_comparison()
    elif choice=="6":
        continent_data.growth_sort()
        
def select_area_type():
    while True:
        print("\nDo you want to work with regions or continents?")
        print("1. Regions")
        print("2. Continents")
        area_choice = input("Choose 1 or 2: ")
        if area_choice=="1":
            return "region"
        elif area_choice=="2":
            return "continent"
        else:
            print("Invalid choice. Please enter 1 or 2.")

def run_menu(region_data, continent_data):
    while True:
        print("""
        Main Menu:
        1. Display the population.
        2. Compare the population between two areas.
        3. Sort areas by population size.
        4. Calculate the annual growth rate.
        5. Compare the growth rate between two areas.
        6. Sort areas by growth rate.
        7. Exit
        """)
        choice = input("Choose an option (1-7): ")

        if choice in ["1", "2", "3", "4", "5", "6"]:
            area_type = select_area_type()
            if area_type=="region":
                handle_region_choice(choice, region_data)
            elif area_type=="continent":
                handle_continent_choice(choice, continent_data)
        elif choice=="7":
            print("Exiting program.")
            break
        else:
            print("Invalid option. Please try again.")
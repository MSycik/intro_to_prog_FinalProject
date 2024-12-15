import pandas as pd
from Regions import Region

class Continent(Region):
    
    def display_population(self):
        try:
            continent=input("Enter the continent: ")
            year=int(input("Enter the year: "))
            row=self.data[(self.data['Continent']==continent) & (self.data['Year']==year)]
            
            if not row.empty:
                print(f"Population of {continent} in {year} was {row['Population'].values[0]}")
            else:
                print(f"No data available for continent '{continent}' in year {year}. Please try again.")
           
        except ValueError:
            print("Invalid input. Please enter a valid year as an integer.")
    
    def population_comparison(self):
        try:
            continent1=input("Enter the first continent: ")
            continent2=input("Enter the second continent: ")
            year=int(input("Enter the year: "))
            
            row1=self.data[(self.data["Continent"]==continent1) & (self.data['Year']==year)]
            row2=self.data[(self.data["Continent"]==continent2) & (self.data['Year']==year)]
            
            if not (row1.empty and row2.empty):
                pop1=row1["Population"].values[0]
                pop2=row2["Population"].values[0]
                
                if pop1>pop2:
                    print(f"Population of {continent1} : {pop1} is higher than population of {continent2} : {pop2}")
                elif pop1<pop2:
                    print(f"Population of {continent2} : {pop2} is higher than population of {continent1} : {pop1}")
                else:
                    print(f"Population of {continent1} : {pop1} is the same population of {continent2} : {pop2}")
                        
            else:
                print(f"No data available for continent '{continent1} and {continent2}' in year {year}. Please try again.")
            
        except ValueError:
            print("Invalid input. Please enter a valid year as an integer.")
            
    def population_sort(self):
        try:
            year=int(input("Enter the year: "))
            year_rows=self.data[self.data["Year"]==year]
            if not year_rows.empty:
                rows_sorted = year_rows.sort_values(by='Population',ascending=False)
                print(f"Regions sorted by population in {year}:\n{rows_sorted[['Continent', 'Population']].reset_index(drop=True)}")
            else:
                print(f"No data available for year {year}. Please try again.")
                
        except ValueError:
            print("Invalid input. Please enter a valid year as an integer.")
        
    def growth_calculator(self):
        try:
            continent=input("Enter the continent: ")
            year=int(input("Enter the year: "))
            row=self.data[(self.data['Continent']==continent) & (self.data['Year']==year)]
            if not row.empty:
                print(f"Annual yearly growth for {continent} in {year} was: {row['Growth'].values[0]}")
            else:
                print(f"No data available for continent '{continent}' in year {year}. Please try again.")
    
        except ValueError:
            print("Invalid input. Please enter a valid year as an integer.")
        
    def growth_comparison(self):
        try:
            continent1=input("Enter the first continent: ")
            continent2=input("Enter the second continent: ")
            year=int(input("Enter the year: "))
            
            row1=self.data[(self.data["Continent"]==continent1) & (self.data['Year']==year)]
            row2=self.data[(self.data["Continent"]==continent2) & (self.data['Year']==year)]
            
            if not(row1.empty and row2.empty):
                grow1=row1["Growth"].values[0]
                grow2=row2["Growth"].values[0]

                if grow1>grow2:
                    print(f"Growth of {continent1} : {grow1} in {year} was higher than growth of {continent2} : {grow2}")
                elif grow1<grow2:
                    print(f"Growth of {continent2} : {grow2} in {year} was higher than growth of {continent1} : {grow1}")
                else:
                    print(f"Growth of {continent1} : {grow1} in {year} was the same growth of {continent2} : {grow2}")
            else:
                print(f"No data available for continent '{continent1} and {continent2}' in year {year}. Please try again.")
            
        except ValueError:
            print("Invalid input. Please enter a valid year as an integer.")
            
    def growth_sort(self):
        try:
            year=int(input("Enter the year: "))
            year_rows=self.data[self.data["Year"]==year]
            if not year_rows.empty:
                rows_sorted = year_rows.sort_values(by='Growth',ascending=False)
                print(f"Regions sorted by growth in {year}:\n{rows_sorted[['Continent', 'Growth']].reset_index(drop=True)}")
            else:
                print(f"No data available for year {year}. Please try again.")
                
        except ValueError:
            print("Invalid input. Please enter a valid year as an integer.")
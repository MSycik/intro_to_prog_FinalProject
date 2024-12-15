import pandas as pd

all_tables=pd.read_html("https://en.wikipedia.org/wiki/List_of_continents_and_continental_subregions_by_population")

#interesting tables: [3-27]
tables=all_tables[3::]

region_names=[
    "Eastern Africa",
    "Middle Africa",
    "Northern Africa",
    "Southern Africa",
    "Western Africa",
    "Total Africa",
    "Total Americas",
    "Caribbean",
    "Central America",
    "Northern America",
    "Total North America",
    "Total South America",
    "Central Asia",
    "Eastern Asia",
    "South-eastern Asia",
    "Southern Asia",
    "Western Asia",
    "Total Asia",
    "Eastern Europe",
    "Northern Europe",
    "Southern Europe",
    "Western Europe",
    "Total Europe",
    "Total Oceania",
    "Total World",
]

#Adding new column "Region" and filling it with region name:

for table, region in zip(tables, region_names):
    table['Region']=region
    
#CSV
for i in range(0,8):
    name=tables[0].iloc[i,0]  #take the name from the 1st column, for example: 1950,1960...
    extracted_rows=[]
    for table in tables:
        extracted_rows.append(table.iloc[i, :])
    new_table=pd.DataFrame(extracted_rows)
    new_table.to_csv(f'{name}.csv', index=False)
    
#Put every data into one clear table with attributes: |year|population|growth|region|
data=pd.concat(tables, ignore_index=True)

continents_names=[
    "Total Africa",
    "Total North America",
    "Total South America",
    "Total Asia",
    "Total Europe",
    "Total Oceania"
]

#Adding new column Continent and filling it with data:
data['Continent'] = None
data.loc[data['Region'].isin(continents_names), 'Continent'] = data['Region']

data.columns=["Year","Population","Growth","Region","Continent"]
data["Growth"]=data["Growth"].str.replace("+","")
data["Growth"]=data["Growth"].str.replace("-","")
data["Growth"]=data["Growth"].str.replace("%","")
data["Growth"]=data["Growth"].str.replace("—","0")
data["Growth"]=data["Growth"].str.replace("−","0")
data["Continent"]=data["Continent"].str.replace("Total ","")

data["Growth"] = data["Growth"].astype(float)
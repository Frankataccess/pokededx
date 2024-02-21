#~~~~~~~~~~~~~~~~~imports~~~~~~~~~~~~~~~~~~~~~~~~~~
import requests
import pandas as pd 
import tkinter 
#~~~~~~~~~~~~~~~~~~check API ~~~~~~~~~~~~~~~~~~~~~~~
#send HTTP GET request to the API endpoint
start_url = "https://pokeapi.co/api/v2/pokemon/"
response = requests.get(start_url)

#check if response was successful
if response.status_code == 200:
    print("Request successful!")
    #store response in a variable
    data = response.json
else :
    (print(f"ERROR: {response.status_code}"))

#~~~~~~~~~~~~~~~~~~pandas~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Create a sample dataframe
poketable= {'Username': [],
        'Password': [],
        'poke1': [],
        'poke2': [],
        'poke3': [],
        'poke4': [],
        'poke5': [],
        'poke6': []
        }
df = pd.DataFrame(poketable)

# Save the dataframe to a CSV file
df.to_csv('Biodata.csv', index=False)
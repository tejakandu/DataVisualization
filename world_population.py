import json

filename = 'population_data.json'

with open(filename) as f:
    pop_data = json.load(f)
# total = 0
for pop_dict in pop_data:
    if pop_dict['Year'] == '2010':
        country_name = pop_dict['Country Name']
        Population = int(float(pop_dict['Value']))
        print(country_name + ":" +str(Population))


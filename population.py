
def get_population(country):
    population_dict = {

        '2022': int(country["2022 Population"]),
        '2020': int(country["2020 Population"]),
        '2015': int(country["2015 Population"]),
        '2010': int(country["2010 Population"]),
        '2000': int(country["2000 Population"]),
        '1990': int(country["1990 Population"]),
        '1980': int(country["1980 Population"]),
        '1970': int(country["1970 Population"])
        
    }

    labels = population_dict.keys()
    values = population_dict.values()

    return labels, values

# Obten la información de los paquetes
# https://platzi.com/clases/7967-python-21-dias/63509-obten-la-informacion-de-los-paquetes/

from functools import reduce

def get_packages_info(packages):
    weights = [package[1] for package in packages]
    weights.append(0)
    countries = [package[2] for package in packages]

    country_output = {country: countries.count(country)
                        for country in countries }
    
    total_weight = 0 if len(weights) < 0 else reduce(lambda x, y: x + y , weights)

    return {
        "total_weight": round(total_weight, 2),
        "destinations": country_output
    }


my_list = [
    (1, 20, "Mexico"),
    (2, 15.5, "Colombia"),
    (3, 30, "Mexico"),
    (4, 12, "Argentina"),
    (5, 8.2, "Colombia"),
    (6, 25, "Mexico"),
    (7, 18.7, "Argentina"),
    (8, 5, "Colombia"),
    (9, 22.3, "Argentina"),
    (10, 14.8, "Colombia")
]

print(get_packages_info(my_list))

# {
#   "total_weight": 171.50,
#   "destinations": {
#     "Mexico": 3,
#     "Colombia": 4,
#     "Argentina": 3
#   }
# }
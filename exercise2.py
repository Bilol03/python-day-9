travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]


def add_new_country(country, visit, cities):
    new_visit = {}
    new_visit["country"] = country
    new_visit["visits"] = visit
    new_visit["cities"] = cities

    travel_log.append(new_visit)


add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)

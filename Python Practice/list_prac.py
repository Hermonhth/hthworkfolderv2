city_names = ["Oakland", "San Francisco", "Dalas", "Los Angeles", "Boston","New York"]
soccer_team_names = ["Chealsea", "Man United", "Man City", "Arsenal", "Everton"]
print(soccer_team_names[2])
print(city_names[1])
three_cities = city_names[0:3]
print(three_cities)
three_teams = soccer_team_names[0:3]
print(three_teams)
city_names[0]= "San Francisco"
city_names[5]= "Brooklyn"
city_names.append("New Jersey")
city_names.extend(["Chicago", "Santa Cruiz", "Washingtron"])
print(city_names)
del city_names[9]
city_names.remove("Santa Cruiz")
city_names.pop[2]

def check_all(list1):
    for element in list1:
        print(element)

    return "Done"

print (check_all(city_names))


def printCityNames():
    counter = 0
    while counter < len(city_names):
        print(city_names[counter])
        counter += 1
    return "completed"
    
printCityNames() 

def organize_cities(cities_list):
    for index in range(len(cities_list)-1):
        if cities_list[index] >= cities_list [index +1]:
         continue
    
        else: 
            city = cities_list[index]
            cities_list.pop[index]
            cities_list.append(city)
        return cities_list



print(organize_cities(city_names))
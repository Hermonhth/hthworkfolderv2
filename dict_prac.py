'''
Chicken $1.59
Beef $1.99
Cheese $1.00
Milk $2.50
'''

grocery_list = {
    "Chicken": 1.59,
    "Beef": 1.99,
    "Cheese": 1,
    "Milk": 2.5,
}
def total_price(item1,item2):
    price1 = grocery_list[item1]
    price2 = grocery_list[item2]
    total = price1 + price2

    return total    
print (total_price("Beef", "Cheese"))

def price_difference (item1, item2):
    price1 = grocery_list[item1]
    price2 = grocery_list[item2]
    dif = price1 - price2

    return dif


EPL_standings = {
    "Chealsea": 4,
    "Mancity": 1,
    "Manunited": 2,
    "Liverpool": 3,
}
chealsea_standing = EPL_standings["Chealsea"]
print(chealsea_standing)

EPL_standings ["Chealsea"]=7
print(chealsea_standing)

shoe_sales= {
"Jordan13": 1,
"Yeezy":8,
"Foamposite":10,
"Airmax":5,
"SB Dunk":20,
}

def restock(shoe_name, multiplier):
    newInv = shoe_sales[shoe_name] * multiplier
    shoe_sales[shoe_name] = newInv
    return shoe_sales

def clearance_sale(shoe_name, discount):
    newInv = shoe_sales[shoe_name] / discount
    shoe_sales[shoe_name] = newInv
    return shoe_sales




shoe_sales ["SB Dunk"] = 22
shoe_sales ["Yeezy"] =7
shoe_sales ["Jordan13"]+=7
shoe_sales ["Yeezy"]+=7
shoe_sales ["Foamposite"]+=7
shoe_sales ["Airmax"]+=7
shoe_sales ["SB Dunk"]+=7
shoe_sales ["Jordan13"]-=3
shoe_sales ["Yeezy"]-=3
shoe_sales ["Foamposite"]-=3
shoe_sales ["Airmax"]-=3
shoe_sales ["SB Dunk"]-=3
print(shoe_sales)


def point_difference (item1, item2):
    team1 = EPL_standings[item1]
    team2 = EPL_standings[item2]
    difference = team1 - team2

    return difference



spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    names_list=[]
    for i in range(0, len(spicy_foods)):
        name = spicy_foods[i]["name"]
        names_list.append(name)
    print(names_list)
    return names_list

get_names(spicy_foods)
    

def get_spiciest_foods(spicy_foods):
    spicyfood=[]
    for i in range(0,len(spicy_foods)):
        if(spicy_foods[i]["heat_level"] > 5):
            
            spicyfood.append(spicy_foods[i])
            print(spicy_foods[i])
            
    return spicyfood  
    
get_spiciest_foods(spicy_foods)

def print_spicy_foods(spicy_foods):
    for i in range(0,len(spicy_foods)):
        name = spicy_foods[i]["name"]
        cuisine = spicy_foods[i]["cuisine"]
        heat = spicy_foods[i]["heat_level"]
        emojis = "🌶" * heat
        print(f"{name} ({cuisine}) | Heat Level: {emojis}")
    return spicy_foods
print_spicy_foods(spicy_foods)

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for i in range(0,len(spicy_foods)):
        if(spicy_foods[i]["cuisine"] == cuisine):
            print(spicy_foods[i])
            return spicy_foods[i]

get_spicy_food_by_cuisine(spicy_foods, "American")

def print_spiciest_foods(spicy_foods):
    for i in range(0,len(spicy_foods)):
        if(spicy_foods[i]["heat_level"] > 5):
            name = spicy_foods[i]["name"]
            cuisine = spicy_foods[i]["cuisine"]
            heat = spicy_foods[i]["heat_level"]
            emojis = "🌶" * heat
            print(f"{name} ({cuisine}) | Heat Level: {emojis}")
print_spiciest_foods(spicy_foods)

def get_average_heat_level(spicy_foods):
    heat_level_list=[]
    for i in range(0,len(spicy_foods)):
        heat_levels = spicy_foods[i]["heat_level"]
        heat_level_list.append(heat_levels)
        
    average_heat_level= sum(heat_level_list)/len(heat_level_list)
    print(average_heat_level)
    
    return average_heat_level
        
get_average_heat_level(spicy_foods)

def create_spicy_food(spicy_foods, spicy_food):
    new_spicy_food = spicy_foods.copy()
    new_spicy_food.append(spicy_food)
    print (new_spicy_food)
    return new_spicy_food
create_spicy_food (spicy_foods, {
        'name': 'Griot',
        'cuisine': 'Haitian',
        'heat_level': 10,
    })
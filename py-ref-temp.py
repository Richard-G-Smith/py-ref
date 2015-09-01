# py-ref-temp Ver. 0.1
# A temporary location for info to be put into py-ref


# Print
print("HelloWorld")
howdy = "HelloWorld"
print(howdy)
print(howdy[3:6])

# Lists
movies = ["Iron Man", "Thor", "Captain America", "The Avengers"]

print(movies)
print(movies[2])
movies[1] = "Iron Man 2"
print(movies)
movies.append("Ant-Man")
print(movies)
print(len(movies))
print(movies[1:3])
print(movies[:2])
print(movies[2:])
print(movies.index("Captain America"))
print(movies)
movies.insert(1, "The Incredible Hulk")
print(movies)
movies.insert(3, "Thor")
print(movies)
movies.append("Captain Marvel")
print(movies)
movies.pop()
print(movies)

for x in movies:
    print(x)

# Dictionaries

heroes = {"Captain America" : "Steve Rogers", "Ant-Man" : "Scott Lang",
"Hulk" : "Bruce Banner"}
print(heroes["Ant-Man"])
print(heroes["Captain America"])
print(str(len(heroes)))
print(heroes)

villians = {}
villians["Red Skull"] = "Agent Smith"
print(villains)
villains["Yellow Jacket"] = "Guy from House of Cards"
villains["Ronan the Accuser"] = "Makup Dude"
print(villains)
del villains["Ronan the Accuser"]
print(villains)

villains.clear()
print(villains)

people = {
"Shield" : "Nick Fury",
"Steve Rogers" : ["Shield", "Serum", "Punch"],
"Hydra" : ["Henchmen", "Barons", "Red Skull", 2]
}

people["Others"] = ["Pepper", "Rhody", "Foggy"]

print(people)

people["Steve Rogers"].sort()
print(people["Steve Rogers"])

people["Steve Rogers"].remove("Punch")
print(people["Steve Rogers"])

print(people["Hydra"])
people["Hydra"].remove("Henchmen")
people["Hydra"].remove("Barons")
people["Hydra"].remove("Red Skull")
print(people["Hydra"])

# Functions

print(movies)

def movie_count(x):
    count = 0
    for item in x:
        if "Man" in item:
            print("He is Iron Man")
            count += 1
        else:
            print("He is not Iron Man")
    print(count)

movie_count(movies)

# Tuples - Basically a list that can not be changed

gold = (1, 2, 4, 8, "Lots")
print(gold)
print(gold[3])

#

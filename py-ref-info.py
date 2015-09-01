# py-ref-info Ver. 0.1


# Print
print("HelloWorld")
howdy = "HelloWorld"
print(howdy)
print(howdy[2:6])

# Lists
movies = ["Iron Man", "The Incredible Hulk", "Thor", "Captain America", "The Avengers",
          "Guardians of the Galaxy", "Ant-Man"]

print(movies)
print(movies[5])
movies[1] = "Iron Man 2"
print(movies)
movies.append("The Incredible Hulk")
print(movies)
print(len(movies))
print(movies[2:5])
print(movies[:3])
print(movies[4:])
print(movies.index("Thor"))
print(movies)
movies.insert(1, "The Incredible Hulk")
print(movies)
movies.pop(8)
print(movies)
movies.insert(9, "Captain Marvel")
print(movies)
movies.remove("Captain Marvel")

for x in movies:
    print(x)

# Dictionaries

heroes = {"Captain America" : "Steve Rogers", "Ant-Man" : "Scott Lang",
          "Hulk" : "Bruce Banner"}
print(heroes["Ant-Man"])
print(heroes["Captain America"])
print(str(len(heroes)))
print(heroes)
villains = {}
villains["Red Skull"] = "Agent Smith"
print(villains)
villains["Yellow Jacket"] = "Guy from House of Cards"
villains["Ronan the Accuser"] = "Makeup Dude"
print(villains)
del villains["Ronan the Accuser"]
print(villains)
villains["Yellow Jacket"] = "The Mayor"
print(villains)

villains.clear()
print(villains)

people = {
    "Shield" : "Nick Fury",
    "Steve Rogers" : ["Shield", "Serum", "Punch"],
    "Hydra" : ["Henchmen", "Barons", "Red Skull", 2]
}

people["Others"] = ["Pepper", "Rhody", "The Kid"]

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

# Tuples - Basically a list that can not be changed.

gold = (1, 2, 4, 8, "Lots")
print(gold)
print(gold[3])

# 

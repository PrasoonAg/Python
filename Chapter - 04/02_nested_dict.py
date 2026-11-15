#=========================================================================#
# 02 - Nested_Dictionary
#=========================================================================#
# Nested Dictionary
# A dictionary inside another dictionary.
student = {
    "name": "Prason Agrawal",
    "subjects": {
        "phy": 95,
        "chem": 100,
        "math": 99,
    }
}
print(student["subjects"])
print(student["subjects"]["phy"])

#=========================================================================#
# Accessing List inside Dictionary
# A dictionary can have a list as its value.

travel_log = {
    "France": ["Paris", "Lille", "Dijon"],
    "Germany": ["Stuttgart", "Berlin"]
}
print(travel_log["France"][0])

lis = [1,2,3,4,5,6,7,8,9]
print(lis[2])

#=========================================================================#
# Accessing Dictionary inside Dictionary
# A dictionary can contain another dictionary as its value.

travel_log = {
    "France": {
        "cities_visited": ["Paris", "Lille", "Dijon"],
        "total_vists": 12
    },
    "Germany": {
        "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
        "total_vists": 5
    },
}
print(travel_log["France"]["cities_visited"][0])
#=========================================================================#
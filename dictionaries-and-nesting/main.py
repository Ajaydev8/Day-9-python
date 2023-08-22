programming_dictionaries = {
    "Bug": "An error in program that prevents the program running as expected.",
    "Function": "A piece of code that you can easily call over and over again.",
    "Loop": "A process that repeats over and over again on a condition.",
}

# Retrieving items from dictionary.
# print(programming_dictionaries["Bug"])
#
# # Adding new items to dictionary
# programming_dictionaries["Software"] = "Software gives the instruction to hardware how to operate."
#
# print(programming_dictionaries["Software"])
#
# print("  ")
#
# print(programming_dictionaries)
#
# # Wipe an existing dictionary
# programming_dictionaries = {}
# print(programming_dictionaries)

# Loop through a dictionary
# for key in programming_dictionaries:
#     print(programming_dictionaries[key])

# Nesting

Capitals = {
    "France": "Paris",
    "Germany": "Berlin",
}

# Nesting a List in a dictionary

travel_log = {
    "France": ["Paris", "Lille", "Dijon"],
    "Germany": ["Berlin", "Hamburg", "Stuttgart"],
}

# Nesting dictionary in dictionary

travel_log_2 = {
    "France": {"cities_visited": ["Paris", "Lille", "Dijon"], "total_visits": 12},
    "Germany": {"cities_visited": ["Berlin", "Hamburg", "Stuttgart"], "total_visits": 10}
}

# Nesting a dictionary inside a List.

travel_log_2 = [
    {
        "country": "France",
        "cities_visited": ["Paris", "Lille", "Dijon"],
        "total_visits": 12},
    {
        "country": "Germany"
        , "cities_visited": ["Berlin", "Hamburg", "Stuttgart"]
        , "total_visits": 10}
]
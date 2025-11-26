"""Write a Python program to sort the following list of dictionaries by the key name:"""

users = [
    {"name": "Alok", "age": 25},
    {"name": "Rahul", "age": 30},
    {"name": "Priya", "age": 28}
]

def sort_list(users):

    users.sort(key = lambda x: x['name'])

    return users

print(sort_list(users))

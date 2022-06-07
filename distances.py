import csv
from HashTable import HashTable

# O(1)
with open('data/distance_table.csv') as file:
    distances = list(csv.reader(file, delimiter=','))

# O(1)
with open('data/target_hubs.csv') as file:
    targets = list(csv.reader(file, delimiter=','))

distance_map = HashTable(len(distances))


# O(m+n)
def check_key(key_to_check):
    if "South" in key_to_check and "East" in key_to_check:
        key_to_check = key_to_check.replace("South", "S")
        key_to_check = key_to_check.replace("East", "E")
    elif "South" in key_to_check and "West" in key_to_check:
        key_to_check = key_to_check.replace("South", "S")
        key_to_check = key_to_check.replace("West", "W")
    elif "North" in key_to_check and "West" in key_to_check:
        key_to_check = key_to_check.replace("North", "N")
        key_to_check = key_to_check.replace("West", "W")
    elif "North" in key_to_check and "East" in key_to_check:
        key_to_check = key_to_check.replace("North", "N")
        key_to_check = key_to_check.replace("East", "E")
    elif "South" in key_to_check:
        key_to_check = key_to_check.replace("South", "S")
    elif "West" in key_to_check:
        key_to_check = key_to_check.replace("West", "W")
    elif "East" in key_to_check:
        key_to_check = key_to_check.replace("East", "E")
    elif "North" in key_to_check:
        key_to_check = key_to_check.replace("North", "N")
    else:
        key_to_check = distances[i][1].split('\n')[0].strip()

    return key_to_check


# O(n)
for i in range(len(distances)):
    key = distances[i][1].split('\n')[0].strip()
    key = check_key(key)
    val = distances[i]
    distance_map.add(key, val)


# O(n)
def return_position(check_position):
    for j in range(1, distance_map.size + 2):
        if distance_map.get(check_position)[j] == "0":
            return j


# O(1)
def get_distance_map():
    return distance_map


# O(1)
def get_distance(current_key, target_key):
    current_index = return_position(current_key)
    target_index = return_position(target_key)
    if target_index > current_index:
        return distance_map.get(target_key)[current_index]
    else:
        return distance_map.get(current_key)[target_index]

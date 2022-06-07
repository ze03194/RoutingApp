import datetime
import time

import load_packages, distances
from datetime import timedelta

CAN_ONLY_BE = "Can only be on truck 2"
DELAYED = "Delayed on flight"
WRONG_ADDRESS = "Wrong address"
MUST_BE_WITH = "Must be delivered with"
TEN_30AM = "10:30 AM"
NINE_AM = "9:00 AM"
EOD = "EOD"

first_delivery_truck = load_packages.get_first_delivery_truck()
second_delivery_truck = load_packages.get_second_delivery_truck()
third_delivery_truck = load_packages.get_third_delivery_truck()

distance_map = distances.get_distance_map()
package_map = load_packages.get_packages_map()
total_miles = float(0)
truck_one_miles = float(0)
truck_two_miles = float(0)
truck_three_miles = float(0)
first_truck_current_location = "HUB"
second_truck_current_location = "HUB"
third_truck_current_location = "HUB"
miles_per_minute = float(18 / 60)
minutes_traveled = 0

first_truck_start_time = datetime.timedelta() + timedelta(hours=9, minutes=10)
first_truck_current_time = first_truck_start_time
second_truck_start_time = datetime.timedelta() + timedelta(hours=8, minutes=0)
second_truck_current_time = second_truck_start_time
third_truck_start_time = datetime.timedelta() + timedelta(hours=11, minutes=30)
third_truck_current_time = third_truck_start_time



def bubble_sort(sort_distances, sort_packages):
    for i in range(len(sort_distances) - 1, 0, -1):
        for j in range(i):
            if sort_distances[j] > sort_distances[j + 1]:
                temp_distance = sort_distances[j]
                temp_package = sort_packages[j]
                sort_distances[j] = sort_distances[j + 1]
                sort_packages[j] = sort_packages[j + 1]
                sort_distances[j + 1] = temp_distance
                sort_packages[j + 1] = temp_package
    return sort_packages


def filter_by_distance(packages, truck_current_location):
    filtered_distances = []
    for i in range(len(packages)):
        current_package = packages[i]
        target_location = current_package[1].strip()
        distance_to_travel = float(distances.get_distance(truck_current_location, target_location))
        filtered_distances.append(distance_to_travel)

    return bubble_sort(filtered_distances, packages)


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
        return key_to_check

    return key_to_check


first_nine_am_packages = []
first_ten_30_packages = []
first_eod_packages = []
second_nine_am_packages = []
second_ten_30_packages = []
second_eod_packages = []
third_nine_am_packages = []
third_ten_30_packages = []
third_eod_packages = []


def split_packages(delivery_truck, nine_am_packages, ten_30_packages, eod_packages):
    for i in range(len(delivery_truck)):
        second_key = delivery_truck[i][1].strip()
        second_key = check_key(second_key)
        current_package = delivery_truck[i]
        current_package[1] = second_key
        package_map.get(current_package[0])[8] = "Status: In Transit"

        if NINE_AM in current_package[5]:
            nine_am_packages.append(current_package)
        if TEN_30AM in current_package[5]:
            ten_30_packages.append(current_package)
        if EOD in current_package[5]:
            eod_packages.append(current_package)
        if WRONG_ADDRESS in current_package[7]:
            current_package[1] = "410 S State St"
            current_package[4] = "84111"
            current_package[7] = "Address Corrected"


split_packages(second_delivery_truck, second_nine_am_packages, second_ten_30_packages, second_eod_packages)
split_packages(first_delivery_truck, first_nine_am_packages, first_ten_30_packages, first_eod_packages)
split_packages(third_delivery_truck, third_nine_am_packages, third_ten_30_packages, third_eod_packages)


def deliver_first_packages(packages):
    global first_truck_current_location, total_miles, first_truck_current_time, package_map, truck_one_miles
    global total_miles
    filtered_packages = filter_by_distance(packages, first_truck_current_location)
    while len(filtered_packages) > 0:
        current_package = filtered_packages[0]
        target_location = current_package[1].strip()
        distance_to_travel = float(distances.get_distance(first_truck_current_location, target_location))
        time_to_travel = int(distance_to_travel / miles_per_minute)
        first_truck_current_location = target_location
        total_miles += distance_to_travel
        truck_one_miles += distance_to_travel
        package_map.get(current_package[0])[8] = "Status: Delivered"
        first_truck_current_time += timedelta(minutes=time_to_travel)
        package_map.get(current_package[0]).append("Delivered at " + str(first_truck_current_time))
        filtered_packages.pop(0)
        deliver_first_packages(filtered_packages)


def deliver_second_packages(packages):
    global second_truck_current_location, total_miles, second_truck_current_time, package_map, truck_two_miles
    global total_miles
    filtered_packages = filter_by_distance(packages, second_truck_current_location)
    while len(filtered_packages) > 0:
        current_package = filtered_packages[0]
        target_location = current_package[1].strip()
        distance_to_travel = float(distances.get_distance(second_truck_current_location, target_location))
        time_to_travel = int(distance_to_travel / miles_per_minute)
        second_truck_current_location = target_location
        total_miles += distance_to_travel
        truck_two_miles += distance_to_travel
        package_map.get(current_package[0])[8] = "Status: Delivered"
        second_truck_current_time += timedelta(minutes=time_to_travel)
        package_map.get(current_package[0]).append("Delivered at " + str(second_truck_current_time))
        filtered_packages.pop(0)
        deliver_second_packages(filtered_packages)


def deliver_third_packages(packages):
    global third_truck_current_location, total_miles, third_truck_current_time, package_map, truck_three_miles
    global total_miles
    filtered_packages = filter_by_distance(packages, third_truck_current_location)
    while len(filtered_packages) > 0:
        current_package = filtered_packages[0]
        target_location = current_package[1].strip()
        distance_to_travel = float(distances.get_distance(third_truck_current_location, target_location))
        time_to_travel = int(distance_to_travel / miles_per_minute)
        third_truck_current_location = target_location
        total_miles += distance_to_travel
        truck_three_miles += distance_to_travel
        package_map.get(current_package[0])[8] = "Status: Delivered"
        third_truck_current_time += timedelta(minutes=time_to_travel)
        package_map.get(current_package[0]).append("Delivered at " + str(third_truck_current_time))
        filtered_packages.pop(0)
        deliver_third_packages(filtered_packages)


# O(1)
def first_start_delivery():
    deliver_first_packages(first_nine_am_packages)
    deliver_first_packages(first_ten_30_packages)
    deliver_first_packages(first_eod_packages)


# O(1)
def second_start_delivery():
    deliver_second_packages(second_nine_am_packages)
    deliver_second_packages(second_ten_30_packages)
    deliver_second_packages(second_eod_packages)


# O(1)
def third_start_delivery():
    deliver_third_packages(third_nine_am_packages)
    deliver_third_packages(third_ten_30_packages)
    deliver_third_packages(third_eod_packages)


first_start_delivery()
second_start_delivery()
third_start_delivery()

target_location = "HUB"
distance_to_travel = float(distances.get_distance(first_truck_current_location, target_location))
time_to_travel = int(distance_to_travel / miles_per_minute)
first_truck_current_location = target_location
total_miles += distance_to_travel
truck_one_miles += distance_to_travel
first_truck_current_time += timedelta(minutes=time_to_travel)


# O(1)
def return_total_miles():
    return total_miles

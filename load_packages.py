import csv
import distances

from HashTable import HashTable

CAN_ONLY_BE = "Can only be on truck 2"
DELAYED = "Delayed on flight"
WRONG_ADDRESS = "Wrong address"
MUST_BE_WITH = "Must be delivered with"
TEN_30AM = "10:30 AM"
NINE_AM = "9:00 AM"
EOD = "EOD"

first_delivery_truck = []
second_delivery_truck = []
third_delivery_truck = []
at_hub = []

packages_map = HashTable(40)

# O(1)
with open('data/package_table.csv') as file:
    packages = list(csv.reader(file, delimiter=','))

# O(n)
for i in range(len(packages)):
    key = packages[i][0]
    val = packages[i]
    val.append("Status: At Hub")
    packages_map.add(key, val)

# O(m + n)
for i in range(1, packages_map.size + 1):
    column_seven_data = packages_map.get(str(i))[7]
    column_five_data = packages_map.get(str(i))[5]
    size_of_first_truck = len(first_delivery_truck)
    size_of_second_truck = len(second_delivery_truck)
    row_data = packages_map.get(str(i))

    # O(n)
    if MUST_BE_WITH in column_seven_data and size_of_second_truck < 16:
        second_delivery_truck.append(row_data)
        start = MUST_BE_WITH.find("h") + 2
        end = len(column_seven_data)
        first_required_packageID = column_seven_data[start:end].split(', ')[0]
        second_required_packageID = column_seven_data[start:end].split(', ')[1]
        first_required_package = packages_map.get(first_required_packageID)
        second_required_package = packages_map.get(second_required_packageID)

        # O(n)
        if first_required_package in first_delivery_truck or first_required_package in third_delivery_truck or \
                first_required_package in second_delivery_truck:
            if first_required_package in first_delivery_truck:
                first_delivery_truck.remove(first_required_package)
            elif first_required_package in third_delivery_truck:
                third_delivery_truck.remove(first_required_package)
            else:
                continue
            second_delivery_truck.append(first_required_package)
        else:
            second_delivery_truck.append(first_required_package)

        # O(m + n)
        if second_required_package in first_delivery_truck or second_required_package in third_delivery_truck or \
                second_required_package in second_delivery_truck:
            if second_required_package in first_delivery_truck:
                first_delivery_truck.remove(second_required_package)
            elif second_required_package in third_delivery_truck:
                third_delivery_truck.remove(second_required_package)
            else:
                continue
            second_delivery_truck.append(second_required_package)
        else:
            second_delivery_truck.append(second_required_package)

    # O(m + n)
    if TEN_30AM in column_five_data and row_data not in first_delivery_truck and row_data not in \
            second_delivery_truck and row_data not in third_delivery_truck and size_of_second_truck < 16:
        second_delivery_truck.append(row_data)
    elif size_of_second_truck == 16:
        first_delivery_truck.append(row_data)

    # O(n)
    if CAN_ONLY_BE in column_seven_data:
        second_delivery_truck.append(row_data)

    # O(n)
    if DELAYED in column_seven_data and TEN_30AM in column_five_data:
        check_for_packages(row_data, second_delivery_truck, third_delivery_truck, first_delivery_truck)

    # O(n)
    if DELAYED in column_seven_data and EOD in column_five_data:
        check_for_packages(row_data, first_delivery_truck, second_delivery_truck, third_delivery_truck)

    # O(n)
    if WRONG_ADDRESS in column_seven_data:
        check_for_packages(row_data, first_delivery_truck, second_delivery_truck, third_delivery_truck)

    # O(n)
    if row_data not in first_delivery_truck and row_data not in second_delivery_truck and row_data not in third_delivery_truck and size_of_first_truck < 13:
        first_delivery_truck.append(row_data)

    # O(n)
    if row_data not in first_delivery_truck and row_data not in second_delivery_truck and row_data not in third_delivery_truck:
        third_delivery_truck.append(row_data)


    # O(m+n)
    def check_for_packages(package_data, check_truck_one, check_truck_two, add_to_truck):
        # O(m+n)
        if package_data in check_truck_one or package_data in check_truck_two or package_data in add_to_truck:
            if package_data in check_truck_one:
                check_truck_one.remove(package_data)
            elif package_data in check_truck_two:
                check_truck_two.remove(package_data)
            else:
                return
            add_to_truck.append(package_data)
        else:
            add_to_truck.append(package_data)


    # O(1)
    def get_packages_map():
        return packages_map


    # O(1)
    def get_first_delivery_truck():
        return first_delivery_truck


    # O(1)
    def get_second_delivery_truck():
        return second_delivery_truck


    # O(1)
    def get_third_delivery_truck():
        return third_delivery_truck


    # O(1)
    def set_package_status(package_id):
        packages_map.get(str(package_id))

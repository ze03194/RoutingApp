
import sys
from datetime import timedelta


import load_packages
import distances
import deliver_packages

package_map = load_packages.get_packages_map()
distance_map = distances.get_distance_map()


# O(1)
def look_up_package(package_id, package_time):
    hour = int(package_time.split(":")[0])
    minute = int(package_time.split(":")[1])

    if timedelta(hours=int(package_map.get(package_id)[9][13:-3].split(":")[0]),
                 minutes=int(package_map.get(package_id)[9][13:-3].split(":")[1])) > timedelta(hours=hour,
                                                                                               minutes=minute):
        temp = package_map.get(package_id)[9]
        package_map.get(package_id)[9] = ""
        package_map.get(package_id)[8] = "Status: In Transit"
    print(package_map.get(package_id))
    package_map.get(package_id)[9] = temp

    return


# O(n)
def display_all_packages(given_time):
    hour = int(given_time.split(":")[0])
    minute = int(given_time.split(":")[1])

    # O(n)
    for i in range(1, package_map.size + 1):
        temp = package_map.get(str(i))[9]
        if timedelta(hours=int(package_map.get(str(i))[9][13:-3].split(":")[0]),
                     minutes=int(package_map.get(str(i))[9][13:-3].split(":")[1])) > timedelta(hours=hour,
                                                                                               minutes=minute):
            package_map.get(str(i))[9] = ""
            package_map.get(str(i))[8] = "Status: In Transit"

        print(package_map.get(str(i)))
        package_map.get(str(i))[9] = temp
        package_map.get(str(i))[8] = "Status: In Transit"

    return


# O(n)
def prompt_user():
    print("---------------------------------------------------------------")
    print("\t\t\tWGUPS Package Management System")
    print("---------------------------------------------------------------")
    print("The total miles driven: %.2f" % deliver_packages.total_miles)
    print("\n1. Lookup a package")
    print("2. Display all packages")
    print("3. Exit")
    print("\nTruck 1 traveled: %.2f" % deliver_packages.truck_one_miles)
    print("Truck 2 traveled: %.2f" % deliver_packages.truck_two_miles)
    print("Truck 3 traveled: %.2f" % deliver_packages.truck_three_miles)


selection = "1"
# O(n)
while selection != "3":
    prompt_user()
    selection = input("\nSelect an option above: ")
    match selection:
        case "1":
            look_up_package(package_id=input("\nEnter Package ID: "),
                            package_time=input("Enter a time (HH:MM) Format: "))
        case "2":
            display_all_packages(given_time=input("Enter a time (HH:MM) Format: "))

        case "3":
            print("Bye..")
            sys.exit()



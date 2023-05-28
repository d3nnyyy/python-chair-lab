"""
A module that demonstrates the usage of the ChairManager class.
"""

from ua.lviv.iot.algo.part1.lab7.chairs.feeding_table import FeedingTable
from ua.lviv.iot.algo.part1.lab7.chairs.gaming_chair import GamingChair
from ua.lviv.iot.algo.part1.lab7.chairs.office_chair import OfficeChair
from ua.lviv.iot.algo.part1.lab7.chairs.recliner_chair import ReclinerChair
from ua.lviv.iot.algo.part1.lab7.manager.chair_manager import ChairManager
from ua.lviv.iot.algo.part1.lab7.manager.set_manager import SetManager

if __name__ == "__main__":

    manager = ChairManager()
    feeding_table1 = FeedingTable(40, "Wood", 0.8, 2)
    feeding_table2 = FeedingTable(20, "Plastic", 0.6, 3)

    office_chair1 = OfficeChair(150, "Steel", 90, True)
    office_chair2 = OfficeChair(130, "Leather", 100, False)

    gaming_chair1 = GamingChair(120, "Plastic", 1.5, True)
    gaming_chair2 = GamingChair(140, "Metal", 1.6, True)

    recliner_chair1 = ReclinerChair(200, "Leather", 120, True)
    recliner_chair2 = ReclinerChair(180, "Fabric", 100, False)

    manager.add_chair(feeding_table1)
    manager.add_chair(feeding_table2)
    manager.add_chair(office_chair1)
    manager.add_chair(office_chair2)
    manager.add_chair(gaming_chair1)
    manager.add_chair(gaming_chair2)
    manager.add_chair(recliner_chair1)
    manager.add_chair(recliner_chair2)

    print("All chairs:\n")
    for chair in manager.chairs:
        print(chair)

    chairs_with_max_weight_more_than = manager.find_chair_with_max_weight_more_than(150)
    chairs_with_certain_material = manager.find_chair_by_material("Leather")

    print("\nChairs with max weight more than:\n")
    for chair in chairs_with_max_weight_more_than:
        print(chair)

    print("\nChairs with certain material:\n")
    for chair in chairs_with_certain_material:
        print(chair)

    print(f"\nThere are {len(manager)} chairs in the manager.")
    print("\nThe first chair in the manager is:")
    print(manager.chairs[0])

    print("\nIterating through the manager:\n")
    chairs_iter = iter(manager)
    while True:
        try:
            print(next(chairs_iter))
        except StopIteration:
            break

    print("\nResults of adjust position functions:\n")
    print(manager.get_results_of_adjust_position_functions())

    print("\nEnumerating chairs:\n")
    enumerated_chairs = manager.enumerate_chairs()
    for chair in enumerated_chairs:
        print(chair)

    print("\nZipping the chair with the results of the adjust position functions:\n")
    zipped_chairs = manager.zip_object_and_results_of_adjust_position_functions()
    for chair in zipped_chairs:
        print(chair)

    print("\nChairs dictionary:\n")
    print(manager.get_chairs_dict())

    print("\nGetting attributes by type:\n")
    print(office_chair1.get_attributes_by_type(bool))
    print(gaming_chair1.get_attributes_by_type(float))

    print("\nIf any chair is made of material: \n")
    print(manager.if_any_chair_is_made_of_material("Wood"))

    print("\nIf all chairs have max weight more than: \n")
    print(manager.if_all_chairs_have_max_weight_more_than(200))

    set_manager = SetManager(manager.chairs)

    print(len(set_manager))

    manager.execute_pylint()

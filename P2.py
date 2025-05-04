class SetOperations:
    def __init__(self):
        self.setA = []
        self.setB = []
        self.setC = []

    def add_element(self, target_set, element):
        if target_set == 'A':
            self.setA.append(element)
        else:
            self.setB.append(element)

    def remove_element(self, target_set, element):
        target = self.setA if target_set == 'A' else self.setB
        if element in target:
            target.remove(element)

    def contains_element(self, target_set, element):
        target = self.setA if target_set == 'A' else self.setB
        print(f"{element} found" if element in target else f"{element} not found")

    def size(self, target_set):
        return len(self.setA) if target_set == 'A' else len(self.setB)

    def display_set(self, target_set):
        target = self.setA if target_set == 'A' else self.setB
        print("{", ", ".join(str(x) for x in target), "}")

    def set_intersection(self):
        self.setC = [x for x in self.setA if x in self.setB]
        print("\nIntersection:", "{", ", ".join(str(x) for x in self.setC), "}")

    def set_union(self):
        self.setC = self.setA[:]
        self.setC.extend(x for x in self.setB if x not in self.setA)
        print("\nUnion:", "{", ", ".join(str(x) for x in self.setC), "}")

    def set_difference(self):
        self.setC = [x for x in self.setA if x not in self.setB]
        print("\nDifference A - B:", "{", ", ".join(str(x) for x in self.setC), "}")

c1 = SetOperations()

while True:
    print("\n*******SET OPERATIONS*******")
    print("1. Add Element\n2. Remove Element\n3. Check Element\n4. Set Size\n5. Display Sets\n6. Intersection\n7. Union\n8. Difference\n9. Exit")
    choice1 = int(input("Enter Your Choice: "))

    if choice1 == 9:
        break

    elif choice1 in [1, 2, 3, 4]:
        set_choice = input("Choose Set (A/B): ").strip().upper()
        if set_choice not in ['A', 'B']:
            print("Invalid set!")
            continue

    if choice1 == 1:
        num = int(input("Enter number to add: "))
        c1.add_element(set_choice, num)

    elif choice1 == 2:
        num = int(input("Enter number to remove: "))
        c1.remove_element(set_choice, num)

    elif choice1 == 3:
        num = int(input("Enter number to check: "))
        c1.contains_element(set_choice, num)

    elif choice1 == 4:
        print(f"Size of Set {set_choice}: {c1.size(set_choice)}")

    elif choice1 == 5:
        print("Set A: ", end="")
        c1.display_set('A')
        print("Set B: ", end="")
        c1.display_set('B')

    elif choice1 == 6:
        c1.set_intersection()

    elif choice1 == 7:
        c1.set_union()

    elif choice1 == 8:
        c1.set_difference()

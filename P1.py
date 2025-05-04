class CollusionHandling:
    def __init__(self):
        self.linearHash = []
        self.quadraticHash = []
        self.linearCount = 0
        self.quadraticCount = 0
        self.bucketSize = 0

    def create_bucket(self, bsize):
        self.bucketSize = bsize
        self.linearHash = [None] * bsize
        self.quadraticHash = [None] * bsize

    def has_key(self, key):
        return key % self.bucketSize

    def linear_Probing(self, name, phoneNo):
        pos = self.has_key(phoneNo)
        if self.linearHash[pos] is None:
            self.linearHash[pos] = {name: phoneNo}
            return pos
        index = (pos + 1) % self.bucketSize
        while index != pos:
            if self.linearHash[index] is None:
                self.linearHash[index] = {name: phoneNo}
                return index
            index = (index + 1) % self.bucketSize
        return -1

    def search_key_Linear_prob(self, phoneNo):
        self.linearCount = 0
        pos = self.has_key(phoneNo)
        index = pos
        while self.linearCount < self.bucketSize:
            self.linearCount += 1
            entry = self.linearHash[index]
            if entry and phoneNo in entry.values():
                print(f"Phone number found at position {index}")
                break
            index = (index + 1) % self.bucketSize
        else:
            print("Phone number not found")
        print(f"Records searched: {self.linearCount}")

    def display_Linear_Hash_Table(self):
        for i, item in enumerate(self.linearHash):
            print(i, item)

    def quadratic_Probing(self, name, phoneNo):
        pos = self.has_key(phoneNo)
        if self.quadraticHash[pos] is None:
            self.quadraticHash[pos] = {name: phoneNo}
            return pos
        i = 1
        while i < self.bucketSize:
            index = (pos + i * i) % self.bucketSize
            if self.quadraticHash[index] is None:
                self.quadraticHash[index] = {name: phoneNo}
                return index
            i += 1
        return -1

    def search_key_quadratic_prob(self, phoneNo):
        self.quadraticCount = 0
        pos = self.has_key(phoneNo)
        i = 0
        while self.quadraticCount < self.bucketSize:
            index = (pos + i * i) % self.bucketSize
            self.quadraticCount += 1
            entry = self.quadraticHash[index]
            if entry and phoneNo in entry.values():
                print(f"Phone number found at position {index}")
                break
            i += 1
        else:
            print("Phone number not found")
        print(f"Records searched: {self.quadraticCount}")

    def display_quadratic_Hash_Table(self):
        for i, item in enumerate(self.quadraticHash):
            print(i, item)


# Driver Code
c1 = CollusionHandling()
bsize = int(input("Enter the Size of hash table: "))
c1.create_bucket(bsize)

while True:
    print("\n1. Linear Probing\n2. Quadratic Probing\n3. Exit")
    choice = int(input("Enter Choice: "))
    if choice == 3:
        break

    while True:
        if choice == 1:
            print("\n1. Add Record\n2. Display Table\n3. Search\n4. Back")
            sub_choice = int(input("Enter Choice: "))
            if sub_choice == 4:
                break
            elif sub_choice == 1:
                name = input("Name: ")
                phoneNo = int(input("Phone No: "))
                if c1.linear_Probing(name, phoneNo) == -1:
                    print("Table Full!")
            elif sub_choice == 2:
                c1.display_Linear_Hash_Table()
            elif sub_choice == 3:
                phoneNo = int(input("Phone No to search: "))
                c1.search_key_Linear_prob(phoneNo)

        elif choice == 2:
            print("\n1. Add Record\n2. Display Table\n3. Search\n4. Back")
            sub_choice = int(input("Enter Choice: "))
            if sub_choice == 4:
                break
            elif sub_choice == 1:
                name = input("Name: ")
                phoneNo = int(input("Phone No: "))
                if c1.quadratic_Probing(name, phoneNo) == -1:
                    print("Table Full!")
            elif sub_choice == 2:
                c1.display_quadratic_Hash_Table()
            elif sub_choice == 3:
                phoneNo = int(input("Phone No to search: "))
                c1.search_key_quadratic_prob(phoneNo)

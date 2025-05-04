import queue

class HospitalQueue:
    def __init__(self):
        self.pq = queue.PriorityQueue()

    def add_patient(self, priority, patient_name):
        self.pq.put((priority, patient_name))

    def serve_patient(self):
        if not self.pq.empty():
            priority, patient_name = self.pq.get()
            priority_dict = {1: "Serious", 2: "Non-serious", 3: "General Checkup"}
            print(f"Serving {patient_name} (Priority: {priority_dict[priority]})")
        else:
            print("No patients in the queue.")

    def display_queue(self):
        print("\nCurrent Queue (Priority -> Patient):")
        temp_queue = list(self.pq.queue)
        for priority, patient_name in sorted(temp_queue):
            priority_dict = {1: "Serious", 2: "Non-serious", 3: "General Checkup"}
            print(f"Priority {priority_dict[priority]}: {patient_name}")

# Driver code
hospital_queue = HospitalQueue()

while True:
    print("\n--- Hospital Priority Queue ---")
    print("1. Add Patient")
    print("2. Serve Patient")
    print("3. Display Queue")
    print("4. Exit")
    
    choice = int(input("Enter your choice: "))

    if choice == 1:
        patient_name = input("Enter patient name: ")
        print("Enter priority:")
        print("1. Serious")
        print("2. Non-serious")
        print("3. General Checkup")
        priority = int(input("Enter priority (1, 2, or 3): "))
        hospital_queue.add_patient(priority, patient_name)

    elif choice == 2:
        hospital_queue.serve_patient()

    elif choice == 3:
        hospital_queue.display_queue()

    elif choice == 4:
        print("Exiting the hospital system.")
        break

    else:
        print("Invalid choice.")

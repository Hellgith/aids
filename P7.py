class Graph:
    def __init__(self):
        self.adjMatrix = []
        self.cityIndex = {}
        self.cities = []

    def addFlight(self, city1, city2, cost):
        if city1 not in self.cityIndex:
            self.cityIndex[city1] = len(self.cities)
            self.cities.append(city1)
            for row in self.adjMatrix:
                row.append(0)
            self.adjMatrix.append([0] * len(self.cities))

        if city2 not in self.cityIndex:
            self.cityIndex[city2] = len(self.cities)
            self.cities.append(city2)
            for row in self.adjMatrix:
                row.append(0)
            self.adjMatrix.append([0] * len(self.cities))

        u, v = self.cityIndex[city1], self.cityIndex[city2]
        self.adjMatrix[u][v] = self.adjMatrix[v][u] = cost

    def displayMatrix(self):
        print("Adjacency Matrix (Flight Costs):")
        print("        ", end="")
        for city in self.cities:
            print(f"{city:10}", end=" ")
        print()

        for i in range(len(self.cities)):
            print(f"{self.cities[i]:<10}", end=" ")
            for j in range(len(self.cities)):
                print(f"{self.adjMatrix[i][j]:<10}", end=" ")
            print()


# Main function
if __name__ == "__main__":
    flightNetwork = Graph()

    # Adding flight paths
    flightNetwork.addFlight("Pune", "Mumbai", 100)
    flightNetwork.addFlight("Pune", "Bangalore", 300)
    flightNetwork.addFlight("Mumbai", "Bangalore", 200)
    flightNetwork.addFlight("Mumbai", "Hyderabad", 150)
    flightNetwork.addFlight("Bangalore", "Hyderabad", 250)
    flightNetwork.addFlight("Ahemadabad", "Pune", 180)
    flightNetwork.addFlight("Ahemadabad", "Mumbai", 160)

    # Display matrix
    flightNetwork.displayMatrix()

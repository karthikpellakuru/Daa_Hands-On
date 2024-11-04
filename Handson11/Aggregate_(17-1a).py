class DynamicTable:
    def __init__(self):
        self.capacity = 1 
        self.elements = [None] * self.capacity
        self.num_elements = 0

    def insert(self, item):
        if self.num_elements == self.capacity:
            self.resize(self.capacity * 2)
        self.elements[self.num_elements] = item
        self.num_elements += 1

    def resize(self, new_capacity):
        new_elements = [None] * new_capacity
        for i in range(self.num_elements):
            new_elements[i] = self.elements[i]
        self.elements = new_elements
        self.capacity = new_capacity

    def aggregate_amortized_runtime(self, n):
        total_cost = 0
        for i in range(n):
            if self.num_elements == self.capacity:
                total_cost += self.capacity
                self.resize(self.capacity * 2)
            total_cost += 1 
            self.num_elements += 1
        return total_cost / n

dynamic_table = DynamicTable()
n = 100
aggregate_amortized = dynamic_table.aggregate_amortized_runtime(n)

print("Amortized runtime using aggregate method:", aggregate_amortized)

________________________OUTPUT_____________________________
Amortized runtime using aggregate method: 2.27

Process finished with exit code 0

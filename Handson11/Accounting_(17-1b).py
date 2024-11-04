class DynamicTable:
    def __init__(self):
        self.size = 1
        self.elements = [None] * self.size
        self.num_elements = 0

    def insert(self, item):
        if self.num_elements == self.size:
            self.resize(self.size * 2)

        self.elements[self.num_elements] = item
        self.num_elements += 1

    def resize(self, new_size):
        new_elements = [None] * new_size
        for i in range(self.num_elements):
            new_elements[i] = self.elements[i]
        self.elements = new_elements
        self.size = new_size

    def accounting_amortized_runtime(self, n):
        total_cost = 0
        for i in range(n):
            if self.num_elements == self.size:
                total_cost += self.size
                self.resize(self.size * 2)
            total_cost += 2 
            self.num_elements += 1
        return total_cost / n

table = DynamicTable()
num_insertions = 1000 
amortized_runtime = table.accounting_amortized_runtime(num_insertions)

print("Amortized runtime using accounting method:", amortized_runtime)

--------------------------OUTPUT----------------------------------
Amortized runtime using accounting method: 3.023

Process finished with exit code 0

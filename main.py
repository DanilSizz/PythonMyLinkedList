class Slivik:

    def __init__(self):

        self.size = 0

        self.first_element = None
        self.last_element = None

    class Node:

        def __init__(self, value):

            self.value = value
            self.next = None
    
    def append(self, value):

        new_node = self.Node(value)

        if self.first_element is None:
            self.first_element = new_node
            self.last_element = new_node

        else:
            self.last_element.next = new_node
            self.last_element = new_node
        
        self.size += 1
    
    def get_value(self, index):

        if index < 0 or index >= self.size:
            raise IndexError("Index out of range")

        
        current_elem = self.first_element
        for _ in range(0, index):
            current_elem = current_elem.next

        return current_elem.value

    def sort(self, myarray):

        current = self.first_element
        lis1 = Slivik()
        lis2 = Slivik()


        for _ in range(self.size):
            if current.next != None:
                if current > current.next:
                    pass



    def __str__(self):

        element = []
        current = self.first_element

        while current:
            element.append(current.value)
            current = current.next
        return "[" + ', '.join(str(e) for e in element) + "]"

    def __len__(self):
        return self.size

myarray = Slivik()

myarray.append('хелоу воролд')

print(myarray)
print(myarray.get_value(1))
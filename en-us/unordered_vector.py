import numpy as np
import random as rnd


class UnorderedVector:
    def __init__(self, size: int):
        self.size = size
        self.last_index = -1
        self.values = np.empty(self.size, dtype=int)


    def __is_empty(self) -> bool:
        return self.last_index == -1


    def __maximum_capacity_reached(self) -> bool:
        return self.last_index == self.size - 1


    def __str__(self) -> str:
        if self.__is_empty():
            return 'The vector is empty'
        else:
            message = ''
            for index in range(self.last_index + 1):
                message += f"Index={index}; Value={self.values[index]}\n"
            return message


    def insert(self, value: int):
        if self.__maximum_capacity_reached():
            print('Maximum capacity reached')
        else:
            self.last_index += 1
            self.values[self.last_index] = value


    def search(self, value: int) -> int:
        for index in range(self.last_index + 1):
            if value == self.values[index]:
                return index
        return -1


    def remove(self, value: int) -> int:
        index = self.search(value)
        if index == -1:
            return -1
        else:
            for i in range(index, self.last_index):
                self.values[i] = self.values[i + 1]
            self.last_index -= 1
            return index


if __name__ == "__main__":
    size = int(input('Which is the size of vector that you want? '))
    vector = UnorderedVector(size)

    # Test insert method
    for value in range(size):
        vector.insert(rnd.randint(1,100))
        print(vector)

    # Test search method
    keep_going = 1
    while keep_going > 0:
        value_to_search= int(input('Type one number to search in vector: '))
        keep_going = vector.search(value_to_search)

    # Test remove method
    vector.remove(int(input('Which value you\'ll want to remove?')))
    print(vector)
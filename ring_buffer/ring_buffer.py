from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        if self.storage.length is self.capacity:
            self.current = 0
            self.storage.remove_from_tail()
        self.storage.add_to_tail(item)

        return True

    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []

        # TODO: Your code here
        for x in range(0, self.storage.length):
            y = self.storage.remove_from_head()
            list_buffer_contents.append(y)
            print(list_buffer_contents)

        return list_buffer_contents

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass

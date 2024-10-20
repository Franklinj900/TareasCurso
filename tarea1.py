class Dequeue:
    def __init__(self):
        self.deque = []
    def is_empty(self):
        return None if self.deque else True
    def add_first(self, item):
        self.deque.insert(0, item)
    def add_last(self, item):
        self.deque.append(item)
    def remove_first(self):
        if self.is_empty():
            return None
        else:
            return self.deque.pop(0)
    def remove_last(self):
        if self.is_empty():
            return None
        else:
            return self.deque.pop()


lista = Dequeue()
lista.add_first("Banana")
lista.add_first("Apple")
lista.add_first("Tomato")
lista.remove_first()
lista.add_first("Strawberry")
lista.add_last("Grapes")
lista.remove_first()
lista.remove_last()
print(lista.deque)
from typing import List, Any


class Shelf:
    def __init__(self):
        self.__stacks: List[List[Any]] = []

    def place_item_on(self, item, thing):
        if thing is self:
            self.__stacks.append([item])
            return
        for stack in self.__stacks:
            if thing == stack[-1]:
                stack.append(item)
                return
        return f'{thing} is not in the shelf'

    def remove_item(self, item):
        for stack in self.__stacks:
            if item == stack[-1]:
                stack.pop()
                if not stack:
                    self.__stacks.remove(stack)
                return
        return f'{item} is not in the shelf'

    def __str__(self):
        res = ''
        for stack in self.__stacks:
            res += ' on '.join(stack[::-1]) + '\n'
        return res


class LUD:
    def __init__(self, capacity):
        self.__capacity = capacity
        self.__dict = {}
        self.__id_generator = 0

    def get_value(self, key):
        if key not in self.__dict:
            raise KeyError(f'{key} is not in the dictionary')
        times, _id, val = self.__dict[key]
        self.__dict[key] = times + 1, _id, val
        return val

    def put(self, key, value):
        if key in self.__dict:
            times, _id, val = self.__dict[key]
            self.__dict[key] = times, _id,  value
            return
        if len(self.__dict) == self.__capacity:
            _min = min(self.__dict, key=lambda x: self.__dict[x][:2])
            self.__dict.pop(_min)
        self.__id_generator += 1
        self.__dict[key] = 0, self.__id_generator, value


class Message:
    def __init__(self, text, log):
        self.text = text
        self.log = log

    def copy(self):
        return Message(self.text, self.log)

    def add(self, more):
        self.text += more
        self.log.append(more)
        return self


msg1 = Message("", []).add("A")
msg2 = msg1.copy().add("B")
print(msg1.text, msg1.log, msg2.text, msg2.log)


class A:
    def __init__(self, im):
        self.im = im

    def inv(self):
        self.im = -self.im
        return self

    def add(self, other):
        self.im += other.im
        return self

    def copy(self):
        return A(self.im)

    def print(self):
        print(self.im, end=',')
        return self


a = A(9)
a.print().add(a).print().copy().add(a.inv()).print()

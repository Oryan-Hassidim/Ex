class SortedDict(object):
    _keys = []
    _values = {}

    def set(self, key, value):
        setted = False
        for i, _key in enumerate(self._keys):
            if _key == key:
                setted = True
                break
            if _key > key:
                self._keys.insert(i, key)
                setted = True
                break
        if not setted:
            self._keys.append(key)
        self._values[key] = value

    def get(self, key, defualt=None):
        return self._values.get(key, defualt)

    def remove(self, key):
        self._keys.remove(key)
        del self._values[key]

    def clear(self):
        self._keys.clear()
        self._values.clear()

    def __len__(self):
        return len(self._keys)

    def __iter__(self):
        return iter(self._keys)

    def add(self, key, value):
        self.set(key, self.get(key, []) + [value])

    def keys(self):
        return self._keys.copy()

    def items(self):
        return [(key, self._values[key]) for key in self._keys]

    def __class_getitem__(self, key):
        return self._values[key]

    def __str__(self):
        result = "{"
        result += ', '.join(map(lambda x: str(x) + ": " + str(self._values[x]), self._keys))
        result += "}"
        return result

s = SortedDict()
print(s)
s.add('a', 1)
print(s)
s.add('c', 3)
print(s)
s.add('a', 4)
print(s)
s.add('b', 2)
print(s)
print(s)
print(s)

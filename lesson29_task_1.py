BLANK = object()

class HashTable:
    def __init__(self, capacity):
        self.values = capacity * [BLANK]

    def __len__(self):
        return len(self.values)

    def __setitem__(self, key, value):
        if self.values[self._index(key)] is BLANK:
            self.values[self._index(key)] = (key, value)
        else:
            next_index = (self._index(key) + 1) % len(self.values)
            while next_index != self._index(key) and self.values[next_index] is not BLANK:
                next_index = (next_index + 1) % len(self.values)
            if next_index == self._index(key):
                raise IndexError("Not have enough space")
            else:
                self.values[next_index] = (key, value)

    def __getitem__(self, key):
        if self.values[self._index(key)] is BLANK:
            raise KeyError(key)
        elif self.values[self._index(key)][0] == key:
            return self.values[self._index(key)][1]
        else:
            next_index = (self._index(key) + 1) % len(self.values)
            while next_index != self._index(key) and self.values[next_index] is not BLANK:
                if self.values[next_index][0] == key:
                    return self.values[next_index][1]
                else:
                    next_index = (next_index + 1) % len(self.values)
            raise KeyError(key)

    def __delitem__(self, key):
        if self.values[self._index(key)] is BLANK:
            raise KeyError(key)
        elif self.values[self._index(key)][0] == key:
            self.values[self._index(key)] = BLANK
        else:
            next_index = (self._index(key) + 1) % len(self.values)
            while next_index != self._index(key) and self.values[next_index] is not BLANK:
                if self.values[next_index][0] == key:
                    self.values[next_index] = BLANK
                    return
                else:
                    next_index = (next_index + 1) % len(self.values)
            raise KeyError(key)

    def _index(self, key):
        return hash(key) % len(self)

    def get(self, key, default=None):
        try:
            return self[key]
        except KeyError:
            return default

if __name__ == "__main__":
    ht = HashTable(10)

    ht['a'] = 4
    ht['b'] = 7
    ht['c'] = 10
    ht['d'] = 13
    ht['e'] = 16
    ht['f'] = 19
    ht['g'] = 22
    ht['h'] = 25
    ht['i'] = 28
    ht['j'] = 31
    # ht['k'] = 34
    print(ht.get('f'))
    print(ht.get('h'))
    # print(ht.get('w'))
    print(ht.values)
    ht.__delitem__('b')
    print(ht.values)

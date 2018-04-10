class MemorizingDict(dict):
    history = []

    def set(self, key,value):
        self.history.append(key)
        self[key] = value

    def get_history(self):
        return self.history

d = MemorizingDict({'foo': 42})
print(d)
d.set('baz', 100500)
print(d)
print(d.get_history())
print(d)
d = MemorizingDict()
d.set('boo', 500100)
print(d.get_history())


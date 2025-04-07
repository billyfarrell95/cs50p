class Jar:
    def __init__(self, capacity=12):
        if not capacity >= 0:
            raise ValueError("Must be greater than 0")
        self.capacity = capacity
        self.cookies = 0

    def __str__(self):
        return "🍪" * self.cookies

    def deposit(self, n):
        if (self.capacity - self.cookies) >= n:
            self.cookies += n
        else:
            raise ValueError("Cookie jar is full!")

    def withdraw(self, n):
        if self.cookies >= n:
            self.cookies -= n
        else:
            raise ValueError(f"Not enough cookies to take {n}")

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        self._capacity = capacity

    @property
    def size(self):
        return self.cookies

    @size.setter
    def size(self, size):
        if not size:
            raise ValueError("Missing size")
        self._size = size

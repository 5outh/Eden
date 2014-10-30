class Identity:
    def __init__(self, value):
        self.value = value

    def empty(self):
        """
        An empty `Identity` is a wrapper around its value's `empty`
        iff its value is also a monoid.
        Identity a
        """
        return Identity(self.value.empty())

    def concat(self, identity):
        """
        Concatenate two `Identity`s iff their values are concatenable
        Identity a -> Identity a -> Identity a
        """
        return Identity(self.value.concat(identity.value))

    def map(self, f):
        """
        Identity a -> (a -> b) -> Identity b
        """
        return Identity(f(self.value))

    def apply(self, identity):
        """
        Assumes that self.value is a function
        Identity (a -> b) -> Identity a -> Identity b
        """
        return Identity(self.value (identity.value))

    @staticmethod
    def of(value):
        """
        `of` is a static method in order to differentiate between other implementations
        a -> Identity a
        """
        return Identity(value)

    def chain(self, f):
        """
        Identity a -> (a -> Identity b) -> Identity b
        """
        return f(self.value)

    def extend(self, f):
        """
        Identity a -> (Identity a -> b) -> Identity b
        """
        return Identity(f(self))

    def extract(self):
        """
        Identity a -> a
        """
        return self.value

from abc import ABCMeta, abstractmethod

class Semigroup(metaclass=ABCMeta):
    @abstractmethod
    def concat(self, semigroup):
        pass

class Monoid(Semigroup):
    @abstractmethod
    def empty(self):
        pass

class Functor(metaclass=ABCMeta):
    @abstractmethod
    def map(self, f):
        pass

class Apply(Functor):
    @abstractmethod
    def apply(self, f):
        pass

class Applicative(Apply):
    @staticmethod
    @abstractmethod
    def of(value):
        pass

class Chain(Apply):
    @abstractmethod
    def chain(self, f):
        pass

class Monad(Chain, Applicative):
    pass

class Extend(metaclass=ABCMeta):
    @abstractmethod
    def extend(self, f):
        pass

class Comonad(Functor, Extend):
    @abstractmethod
    def extract(self):
        pass

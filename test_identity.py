from identity import Identity

print( Identity(2).map(lambda x: x**3).extract() )
print( Identity(lambda x: x**3).apply(Identity(2)).extract() )
print( Identity.of(8).extract() )
print( Identity.of(2).chain(lambda x: Identity(x**3)).extract() )

class AdditiveGroup:
    def __init__(self, value):
        self.value = value

    def empty(self):
        return AdditiveGroup(0)

    def concat(self, group):
        return AdditiveGroup(self.value + group.value)

    def extract(self):
        return self.value

print ( Identity(AdditiveGroup(0)).empty().concat(Identity(AdditiveGroup(8))).extract().extract() )

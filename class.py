class Animal:
    def init(self, name, sound):
        self._name = name
        self._sound = sound

    def name(self):
        return self._name

    def sound(self):
        return self._sound

class Dog(Animal):
    def init(self, name):
        super().init(name, "Woof!")


class Cat(Animal):
    def init(self, name):
        super().init(name, "Meow!")


class Cow(Animal):
    def init(self, name):
        super().init(name, "Moo!")
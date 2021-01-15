from abc import ABC, abstractmethod


class Shmotki:
    def __init__(self):
        pass
    total = 0

    @abstractmethod
    def podschet(self):
        pass


class Coat(Shmotki):
    def __init__(self, weidth):
        super().__init__()
        self.w = weidth

    @property
    def podschet(self):
        result = self.w / 6.5 + 0.5
        Shmotki.total += result
        return f"объем ткани на пальто {result}"


class Suit(Shmotki):
    def __init__(self, height):
        super().__init__()
        self.h = height

    @property
    def podschet(self):
        result = 2 * self.h + 0.3
        Shmotki.total += result
        return f"обьем ткани на костюм = {result}"


palto = Coat(2)
print(palto.podschet)
suit = Suit(3)
print(suit.podschet)
print(Shmotki.total)

from abc import ABC, abstractmethod

class AbstractClothes(ABC):
    @property
    @abstractmethod
    def tissue_required(self):
        pass

    @property
    @abstractmethod
    def measuring(self):
        pass

    @abstractmethod
    def _calc_tissue_required(self):
        pass


class Clothes(AbstractClothes):
    _clothes = []

    def __init__(self, measuring):
        self._measuring = measuring
        self._tissue_required = None
        self._clothes.append(self)

    def _calc_tissue_required(self):
        raise NotImplemented

    @property
    def tissue_required(self) -> float:
        if not self._tissue_required:
            self._calc_tissue_required()

        return self._tissue_required

    @property
    def measuring(self):
        return self._measuring

    @measuring.setter
    def measuring(self, measuring):
        self._measuring = measuring
        self._tissue_required = None

    @property
    def total_tissue_required(self):
        return f'{sum([item.tissue_required for item in self._clothes])} кв.м'


class Coat(Clothes):
    def _calc_tissue_required(self):
        self._tissue_required = round(self.measuring / 6.5 + 0.5, 2)

    @property
    def V(self):
        return self.measuring

    def __str__(self):
        return f"Для пошива пальто {self.measuring} размера " \
               f"требуется {self.tissue_required} кв. метров ткани"


class Suit(Clothes):
    def _calc_tissue_required(self):
        self._tissue_required = round(2 * self.measuring * 0.01 + 0.3, 2)

    @property
    def H(self):
        return self.measuring


    def __str__(self):
        return f"Для пошива костюма на рост {self.measuring} см. " \
               f"требуется {self.tissue_required} кв. метров ткани"



coat = Coat(5)

print(coat)

suit = Suit(178)
print(suit)


print(coat.total_tissue_required)
print(suit.total_tissue_required)

class Item:
    def __init__(self, value, prev=None):
        self.value = value
        self.next = None
        self.prev = prev

    def __str__(self):
        return str(self.value)


class RunningMediane:
    def __init__(self):
        self.__list = None
        self.__left_border = None
        self.__right_border = None
        self.__mediane = None
        self.__len = 0

    def __str__(self):
        pointer = self.__list
        s = ''

        while pointer is not None:
            s += str(pointer.value) + ' '
            pointer = pointer.next

        return s

    def __add(self, value):
        if self.__list is None:
            self.__list = Item(value)
            self.__mediane = self.__list
            return 0

        pointer = self.__list
        move = -1
        while pointer is not None:
            if value > pointer.value:
                item = Item(pointer.value, pointer)
                item.next = pointer.next
                if pointer.next is not None:
                    pointer.next.prev = item

                pointer.value = value
                pointer.next = item

                return 0 if pointer == self.__mediane else move

            if pointer == self.__mediane:
                move = 1

            if pointer.next is None:
                pointer.next = Item(value, pointer)
                break

            pointer = pointer.next

        return move

    def add(self, value):
        move_increment = self.__add(value)
        self.__len += 1

        if self.__len == 1:
            return self

        odd = self.__len % 2 != 0
        if odd and move_increment >= 0:
            self.__mediane = self.__mediane.next
        if not odd and move_increment < 0:
            self.__mediane = self.__mediane.prev

        return self

    @staticmethod
    def scale(f):
        return int(f * 10) / 10

    def calculate(self):
        if self.__len == 0:
            return 0

        if self.__len % 2 == 0:
            return RunningMediane.scale(self.__mediane.value + self.__mediane.next.value) / 2

        return RunningMediane.scale(self.__mediane.value)

    @staticmethod
    def test_it():
        mediane = RunningMediane()
        mediane.add(1)
        mediane.add(7)
        mediane.add(3)
        mediane.add(14)
        print(mediane)

        assert 1.0 == RunningMediane.scale(1)
        assert 1.5 == RunningMediane.scale(1.567)

        mediane = RunningMediane()
        assert 0 == mediane.calculate()
        assert 12 == mediane.add(12).calculate()
        assert 8.0 == mediane.add(4).calculate()
        assert 5.0 == mediane.add(5).calculate()
        assert 4.5 == mediane.add(3).calculate()
        assert 5.0 == mediane.add(8).calculate()
        assert 6.0 == mediane.add(7).calculate()

        mediane = RunningMediane()
        assert 1 == mediane.add(1).calculate()
        assert 1.5 == mediane.add(2).calculate()
        assert 2 == mediane.add(3).calculate()
        assert 2.5 == mediane.add(4).calculate()
        assert 3 == mediane.add(5).calculate()
        assert 3.5 == mediane.add(6).calculate()
        assert 4 == mediane.add(7).calculate()
        assert 4.5 == mediane.add(8).calculate()
        assert 5 == mediane.add(9).calculate()
        assert 5.5 == mediane.add(10).calculate()


RunningMediane.test_it()

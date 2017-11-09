class ContactNode:
    def __init__(self):
        self.count = 1
        self.next = {}


class Contacts:
    def __init__(self):
        self.__contacts = {}

    def add(self, contact):
        current_level = self.__contacts
        for ch in contact:
            if ch in current_level:
                current_level[ch].count += 1
            else:
                current_level[ch] = ContactNode()

            current_level = current_level[ch].next

    def find_partial(self, contact):
        current_level = self.__contacts
        count = 0
        for ch in contact:
            if ch in current_level:
                count = current_level[ch].count
            else:
                return 0
            current_level = current_level[ch].next

        return count

    @staticmethod
    def test_it():
        contacts = Contacts()
        contacts.add('some')
        contacts.add('so')
        assert 1 == contacts.find_partial('some')
        assert 2 == contacts.find_partial('s')
        assert 0 == contacts.find_partial('something')
        assert 0 == contacts.find_partial('else')

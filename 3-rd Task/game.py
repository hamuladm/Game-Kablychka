'''
3-rd Task
'''


class Room:
    def __init__(self, room, linked_rooms = {}) -> None:
        self.room = room
        self.linked_rooms = linked_rooms
        self.description = None
        self.item = None
        self.character = None

    def set_description(self, description):
        self.description = description

    def link_room(self, room: object, direction):
        self.linked_rooms[direction] = room

    def set_item(self, item):
        self.item = item

    def set_character(self, character: object):
        self.character = character

    def get_details(self):

        print(self.description)

        for direction in self.linked_rooms:
            room = self.linked_rooms[direction]
            print(f'The {room.get_room()} is {direction}')

    def move(self, direction):
        if direction in self.linked_rooms:
            return self.linked_rooms[direction]
        else:
            print('You can not go that way!')
            return self

    def get_room(self):
        return self.room

    def get_item(self):
        return self.item

    def get_character(self):
        return self.character


class Enemy:
    def __init__(self, enemy, description, defeated = 0) -> None:
        self.enemy = enemy
        self.description = description
        self.defeated = defeated
        self.conversation = None
        self.weakness = None

    def set_conversation(self, conversation):
        self.conversation = conversation

    def set_weakness(self, weakness):
        self.weakness = weakness

    def fight(self, weakness):
        if weakness == self.weakness:
            print(f'You fend {self.enemy} off with the {weakness}')
            self.defeated += 1
            return True
        else:
            print(f'{self.enemy} crushes you, puny adventurer')
            return False

    def talk(self):
        print(self.conversation)

    def get_defeated(self):
        return self.defeated
    
    def describe(self):
        print(self.description)


class Item:
    def __init__(self, item) -> None:
        self.item = item
        self.description = None
        self.weakness = None

    def set_description(self, description):
        self.description = description

    def set_weakness(self, weakness):
        self.weakness = weakness

    def get_name(self):
        return self.item

    def describe(self):
        print(self.description)

class Room():
    def __init__(self, name, description, items=None, exits=None):
        self.name = name
        self.description = description
        self.items = items or []
        self.exits = exits or {}

class Item():
    def __init__(self, name, description):
        self.name = name
        self.description = description

class Game():
    def __init__(self, rooms, current_room="home", inventory=None):
        self.rooms = rooms
        self.current_room = current_room
        self.inventory = inventory or []

    def move(self, direction):
        room_name = self.current_room
        current_room = self.rooms[room_name]
        if direction in current_room.exits:
            self.current_room = current_room.exits[direction]
            return {"type": "move", "description": self.rooms[self.current_room].description}
        else:
            return {"type": "error", "message": "You can't go that way."}
        
    def take_item(self, item_name):
        current_room = self.rooms[self.current_room]
        for item in current_room.items:
            if item.name.lower() == item_name:
                self.inventory.append(item)
                current_room.items.remove(item)
                return {"type": "take", "message": f"You picked up {item.name}."}
        return {"type": "error", "message": "No item that matches."}
        
    def examine(self):
        current_room = self.rooms[self.current_room]

        return {
            "type": "look", 
            "description": f'{current_room.name}\n{current_room.description}',
            "items": [item.name for item in current_room.items],
            "exits": list(current_room.exits.keys())
        }

        









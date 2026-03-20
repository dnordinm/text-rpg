from game import Room, Item

pick = Item("pick", "A rusty pickaxe, could be useful.")
straw = Item("straw", "A pile of dirty straw.")
apple = Item("apple", "A fresh red apple.")

home = Room("Home", "You wake up in your home. A single room with a bed in the corner and a small dinner table with last night's dishes still sitting there.", [pick, straw, apple], {"east": "town"})
town = Room("Town", "You walk outside. To the North is a black smith. To the South is a cook. To the West is a path leading to the forest. To the East is your home.", [], {"south": "cook", "north": "black_smith", "east": "home", "west": "forest"})
black_smith = Room("Black_Smith", "A portly man walks up to the counter. \"The name's Bruber. What can I do for 'ya?\"", [], {"south": "town"})

rooms = {
    "home": home,
    "town": town,
    "black_smith": black_smith,
}
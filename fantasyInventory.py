stuff = {"rope": 1, "torch": 6, "gold coin": 42, "dagger": 1, "arrow": 12}
dragonLoot = ["gold coin", "dagger", "gold coin", "gold coin", "ruby"]


def displayInventory(inventory):
    print("Inventory:")
    item_total = 0
    for k, v in inventory.items():
        print(str(v) + " - " + k)
        item_total += v
    print("Total number of items: " + str(item_total))


def addToInventory(inventory, loots):
    inv = inventory
    for loot in loots:
        if loot in inv:
            inv[loot] += 1
        else:
            inv[loot] = 1
    return inv


displayInventory(stuff)
stuff = addToInventory(stuff, dragonLoot)
displayInventory(stuff)

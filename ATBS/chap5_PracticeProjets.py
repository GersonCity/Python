# Fantasy Game Inventory

stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}


def displayInventory(inventory):
    print("Inventory:")
    item_total = 0
    for k, v in inventory.items():
        item_total = item_total + v
        print(str(v) + ' ' + k)
    print("Total number of items: " + str(item_total))


# displayInventory(stuff)


def addToInventory(inventory, addedItems):
    # item = addedItems
    # while True:
    #     if item in inventory:
    #         print(item)
    #     else:
    #         print(item)

    # print(addedItems)
    # for k, v in list(inventory.items()):
        # print(k, v)
    for k in addedItems:
        print(k)
        # if k in addedItems:
        #     print(k)
        #     # item = v + 1
        #     # inv[str(k)] = item
        # else:
        #     new_item = 1
        # inventory[addedItems] = new_item
    # return inventory, addedItems


inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = addToInventory(inv, dragonLoot)
# displayInventory(inv)
print(inv)

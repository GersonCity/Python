# Fantasy Game Inventory

stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}


def displayInventory(inventory):
    print("Inventory:")
    item_total = 0
    # print(inventory)
    for k, v in inventory.items():
        item_total = item_total + v
        print(str(v) + ' ' + k)
    print("Total number of items: " + str(item_total))


# displayInventory(stuff)


def addToInventory(inventory, addedItems):
    # print(k, v)
    for k in addedItems: # Recorremos dragonLoot
        # print(k)
        if k in inv: # Preguntamos si algun item que esta en en diccionario "INV" entra
            # print(k)
            new_item = inventory.get(k, 0) # obtenemos el valor en el diccionario y se lo asignamos a variable
            # print(new_item)
            inventory[k] = new_item + 1 # le sumamos el valor y se lo agregamos al diccionario
        else:
            # print(k)
            inventory[k] = 1
    # print(inventory)
    return inventory  # , addedItems


inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = addToInventory(inv, dragonLoot)
displayInventory(inv)
# print(inv)


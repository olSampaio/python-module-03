import sys

def build_inventory():
	inventory = {}

	print("=== Inventory System Analysis ===")
	for argument in sys.argv[1:]:

		parts = argument.split(":")

		if (len(parts) != 2):
			print(f"Error - invalid parameter '{argument}'")
			continue
		
		item = parts[0]

		if (item in inventory):
			print(f"Redundant item '{item}' - discarding")
			continue

		try:
			quantity = int(parts[1])
		except ValueError as error:
			print(f"Quantity error for '{item}': {error}")
			continue

		inventory[item] = quantity

	return inventory

def show_inventory():
	inventory = build_inventory()
	items = list(inventory.keys())

	most_item = items[0]
	least_item = items[0]

	print(f"Got inventory: {inventory}")
	print(f"Item list: {items}")
	print(f"Total quantity of the {len(items)} items: {sum(inventory.values())}")
	for item in items:
		print(f"Item {item} represents {round((inventory[item] / sum(inventory.values()) * 100), 1)}%")

	for item in items:
		if inventory[item] > inventory[most_item]:
			most_item = item	
		if inventory[item] < inventory[least_item]:
			least_item = item

	print(f"Item most abundant: {most_item} with quantity {inventory[most_item]}")
	print(f"Item least abundant: {least_item} with quantity {inventory[least_item]}")

	inventory.update({"magic_item": 1})
	print(f"Updated inventory: {inventory}")
if __name__ == "__main__":
	show_inventory()
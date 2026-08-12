import random

achievements = [
    "First Steps",
    "Master Explorer",
    "Boss Slayer",
    "Treasure Hunter",
    "Speed Runner",
    "Crafting Genius",
    "World Savior",
    "Strategist",
    "Survivor",
    "Collector Supreme",
    "Untouchable",
    "Unstoppable",
    "Sharp Mind",
    "Hidden Path Finder",
    "Legendary Warrior",
    "Secret Keeper",
    "Puzzle Master",
    "Elite Hunter",
    "Resource Master",
    "Ultimate Champion"
]

def gen_player_achievements():
	quantity = random.randint(4, 15)
	player_achievements = random.sample(achievements, quantity)
	return (set(player_achievements))


def main():
	alice = gen_player_achievements()
	bob = gen_player_achievements()
	charlie = gen_player_achievements()
	dylan = gen_player_achievements()

	all_achievements = alice.union(bob, charlie, dylan)

	print(f"Player Alice: {alice}")
	print(f"Player Bob: {bob}")
	print(f"Player Charlie: {charlie}")
	print(f"Player Dylan: {dylan}")

	print(f"All distinct achievements: {all_achievements}\n")
	print(f"Common achievements: {alice.intersection(bob, charlie, dylan)}")

	print(f"Only Alice has: {alice.difference(bob, charlie, dylan)}")
	print(f"Only Bob has: {bob.difference(alice, charlie, dylan)}")
	print(f"Only Charlie has: {charlie.difference(bob, alice, dylan)}")
	print(f"Only Dylan has: {dylan.difference(bob, charlie, alice)}")

	print(f"Alice is missing: {all_achievements.difference(alice)}")
	print(f"Bob is missing: {all_achievements.difference(bob)}")
	print(f"Charlie is missing: {all_achievements.difference(charlie)}")
	print(f"Dylan is missing: {all_achievements.difference(dylan)}")

if __name__ == "__main__":
	main()
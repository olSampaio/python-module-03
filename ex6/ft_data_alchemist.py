import random


if __name__ == "__main__":
    print("=== Game Data Alchemist ===")

    players = ["Alice", "bob", "Charlie", "dylan", "Emma", "Gregory",
               "john", "kevin", "Liam"]
    print(f"\nInitial list of players: {players}")

    capitalized = [name.capitalize() for name in players]
    print(f"\nNew list with all names capitalized: {capitalized}")

    already_capitalized = [name for name in players if
                           name.capitalize() == name]
    print(f"\nNew list of capitalized names only: {already_capitalized}")

    scores = {name: random.randint(0, 1000) for name in capitalized}
    print(f"\nScore dict: {scores}")

    average = sum(scores.values()) / len(scores)
    print(f"\nScore average is {round(average, 2)}")

    high_scores = {name: score for name, score in scores.items() if
                   score > average}
    print(f"\nHigh scores: {high_scores}")

import math

def get_player_pos():
    while True:        
        coordinates = input("Enter new coordinates as floats in format 'x,y,z': ")
        values = coordinates.split(",")

        if len(values) != 3:
            print("Invalid syntax")
            continue

        try:
            x = float(values[0])
        except ValueError as error:
            print(f"Error on parameter '{values[0]}': {error}")
            continue
        try:
            y = float(values[1])
        except ValueError as error:
            print(f"Error on parameter '{values[1]}': {error}")
            continue
        try:
            z = float(values[2])
        except ValueError as error:
            print(f"Error on parameter '{values[2]}': {error}")
            continue

        return (x, y, z)

def main():
    print("=== Game Coordinate System ===")

    print("Get a first set of coordinates")
    first_pos = get_player_pos()

    print(f"Got a first tuple: {first_pos}")
    print(f"It includes: X={first_pos[0]}, Y={first_pos[1]}, Z={first_pos[2]}")

    distance = math.sqrt(
        first_pos[0] ** 2
        + first_pos[1] ** 2
        + first_pos[2] ** 2
    )

    print(f"Distance to center: {round(distance, 4)}\n")

    print("Get a second set of coordinates")
    second_pos = get_player_pos()

    distance = math.sqrt(
        (second_pos[0] - first_pos[0]) ** 2
        + (second_pos[1] - first_pos[1]) ** 2
        + (second_pos[2] - first_pos[2]) ** 2
    )

    print(f"Distance between the 2 sets of coordinates: {round(distance, 4)}")

if (__name__ == "__main__"):
    main()
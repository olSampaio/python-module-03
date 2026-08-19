import random
from typing import Generator

PLAYERS = ["bob", "alice", "dylan", "charlie"]
ACTIONS = ["run", "eat", "sleep", "grab", "move", "climb", "swim", "use",
           "release"]


def gen_event() -> Generator[tuple, None, None]:
    while True:
        name = random.choice(PLAYERS)
        action = random.choice(ACTIONS)
        yield (name, action)


def consume_event(events: list) -> Generator[tuple, None, None]:
    while len(events) > 0:
        index = random.randrange(len(events))
        event = events[index]
        del events[index]
        yield event


if __name__ == "__main__":
    print("=== Game Data Stream Processor ===")

    stream = gen_event()
    for i in range(1000):
        name, action = next(stream)
        print(f"Event {i}: Player {name} did action {action}")

    event_list = [next(stream) for i in range(10)]
    print(f"\nBuilt list of 10 events: {event_list}")

    for event in consume_event(event_list):
        print(f"Got event from list: {event}")
        print(f"Remains in list: {event_list}")

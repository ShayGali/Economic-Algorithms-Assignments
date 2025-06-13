import itertools
from typing import List, Dict


def calc_expected_value(
    players_to_values: Dict[str, Dict[str, int]],
    tasks: List[str],
    players_permutations: List[str],
) -> Dict[str, float]:
    """
    will calc the expected value for each player assuming that we have n players and n tasks, and the probability of each permutation is equal.
    """
    expected_values = {player: 0 for player in players_to_values.keys()}
    for perm in players_permutations:
        remaining_tasks = tasks.copy()
        for player in perm:
            # get the best task for the player
            best_task = max(
                remaining_tasks, key=lambda task: players_to_values[player][task]
            )
            expected_values[player] += (players_to_values[player][best_task]) / len(
                players_permutations
            )
            remaining_tasks.remove(best_task)

    return expected_values


def calc_full_expected_value(
    players_to_values: Dict[str, Dict[str, int]], tasks: List[str]
) -> Dict[str, Dict[str, float]]:
    """
    will calc the expected value for each player, and how the player see the expected value of the other players in his perspective.
    the return value is a dict of dicts, where the key is the player and the value is a dict of the expected values of all of the players in the perspective of the player.
    """
    expected_values = {
        player: {p: 0 for p in players_to_values.keys()}
        for player in players_to_values.keys()
    }
    players_permutations = list(itertools.permutations(players_to_values.keys()))
    for perm in players_permutations:
        remaining_tasks = tasks.copy()
        for player in perm:
            # get the best task for the player
            best_task = max(
                remaining_tasks, key=lambda task: players_to_values[player][task]
            )
            remaining_tasks.remove(best_task)
            for p in perm:
                # update the expected values of all of the players in the perspective of the player
                expected_values[p][player] += (players_to_values[p][best_task]) / len(
                    players_permutations
                )

    return expected_values


def method2_advantage_example():
    players_to_values = {
        "1": {"a": 1, "b": 1, "c": 1},
        "2": {"a": 75, "b": 4, "c": 25},
        "3": {"a": 60, "b": 65, "c": 5},
    }

    tasks = ["a", "b", "c"]

    print("Method 1 (all permutations):")
    # All 6 possible permutations
    players_permutations = list(itertools.permutations(players_to_values.keys()))
    expected_values = calc_expected_value(
        players_to_values, tasks, players_permutations
    )
    print("\tExpected values:")
    for player, value in expected_values.items():
        print(f"\t\tPlayer {player}: {value}")

    print("\nMethod 2 (strategic permutations):")
    # Only include permutations that lead to optimal assignments
    players_permutations = [
        ["3", "2", "1"],
        ["3", "1", "2"],
    ]
    expected_values = calc_expected_value(
        players_to_values, tasks, players_permutations
    )
    print("\tExpected values:")
    for player, value in expected_values.items():
        print(f"\t\tPlayer {player}: {value}")


def not_envy():
    players_to_values = {
        "p1": {"a": 0, "b": 5, "c": 0},
        "p2": {"a": 10, "b": 0, "c": 4},
        "p3": {"a": 5, "b": 4, "c": 0},
    }
    tasks = ["a", "b", "c"]
    expected = calc_full_expected_value(players_to_values, tasks)
    print("Expected values:")
    for player, value in expected.items():
        print(f"\tPlayer {player}:")
        for p, v in value.items():
            print(f"\t\tPlayer {p}: {v}")


if __name__ == "__main__":
    method2_advantage_example()
    print( "---------------------")
    not_envy()

from typing import List, Tuple

def _divisor_method(n_seats:int, votes: List[int], divide_function) -> List[int]:
    # Initialize the number of seats allocated to each party
    seats = [0] * len(votes)
    
    # Allocate seats using the Jefferson method
    for _ in range(n_seats):
        # find the party with the highest vote-to-seat ratio
        max_ratio = 0
        max_party = -1
        for i in range(len(votes)):
            calc = votes[i] / divide_function(seats[i])
            if calc > max_ratio:
                max_ratio = calc
                max_party = i
        
        # Allocate a seat to the party with the highest ratio
        seats[max_party] += 1

    return seats


def jefferson_method(n_seats:int, votes: List[int]) -> List[int]:
    return _divisor_method(n_seats, votes, lambda s: s + 1)

def webster_method(n_seats:int, votes: List[int]) -> List[int]:
    return _divisor_method(n_seats, votes, lambda s: (s + 0.5))


def apparentment_3(n_seats:int, votes: List[int], i, j, allocate_function) -> List[int]:
    new_votes = []
    for k in range(len(votes)):
        if k == i:
            new_votes.append(votes[k] + votes[j])
        elif k == j:
            new_votes.append(0)
        else:
            new_votes.append(votes[k])

    # get the number of seats allocated to each party using the Jefferson method
    seats = allocate_function(n_seats, new_votes)

    # now use the hamilton method for i and j apparentment
    n_seats = seats[i]
    votes = [votes[i], votes[j]]
    i_j_seats = allocate_function(n_seats, votes)
    seats[i] = i_j_seats[0]
    seats[j] = i_j_seats[1]

    return seats


# Example usage
def jefferson_example():
    print("Jefferson example")
    n_seats = 5
    votes = [40,135,325]
    plain_jefferson = jefferson_method(n_seats, votes)
    apparentment = apparentment_3(n_seats, votes, 0, 1, jefferson_method)
    print(f"Seats allocated with jefferson method: {plain_jefferson}")
    print(f"Seats allocated with apparentment 0 and 1: {apparentment}")

    for_2 = jefferson_method(n_seats, [175,325])
    print(f"Seats allocated with jefferson method for 2 parties: {for_2}")
    print(f"after the apparentment: {jefferson_method(for_2[0], [40,135])}")


def webster_example():
    print("Webster example")
    n_seats = 5
    votes = [40,135,325]
    plain_webster = webster_method(n_seats, votes)
    apparentment = apparentment_3(n_seats, votes, 0, 1, webster_method)
    print(f"Seats allocated with webster method: {plain_webster}")
    print(f"Seats allocated with apparentment 0 and 1: {apparentment}")

    for_2 = webster_method(n_seats, [175,325])
    print(f"Seats allocated with webster method for 2 parties: {for_2}")
    print(f"after the apparentment: {webster_method(for_2[0], [40,135])}")

if __name__ == "__main__":
    webster_example()
    jefferson_example()
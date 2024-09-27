from typing import List


def get_max_people(people: List[int], status: List[str]) -> int:
    people_at_party_at_t = set()

    for i, person in enumerate(people):
        if status[i] == '+':
            if person in people_at_party_at_t:
                return -1
            else:
                people_at_party_at_t.add(person)

        else:
            # status[i] is '-'
            if person in people_at_party_at_t:
                people_at_party_at_t.remove(person)
            else:
                return -1

    return len(people_at_party_at_t)

from dataclasses import dataclass
from typing import List

from constants import MEAT, NO_SOLUTION, VEGETARIAN


@dataclass
class Curry:
    type: int
    base: str = VEGETARIAN


@dataclass
class Customer:
    preferences: List[Curry]

    def __post_init__(self):
        # Sort preferences by first vegetarian options and then meat options, for the customer this preferences are
        # unranked but for the system is more valuable to produce vegetarian than meat options.
        self.preferences = [
            curry for curry in self.preferences if curry.base == VEGETARIAN
        ] + [curry for curry in self.preferences if curry.base == MEAT]


@dataclass
class Proposals:
    num_types: int
    customers: List

    def __post_init__(self):
        # Sort customers on number of preferences they have from less to more.
        # Less preferences makes the customer to have more constrains an more difficult to please,
        # so we deal with these first.
        self.customers.sort(key=lambda x: len(x.preferences), reverse=False)

    def resolve(self):
        result = {}
        for x in range(1, self.num_types + 1):
            result[x] = None

        for customer in self.customers:
            found = False
            for preference in customer.preferences:
                if result[preference.type] is None:
                    result[preference.type] = preference.base
                    found = True
                    break
                elif result[preference.type] == preference.base:
                    found = True
                    break
            if not found:
                return NO_SOLUTION
        result = {k: (VEGETARIAN if v is None else v) for k, v in result.items()}
        # return " ".join(result.values())
        return result

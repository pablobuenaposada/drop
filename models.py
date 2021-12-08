from dataclasses import dataclass
from typing import List

from constants import VEGETARIAN, MEAT


@dataclass
class Curry:
    id: int
    type: str = VEGETARIAN

    def asdict(self):
        return {self.id:  self.type}


@dataclass
class Customer:
    preferences: List  # de curryes

    def get_ordered_preferences(self):
        result = []
        result = [curry for curry in self.preferences if curry.type == VEGETARIAN]
        result += [curry for curry in self.preferences if curry.type == MEAT]
        return result


@dataclass
class Proposals:
    types: int
    customers: List

    def _get_ordered_customers(self):
        return sorted(self.customers, key=lambda x: len(x.preferences), reverse=False)  # sort o sorted?

    def main(self):
        result = {}
        for x in range(1, self.types+1):
            result[x] = None

        for customer in self._get_ordered_customers():
            found = False
            for preference in customer.get_ordered_preferences():
                if result[preference.id] is None:
                    result[preference.id] = preference.type
                    found = True
                    break
                elif result[preference.id] == preference.type:
                    found = True
                    break
            if not found:
                return "No solution"
        return result

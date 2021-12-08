import random
from unittest.mock import ANY

import pytest

from constants import MEAT, NO_SOLUTION, VEGETARIAN
from models import Curry, Customer, Proposals


class TestCustomer:
    @pytest.mark.parametrize(
        "preferences, expected",
        (
            ([], []),
            ([Curry(1, MEAT)], [Curry(1, MEAT)]),
            (
                [Curry(1, VEGETARIAN), Curry(2, MEAT)],
                [Curry(1, VEGETARIAN), Curry(2, MEAT)],
            ),
            (
                [Curry(1, MEAT), Curry(2, VEGETARIAN)],
                [Curry(2, VEGETARIAN), Curry(1, MEAT)],
            ),
        ),
    )
    def test_valid(self, preferences, expected):
        """Make sure order of the preferences are first vegetarian and later meat"""
        assert Customer(preferences).preferences == expected


class TestProposals:
    @pytest.mark.parametrize(
        "num_types, customers, expected",
        (
            (ANY, [], []),
            (
                ANY,
                [
                    Customer([Curry(1, MEAT), Curry(2, VEGETARIAN)]),
                    Customer([Curry(1, VEGETARIAN)]),
                ],
                [
                    Customer([Curry(1, VEGETARIAN)]),
                    Customer([Curry(1, MEAT), Curry(2, VEGETARIAN)]),
                ],
            ),
            (
                ANY,
                [
                    Customer([Curry(1, VEGETARIAN)]),
                    Customer([Curry(1, MEAT), Curry(2, VEGETARIAN)]),
                ],
                [
                    Customer([Curry(1, VEGETARIAN)]),
                    Customer([Curry(1, MEAT), Curry(2, VEGETARIAN)]),
                ],
            ),
        ),
    )
    def test_valid(self, num_types, customers, expected):
        """Make sure order of the customers are from less to more preferences"""
        assert Proposals(num_types, customers).customers == expected

    @pytest.mark.parametrize(
        "num_types, customers, expected",
        (
            (
                5,
                [
                    Customer(
                        [
                            Curry(1, MEAT),
                            Curry(3, VEGETARIAN),
                            Curry(5, VEGETARIAN),
                        ]
                    ),
                    Customer(
                        [
                            Curry(2, VEGETARIAN),
                            Curry(3, MEAT),
                            Curry(4, VEGETARIAN),
                        ]
                    ),
                    Customer([Curry(5, MEAT)]),
                ],
                {1: VEGETARIAN, 2: VEGETARIAN, 3: VEGETARIAN, 4: VEGETARIAN, 5: MEAT},
            ),
            (
                1,
                [
                    Customer([Curry(1, VEGETARIAN)]),
                    Customer([Curry(1, MEAT)]),
                ],
                NO_SOLUTION,
            ),
            (
                2,
                [
                    Customer([Curry(1, VEGETARIAN), Curry(2, MEAT)]),
                    Customer([Curry(1, MEAT)]),
                ],
                {1: MEAT, 2: MEAT},
            ),
            (
                2,
                [
                    Customer(
                        [
                            Curry(1, VEGETARIAN),
                        ]
                    ),
                    Customer(
                        [
                            Curry(1, VEGETARIAN),
                            Curry(2, MEAT),
                        ]
                    ),
                    Customer(
                        [
                            Curry(1, VEGETARIAN),
                            Curry(2, MEAT),
                        ]
                    ),
                ],
                {1: VEGETARIAN, 2: VEGETARIAN},
            ),
            (
                5,
                [
                    Customer([Curry(2, MEAT)]),
                    Customer([Curry(5, VEGETARIAN)]),
                    Customer([Curry(1, VEGETARIAN)]),
                    Customer(
                        [
                            Curry(5, VEGETARIAN),
                            Curry(1, VEGETARIAN),
                            Curry(4, MEAT),
                        ]
                    ),
                    Customer([Curry(3, VEGETARIAN)]),
                    Customer([Curry(5, VEGETARIAN)]),
                    Customer(
                        [
                            Curry(3, VEGETARIAN),
                            Curry(5, VEGETARIAN),
                            Curry(1, VEGETARIAN),
                        ]
                    ),
                    Customer([Curry(3, VEGETARIAN)]),
                    Customer([Curry(2, MEAT)]),
                    Customer([Curry(5, VEGETARIAN), Curry(1, VEGETARIAN)]),
                    Customer([Curry(2, MEAT)]),
                    Customer([Curry(5, VEGETARIAN)]),
                    Customer([Curry(4, MEAT)]),
                    Customer([Curry(5, VEGETARIAN), Curry(4, MEAT)]),
                ],
                {1: VEGETARIAN, 2: MEAT, 3: VEGETARIAN, 4: MEAT, 5: VEGETARIAN},
            ),
        ),
    )
    def test_resolve(self, num_types, customers, expected):
        assert Proposals(num_types, customers).resolve() == expected

    def test_random_resolve(self):
        """
        Creates random orders scenarios and checks if the solution works for each customer.
        Ideally you don't want these type of tests but due the brainteaser that this problem is, doesn't hurt
        to create quite some random cases and check that they pass green.
        """
        NUM_CUSTOMERS = 50
        NUM_TYPES = 5
        NUM_TESTS_WITH_SOLUTION = 1000

        results_with_solution = 0
        while results_with_solution < NUM_TESTS_WITH_SOLUTION:
            customers = []
            for _ in range(NUM_CUSTOMERS):
                # create random preferences
                bases = [VEGETARIAN for _ in range(NUM_TYPES - 1)] + [MEAT]
                types = [type for type in range(1, NUM_TYPES + 1)]
                random.shuffle(bases)
                random.shuffle(types)

                # the number of preferences per customer is also random
                num_preferences = random.randint(1, NUM_TYPES)
                list_of_curries = []
                for pref_index in range(0, num_preferences):
                    list_of_curries.append(
                        Curry(type=types[pref_index], base=bases[types[pref_index] - 1])
                    )

                customers.append(Customer(list_of_curries))

            result = Proposals(NUM_TYPES, customers).resolve()

            if (
                result != NO_SOLUTION
            ):  # if it's a no solution case then we don't care about this one
                results_with_solution += 1
                for customer in customers:
                    preferences = {}
                    for preference in customer.preferences:
                        preferences.update({preference.type: preference.base})
                    # the intersection between the solution and the customer preferences should reveal
                    # if any of the customer preferences are pleased within the retrieved solution
                    assert len(dict(result.items() & preferences.items())) > 0

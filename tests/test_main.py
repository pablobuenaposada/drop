import random

from constants import VEGETARIAN, MEAT
from models import Customer, Curry, Proposals


class TestMain:
    def test_main(self):
        CUSTOMERS = 30
        NUM_TYPES = 5
        NUM_TESTS = 1000

        results_with_solution = 0
        while results_with_solution < NUM_TESTS:
            customers = []
            for _ in range(CUSTOMERS):
                types = [VEGETARIAN for _ in range(1, NUM_TYPES)] + [MEAT]
                ids = [id for id in range(1, NUM_TYPES+1)]
                random.shuffle(types)
                random.shuffle(ids)

                list_of_curry = []
                num_preferences = random.randint(1, NUM_TYPES)
                for x in range(0, num_preferences):
                    list_of_curry.append(Curry(id=ids[x], type=types[ids[x]-1]))
                customers.append(Customer(list_of_curry))

            result = Proposals(NUM_TYPES, customers).main()
            if isinstance(result, dict):
                results_with_solution += 1
                for customer in customers:
                    preferences = {}
                    for preference in customer.get_ordered_preferences():
                       preferences.update(preference.asdict())
                    assert len(dict(result.items() & preferences.items())) > 0

import random

MIN_RANDOM_NUMBER = 1
MAX_RANDOM_NUMBER = 1_000_000


class Randomizer:
    # noinspection PyShadowingBuiltins
    @staticmethod
    def number(min=MIN_RANDOM_NUMBER, max=MAX_RANDOM_NUMBER):
        return random.randint(min, max)

"""
Liner
"""


def study_schedule(permanence_period, target_time):
    """
    Liner
    """
    counter = 0

    try:
        for period in permanence_period:
            if period[0] <= target_time <= period[1]:
                counter += 1
    except TypeError:
        return None

    return counter


# test = [(2, 2), (1, 2), (2, 3), (1, 5), (4, 5), (4, 5)]
# target = 5

# study_schedule(test, target)

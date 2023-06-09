permanence_period = [(2, 2), (1, 2), (2, 3), (1, 5), (4, 5), (4, 5)]
target_time = 5 
print(permanence_period)
def study_schedule(permanence_period, target_time):
    counter = 0

    try:
        for period in permanence_period:
            if period[0] <= target_time <= period[1]:
                counter += 1
    except Exception:
        return print(None)

    return print(counter)

study_schedule(permanence_period,target_time)
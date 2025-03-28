EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 2

def bake_time_remaining(elapsed_bake_time):
    bake_time_remaining = EXPECTED_BAKE_TIME - elapsed_bake_time
    return bake_time_remaining

# Each layer takes 2 minutes
def preparation_time_in_minutes(number_of_layers):
    preparation_time_in_minutes = number_of_layers*PREPARATION_TIME
    return preparation_time_in_minutes

def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    elapsed_time_in_minutes = preparation_time_in_minutes(number_of_layers) + elapsed_bake_time
    return elapsed_time_in_minutes

print(bake_time_remaining(39))
print(preparation_time_in_minutes(2))
print(elapsed_time_in_minutes(10, 1))


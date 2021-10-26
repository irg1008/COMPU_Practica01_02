import numpy as np

config, rides, adapted = [], [], []

def sort_rides(car_rides):
    def sort_ride(ride):
        a, b, x, y, s, f, _ = ride
        origin = [a, b]
        destiny = [x, y]
        distance = dis(origin, destiny)

        return s + f - distance

    return sorted(car_rides, key=lambda ride: sort_ride(ride[1]))


def get_rides_from_ind(individual):
    F = config[0]
    
    vehicles_rides = np.full(F, None)

    for i, vehicle in enumerate(individual):
        v_r = vehicles_rides[vehicle]

        if v_r is None:
            v_r = []

        ride = rides[i]
        v_r.append([i, ride])

        vehicles_rides[vehicle] = v_r

    return vehicles_rides


def dis(a, b): return np.abs(a[0] - b[0]) + np.abs(a[1]-b[1])

def get_penalty(adapted_car, adapted_ride):  
    if adapted_car == 0 and adapted_ride == 1:
        return 1
    return 0


def calc_fitness(car, car_rides):
    _, _, B, T = config
    
    fitness = 0
    penalty = 0
    step = 0
    pos = [0, 0]

    # Sort car_rides given earliest time.
    car_rides = sort_rides(car_rides)

    for _, ride in car_rides:
        a, b, x, y, earliest_start, latest_finish, adapted_ride = ride
        origin = [a, b]
        destiny = [x, y]

        adapted_car = adapted[car]

        # 0.- Set penalty of adaptability of car/ride.
        penalty += get_penalty(adapted_car, adapted_ride)

        # 1.- Go to origin.
        step += dis(pos, origin)

        # 2.- If arrived before the earliest time. Wait and earn bonus.
        if step <= earliest_start:
            fitness += B
            step = earliest_start

        # 3.- Go to destiny.
        dis_ori_des = dis(origin, destiny)
        step += dis_ori_des

        # 4.- If reached destiny before latest finish. Earn points.
        if step <= latest_finish:
            fitness += dis_ori_des

        # 5.- Update position.
        pos = destiny

        # 6.- Check if reached max distance with one car.
        if step > T:
            break

    return fitness, penalty


def eval_ind(ind, new_config, new_rides, new_adapted):
    global config, rides, adapted
    config = new_config
    rides = new_rides
    adapted = new_adapted
    
    all_rides = get_rides_from_ind(ind)

    fitness = 0
    penalty = 0

    for car, car_rides in enumerate(all_rides):
        if car_rides is not None:
            _fitness, _penalty = calc_fitness(car, car_rides)
            fitness += _fitness
            penalty += _penalty

    return fitness, penalty

import numpy as np
from HashData import get_data

config, rides, _ = get_data()
F, _, B, T = config


def sort_rides(vehicle_rides):
    def sort_ride(ride):
        a, b, x, y, s, f = ride[1]
        origin = [a, b]
        destiny = [x, y]
        distance = dis(origin, destiny)

        return s + f - distance

    return sorted(vehicle_rides, key=lambda ride: sort_ride(ride))


def get_rides_from_ind(individual):
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


def calc_fitness(car_rides):
    fitness = 0
    step = 0
    pos = [0, 0]

    # Sort car_rides given earliest time.
    car_rides = sort_rides(car_rides)

    for _, ride in car_rides:
        a, b, x, y, s, f = ride
        origin = [a, b]
        destiny = [x, y]
        earliest_start = s
        latest_finish = f

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

        # 6.- Check if reached max distance with one vehicle.
        #     Delete rides after this one.
        if step > T:
            break

    return fitness


def eval_ind(ind):
    all_rides = get_rides_from_ind(ind)

    fitness = 0

    for car_rides in all_rides:
        if car_rides is not None:
            fitness += calc_fitness(car_rides)

    return fitness,

import numpy as np
import HashData as hd

INITIAL_VEHICLE_POSITION = [0, 0]
config, rides = hd.get_data()
F, N, B, T = config

def get_rides_from_ind(individual):
    vehicles_rides = np.full(F, None)

    for i, vehicle in enumerate(individual):
        v_r = vehicles_rides[vehicle]
        if v_r is None:
            v_r = []
        v_r.append(i)
        vehicles_rides[vehicle] = v_r

    return vehicles_rides


def dis(a, b): return np.abs(a[0] - b[0]) + np.abs(a[1]-b[1])


def calculate_ride(ride, init_pos):
    a, b, x, y, s, f = ride

    origin = [a, b]
    destiny = [x, y]
    earliest_start = s
    latest_finish = f

    # 0.- Initial value and points to 0.
    step = 0
    points = 0

    # 1.- Go to origin.
    dis_init_origin = dis(init_pos, origin)
    step += dis_init_origin

    # 2.- If step after origin is earliest start.
    if step == earliest_start:
        points += B

    # 3.- If step before earliest start, wait.
    elif step < earliest_start:
        step = earliest_start

    # 4.- Drive to destiny.
    dis_origin_destiny = dis(origin, destiny)
    step += dis_origin_destiny
    
    # 5.- Bonus if not surpassed deadline.
    points += dis_origin_destiny
    
    # 6.- If surpasses deadline or number of steps T.
    if step > latest_finish:
        points = 0

    return points, destiny, step


def simulate(vehicle, vehicle_rides):
    points = 0
    step = 0
    pos = INITIAL_VEHICLE_POSITION

    for n_ride in vehicle_rides:
        ride = rides[n_ride]
        #print(f"Vehicle: {vehicle}. Pos: {pos}. Ride(a, b, x, y, s, f): {ride}")
        ride_points, new_pos, ride_step = calculate_ride(ride, pos)
        points += ride_points
        step += ride_step
        pos = new_pos
        
        # If surpasses T. Max distance with one car.
        if step > T:
            points = 0
            break

    return points, step

def evalRide(individual):
    points = 0
    step = 0
    vehicles_rides = get_rides_from_ind(individual)
    
    for i, v_r in enumerate(vehicles_rides):
        if v_r is not None:
            sim_points, sim_step = simulate(i, v_r)
            points += sim_points
            step += sim_step
    
    return points,
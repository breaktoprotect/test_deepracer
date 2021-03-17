def reward_function(params):
    # Reward parameters
    FAST_OPTIMAL_SPEED = 4.0
    MID_OPTIMAL_SPEED = 2.68
    
    # Read input parameters
    all_wheels_on_track = params['all_wheels_on_track']
    track_width = params['track_width']
    distance_from_center = params['distance_from_center']
    progress = params['progress']
    speed = params['speed']
    steps = params['steps']
    steering_angle = params['steering_angle']
    
    # Init
    reward = 0
    
    # 0. all_wheels_on_track = params['all_wheels_on_track'] 
    #    If off track, penalize
    if not all_wheels_on_track:
        reward -= 1
    
    # 1. distance_from_center 
    #    Further away from center, less rewards
    reward += 1-distance_from_center 
    
    # 2. speed
    #    Slower than certain speed, less rewards #TODO
    if distance_from_center < 0.1:
        if speed > FAST_OPTIMAL_SPEED:
            reward += 1
    elif distance_from_center < 0.3:
        if speed > MID_OPTIMAL_SPEED:
            reward += 0.8
    
    # 3. completion #TODO
    if round(progress) == 100:
        reward += 1000/steps
    
    # 4. steering angle
    # Keep it center at center
    if distance_from_center < 0.1:
        if abs(steering_angle) < 10:
            reward += 1
        elif abs(steering_angle) < 15:
            reward += 0.5
    elif distance_from_center < 0.3:
        if abs(steering_angle) < 15:
            reward += 1
        elif abs(steering_angle) < 20:
            reward += 0.5
    elif distance_from_center > 0.6:
        if abs(steering_angle) > 25:
            reward += 1.0
        elif abs(steering_angle) > 20: 
            reward += 0.5
    
    return float(reward)
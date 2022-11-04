def reward_function(params):
	'''
	Example that penalizes  driving further from track and steering.
	'''

	# # Give higher reward if the car is closer to center line
	marker = 0.5 * params['track_width']
	penalty_coefficient = -1.682243

	if params['distance_from_center'] > marker:
		reward = 1e-3  # likely crashed/ close to off track
	else:
		reward = 1 + params['distance_from_center'] * penalty_coefficient


    # Penalize reward if the car is steering too much
	abs_steering = abs(params['steering_angle']) # Only need the absolute steering angle
    # Steering penalty threshold, change the number based on your action space setting
	ABS_STEERING_THRESHOLD = 15 

	if abs_steering > ABS_STEERING_THRESHOLD:
		reward *= 0.7

	return float(reward)
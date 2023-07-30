from gym import spaces
import gym
import numpy as np 
from stable_baselines3 import PPO

class UVunwrap(gym.Env):
    def __init__(self):
        super(UVunwrap, self).__init__()

        # Define action and observation space
        n_actions = 5
        self.action_space = spaces.Discrete(n_actions)
        
        # Define observation space
        obs_height = 64
        obs_width = 64
        obs_channels = 1
        obs_shape = (obs_height, obs_width, obs_channels)
        self.observation_space = spaces.Box(low=0, high=255, shape=obs_shape, dtype=np.uint8)


    def step(self, action):
        # Apply the action to the environment
        self.state = apply_action(self.state, action) # placeholder function

        # Calculate the reward based on the rules you've provided
        reward = 0

        # Reward seams along hard edges
        if is_seam_along_hard_edge(self.state): # placeholder function
            reward += 1

        # Reward hidden seams
        if is_seam_hidden(self.state): # placeholder function
            reward += 1

        # Penalize noticeable seams
        if is_seam_noticeable(self.state): # placeholder function
            reward -= 1

        # Penalize overlapping UVs
        if is_overlapping(self.state): # placeholder function
            reward -= 1

        # Check if we're done
        done = is_done(self.state) # placeholder function

    # Optionally we can pass additional info, we are not using that for now
    info = {}

    return self.state, reward, done, info


    def reset(self):
        self.state = load_initial_state()
        return self.state
    
    def render(self, mode='human'):

    

env = UVunwrap()

model = PPO("MlpPolicy", env, verbose=1)

model.learn(total_timesteps=10000)

model.save("uv_unwrapping_agent")

model = PPO.load("uv_unwrapping_agent")

# test the agent 
obs = env.reset()
for i in range(100):
    action, _states = model.predict(obs)
    obs, rewards, dones, info = env.step(action)
    env.render()
import numpy as np


def analyze_agent_proximity(target_agent, observations, env, r, partitions):
    """
    Combines functionality to compute distances between agents and partitions agents
    around a target agent within a given radius into partitions.

    :param target_agent: target agent centered around
    :param observations: observations for a given step
    :param env: current environment
    :param r: radius of the circle
    :param partitions: number of partitions
    :return: vector of counts indicating how many agents fall into each partition within the radius
    """

    def distance(agent1, agent2):
        """ Computes the Euclidean distance between two agents based on their observations. """
        return np.sqrt((observations[agent1]['x'] - observations[agent2]['x']) ** 2 +
                       (observations[agent1]['y'] - observations[agent2]['y']) ** 2)

    vec_counts = np.zeros(partitions)
    target_x = observations[target_agent]['x']
    target_y = observations[target_agent]['y']

    for agent in env.agents:
        if agent != target_agent:
            agent_x = observations[agent]['x']
            agent_y = observations[agent]['y']

            # Compute the distance and angle (theta) to the agent
            radius = distance(target_agent, agent)
            theta = np.arctan2((agent_y - target_y), (agent_x - target_x))

            # Normalize theta to be in the range [0, 2*pi)
            theta = (theta + 2 * np.pi) % (2 * np.pi)
            # Calculate the sector size for the given number of partitions
            sector_size = 2 * np.pi / partitions

            # Determine the partition index
            partition_index = int(np.floor(theta / sector_size))

            # Only add to count if within specified radius
            if radius <= r:
                vec_counts[partition_index] += 1

    return vec_counts
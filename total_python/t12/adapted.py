import numpy as np


def calculate_distance(agent1, agent2, position_data):
    """
    Calculate the Euclidean distance between two agents using their positions.
    """
    dx = position_data[agent1]['x'] - position_data[agent2]['x']
    dy = position_data[agent1]['y'] - position_data[agent2]['y']
    return np.sqrt(dx ** 2 + dy ** 2)


def analyze_spatial_distribution(center_agent, positions, environment, radius, num_sectors):
    """
    Analyze the spatial distribution of agents around a central agent within a specified radius.
    Divide the area into equal angular sectors and count the number of agents in each sector.
    """
    counts = np.zeros(num_sectors)
    center_x, center_y = positions[center_agent]['x'], positions[center_agent]['y']

    for agent in environment.agents:
        if agent != center_agent:
            agent_x, agent_y = positions[agent]['x'], positions[agent]['y']
            distance = calculate_distance(center_agent, agent, positions)
            angle = np.arctan2(agent_y - center_y, agent_x - center_x)
            angle = (angle + 2 * np.pi) % (2 * np.pi)  # Normalize angle to [0, 2*pi)
            sector_index = int(angle / (2 * np.pi / num_sectors))  # Determine sector index

            if distance <= radius:
                counts[sector_index] += 1
    return counts

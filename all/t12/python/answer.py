import numpy as np


def calculate_distance(agent1: str, agent2: str, observations: dict) -> float:
    """
    Calculates the Euclidean distance between two agents based on their coordinates in the observations.

    :param agent1: String representation of agent1's identifier.
    :param agent2: String representation of agent2's identifier.
    :param observations: Dictionary containing observation question with agent identifiers as keys.
                         Each value is a dictionary with 'x' and 'y' keys representing coordinates.
    :return: Euclidean distance between the two agents.
    """
    # Extract coordinates of both agents
    x1, y1 = observations[agent1]['x'], observations[agent1]['y']
    x2, y2 = observations[agent2]['x'], observations[agent2]['y']

    # Calculate the Euclidean distance
    distance = np.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

    return distance
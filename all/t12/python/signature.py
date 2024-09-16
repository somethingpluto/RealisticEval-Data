def calculate_distance(agent1: str, agent2: str, observations: dict) -> float:
    """
    Calculates the Euclidean distance between two agents based on their coordinates in the observations.

    Args:
        agent1 (str): String representation of agent1's identifier.
        agent2 (str): String representation of agent2's identifier.
        observations (dict): Dictionary containing observation question with agent identifiers as keys.Each value is a dictionary with 'x' and 'y' keys representing coordinates.

    Returns:
        float: Euclidean distance between the two agents.
    """

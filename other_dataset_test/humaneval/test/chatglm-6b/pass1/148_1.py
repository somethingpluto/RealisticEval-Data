def check(candidate):

    # Check some simple cases
    assert candidate("Jupiter", "Neptune") == ("Saturn", "Uranus"), "First test error: " + str(len(candidate("Jupiter", "Neptune")))      
    assert candidate("Earth", "Mercury") == ("Venus",), "Second test error: " + str(candidate("Earth", "Mercury"))  
    assert candidate("Mercury", "Uranus") == ("Venus", "Earth", "Mars", "Jupiter", "Saturn"), "Third test error: " + str(candidate("Mercury", "Uranus"))      
    assert candidate("Neptune", "Venus") == ("Earth", "Mars", "Jupiter", "Saturn", "Uranus"), "Fourth test error: " + str(candidate("Neptune", "Venus"))  


    # Check some edge cases that are easy to work out by hand.
    assert candidate("Earth", "Earth") == ()
    assert candidate("Mars", "Earth") == ()
    assert candidate("Jupiter", "Makemake") == ()


def bf(planet1, planet2):
    """
    There are eight planets in our solar system: the closerst to the Sun is Mercury, the next one is Venus, then Earth, Mars, Jupiter, Saturn, Uranus, Neptune.
    Write a function that takes two planet names as strings planet1 and planet2. The function should return a tuple containing all planets whose orbits are located between the orbit of planet1 and the orbit of planet2, sorted by proximity to the sun.
    The function should return an empty tuple if planet1 or planet2 are not correct planet names.
    Examples:
    bf("Jupiter", "Neptune") ==> ("Saturn", "Uranus")
    bf("Earth", "Mercury") ==> ("Venus")
    bf("Mercury", "Uranus") ==> ("Venus", "Earth", "Mars", "Jupiter", "Saturn")
    """
    # Check if planet1 and planet2 are valid planet names
    if planet1 not in ["Mercury", "Venus", "Earth"] and planet2 not in ["Jupiter", "Neptune"]:
        return []

    # Find all planets between planet1 and planet2
     planets = []
    for planet in planet1:
        if planet not in planets:
            planets.append( planet )
     planets.sort(key=lambda x: x[1])

    # Return the planets in the list
    return planets

candidate = bf
check(candidate)
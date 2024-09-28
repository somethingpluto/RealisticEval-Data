# analyze input equations and determine the order they are routed
# most complex equations are routed first
def analyze_eq(eq_adt: list):
    # get the number of literals and ops in each equation
    # higher generally means more complex
    complexity = []
    for each in eq_adt:
        complexity.append(len(each.literals) + len(each.ops))

    # sort the equations by complexity
    # the most complex equations are routed first

    # sort the equations by complexity
    output = [
        x
        for _, x in sorted(
            zip(complexity, eq_adt), key=lambda pair: pair[0], reverse=True
        )
    ]
    return output
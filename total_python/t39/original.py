def search(crossover: bool) -> None:
    group: list[float] = [0.01 * k for k in range(10)]  # create the N = 10 individuals

    # run for 100 generations
    for _ in range(100):
        new_group: list[float] = []  # create the list representing the next gen's group

        # iterate over each individual in the group
        for i in range(10):
            selected: list[float] = selection(group)  # run selection on the current group

            # if specified, use crossover on the given value.
            if not crossover:
                offspring: float = selected[i]  # simply set the "offspring" to the selcted value if NOT doing crossover
            else:
                a: float = random.uniform(0, 1)
                x: float = random.choice(selected)
                y: float = random.choice(selected)
                offspring: float = cross(x, y, a)  # set the selected value to the result of a crossover method

            r: float = random.random()  # get a random probability

            if r <= 0.3:  # x - epsilon with probability of 0.3
                new_group.append(np.clip(offspring - 0.01, 0, 1))
            elif r <= 0.6:  # x + epsilon with probability of 0.3
                new_group.append(np.clip(offspring + 0.01, 0, 1))
            else:  # copy with probability of 0.4
                new_group.append(offspring)

        group = new_group  # replace the old group with the new group

    # print the results.
    bestN = max(group, key=fitness)
    print(f"Best N: {bestN}.")
    print(f"Best Fitness: {fitness(bestN)}")
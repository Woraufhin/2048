

def utilityf(grid):
    """
    Calculates the utility given the heuristics & weights

    C(x) = w1.f1 + w2.f2 + ... + wn.fn

    :param grid
    :return int(cost)
    """
    weight = {
        'os': 0.3,
        'lve': 0.6,
        'pm': 0.3,
        's': 0.4,
        'm': 0.6
    }

    return \
        weight['os'] * open_squares(grid) + \
        weight['lve'] * large_vals_edges(grid) + \
        weight['pm'] * potential_merges(grid) + \
        weight['s'] * smoothness(grid) + \
        weight['m'] * monotony(grid)


def open_squares(grid):
    """
    Calculates quantity of empty squares

    :param grid
    :return int(utility)
    """
    return len([i for s in grid.map for i in s if i == 0])


def large_vals_edges(grid):
    """
    Calculates if large values are on the edges

    :param grid
    :return int(utility)
    """
    corner_idx = (0, 4, 13, 16)
    threshold = 200
    flat_grid = [e for s in grid.map for e in s]

    h_idx = 0
    for val in range(0, len(flat_grid)):
        if flat_grid[val] > flat_grid[h_idx]:
            h_idx = val

    if flat_grid[h_idx] < threshold:
        return 0

    if h_idx in corner_idx:
        return 10

    return 0


def smoothness(grid):
    """
    Calculates the total number of merges possible given a state

    :param grid
    :return int(utility)
    """
    utility = 0
    columns = zip(*grid.map)

    # smoothness for rows?
    for row in grid.map:
        if all(e == l for e, l in zip(row, row[1:]) if all([e, l])):
            utility += 1

    # smoothness for columns?
    for col in columns:
        if all(e == l for e, l in zip(col, col[1:]) if all([e, l])):
            utility += 1

    return utility


def potential_merges(grid):
    """
    Ok, so, penalty for non-monotonic (rows|columns) that tend to decrease
    as highest value on board increases.

    :param grid
    :return int(utility)
    """
    utility = 0
    columns = zip(*grid.map)

    # Merges for rows?
    for row in grid.map:
        for e, l in zip(row, row[1:]):
            if e == l and any([e, l]):
                utility += 1

    # Merges for columns?
    for col in columns:
        for e, l in zip(col, col[1:]):
            if e == l and any([e, l]):
                utility += 1

    return utility


def monotony(grid):
    """
    Mmmm, this is like "keep (rows|columns) in increasing order"

    :param grid
    :return int(utility)
    """
    utility = 0
    columns = zip(*grid.map)

    # Are rows in descending order?
    for row in grid.map:
        if all(e >= l for e, l in zip(row, row[1:])):
            utility += 1

    # Are clumns in descending order?
    for col in columns:
        if all(e >= l for e, l in zip(col, col[1:])):
            utility += 1

    return utility


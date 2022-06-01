import pygame

min_allowed = 1e-5  # guard against overflow
big_value = 1e10  # use instead (if overflow would have occurred)


def slope(p1, p2):
    if abs(p2[0] - p1[0]) < min_allowed:
        return big_value
    return (p2[1] - p1[1]) * 1. / (p2[0] - p1[0])


def y_intercept(slop, p1):
    return p1[1] - 1. * slop * p1[0]


def intersect(line1, line2):
    m1 = slope(line1[0], line1[1])
    b1 = y_intercept(m1, line1[0])
    m2 = slope(line2[0], line2[1])
    b2 = y_intercept(m2, line2[0])
    if abs(m1 - m2) < min_allowed:
        x = big_value
    else:
        x = (b2 - b1) / (m1 - m2)
    y = m1 * x + b1
    y2 = m2 * x + b2
    return int(x), int(y)


def segment_intersect(line1, line2):
    # List [(x1,y1),(x2,y2)]

    intersection_pt = intersect(line1, line2)

    if intersection_pt[0] < min(line1[0][0], line1[1][0]):
        return None
    if intersection_pt[0] < min(line2[0][0], line2[1][0]):
        return None
    if intersection_pt[1] < min(line1[0][1], line1[1][1]):
        return None
    if intersection_pt[1] < min(line2[0][1], line2[1][1]):
        return None
    if intersection_pt[0] > max(line1[0][0], line1[1][0]):
        return None
    if intersection_pt[0] > max(line2[0][0], line2[1][0]):
        return None
    if intersection_pt[1] > max(line1[0][1], line1[1][1]):
        return None
    if intersection_pt[1] > max(line2[0][1], line2[1][1]):
        return None
    # if line1[0][0] < line1[1][0]:
    #     if intersection_pt[0] < line1[0][0] or intersection_pt[0] > line1[1][0]:
    #         return None
    # else:
    #     if intersection_pt[0] > line1[0][0] or intersection_pt[0] < line1[1][0]:
    #         return None
    #
    # if line2[0][0] < line2[1][0]:
    #     if intersection_pt[0] < line2[0][0] or intersection_pt[0] > line2[1][0]:
    #         return None
    # else:
    #     if intersection_pt[0] > line2[0][0] or intersection_pt[0] < line2[1][0]:
    #         return None

    return intersection_pt


def rectIntersect(rect: pygame.Rect, line):
    point = segment_intersect((rect.bottomright, rect.bottomleft), line)
    if point:
        return point

    point = segment_intersect((rect.bottomleft, rect.topleft), line)
    if point:
        return point

    point = segment_intersect((rect.topleft, rect.topright), line)
    if point:
        return point

    point = segment_intersect((rect.topright, rect.bottomright), line)
    if point:
        return point

    return None

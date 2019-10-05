# task from https://www.hackerrank.com/test/2ocejn4tppb/a3f396f86532452b0cfc3ef973a0d989
def visualize_fountain(a, points):
    fountains1 = ["---"] * len(a)
    fountains2 = ["   "] * len(a)
    for point in points:
        fountains1[max(0, point - a[point])] = " .."
        fountains2[max(0, point - a[point])] = "/  "
        fountains1[min(point + a[point], len(a) - 1)] = ".. "
        fountains2[min(point + a[point], len(a) - 1)] = "  \\"

    for point in points:
        fountains1[point] = "   "
        fountains2[point] = "\|/"

    print(" " + "".join(fountains1)[1:-1:])
    print("".join(fountains2))
    print(a)


def found_min_required_fountains(a):
    array_length = len(a)
    scores = []
    position_availability = [set() for _ in range(array_length)]
    for i in range(array_length):
        right = min(i + a[i] + 1, array_length)
        left = max(0, i - a[i])
        scores.append({
            "index": i,
            "score": right - left,
            "left": left,
            "right": right
        })
        for availability in range(left, right):
            position_availability[availability].add(i)

    # print("\nScores: {}".format(scores))
    # print("Max score: {}".format(max(scores, key=lambda element: element["score"])))
    # print("Sum: {}".format(sum(map(lambda element: element["score"], scores))))
    # print("Availability: {}".format(position_availability))
    points = []
    total_score = sum(map(lambda element: element["score"], scores))
    while True:
        max_scored_item = max(scores, key=lambda element: element["score"])
        points.append(max_scored_item["index"])
        for i in range(max_scored_item["left"], max_scored_item["right"]):
            for positions in position_availability[i]:
                scores[positions]["score"] -= 1

        new_total_score = sum(map(lambda element: element["score"], scores))
        if total_score == new_total_score or new_total_score <= 0:
            break
        total_score = new_total_score
    print("\n")
    visualize_fountain(a, points)
    return len(points)


print("Result " + str(found_min_required_fountains([1, 1, 1])))
print("Result " + str(found_min_required_fountains([1, 1, 1, 1, 1])))
print("Result " + str(found_min_required_fountains([1, 1, 2, 1, 1])))
print("Result " + str(found_min_required_fountains([3, 1, 1, 2, 1, 0, 4, 0, 0, 3])))
print("Result " + str(found_min_required_fountains([3, 1, 1, 2, 1, 0, 2, 0, 0, 3])))
print("Result " + str(found_min_required_fountains([1, 1, 2, 1, 3, 1, 1, 1, 1, 4, 1, 1, 1, 1, 3, 1, 2, 1, 1])))

#  ..   ..
# /  \|/ \
# [1, 1, 1]
# Result 1

#    --- .... ------   ------..
# \|/   /    \      \|/ \
# [3, 1, 1, 2, 1, 0, 4, 0, 0, 3]
# Result 2

def found_min_required_fountains(a):
    print("Array: {}".format(a))
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
    iterations = 0
    total_score = sum(map(lambda element: element["score"], scores))
    while True:
        iterations += 1
        max_scored_item = max(scores, key=lambda element: element["score"])
        for i in range(max_scored_item["left"], max_scored_item["right"]):
            for positions in position_availability[i]:
                scores[positions]["score"] -= 1

        new_total_score = sum(map(lambda element: element["score"], scores))
        if total_score == new_total_score or new_total_score <= 0:
            break
        total_score = new_total_score

    return iterations


print("Result " + str(found_min_required_fountains([1, 1, 1])))
print("Result " + str(found_min_required_fountains([1, 1, 1, 1, 1])))
print("Result " + str(found_min_required_fountains([1, 1, 2, 1, 1])))
print("Result " + str(found_min_required_fountains([1, 1, 2, 1, 3, 1, 1, 1, 1, 4, 1, 1, 1, 1, 3, 1, 2, 1, 1])))

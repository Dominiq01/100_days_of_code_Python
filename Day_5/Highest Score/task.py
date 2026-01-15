student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89, 86, 55, 91, 64, 89]
print(range(1, 10))

print(sum(student_scores))
sum_score = 0
for score in student_scores:
    sum_score += score

print(sum_score)

print(max(student_scores))

highest_score = student_scores[0]
for score in student_scores:
    if score > highest_score:
        highest_score = score


print(highest_score)
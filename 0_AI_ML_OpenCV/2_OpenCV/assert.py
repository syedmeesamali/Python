def avgMarks(marks):
    assert len(marks) != 0, "Marks list is empty!"
    return sum(marks) / len(marks)

marks1 = [1, 5, 7]
print(avgMarks(marks1))

marks2 = []
print(avgMarks(marks2))
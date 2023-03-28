subject_marks = [('English', 88), ('Science', 90), ('Maths', 88),
                 ('Physics', 93), ('History', 78), ('French', 78),
                 ('Art', 78), ('Chemistry', 88), ('Programming', 91)]

[print(*item) for item in sorted(sorted(subject_marks, key=lambda y: y[0]), key=lambda x: -x[1])]

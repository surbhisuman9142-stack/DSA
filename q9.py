def grade(score):
    if score >= 90:
       return 'A'
    if score >= 75:
        return 'B'
    if score >= 40:
        return 'C'
    else:
        return'Fail'
score = 80
print(grade(score))
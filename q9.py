def grade(score):
    if score >= 90:
        return  "a"
    if score >= 75:
        return  "b"
    if score >= 40:
        return  "c"
    else :
        return  "fail"
score = 80
print(grade(score))
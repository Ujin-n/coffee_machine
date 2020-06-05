stud_score = int(input())
max_score = int(input())

prc = stud_score * 100 / max_score

if prc >= 90:
    print("A")
elif prc >= 80:
    print("B")
elif prc >= 70:
    print("C")
elif prc >= 60:
    print("D")
else:
    print("F")

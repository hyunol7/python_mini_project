students = {
    "tom": 82,
    "jerry": 93,
    "joon": 99,
    "misha": 88,
    "amy": 74
}

def get_grade(score: int):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    else:
        return "F"

for name, score in students.items():
    print(f"{name} got a {get_grade(score)}")
    print(f"then, {get_grade(score)}")

student_marks={
    "Alice":85,
    "Anjali":78,
    "Vishu":65,
    "Niki":82,
    "Rutu":70}

student_name=input("ENter the Student's name:")
if student_name in student_marks:
    print(f"{student_name}'s marks:{student_marks[student_name]}")
else:
    print(f"{student_name} not found in this record")
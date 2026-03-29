def grade_students(student_list):
    grade_students = {}
    for student in student_list:
        score = student['score']
        if score >= 90:
            student['grade'] = 'A'
        elif score >= 75:
            student['grade'] = 'B'
        elif score >= 60:
            student['grade'] = 'C'
        else:
            student['grade'] = 'F'
        
        grade_students[student['name']] = student['grade']
     
    return grade_students
  
             
students = [
      {'name': 'Alice', 'score': 92},
      {'name': 'Bob',   'score': 74},
      {'name': 'Carol', 'score': 61},
      {'name': 'Dave',  'score': 45}
  ]


result = grade_students(students)
print(result)


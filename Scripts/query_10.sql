SELECT students.name, subjects.name
FROM students
JOIN grades ON students.id = grades.student_id
JOIN subjects ON grades.subject_id = subjects.id
JOIN teachers ON subjects.teacher_id = teachers.id
WHERE students.name = 'Студент' AND teachers.name = 'Викладач';

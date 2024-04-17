SELECT teachers.name, AVG(grades.grade) as average_grade
FROM teachers
JOIN subjects ON teachers.id = subjects.teacher_id
JOIN grades ON subjects.id = grades.subject_id
GROUP BY teachers.id;

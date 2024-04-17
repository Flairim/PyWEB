import sqlite3
from faker import Faker
import random

fake = Faker('uk_UA')

conn = sqlite3.connect('university.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    group_id INTEGER
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS groups (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS teachers (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS subjects (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    teacher_id INTEGER
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS grades (
    id INTEGER PRIMARY KEY,
    student_id INTEGER,
    subject_id INTEGER,
    grade INTEGER,
    date TEXT,
    FOREIGN KEY (student_id) REFERENCES students (id),
    FOREIGN KEY (subject_id) REFERENCES subjects (id)
)
''')

groups = ['Група 1', 'Група 2', 'Група 3']
for group in groups:
    cursor.execute("INSERT INTO groups (name) VALUES (?)", (group,))

for _ in range(30):
    name = fake.name()
    group_id = random.randint(1, 3)
    cursor.execute("INSERT INTO students (name, group_id) VALUES (?, ?)", (name, group_id))

teachers = [fake.name() for _ in range(5)]
for teacher in teachers:
    cursor.execute("INSERT INTO teachers (name) VALUES (?)", (teacher,))

subjects = ['Математика', 'Фізика', 'Хімія', 'Історія', 'Література']
for idx, subject in enumerate(subjects):
    teacher_id = random.randint(1, 5)
    cursor.execute("INSERT INTO subjects (name, teacher_id) VALUES (?, ?)", (subject, teacher_id))

for student_id in range(1, 31):
    for subject_id in range(1, 6):
        grade = random.randint(60, 100)
        date = fake.date_this_decade().strftime('%Y-%m-%d')
        cursor.execute("INSERT INTO grades (student_id, subject_id, grade, date) VALUES (?, ?, ?, ?)", 
                       (student_id, subject_id, grade, date))

conn.commit()
conn.close()

PRAGMA foreign_keys = ON;

CREATE TABLE IF NOT EXISTS courses (
    course_id INTEGER PRIMARY KEY AUTOINCREMENT,
    course_name TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS students (
    student_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    enrolled_course_id INTEGER,
    FOREIGN KEY (enrolled_course_id) REFERENCES courses(course_id)
);
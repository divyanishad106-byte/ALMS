-- Adaptive Learning Management System Database

CREATE TABLE Users (
  user_id INTEGER PRIMARY KEY AUTOINCREMENT,
  username VARCHAR(100),
  password VARCHAR(100),
  email VARCHAR(255),
  preferences TEXT,
  progress TEXT
);

CREATE TABLE Courses (
  course_id INTEGER PRIMARY KEY AUTOINCREMENT,
  title VARCHAR(255),
  description TEXT,
  start_date DATE,
  end_date DATE
);

CREATE TABLE Modules (
  module_id INTEGER PRIMARY KEY AUTOINCREMENT,
  course_id INTEGER,
  title VARCHAR(255),
  content TEXT,
  order_no INTEGER,
  FOREIGN KEY (course_id) REFERENCES Courses(course_id)
);

CREATE TABLE Assessments (
  assessment_id INTEGER PRIMARY KEY AUTOINCREMENT,
  module_id INTEGER,
  title VARCHAR(255),
  questions TEXT,
  FOREIGN KEY (module_id) REFERENCES Modules(module_id)
);

CREATE TABLE Feedback (
  feedback_id INTEGER PRIMARY KEY AUTOINCREMENT,
  user_id INTEGER,
  module_id INTEGER,
  rating INTEGER,
  comments TEXT,
  FOREIGN KEY (user_id) REFERENCES Users(user_id),
  FOREIGN KEY (module_id) REFERENCES Modules(module_id)
);
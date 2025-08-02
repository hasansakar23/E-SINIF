
CREATE TABLE Teachers (
    id TEXT PRIMARY KEY,       
    email TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL,
    created_at TEXT DEFAULT (datetime('now'))
);

CREATE TABLE Classes (
    id TEXT PRIMARY KEY,       
    teacher_id TEXT NOT NULL,
    name TEXT NOT NULL,
    description TEXT,
    code TEXT UNIQUE NOT NULL,
    created_at TEXT DEFAULT (datetime('now')),
    FOREIGN KEY (teacher_id) REFERENCES Teachers(id)
);

CREATE TABLE Students (
    id TEXT PRIMARY KEY,        
    class_id TEXT NOT NULL,
    code_name TEXT UNIQUE NOT NULL,
    created_at TEXT DEFAULT (datetime('now')),
    FOREIGN KEY (class_id) REFERENCES Classes(id)
);

CREATE TABLE Assignments (
    id TEXT PRIMARY KEY,         
    student_id TEXT NOT NULL,
    file_path TEXT NOT NULL,
    uploaded_at TEXT DEFAULT (datetime('now')),
    status TEXT CHECK( status IN ('Pending', 'Evaluated') ) DEFAULT 'Pending',
    FOREIGN KEY (student_id) REFERENCES Students(id)
);

CREATE TABLE Evaluations (
    id TEXT PRIMARY KEY,        
    assignment_id TEXT NOT NULL,
    teacher_id TEXT NOT NULL,
    coherence INTEGER CHECK (coherence BETWEEN 1 AND 5),
    sources INTEGER CHECK (sources BETWEEN 1 AND 5),
    reasoning INTEGER CHECK (reasoning BETWEEN 1 AND 5),
    language INTEGER CHECK (language BETWEEN 1 AND 5),
    total_score INTEGER,
    feedback TEXT,
    ai_suggestion TEXT,
    evaluated_at TEXT DEFAULT (datetime('now')),
    FOREIGN KEY (assignment_id) REFERENCES Assignments(id),
    FOREIGN KEY (teacher_id) REFERENCES Teachers(id)
);
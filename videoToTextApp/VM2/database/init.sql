CREATE DATABASE transcriptions;
CREATE TABLE transcriptions (
    id SERIAL PRIMARY KEY,
    filename TEXT,
    content TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
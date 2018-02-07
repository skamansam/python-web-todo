-- Should already be done when creating user
-- CREATE DATABASE python_todo;


CREATE TABLE IF NOT EXISTS users (
    id SERIAL NOT NULL PRIMARY KEY,
    email VARCHAR(100) NOT NULL UNIQUE,
    name VARCHAR(100) NOT NULL,
    hashed_password VARCHAR(100) NOT NULL
);

CREATE TABLE IF NOT EXISTS lists (
    id SERIAL NOT NULL PRIMARY KEY,
    created_by INTEGER NOT NULL REFERENCES users(id),
    title VARCHAR(512) NOT NULL,
    about text NOT NULL,
    created_at TIMESTAMP NOT NULL,
    updated_at TIMESTAMP NOT NULL
);

CREATE TABLE IF NOT EXISTS list_items (
    id SERIAL NOT NULL PRIMARY KEY,
    list_id INTEGER NOT NULL REFERENCES lists(id),
    body text NOT NULL
);

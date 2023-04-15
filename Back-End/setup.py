import psycopg2

connection = psycopg2.connect(
    database="exam_system",
    host="localhost",
    user="asad",
    password="123"
)

cursor = connection.cursor()

create_table_query = '''
CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL,
    address VARCHAR(255) 
);
CREATE TABLE IF NOT EXISTS examiners (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL,
    institution VARCHAR(255) ,
    availability BOOLEAN,
    ranking INTEGER,
    resume VARCHAR(255), 
    acceptance_count INTEGER,
    rejection_count INTEGER,
);

'''

cursor.execute(create_table_query)
connection.commit()

cursor.close()
connection.close()

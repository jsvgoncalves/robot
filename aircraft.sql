CREATE TABLE crew (
    id SERIAL PRIMARY KEY,
    birthday date NOT NULL,
    name text NOT NULL
);

INSERT INTO crew (birthday, name) VALUES
    ('1989-02-08', 'Honza'),
    ('1980-05-15', 'Jan');

CREATE TABLE aircraft (
    id SERIAL PRIMARY KEY,
    name text NOT NULL
);

INSERT INTO aircraft (name) VALUES
    ('CZ Cimrman'),
    ('CZ Kafka');


CREATE TABLE experience (
    fk_crew integer REFERENCES crew (id),
    fk_aircraft integer REFERENCES aircraft (id)
);

INSERT INTO experience (fk_crew, fk_aircraft) VALUES
    (1,1),
    (1,2),
    (2,1);


-- Question 1 and 2 (Even though one could use MIN() for question 1)
-- Find name of the oldest crew member
-- Find name of the n-th crew member (second oldest, fifth oldest and so on)
SELECT
    name, birthday
FROM crew
ORDER BY birthday ASC
LIMIT 1 OFFSET 0; -- nth-1 is given by the offset

-- Find name of the most experienced crew member - that one who knows most aircrafts
SELECT crew.name as name, COUNT(experience.fk_crew) AS exp_count
FROM crew
LEFT JOIN experience
ON (crew.id = experience.fk_crew)
GROUP BY
    crew.id
ORDER BY exp_count DESC
LIMIT 1;

-- Find name of the least experienced crew member - that one who knows least aircrafts (counting from zero)
SELECT crew.name as name, COUNT(experience.fk_crew) AS exp_count
FROM crew
LEFT JOIN experience
ON (crew.id = experience.fk_crew)
GROUP BY
    crew.id
ORDER BY exp_count ASC
LIMIT 1;

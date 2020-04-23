## Tietokantakaavio

<img src="https://github.com/nicholsss/Jobber/blob/master/Documentation/UusiKaavio.png">

CREATE TABLE lauseet
```
CREATE TABLE account (
        id INTEGER NOT NULL,
        date_created DATETIME,
        date_modified DATETIME,
        username VARCHAR(144) NOT NULL,
        password VARCHAR(144) NOT NULL,
        roles VARCHAR(144) NOT NULL,
        PRIMARY KEY (id),
        UNIQUE (username)
);
```

```
CREATE TABLE job (
        id INTEGER NOT NULL,
        date_created DATETIME,
        date_modified DATETIME,
        name VARCHAR(144) NOT NULL,
        salary INTEGER NOT NULL,
        active BOOLEAN NOT NULL,
        description VARCHAR NOT NULL,
        account_id INTEGER NOT NULL,
        PRIMARY KEY (id),
        CHECK (active IN (0, 1)),
        FOREIGN KEY(account_id) REFERENCES account (id)
);
```

```
CREATE TABLE IF NOT EXISTS "userJobs" (
        job_id INTEGER,
        account_id INTEGER,
        FOREIGN KEY(job_id) REFERENCES job (id),
        FOREIGN KEY(account_id) REFERENCES account (id)
);
```

```
CREATE TABLE question (
        id INTEGER NOT NULL,
        date_created DATETIME,
        date_modified DATETIME,
        content VARCHAR(144) NOT NULL,
        account_id INTEGER NOT NULL,
        job_id INTEGER NOT NULL,
        PRIMARY KEY (id),
        FOREIGN KEY(account_id) REFERENCES account (id),
        FOREIGN KEY(job_id) REFERENCES job (id)
);
```

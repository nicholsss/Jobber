# User Stories

* **As a Student**, I want to   **Show my intrest for a job**, So that **I can land the specific job**

```
Tämä tulee viimeistään ennen 7 viikkoa
```
* **As a Entrepreneur**, I want to **List my jobs**, So that **I can see if someone is interested in them**

```
INSERT INTO Job(id,date_created,date_modified,name,salary,active,description,account_id)
         VALUES (?,?,?,'?',?,?,'?',?);
```

* **As a  Unemployed**, I want to **Track how much i have earned**, So that **Kela doesn't cut unemployed money**

```
SELECT SUM(salary) from Job
```

* **As a Interested user**, I want to **View different jobs**, So that **I get to know what kind of jobs there are**
```
SELECT * FROM Job;
```

* **As Employer** I want to **Delete my older job postings**, So that **So that it doesn't confuse others**
```
DELETE FROM Job WHERE id = ?;
```

* **As a Employer** I want to **Edit my job posting**, In case **I made a mistake in the posting**

```
 UPDATE Job SET date_modified = ?,
          name = '?', salary = ?, active=?,description='?' WHERE id = ?;
```

* **As a Confused user** I want to **Ask a question from the employeer**, So that **I can clear out something about the job descritpion**

```
 INSERT INTO Question (id,date_created,date_modified, account_id, job_id,content)
        VALUES(?,?,?,?,?,'?');
```

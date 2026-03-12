# Job Tracker App

A full-stack job application tracker built with Java, Spring Boot, and MySQL.

## Features

- Create job applications
- View all job applications
- Delete job entries
- RESTful API using Spring Boot
- MySQL database integration using Spring Data JPA

## Tech Stack

- Java
- Spring Boot
- MySQL
- Maven

## Project Structure

```
src/main/java/com/jobtracker
│
├── controller
├── model
├── repository
└── service
```

## API Endpoints

GET all jobs

```
GET /jobs
```

Create job

```
POST /jobs
```

Delete job

```
DELETE /jobs/{id}
```

## Database Setup

Create the database in MySQL:

```
CREATE DATABASE jobtracker;
```

Update your database configuration in:

```
src/main/resources/application.properties
```

## Run the Project

Run the Spring Boot application:

```
mvn spring-boot:run
```

Server runs on:

```
http://localhost:8080
```


-- ============================================
-- Gym Management System — Database Schema
-- ============================================

CREATE DATABASE IF NOT EXISTS gym_app;
USE gym_app;

-- 1. Trainers
CREATE TABLE gym_trainer (
    id             INT AUTO_INCREMENT PRIMARY KEY,
    name           VARCHAR(100) NOT NULL,
    specialization VARCHAR(100) NOT NULL,
    experience     INT          NOT NULL,
    contact        VARCHAR(15)  NOT NULL
);

-- 2. Members
CREATE TABLE gym_member (
    id           INT AUTO_INCREMENT PRIMARY KEY,
    name         VARCHAR(100) NOT NULL,
    age          INT          NOT NULL,
    email        VARCHAR(254) NOT NULL,
    phone        VARCHAR(15)  NOT NULL,
    trainer_id   INT          NOT NULL,
    trainer_name VARCHAR(15)  NOT NULL,
    FOREIGN KEY (trainer_id) REFERENCES gym_trainer(id)
);

-- 3. Memberships
CREATE TABLE gym_membership (
    id           INT AUTO_INCREMENT PRIMARY KEY,
    member_id    INT          NOT NULL,
    member_name  VARCHAR(15)  NOT NULL,
    type         VARCHAR(50)  NOT NULL,
    start_date   DATETIME     NOT NULL,
    end_date     DATETIME     NOT NULL,
    fee          FLOAT        NOT NULL,
    FOREIGN KEY (member_id) REFERENCES gym_member(id)
);

-- 4. Payments
CREATE TABLE gym_payment (
    id           INT AUTO_INCREMENT PRIMARY KEY,
    member_id    INT          NOT NULL,
    member_name  VARCHAR(15)  NOT NULL,
    amount       FLOAT        NOT NULL,
    payment_date DATETIME     NOT NULL DEFAULT CURRENT_TIMESTAMP,
    method       VARCHAR(50)  NOT NULL,
    FOREIGN KEY (member_id) REFERENCES gym_member(id)
);

-- 5. Exercises
CREATE TABLE gym_exercise (
    id           INT AUTO_INCREMENT PRIMARY KEY,
    name         VARCHAR(100) NOT NULL,
    muscle_group VARCHAR(100) NOT NULL,
    reps         INT          NOT NULL,
    sets         INT          NOT NULL
);

-- 6. Workout Plans
CREATE TABLE gym_workplan (
    id            INT AUTO_INCREMENT PRIMARY KEY,
    name          VARCHAR(100) NOT NULL,
    description   TEXT         NOT NULL,
    duration      INT          NOT NULL,
    exercise_id   INT          NOT NULL,
    exercise_name VARCHAR(15)  NOT NULL,
    member_id     INT          NOT NULL,
    member_name   VARCHAR(15)  NOT NULL,
    FOREIGN KEY (exercise_id) REFERENCES gym_exercise(id),
    FOREIGN KEY (member_id)   REFERENCES gym_member(id)
);

-- 7. Equipment
CREATE TABLE gym_equipment (
    id               INT AUTO_INCREMENT PRIMARY KEY,
    name             VARCHAR(100) NOT NULL,
    type             VARCHAR(100) NOT NULL,
    maintenance_date DATETIME     NOT NULL,
    status           VARCHAR(50)  NOT NULL
);

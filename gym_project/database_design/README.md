# Database Design — Gym Management System

## Overview

The database consists of 7 tables managing trainers, members, memberships, payments, exercises, workout plans, and equipment.

---

## Tables

### 1. gym_trainer
| Column         | Type         | Constraints  |
|----------------|--------------|--------------|
| id             | INT          | PK, AUTO INC |
| name           | VARCHAR(100) | NOT NULL     |
| specialization | VARCHAR(100) | NOT NULL     |
| experience     | INT          | NOT NULL     |
| contact        | VARCHAR(15)  | NOT NULL     |

---

### 2. gym_member
| Column       | Type         | Constraints       |
|--------------|--------------|-------------------|
| id           | INT          | PK, AUTO INC      |
| name         | VARCHAR(100) | NOT NULL          |
| age          | INT          | NOT NULL          |
| email        | VARCHAR(254) | NOT NULL          |
| phone        | VARCHAR(15)  | NOT NULL          |
| trainer_id   | INT          | FK → gym_trainer  |
| trainer_name | VARCHAR(15)  | NOT NULL          |

---

### 3. gym_membership
| Column      | Type         | Constraints      |
|-------------|--------------|------------------|
| id          | INT          | PK, AUTO INC     |
| member_id   | INT          | FK → gym_member  |
| member_name | VARCHAR(15)  | NOT NULL         |
| type        | VARCHAR(50)  | NOT NULL         |
| start_date  | DATETIME     | NOT NULL         |
| end_date    | DATETIME     | NOT NULL         |
| fee         | FLOAT        | NOT NULL         |

---

### 4. gym_payment
| Column       | Type        | Constraints      |
|--------------|-------------|------------------|
| id           | INT         | PK, AUTO INC     |
| member_id    | INT         | FK → gym_member  |
| member_name  | VARCHAR(15) | NOT NULL         |
| amount       | FLOAT       | NOT NULL         |
| payment_date | DATETIME    | AUTO (now)       |
| method       | VARCHAR(50) | NOT NULL         |

---

### 5. gym_exercise
| Column       | Type         | Constraints  |
|--------------|--------------|--------------|
| id           | INT          | PK, AUTO INC |
| name         | VARCHAR(100) | NOT NULL     |
| muscle_group | VARCHAR(100) | NOT NULL     |
| reps         | INT          | NOT NULL     |
| sets         | INT          | NOT NULL     |

---

### 6. gym_workplan
| Column        | Type         | Constraints        |
|---------------|--------------|--------------------|
| id            | INT          | PK, AUTO INC       |
| name          | VARCHAR(100) | NOT NULL           |
| description   | TEXT         | NOT NULL           |
| duration      | INT          | NOT NULL           |
| exercise_id   | INT          | FK → gym_exercise  |
| exercise_name | VARCHAR(15)  | NOT NULL           |
| member_id     | INT          | FK → gym_member    |
| member_name   | VARCHAR(15)  | NOT NULL           |

---

### 7. gym_equipment
| Column           | Type         | Constraints  |
|------------------|--------------|--------------|
| id               | INT          | PK, AUTO INC |
| name             | VARCHAR(100) | NOT NULL     |
| type             | VARCHAR(100) | NOT NULL     |
| maintenance_date | DATETIME     | NOT NULL     |
| status           | VARCHAR(50)  | NOT NULL     |

---

## Relationships

```
gym_trainer  ──< gym_member      (one trainer → many members)
gym_member   ──< gym_membership  (one member  → many memberships)
gym_member   ──< gym_payment     (one member  → many payments)
gym_member   ──< gym_workplan    (one member  → many workout plans)
gym_exercise ──< gym_workplan    (one exercise → many workout plans)
```

---

## ER Diagram (text)

```
┌─────────────┐        ┌──────────────┐        ┌────────────────┐
│ gym_trainer │ 1────* │  gym_member  │ 1────* │ gym_membership │
│─────────────│        │──────────────│        │────────────────│
│ id (PK)     │        │ id (PK)      │        │ id (PK)        │
│ name        │        │ name         │        │ member_id (FK) │
│ specializ.. │        │ age          │        │ type           │
│ experience  │        │ email        │        │ start_date     │
│ contact     │        │ phone        │        │ end_date       │
└─────────────┘        │ trainer_id   │        │ fee            │
                       │   (FK)       │        └────────────────┘
                       └──────┬───────┘
                              │ 1
                    ┌─────────┼──────────┐
                    *         *          *
          ┌─────────────┐  ┌──────────────────┐
          │ gym_payment │  │   gym_workplan   │
          │─────────────│  │──────────────────│
          │ id (PK)     │  │ id (PK)          │
          │ member_id   │  │ name             │
          │   (FK)      │  │ description      │
          │ amount      │  │ duration         │
          │ pay_date    │  │ member_id (FK)   │
          │ method      │  │ exercise_id (FK) │
          └─────────────┘  └────────┬─────────┘
                                    * 
                           ┌────────┴──────┐
                           │ gym_exercise  │
                           │───────────────│
                           │ id (PK)       │
                           │ name          │
                           │ muscle_group  │
                           │ reps          │
                           │ sets          │
                           └───────────────┘

┌───────────────┐
│ gym_equipment │   (standalone — no FK relations)
│───────────────│
│ id (PK)       │
│ name          │
│ type          │
│ maint_date    │
│ status        │
└───────────────┘
```

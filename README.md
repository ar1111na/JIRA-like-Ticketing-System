# JIRA-like Ticketing System

## Table of Contents
- [Project Overview](#project-overview)
- [Features](#features)
- [User Stories](#user-stories)
- [System Requirements](#system-requirements)
- [Tech Stack](#tech-stack)
- [Installation Instructions](#installation-instructions)
- [Database Schema](#database-schema)
- [Future Enhancements](#future-enhancements)
- [Contributors](#contributors)

---

## Project Overview
We have created a **JIRA-like Ticketing System** that facilitates efficient task and issue management for software projects. Our system enables project managers and team members to create, assign, track, and resolve tickets, while promoting collaboration through comments and attachments. The project focuses on delivering a user-friendly task management workflow to handle software project issues.

---

## Features
- **User Authentication:** Secure registration and login with hashed passwords.
- **Ticket Creation & Management:** Users can create, assign, update, and resolve tickets.
- **Ticket Filters:** Easily filter tickets by status, priority, assignee, and due date.
- **Project Dashboard:** Aggregated view of ticket statuses and project health.
- **Comments & Attachments:** Collaboration on tickets through comments and file uploads.
- **Ticket Prioritization:** Organize tickets by priority (Low, Medium, High, Critical).
- **Deadlines:** Set and track ticket deadlines, with overdue task notifications.
- **Ticket Assignment:** Project managers can assign/reassign tickets to team members.

---

## User Stories
1. **User Registration & Authentication:** As a user, I want to securely register, log in, and manage my account details.
2. **Ticket Creation:** As a user, I want to create tickets with title, description, assignee, priority, status, and due date.
3. **Ticket Updates:** As a user, I want to update the ticket status (Open, In Progress, Resolved, Closed).
4. **Ticket Filters:** As a user, I want to filter tickets by status, assignee, priority, and due date.
5. **Ticket Assignment:** As a project manager, I want to assign tickets to specific team members.
6. **View Assigned Tickets:** As a team member, I want to view tickets assigned to me and track their progress.
7. **Project Dashboard:** As a project manager, I want to view the overall project status.
8. **Comments:** As a user, I want to comment on tickets for collaboration.
9. **Deadlines & Overdue Tracking:** As a user, I want to set deadlines for tickets and track overdue tasks.
10. **File Attachments:** As a user, I want to attach files or screenshots to tickets for better issue reporting.

---

## System Requirements
### Authentication System:
- User registration and login with secure password hashing.
- Proper session handling and user validation.

### Ticket Management:
- Create, update, and delete tickets.
- Add comments and attachments to tickets.
- Assign or reassign tickets to team members.

### Ticket Filtering:
- Filter tickets by status, assignee, priority, and due date.

### Reporting & Dashboard:
- View project metrics such as total tickets, tickets by status, overdue tickets, and tickets by priority.

---

## Tech Stack
- **Backend:**
  - Python (Flask)
  - MySQL (RDBMS)
  - RESTful API
- **Frontend:**
  - HTML/CSS
  - JavaScript
- **Other Tools:**
  - Git & GitHub for version control.
 
---

## Installation Instructions

---

## Database Schema
# Database Schema for JIRA-like Ticketing System

This section describes the database schema used for our ticketing system. The schema consists of five main tables: `Roles`, `Users`, `Tickets`, `Comments`, and `Attachments`.

## Tables Overview

### Roles Table
Stores user roles for task management purposes.

| Column Name | Data Type    | Description                    |
|-------------|--------------|--------------------------------|
| role_id     | Primary Key  | Unique identifier for each role |
| role        | VARCHAR      | Name of the role                |

### Users Table
Stores information about users, including their credentials and roles.

| Column Name   | Data Type    | Description                           |
|---------------|--------------|---------------------------------------|
| user_id       | Primary Key  | Unique identifier for each user       |
| username      | VARCHAR      | Username of the user                  |
| email         | VARCHAR      | Email address of the user             |
| password_hash | VARCHAR      | Hashed password for security         |
| role_id       | Foreign Key  | References `Roles.role_id`            |
| created_at    | TIMESTAMP    | Timestamp of when the user was created |

### Tickets Table
Stores details about the tickets/issues in the system.

| Column Name  | Data Type    | Description                                        |
|--------------|--------------|----------------------------------------------------|
| ticket_id    | Primary Key  | Unique identifier for each ticket                  |
| title        | VARCHAR(255) | Title of the ticket                                |
| description  | TEXT         | Detailed description of the ticket                 |
| priority     | ENUM         | Priority level (e.g., Low, Medium, High, Critical) |
| status       | ENUM         | Current status (e.g., Open, In Progress, Resolved, Closed) |
| assignee_id  | Foreign Key  | References `Users.user_id`                         |
| reporter_id  | Foreign Key  | References `Users.user_id`                         |
| due_date     | DATE         | Due date for the ticket                            |
| created_at   | TIMESTAMP    | Timestamp when the ticket was created              |
| updated_at   | TIMESTAMP    | Timestamp of the last ticket update                |

### Comments Table
Stores comments added to tickets for collaboration purposes.

| Column Name  | Data Type    | Description                            |
|--------------|--------------|----------------------------------------|
| comment_id   | Primary Key  | Unique identifier for each comment     |
| comment_text | TEXT         | The actual content of the comment      |
| user_id      | Foreign Key  | References `Users.user_id`             |
| ticket_id    | Foreign Key  | References `Tickets.ticket_id`         |
| created_at   | TIMESTAMP    | Timestamp of when the comment was created |

### Attachments Table
Stores attachments associated with tickets for enhanced issue reporting.

| Column Name   | Data Type    | Description                                |
|---------------|--------------|--------------------------------------------|
| attachment_id | Primary Key  | Unique identifier for each attachment      |
| ticket_id     | Foreign Key  | References `Tickets.ticket_id`             |
| file_path     | VARCHAR(255) | File path to the stored attachment         |
| uploaded_at   | TIMESTAMP    | Timestamp of when the attachment was uploaded |

---

## Future Enhancements
- **Activity Log:** Track user actions like ticket creation, updates, and comments.
- **Email Notifications:** Send email notifications when a ticket is assigned or updated.
- **Sprint Management:** Group tickets into sprints for time-based tracking.
- **Tagging System:** Allow users to add tags to tickets for better categorization.

---

# Contributors
- Mahammad Abdullayev
- Benjamin Adebanjo Ikuesan
- Arina Semianiuk

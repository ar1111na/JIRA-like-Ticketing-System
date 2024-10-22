# Debug Dynasty: JIRA-like Ticketing System

## Table of Contents
- [Project Overview](#project-overview)
- [Features](#features)
- [User Stories](#user-stories)
- [System Requirements](#system-requirements)
- [Tech Stack](#tech-stack)
- [Installation Instructions](#installation-instructions)
- [Database Schema](#database-schema)
- [API Endpoints](#api-endpoints)
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

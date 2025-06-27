# Event Management System

A Django-based web application for managing events, attendees, and tickets. It includes user authentication, ticket booking, search functionality, and downloadable ticket PDFs with QR codes.

## Features

- User registration and login
- Only authenticated users can create, update, or delete events and tickets
- Anyone can view and search events
- Attendees can register and book tickets for events
- Each ticket is generated with user details, event info, and status
- Tickets can be viewed and downloaded as a PDF
- QR code generation included on each confirmed ticket
- Admin panel for managing all records

## Tech Stack

- Python 3.8+
- Django 4.2
- Bootstrap 5 (with dark theme)
- SQLite3 (default, can be switched to PostgreSQL or MySQL)
- WeasyPrint (for PDF generation)
- qrcode (for generating ticket QR codes)

## Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/your-username/Event_Management_System.git
cd Event_Management_System

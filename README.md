# Fortis



## Link for the website
http://77.110.116.47

## Description

**Fortis** is a web platform that connects soldiers in need of assistance with volunteers ready to help. Soldiers can submit aid requests, while volunteers can browse, filter, and fulfill those requests. The project’s goal is to build an effective bridge between those who need help and those who can provide it.


## Motivation

This project was developed as part of the “Basics of Programming” course. Our aim was to combine practical web development experience with a meaningful social impact. **Fortis** is our way of supporting soldiers and volunteers through modern technology.


## Features

- **User roles**: Two types of accounts — soldiers and volunteers.
- **Request creation**: Soldiers can describe what they need (text, tags, location, etc.).
- **Browse requests**: Volunteers can view a list of open requests.
- **Search & filter**: Volunteers can filter requests by categories and the closest request to the choosen location.
- **Claim request**: Volunteers can "take request" to begin helping.
- **Mark as completed**: Volunteers mark requests as fulfilled once the task is done.


## Tech Stack

- **Frontend**: Angular 19, TypeScript, HTML/CSS,SweetAlert2, FormsModule, ReactiveFormsModule, Angular Router
- **Backend**: FastAPI (Python)
- **Database**: PostgreSQL
- **Other**: Docker, REST API, JWT for authentication
- **Server**: Uvicorn
- **Validation**: Pydantic
- **orm**: SQLAlchemy


## Getting Started

1. Clone the repository:

```bash
git clone https://github.com/weqpro/OpMiniProject3.git
```

2. Navigate to the project directory:
```bash
cd OpMiniProject3
```
3. Launch the project with Docker Compose:
```bash
docker-compose up --build
```
## Example of use:

### Soldier Workflow:
- A soldier registers on the website.
- Goes to the “New Request” section.
- Fills in a form (e.g., “Need a power bank near Kupiansk”).
- Submits the request and waits for a volunteer to respond.

### Volunteer Workflow:
- A volunteer logs into the platform.
- Browses the list of open requests.
- Chooses a request and clicks "Take request".
- After delivering the aid, marks the request as "Completed".

### Full Example:
A soldier requests a medical kit. A volunteer sees the request, accepts it, delivers the kit, and marks it as fulfilled. Both users can track the request in their dashboards.


## Team

- Konovalenko Stanislav
- Vus Yuliana
- Prytula Daryna
- Pereima Sofia

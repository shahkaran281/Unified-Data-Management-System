# DSCI 551 - Hybrid Database System

## Project Overview
This project involves designing and implementing a hybrid database system that integrates both SQL and NoSQL data models. The system will handle YouTube analytics data using a relational database and Air Traffic Landing statistics at San Francisco International Airport (SFO) using a NoSQL database.

## System Design
### 1. Relational Model (SQL)
**Dataset:** [YouTube Global Statistics 2023](https://www.kaggle.com/datasets/nelgiriyewithana/global-youtube-statistics-2023)

- **Entities:**
  - Creator
  - Video Statistics
  - Country Details
  - Subscribers
  - Monetary Statistics
- **Implementation Details:**
  - Data is extracted, filtered, and normalized into relational tables.
  - A Python-based custom key-value store enables efficient joins and projections.
  - UUIDs ensure uniqueness and prevent hash conflicts.

### 2. Non-Relational Model (NoSQL)
**Dataset:** [SFO Air Traffic Landing Statistics](https://www.kaggle.com/datasets/lostinworlds/sf-air-traffic-landing-statistics)

- **Collections:**
  - Airlines
  - AirportRegions
  - AircraftDetails
- **Implementation Details:**
  - Data is stored in JSON format, simulating NoSQL collections.
  - Schema is adjustable on the fly for flexibility.

## Team Members
### **Karan Manishkumar Shah**
- **Role:** NoSQL Database Specialist
- **Skills:** NoSQL systems, data modeling, data integration
- **Responsibilities:**
  - Implement NoSQL database structure
  - Define schema and queries
  - Ensure data consistency and scalability

### **Aniket Kumar**
- **Role:** SQL Database Specialist
- **Skills:** SQL, relational schema design, query optimization
- **Responsibilities:**
  - Implement relational database schema
  - Optimize SQL queries
  - Develop stored procedures

## Getting Started
1. Clone the repository:
   ```bash
   git clone https://github.com/your-repo-name.git
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the database setup:
   ```bash
   python setup.py
   ```

## License
This project is open-source and available under the [MIT License](LICENSE).

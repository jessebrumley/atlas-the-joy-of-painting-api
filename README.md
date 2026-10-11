# Bob Ross Paintings: ETL Pipeline & REST API

A full-stack data engineering project that ingests raw, unstructured Bob Ross painting datasets, transforms them through a custom Python ETL pipeline, loads them into a fully normalized relational MySQL database, and exposes the data via a Flask REST API.

This project was built to demonstrate proficiency in data ingestion, file parsing, schema normalization, and backend API design.

---

## Architecture & Tech Stack

* **Language:** Python 3.x
* **Framework:** Flask (REST API)
* **Database & Management:** MySQL, Relational Database Design (RDBMS)
* **Data Handling:** Pandas / Custom Python File Parsing (JSON, CSV, unstructured text)
* **Workflow & Tools:** Git, GitHub, Linux/Unix CLI

---

## Data Pipeline & ETL Architecture

To convert disparate, untyped source datasets into structured relational tables, this project implements a custom extraction and transformation pipeline located in `/etl_data_transformation`:

1. **Ingestion & Parsing (`/scripts`)**: Custom Python scripts (`parse_colors.py`, `parse_episodes.py`, `parse_subjects.py`) ingest raw multi-source text and flat files, executing string cleaning, type casting, and data validation.
2. **Staging & Intermediate Transformation**: Cleaned records are normalized into intermediate CSV structures (`/data`) to eliminate anomalies, check for duplication, and format datetime objects.
3. **Database Loading**: Processed datasets are loaded into a normalized relational schema with strict data types, primary keys, and foreign key constraints.

---

## Database Schema & Normalization

To eliminate data redundancy and maintain referential integrity, the raw data is structured across normalized tables:

* **`episodes`**: Stores broadcast metadata (Episode ID, Code, Title, Date).
* **`paintings`**: Stores visual and media assets (Painting ID, Image URL, Title, Season, Episode reference, Color Count, YouTube Embed).
* **`colors`**: Normalized master list of unique oil paint colors and their HEX codes.
* **`subjects`**: Normalized master list of painting visual subjects (e.g., mountains, lakes, cabins).
* **Junction / Bridging Tables**: 
  * `painting_colors`: Manages the many-to-many relationship between paintings and multiple paint colors.
  * `episode_subjects`: Manages the many-to-many relationship between episodes and multiple subject categories.

---

## API Endpoints & Query Filtering

The Flask backend (`app.py`) provides a query-driven REST endpoint supporting multi-parameter filtering, custom logical operators (`any` vs `all`), and robust error handling.

### Get Episodes
* **URL:** `/episodes`
* **Method:** `GET`
* **Query Parameters:**
  * `month`: Month number (`1-12`) or full name (e.g., `"January"`).
  * `subject`: Comma-separated list of subjects (e.g., `"mountain,lake"`).
  * `color`: Comma-separated list of colors (e.g., `"black_gesso,bright_red"`).
  * `filter_type`: Logical matching rule (`all` or `any`, default is `all`).

**Example Request:**
```bash
GET /episodes?month=1&subject=mountain,lake&color=black_gesso,bright_red&filter_type=any

```bash
GET /episodes?month=1&subject=mountain,lake&color=black_gesso,bright_red&filter_type=any

Example Response:

[
    {
        "episode_id": 1,
        "episode": "The Joy of Painting - Mountain and Lake",
        "title": "Mountain and Lake",
        "date": "1983-01-10"
    },
    ...
]
```

## Local Setup & Installation
### Clone the Repository:

```bash
git clone [https://github.com/jessebrumley/bob-ross-paintings-api.git](https://github.com/jessebrumley/bob-ross-paintings-api.git)
cd bob-ross-paintings-api
```
### Install Dependencies:

```bash
pip install -r requirements.txt
```
### Configure the Database:
* Ensure MySQL server is running locally.
* Create the database: CREATE DATABASE bob_ross_paintings;
* Import the schema and seed data from jop_sql.sql or run the ETL pipeline scripts in etl_data_transformation/.
* Update database credentials in app.py under db_config.

### Run the Application:
```bash
python app.py
```
The API will be accessible at http://localhost:5000.

## Author

**Jesse Brumley**  
[GitHub](https://github.com/jessebrumley) | [Website](https://hirejesse.dev) | [LinkedIn](https://linkedin.com/in/jessebrumley)
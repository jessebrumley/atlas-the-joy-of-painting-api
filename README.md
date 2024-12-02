# Bob Ross Paintings API

This project provides an API to retrieve information about Bob Ross's painting episodes. The API allows filtering episodes by various criteria such as subject matter, color palette, and the month of the original broadcast. 

## Features

- **Filter by month**: Filter episodes by the month of the original broadcast (numeric or name).
- **Filter by subject**: Filter episodes by specific subjects (e.g., mountain, lake, tree).
- **Filter by color**: Filter episodes by colors used in the paintings (e.g., black gesso, bright red).
- **Filter logic**: Support for filtering episodes by all or any of the given criteria.
- **Database-backed**: Uses a MySQL database to store and retrieve episode data.

## Prerequisites

To run this project locally, you'll need:

- Python 3.x
- Flask
- MySQL (or MariaDB)
- MySQL connector for Python

## Setup Instructions

1. Clone the repository:

    ```bash
    git clone <repository-url>
    cd bob-ross-paintings-api
    ```

2. Install the required Python packages:

    ```bash
    pip install -r requirements.txt
    ```

3. Set up the MySQL database:

    - Make sure you have a MySQL server running.
    - Create a database called `bob_ross_paintings` (or update `db_config` in `app.py` with your own database credentials).
    - Populate the database with relevant tables (`episodes`, `paintings`, `painting_colors`, `colors`, `episode_subjects`, `subjects`).

4. Run the Flask application:

    ```bash
    python app.py
    ```

5. The API will be accessible at `http://localhost:5000`.

## API Endpoints

### Get Episodes

Retrieve episodes with optional filtering by month, subject, and color.

- **URL**: `/episodes`
- **Methods**: `GET`
- **Query Parameters**:
    - `month`: Month number (1-12) or full month name (e.g., "January").
    - `subject`: Comma-separated list of subjects (e.g., "mountain,lake").
    - `color`: Comma-separated list of colors (e.g., "black_gesso,bright_red").
    - `filter_type`: Type of filtering (`all` or `any`, default is `all`).
  
**Example Request**:

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

### Author
[Jesse Brumley](https://github.com/jessebrumley)
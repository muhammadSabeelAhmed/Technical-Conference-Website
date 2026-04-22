# Google Cloud Summit 2026 - 1 Day Event Planner

This is a web application for a 1-day technical conference focused on Google Cloud Technologies. It features a schedule of 8 talks, 1 lunch break, and allows users to search by talk title, speaker name, and category.

## Tech Stack
- **Backend:** Python, Flask
- **Frontend:** HTML5, CSS3 (Vanilla, Custom Variables, Flexbox), JavaScript (Vanilla)

## Setup and Installation

### Prerequisites
- Python 3.8+ installed on your system.

### 1. Create a Virtual Environment
Navigate to the project directory and create a virtual environment:
```bash
cd "/Users/sabeel/Desktop/AI Learning/BuildWithAntiGravity/1DayEventPlanner"
python3 -m venv venv
```

### 2. Activate the Virtual Environment
- **Mac/Linux:**
  ```bash
  source venv/bin/activate
  ```
- **Windows:**
  ```bash
  venv\Scripts\activate
  ```

### 3. Install Dependencies
Install the required packages using pip:
```bash
pip install -r requirements.txt
```

### 4. Run the Application
Start the Flask development server:
```bash
flask run
```
Or alternatively:
```bash
python app.py
```

The application will be running at `http://127.0.0.1:5000/`.

## Project Structure
- `app.py`: Main Flask application containing the dummy data and routing logic.
- `templates/index.html`: The HTML template.
- `static/css/style.css`: The CSS stylesheet with premium dark mode styling.
- `static/js/script.js`: Client-side logic for real-time search and filtering.

## Customization
To modify the talks, open `app.py` and edit the `talks` list inside the script. You can change the titles, add new speakers, adjust times, or modify the categories. The frontend will automatically reflect these changes.

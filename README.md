# Stepford County Railway Route Randomizer

This is a simple web application that randomizes routes for the Stepford County Railway game, allowing users to select a difficulty level.

## Features

*   Randomizes starting and ending stations for a route.
*   Difficulty slider to influence the randomization (though currently, the `random.seed` is removed for true randomness).
*   Modern dark theme for a pleasant user experience.

## Setup and Installation

To get this project up and running on your local machine, follow these steps:

1.  **Clone the repository (if you haven't already):**
    ```bash
    git clone https://github.com/Samm8g/StepfordCountyRailwayRouteRandomizer.git
    cd StepfordCountyRailwayRouteRandomizer
    ```

2.  **Create and activate a Python virtual environment:**
    ```bash
    python3 -m venv .venv
    source .venv/bin/activate
    ```

3.  **Install Flask:**
    ```bash
    .venv/bin/pip install Flask
    ```

## Usage

1.  **Start the Flask application:**
    ```bash
    .venv/bin/python main.py
    ```
    The application will typically run on `http://127.0.0.1:5001`.

2.  **Open your web browser:**
    Navigate to `http://127.0.0.1:5001`.

3.  **Randomize a Route:**
    *   Adjust the difficulty slider (1-5) to your preference.
    *   Click the "Randomize Route" button.
    *   The randomized starting and ending stations will be displayed below the button.

## Technologies Used

*   **Backend:** Python (Flask)
*   **Frontend:** HTML, CSS, JavaScript

## Upcoming Ideas

*   Themed colors for stations (e.g., start/end points).
*   More true randomness (e.g., avoiding immediate repeats).
*   Ability to log generated routes.
*   Checker to see unvisited stations.

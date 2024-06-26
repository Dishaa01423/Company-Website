# The Best Company

This is a Streamlit application that presents information about "The Best Company" and showcases its team members.

## Features

- Displays a company description.
- Presents a list of team members with their roles and photos.
- Uses a responsive layout with columns to organize team members.

## Requirements

- Python 3.x
- `streamlit` library
- `pandas` library
- A CSV file (`data1.csv`) containing team member data with the following columns:
  - `first name`
  - `last name`
  - `role`
  - `image` (URL or path to the image)

## Setup

1. Clone the repository:

    ```sh
    git clone https://github.com/your-username/your-repo.git
    cd your-repo
    ```

2. Install the required packages:

    ```sh
    pip install streamlit pandas
    ```

3. Ensure you have a `data1.csv` file in the same directory with the required columns.

## Usage

1. Run the Streamlit app:

    ```sh
    streamlit run app.py
    ```

2. Open the provided URL in your web browser to view the app.

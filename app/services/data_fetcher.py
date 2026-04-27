import os
import json
import requests
from datetime import datetime


def fetch_and_save_data(url: str, save_dir: str = "data/raw"):

    try:
        # Step 1: Make API request
        response = requests.get(url, timeout=10)

        # Step 2: Check if request was successful
        if response.status_code != 200:
            print(f"Error: Received status code {response.status_code}")
            return

        # Step 3: Convert response to JSON
        data = response.json()

        # Step 4: Create directory if it doesn't exist
        os.makedirs(save_dir, exist_ok=True)

        # Step 5: Create filename with timestamp
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        file_path = os.path.join(save_dir, f"comments.json")

        # Step 6: Save JSON data
        with open(file_path, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4)

        print(f"Data successfully saved to {file_path}")

    except requests.exceptions.Timeout:
        print("Error: Request timed out")

    except requests.exceptions.RequestException as e:
        print(f"Error: API request failed -> {e}")

    except Exception as e:
        print(f"Unexpected error: {e}")
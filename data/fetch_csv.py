# Downloads CSV files from TfL using the filtered CSV file names and stores them in tfl_cycling_data

import requests
import os
import time

def fetch_csv(filtered_csv_files, base_url, download_folder, retries=3, delay=5):
    # Ensure download directory exists
    os.makedirs(download_folder, exist_ok=True)

    # Read list of filenames from CSV
    with open(filtered_csv_files, 'r') as f:
        csv_list = f.read().splitlines()

    # Download files
    for filename in csv_list:
        file_url = f"{base_url}{filename}"
        output_path = os.path.join(download_folder, filename)

        if os.path.exists(output_path):
            print(f"Skipping {filename} (already downloaded)")
            continue  # Skip if file already exists

        attempt = 0
        while attempt < retries:
            try:
                print(f"Downloading {file_url} (Attempt {attempt + 1}/{retries})...")
                response = requests.get(file_url, timeout=60)  # Set timeout
                response.raise_for_status()  # Raise an error for bad responses

                with open(output_path, 'wb') as file:
                    file.write(response.content)

                print(f"Saved: {output_path}")
                break  # Exit loop if download is successful

            except requests.exceptions.RequestException as e:
                print(f"Error downloading {file_url}: {e}")
                attempt += 1
                if attempt < retries:
                    print(f"Retrying in {delay} seconds...")
                    time.sleep(delay)
                else:
                    print(f"Failed to download {file_url} after {retries} attempts.")

    print("Download process completed.")

if __name__ == "__main__":
    filtered_csv_files = 'filtered_cycle_data.csv'
    base_url = 'https://cycling.data.tfl.gov.uk/usage-stats/'
    download_folder = 'tfl_cycling_data'

    fetch_csv(filtered_csv_files, base_url, download_folder)
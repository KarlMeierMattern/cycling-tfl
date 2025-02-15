# Downloads CSV files from TfL using the filtered CSV file names and stores them in tfl_cycling_data

import requests
import os

def fetch_csv(filtered_csv_files, base_url, download_folder):

    # Define base URL and output folder
    os.makedirs(download_folder, exist_ok=True)

    ## Read list of names of all files from a separate CSV - can't scrape them from website as they're hidden
    with open(filtered_csv_files, 'r') as f:
        csv_list = f.read().splitlines()

    # Step 3: Download files
    for filename in csv_list:
        file_url = f"{base_url}{filename}"
        output_path = os.path.join(download_folder, filename)

        if not os.path.exists(output_path):  # Avoid re-downloading
            print(f"Downloading {file_url}...")
            response = requests.get(file_url)

            if response.status_code == 200:
                with open(output_path, 'wb') as file:
                    file.write(response.content)
                print(f"Saved: {output_path}")
            else:
                print(f"Failed to download: {file_url} (Status {response.status_code})")

    print("Download process completed.")

if __name__ == "__main__":
    filtered_csv_files = 'filtered_cycle_data.csv'
    base_url = 'https://cycling.data.tfl.gov.uk/usage-stats/'
    download_folder = 'tfl_cycling_data'
    fetch_csv(filtered_csv_files, base_url, download_folder)
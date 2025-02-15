# Inputs full cycle_data.csv with all file names, filters for relevant data, and outputs to filterd_cycle_data

import csv
import urllib.parse

def filter_files(input_csv, output_csv, start_range, end_range):
    # Read in csv files

    with open(input_csv, mode='r') as infile:
        reader = csv.reader(infile)

        # empty list to store csv file names
        filtered_files = []

        # loop over files names and filter by first 3 digits
        for row in reader:
            file_name = row[0]
            
            # convert URL-encoded characters back to original names
            decoded_file_name = urllib.parse.unquote(file_name)
            
            # Extract the first three digits
            try:
                first_three_digits = int(decoded_file_name[:3])  # Extract the first three digits
            except ValueError:
                # Skip files that don't have valid first three digits
                continue

            # Step 3: Check if the first three digits fall within the specified range
            if start_range <= first_three_digits <= end_range:
                filtered_files.append(row)

    # Step 4: Write the filtered file names to the output CSV
    with open(output_csv, mode='w', newline='') as outfile:
        writer = csv.writer(outfile)
        writer.writerows(filtered_files)

    print(f"Filtered file names saved to '{output_csv}'.")

if __name__ == "__main__":
    input_csv = 'cycle_data.csv'  # The CSV with all file names
    output_csv = 'filtered_cycle_data.csv'  # The new CSV to save the filtered file names
    start_range = 246  # Start range for filtering (inclusive)
    end_range = 386  # End range for filtering (inclusive)

    # Call the filter function
    filter_files(input_csv, output_csv, start_range, end_range)
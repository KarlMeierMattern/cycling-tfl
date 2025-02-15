# Scrape all CSV file names from TfL website and save them to cycle_data.csv

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import csv
import time

def scrape_tfl_bike_data(url, storage_file):
    # Set up the WebDriver for Chrome
    driver = webdriver.Chrome()

    # Open the TfL cycling data page
    driver.get(url)

    # Wait for 30 seconds to let the page load completely
    time.sleep(30)

    # Wait until all links containing ".csv" are visible
    try:
        WebDriverWait(driver,20).until(
            EC.presence_of_all_elements_located((By.XPATH, '//a[contains(@href, ".csv")]'))
        )
    except TimeoutException:
        print("Timed out waiting for page to load!")

    # Find all links containing ".csv"
    file_elements = driver.find_elements(By.XPATH, '//a[contains(@href, ".csv")]')

    # Extract file names from the href attribute
    filenames = [element.get_attribute('href').split('/')[-1] for element in file_elements]

    # Write the file names to a CSV file (cycle_data.csv)
    with open(storage_file, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Filename'])  # Write the header
        for filename in filenames:
            writer.writerow([filename])  # Write each file name

    # Close the WebDriver
    driver.quit()

    print(f"File names saved to 'cycle_data.csv'.")

if __name__ == "__main__":
    storage_file = 'cycle_data.csv'
    url = 'https://cycling.data.tfl.gov.uk/'
    scrape_tfl_bike_data(url, storage_file)
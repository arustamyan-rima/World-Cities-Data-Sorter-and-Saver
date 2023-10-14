# World-Cities-Data-Sorter-and-Saver

This project involves reading a CSV file named 'worldcities.csv' with the CSV-Reader, sorting the entries by 'city_ascii', and saving the sorted entries in a new data file named 'worldcities_sorted.csv'. The script includes functions to load the cities from the CSV file, sort the cities by their ASCII names, and save the sorted cities to a new file.

### Project Structure

- The main script is named `world_cities.py`.
- The script utilizes the CSV library for reading and writing CSV files.
- The script includes three main functions: `load_cities`, `sort_cities_by_ascii_name`, and `save_cities_to_file`.

### Usage

Ensure you have the necessary libraries installed to run the code. You can run the script using Python.

The script will read the data from the 'worldcities.csv' file, sort the cities by their ASCII names, and save the sorted cities to a new file named 'worldcities_sorted.csv'.

### Functions
The script includes the following functions:  

load_cities: Loads cities from a CSV file and returns a list.  
sort_cities_by_ascii_name: Sorts the cities by the 'city_ascii' column.  
save_cities_to_file: Saves the sorted rows to a new file.  

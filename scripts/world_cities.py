# read the file worldcities.csv with the CSV - Reader,
# sort the entries by city_ascii and save them in a
# new data worldcities_sorted.csv.
# Write the function load_cities, sort_cities_by_ascii_name and
# save_cities_to_file.


import csv
from pathlib import Path


def load_cities(filename, country=None):
    """Load Cities from CSV File and return list."""
    list = []
    with open(Path(__file__).parent / filename, encoding="utf-8") as f:
        reader=csv.reader(f, delimiter = ',')
        header = next(reader)
        for line in reader:
            
            # Country Filter
            if country and isinstance(country, str):
                if line[4].lower() == country.lower():
                    list.append(line)
                continue
            list.append(line)
    return list, header


def sort_cities_by_ascii_name(list):
    """Sort cities by column ascii_name."""
    result = sorted(list, key = lambda x: x[1])
    return result
    

def save_cities_to_file(filename, list, header):
    """Save rows to file."""
    with open(Path(__file__).parent / filename, 'w', newline = '', encoding="utf-8") as f:
        writer=csv.writer(f, delimiter = ',')
        writer.writerow(header)
        writer.writerows(list)


def main():
    FILE_IN = "worldcities.csv"
    FILE_OUT = "worldcities_sorted_germany.csv"
    list, header = load_cities(FILE_IN, country = "Germany")
    sorted_cities = sort_cities_by_ascii_name(list)
    save_cities_to_file(FILE_OUT, sorted_cities, header)


main()
    
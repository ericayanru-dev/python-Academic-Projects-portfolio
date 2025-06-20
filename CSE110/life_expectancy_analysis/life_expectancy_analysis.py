"""
Author: Eric Ayanru
Course: CSE110
Project: Life Expectancy Data Analysis

Description:
This program analyzes life expectancy data from a CSV file. It reports:
- The overall minimum and maximum life expectancies in the dataset
- For a year of interest entered by the user:
    - The average life expectancy
    - The country with the highest and lowest life expectancy
"""

def main():
    filename = "CSE110/life_expectancy_analysis/life-expectancy.csv"

    try:
        with open(filename, "r") as file:
            year_of_interest = int(input("Enter the year of interest: "))
            next(file)  # Skip header

            # Overall stats
            global_min = float("inf")
            global_max = float("-inf")
            global_min_country = ""
            global_max_country = ""
            global_min_year = 0
            global_max_year = 0

            # Year-specific stats
            year_min = float("inf")
            year_max = float("-inf")
            year_min_country = ""
            year_max_country = ""
            year_total = 0
            year_count = 0

            for line in file:
                parts = line.strip().split(",")
                if len(parts) != 4:
                    continue  # Skip malformed lines

                country = parts[0]
                try:
                    year = int(parts[2])
                    life_expectancy = float(parts[3])
                except ValueError:
                    continue  # Skip rows with invalid numbers

                # Global min/max
                if life_expectancy < global_min:
                    global_min = life_expectancy
                    global_min_country = country
                    global_min_year = year

                if life_expectancy > global_max:
                    global_max = life_expectancy
                    global_max_country = country
                    global_max_year = year

                # Year-specific calculations
                if year == year_of_interest:
                    year_total += life_expectancy
                    year_count += 1

                    if life_expectancy < year_min:
                        year_min = life_expectancy
                        year_min_country = country

                    if life_expectancy > year_max:
                        year_max = life_expectancy
                        year_max_country = country

            # Display results
            print(f"\nGlobal Statistics:")
            print(f"The min life expectancy was {global_min:.2f} from {global_min_country} in {global_min_year}")
            print(f"The max life expectancy was {global_max:.2f} from {global_max_country} in {global_max_year}")

            print(f"\nStatistics for the year {year_of_interest}:")
            if year_count > 0:
                average = year_total / year_count
                print(f"Average life expectancy: {average:.2f}")
                print(f"Max life expectancy: {year_max:.2f} in {year_max_country}")
                print(f"Min life expectancy: {year_min:.2f} in {year_min_country}")
            else:
                print("No data available for that year.")

    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")

if __name__ == "__main__":
    main()

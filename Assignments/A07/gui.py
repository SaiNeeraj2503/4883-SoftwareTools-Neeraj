import PySimpleGUI as sg
import csv
import calendar
from datetime import datetime

Filter=""
def readAirportCodes():
    airport_codes = []
    with open('airport-codes.csv', 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        next(reader)  # Skip header row
        for row in reader:
            airport_codes.append(row[0])
    return airport_codes

def buildWeatherURL(month=None, day=None, year=None, Code=None, filter=None):
   

    if not month:
        month = 1
    if not day:
        day = 1
    if not year:
        year = 2023
    if not Code:
        Code = "YPJT"
    if not filter:
        filter = "daily"

    # Define the range of values for month, day, and year
    month_range = list(range(1, 13))
    day_range = list(range(1, 32))
    year_range = list(range(1900, 2024))  # Assuming years up to 2023 are valid

    # Read airport codes from CSV
    airport_codes = readAirportCodes()
    

    # Create the GUI layout using dropdown lists
    
    layout = [
    [sg.Text('Month', size=(10, 1)), sg.DropDown(month_range, default_value=month, key='-MONTH-', enable_events=True)],
    [sg.Text('Day', size=(10, 1)), sg.DropDown(day_range, default_value=day, key='-DAY-', enable_events=True)],
    [sg.Text('Year', size=(10, 1)), sg.DropDown(year_range, default_value=year, key='-YEAR-', enable_events=True)],
    [sg.Text('Code', size=(10, 1)), sg.DropDown(airport_codes, key='-CODE-')],
    [sg.Text('Daily / Weekly / Monthly', size=(20, 1)), sg.DropDown(['daily', 'weekly', 'monthly'], key='-FILTER-')],
    [sg.Submit(), sg.Cancel()]
    ]

    window = sg.Window('Get The Weather', layout, size=(300, 200))



    while True:
        event, values = window.read()

        # Handle events from dropdown lists
        if event == '-MONTH-':
            selected_month = int(values['-MONTH-'])
            max_days = calendar.monthrange(int(year), selected_month)[1]
            window['-DAY-'].update(values=list(range(1, max_days + 1)))
        elif event == '-YEAR-':
            selected_year = int(values['-YEAR-'])
            selected_month = int(values['-MONTH-'])
            max_days = calendar.monthrange(selected_year, selected_month)[1]
            window['-DAY-'].update(values=list(range(1, max_days + 1)))

        if event == sg.WINDOW_CLOSED or event == 'Close':
            break
        elif event == 'Submit':
            month = int(values['-MONTH-'])
            day = int(values['-DAY-'])
            year = int(values['-YEAR-'])
            code = values['-CODE-']
            filter = values['-FILTER-']
            

            sg.popup('You entered', f"Month: {month}, Day: {day}, Year: {year}, Code: {code}, Filter: {filter}")

            # Return the URL to pass to wunderground to get appropriate weather data
            return f"http://www.wunderground.com/history/{filter}/{code}/date/{year}-{month:02d}-{day:02d}",filter
            

    window.close()


if __name__ == '__main__':
    buildWeatherURL()

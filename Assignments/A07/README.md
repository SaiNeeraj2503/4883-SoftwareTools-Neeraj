# A07 : Web Scraping
## Name: Sai Neeraj Chandragiri
## Project Description :
This application allows users to retrieve weather data from Wunderground by providing specific parameters through a data entry form. The application utilizes PySimpleGUI for creating the form, Selenium for obtaining async data from Wunderground, and BeautifulSoup (BS4) for parsing the data. The retrieved data is then displayed in a tabular view using PySimpleGUI.

## Features

- Data entry form with the following fields:
  - Day: Select the day of the month.
  - Month: Select the month.
  - Year: Select the year.
  - Airport: Select the airport code.
  - Filter: Select the desired data filter (daily, weekly, or monthly).
- Submitting the form generates the appropriate URL to query Wunderground for the specified weather data.
- Selenium is used to obtain the async data sent back from Wunderground.
- BeautifulSoup is used to parse the data and extract the requested information.
- The retrieved data is displayed in a tabular view using PySimpleGUI.

## Usage

1. Run the application:


   gui.py  in visual code application.

2. Fill in the data entry form with the desired parameters:
   - Select the day, month, year, airport, and filter options.
   - Click the "Submit" button to retrieve the weather data.

3. The application will generate the URL based on the provided parameters and use Selenium to obtain the data from Wunderground.

4. Once the data is retrieved and parsed, it will be displayed in a tabular view using PySimpleGUI.

5. Review the weather data in the tabular view. You can scroll through the table to view all the data.

6. To exit the application, click the "Close" button or close the window.

## Files

| S.No  | File  | Description |    
| :---:   | :---: | :---: |
|    1  |  [airport-codes.csv](https://github.com/SaiNeeraj2503/4883-SoftwareTools-Neeraj/blob/main/Assignments/A07/airport-codes.csv)  | airport data for the GUI and scraping   |
| 2  | [gui.py](https://github.com/SaiNeeraj2503/4883-SoftwareTools-Neeraj/blob/main/Assignments/A07/gui.py)    | python code to create GUI   |
| 3  | [get_weather.py](https://github.com/SaiNeeraj2503/4883-SoftwareTools-Neeraj/blob/main/Assignments/A07/get_weather.py)    | python code to scrape the data from a dynamic website   |

## Output
### Case-1 : Daily Observations
![alt](https://github.com/SaiNeeraj2503/4883-SoftwareTools-Neeraj/blob/main/Assignments/A07/Output/Daily_Data%20Entry%20console.png)
![alt](https://github.com/SaiNeeraj2503/4883-SoftwareTools-Neeraj/blob/main/Assignments/A07/Output/Daily_Weather%20data%20Output.png)
### Case-2 : Monthly Observations
![alt](https://github.com/SaiNeeraj2503/4883-SoftwareTools-Neeraj/blob/main/Assignments/A07/Output/Monthly_Data%20Entry.png)
![alt](https://github.com/SaiNeeraj2503/4883-SoftwareTools-Neeraj/blob/main/Assignments/A07/Output/Montly_Weather%20data%20output.png)
### Case-3 : Weekly Observations
![alt](https://github.com/SaiNeeraj2503/4883-SoftwareTools-Neeraj/blob/main/Assignments/A07/Output/Weekly_Data%20Entry.png)
![alt](https://github.com/SaiNeeraj2503/4883-SoftwareTools-Neeraj/blob/main/Assignments/A07/Output/Weekly_Weather%20data%20output.png)




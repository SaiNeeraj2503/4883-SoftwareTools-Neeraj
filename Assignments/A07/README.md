# Project Title : Web Scraping
# Name: Sai Neeraj Chandragiri
# Project Description :
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

## Installation

1. Clone the repository:

```bash
git clone https://github.com/your/repository.git
```

2. Install the required dependencies:

```bash
pip install -r requirements.txt
```

3. Download and install the ChromeDriver executable suitable for your operating system from the [ChromeDriver website](https://sites.google.com/a/chromium.org/chromedriver/). Make sure to add the ChromeDriver executable to your system's PATH.

## Usage

1. Run the application:

```bash
python main.py
```

2. Fill in the data entry form with the desired parameters:
   - Select the day, month, year, airport, and filter options.
   - Click the "Submit" button to retrieve the weather data.

3. The application will generate the URL based on the provided parameters and use Selenium to obtain the data from Wunderground.

4. Once the data is retrieved and parsed, it will be displayed in a tabular view using PySimpleGUI.

5. Review the weather data in the tabular view. You can scroll through the table to view all the data.

6. To exit the application, click the "Close" button or close the window.

# Output
## Case-1 : Daily Observations
<img src=""/>

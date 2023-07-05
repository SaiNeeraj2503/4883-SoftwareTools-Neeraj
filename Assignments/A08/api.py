from fastapi import FastAPI, HTTPException, Query
from fastapi.responses import RedirectResponse
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import csv

description = """🚀
## 4883 Software Tools
### Where awesomeness happens
"""

app = FastAPI(
    description=description,
)

db = []

# Open the CSV file
with open('data.csv', 'r') as file:
    # Create a CSV reader object
    reader = csv.reader(file)

    i = 0
    # Read each row in the CSV file
    for row in reader:
        if i == 0:
            i += 1
            continue
        db.append(row)


def getUniqueCountries():
    global db
    countries = set()
    for row in db:
        countries.add(row[2])
    return list(countries)


def getUniqueRegions():
    global db
    regions = set()
    for row in db:
        regions.add(row[3])
    return list(regions)


def filterData(country=None, region=None, year=None):
    
    filtered_data = []
    for row in db:
        if country and country.lower() != row[2].lower():
            continue
        if region and region.lower() != row[3].lower():
            continue
        if year is not None and row[0][:4] != year:
            continue
        filtered_data.append(row)
    return filtered_data


def findCountryWithMaxDeaths(min_date=None, max_date=None):
    global db
   
    DeathsData=[]
    for row in db:
        if min_date is not None and row[0] < min_date:
            continue
        if max_date is not None and row[0] > max_date:
            continue
 
        DeathsData.append(row)

    max_death_row=DeathsData[0]
    for row in DeathsData:
        if int(row[7])>int(max_death_row[7]):
            max_death_row=row
    
    return{
         max_death_row[2],
         max_death_row[7]
    }

def findCountryWithMinDeaths(min_date=None, max_date=None):
    global db
    min_deaths = float('inf')
    country_with_min_deaths = None
    deathsByCountry={}
    DeathsData=[]
    for row in db:
        if min_date is not None and row[0] < min_date:
            continue
        if max_date is not None and row[0] > max_date:
            continue
        DeathsData.append(row)
    
    min_death_row=DeathsData[0]
    for row in DeathsData:
        if int(row[7])<int(min_death_row[7]):
            min_death_row=row

    return{
         min_death_row[2],
         min_death_row[7]
         }
    
@app.get("/")
async def docs_redirect():
    """Api's base route that displays the information created above in the ApiInfo section."""
    return RedirectResponse(url="/docs")


@app.get("/countries/")
async def countries():
    """
    Retrieves a list of unique countries from the database.

    - *Returns:*
      - (list) : A list of unique country names.

    #### Example:

    [http://localhost:8080/countries/](http://localhost:8080/countries/)

    #### Response:

        {
            "countries": ["Cambodia", "Guatemala", "Cabo Verde", ...],
            "success": true
        }

    """
    
    try:
        key="true"
        return {"countries": getUniqueCountries(),
                "success":key}
    except Exception as e:
        key="false"
        print("An error occurred:", str(e))
        return {"error": "An error occurred while processing the request.",
                "success":key
                }



@app.get("/regions/")
async def regions():
    """
    Fetches the unique regions from the database.

    - *Returns:*
      - (list) : A list of unique region names.

    #### Example:

    [http://localhost:8080/regions/](http://localhost:8080/regions/)

    #### Response:

        {
            "regions": ["AFRO", "AMRO", "EMRO", ...],
            "success": true
        }

    """
    try:
        key="true"
        return {"Regions": getUniqueRegions(),
                "success":key}
    except Exception as e:
        key="false"
        print("An error occurred:", str(e))
        return {"error": "An error occurred while processing the request.",
                "success":key
                }

    


@app.get("/deaths/")
async def deaths(
    country: str = Query(None, title="Country"),
    region: str = Query(None, title="Region"),
    year: str = Query(None, title="Year"),
):
    """
    Calculates the total deaths based on the provided filters (country, region, year).

    - *Params:*
      - country (str): A country name.
      - region (str): A region name.
      - year (int): A 4-digit year.

    - *Returns:*
      - (dict): A dictionary containing the total deaths based on the filters.

    #### Example 1:

    [http://localhost:8080/deaths/?country=Brazil](http://localhost:8080/deaths/?country=Brazil)

    #### Response 1:

        {
            "total_deaths": 703399,
            "success": true,
            "params": {
                "country": "Brazil",
                "region": null,
                "year": null
            }
        }

    #### Example 2:

    [http://localhost:8080/deaths/?region=EMRO&year=2023](http://localhost:8080/deaths/?region=EMRO&year=2023)

    #### Response 2:

        {
            "total_deaths": 2246,
            "success": true,
            "params": {
                "country": null,
                "region": "EMRO",
                "year": "2023"
            }
        }

    #### Example 3:

    [http://localhost:8080/deaths/](http://localhost:8080/deaths/)

    #### Response 3:

        {
            "total_deaths": 6945714,
            "success": true,
            "params": {
                "country": null,
                "region": null,
                "year": null
            }
        }

    """
    filtered_data = filterData(country, region, year)
    total_deaths = sum(int(row[6]) for row in filtered_data)
    try:
        key="true"
        return {"total_deaths": total_deaths,
                "success": key,
                "params": {
                    "country": country,
                    "region": region,
                    "year": year
                }
                }
    except Exception as e:
        key="false"
        print("An error occurred:", str(e))
        return {"error": "An error occurred while processing the request.",
                "success":key}
    
    


@app.get("/cases/")
async def cases(
    country: str = Query(None, title="Country"),
    region: str = Query(None, title="Region"),
    year: str = Query(None, title="Year"),
):
    """
    Calculates the total deaths based on the provided filters (country, region, year).

    - *Params:*
      - country (str): A country name.
      - region (str): A region name.
      - year (int): A 4-digit year.

    - *Returns:*
      - (dict): A dictionary containing the total deaths based on the filters.

    #### Example 1:

    [http://localhost:8080/cases/?country=Brazil](http://localhost:8080/cases/?country=Brazil)

    #### Response 1:

        {
            "total_cases": 37639324,
            "success": true,
            "params": {
                "country": "Brazil",
                "region": null,
                "year": null
            }
        }

    #### Example 2:

    [http://localhost:8080/cases/?region=EMRO&year=2023](http://localhost:8080/cases/?region=EMRO&year=2023)

    #### Response 2:

        {
            "total_cases": 42,
            "success": true,
            "params": {
                "country": null,
                "region": "EMRO",
                "year": 2023
            }
        }

    #### Example 3:

    [http://localhost:8080/cases/](http://localhost:8080/cases/)

    #### Response 3:

        {
            "total_cases": 768187096,
            "success": true,
            "params": {
                "country": null,
                "region": null,
                "year": null
            }
        }

    """
    
    filtered_data = filterData(country, region, year)
    total_cases = sum(int(row[4]) for row in filtered_data)
    try:
        key="true"
        return {"total_cases": total_cases,
                "success": key,
                "params": {
                    "country": country,
                    "region": region,
                    "year": year
                }
                }
    except Exception as e:
        key="false"
        print("An error occurred:", str(e))
        return {"error": "An error occurred while processing the request.",
                "success":key}
    


@app.get("/max_deaths/")
async def get_country_with_max_deaths(min_date: str = Query(None), max_date: str = Query(None)):
    """
    Calculates the country with the highest number of deaths within the given date range.

    - *Params:*
      - start_date (str): The start date in the format "YYYY-MM-DD".
      - end_date (str): The end date in the format "YYYY-MM-DD".

    - *Returns:*
      - (dict): A dictionary containing the country with the highest deaths and its death count.

    #### Example 1:

    [http://localhost:8080/max_deaths/?min_date=2021-01-01&max_date=2021-12-31](http://localhost:8080/max_deaths/?min_date=2021-01-01&max_date=2021-12-31)

    #### Response 1:

        {
            "Death_Count": "United States of America",
            "country": "819055",
            "min_date": "2021-01-01",
            "max_date": "2021-12-31",
            "success": true
        }

    #### Example 2:

    [http://localhost:8080/max_deaths/](http://localhost:8080/max_deaths/)

    #### Response 2:

        {
            "Death_Count": "1127152",
            "country": "United States of America",
            "min_date": null,
            "max_date": null,
            "success": true
            }

    """
    try:
        key="true"
        country,count = findCountryWithMaxDeaths(min_date, max_date)
        max_death={
            "Death_Count": count,
            "country":  country,
            "min_date": min_date,
            "max_date": max_date,      
             "success": key,
            }
        
        return max_death
    except Exception as e:
        key="false"
        print("An error occurred:", str(e))
        return {"error": "An error occurred while processing the request.",
                "success":key}


@app.get("/min_deaths/")
async def get_country_with_min_deaths(min_date: str = Query(None), max_date: str = Query(None)):
    """
    Calculates the country with the lowest number of deaths within the given date range.

    - *Params:*
      - start_date (str): The start date in the format "YYYY-MM-DD".
      - end_date (str): The end date in the format "YYYY-MM-DD".

    - *Returns:*
      - (dict): A dictionary containing the country with the highest deaths and its death count.

    #### Example 1:

    [http://localhost:8080/min_deaths/?min_date=2021-01-01&max_date=2021-12-31](http://localhost:8080/min_deaths/?min_date=2021-01-01&max_date=2021-12-31)

    #### Response 1:

        {
            "Death_Count":"American Samoa",
            "country":"0",
            "min_date":"2021-01-01",
            "max_date":"2021-12-31",
            "success":"true"
            }

    #### Example 2:

    [http://localhost:8080/min_deaths/](http://localhost:8080/min_deaths/)

    #### Response 2:

        {
            "Death_Count": "Afghanistan",
            "country": "0",
            "min_date": null,
            "max_date": null,
            "success": "true"
            }

    """
    try:
        key="true"
        country, count = findCountryWithMinDeaths(min_date, max_date)
        min_death={
            "Death_Count": count,
            "country":  country,
            "min_date": min_date,
            "max_date": max_date,      
             "success": key,
            }
        
        return min_death
    except Exception as e:
        key="false"
        print("An error occurred:", str(e))
        return {"error": "An error occurred while processing the request.",
                "success":key}

@app.get("/avg_deaths/")
async def avg_deaths():
    """
Calculates the average number of deaths across all countries in the database.

Returns:
(dict): A dictionary containing the average number of deaths.
Example:
http://localhost:8080/avg_deaths/

Response:

{
    "avg_deaths": 23.149139120523127
}
"""
    total_deaths = sum(int(row[6]) for row in db)
    avg_deaths = total_deaths / len(db)
    return {"avg_deaths": avg_deaths}


if __name__ == "__main__":
    uvicorn.run("api:app", host="localhost", port=8080, log_level="debug", reload=True)

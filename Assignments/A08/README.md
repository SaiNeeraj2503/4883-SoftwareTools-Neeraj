
# Description:
This code demonstrates the utilization of FastAPI to develop a RESTful API for accessing COVID-19 data.This is an API provides various endpoints to access and analyze data from a CSV file. The API allows you to retrieve information about countries, regions, deaths, cases, and more.


## Files:

|  #  | Column            | Description                       |
| :-: | :---------------- | :-------------------------------- |
|  0  | [data.csv](https://github.com/SaiNeeraj2503/4883-SoftwareTools-Neeraj/blob/main/Assignments/A08/data.csv) | file that holds covid data       |
|  1  | [api.py](https://github.com/SaiNeeraj2503/4883-SoftwareTools-Neeraj/blob/main/Assignments/A08/api.py)     |  python code for api routes     |



## Routes:
* /docs
  
[http://localhost:8080](http://localhost:8080/docs#/default/docs_redirect__get) redirect to the homepage of the FastApi Swagger UI like below snip

![image](https://github.com/SaiNeeraj2503/4883-SoftwareTools-Neeraj/assets/81518238/40d3cb6f-935c-4a54-8620-facaf7794a55)


* /country
  
  [http://localhost:8080/countries](http://localhost:8080/countries/) will provide the data of the country list like below

   ![image](https://github.com/SaiNeeraj2503/4883-SoftwareTools-Neeraj/assets/81518238/dd37e61a-0a91-49f5-86c5-3c5a545f6c9f)


* /regions
    
[http://localhost:8080/regions](http://localhost:8080/regions/) will provide the information of tjhe country codes we have in the csv
![image](https://github.com/SaiNeeraj2503/4883-SoftwareTools-Neeraj/assets/81518238/9485304a-6f27-40ae-9e88-7fcccb5588f6)


* /deaths
  
[http://localhost:8080/deaths](http://localhost:8080/deaths/) will provide the information of thr total death rates in each countries
![image](https://github.com/SaiNeeraj2503/4883-SoftwareTools-Neeraj/assets/81518238/64f40c2b-d94f-48aa-afe6-cf450674fd54)

We can also filter the death rates depending on the country, region and year as below

[http://localhost:8080/deaths/?country=Brazil&year=2023](http://localhost:8080/deaths/?country=Brazil&year=2023)
![image](https://github.com/SaiNeeraj2503/4883-SoftwareTools-Neeraj/assets/81518238/2c149a6f-fa00-4b37-9ab2-0d47b81a7bbd)


* /cases
[http://localhost:8080/cases](http://localhost:8080/cases/) will provide the cases present in all countries
![image](https://github.com/SaiNeeraj2503/4883-SoftwareTools-Neeraj/assets/81518238/db12af5a-44a6-45d1-b2e0-7618fd184e7d)

we can also search via country, region or year like below
[http://localhost:8080/cases/?country=India](http://localhost:8080/cases/?country=India) 
![image](https://github.com/SaiNeeraj2503/4883-SoftwareTools-Neeraj/assets/81518238/c6039f67-621e-4f6b-a5d2-df8a1248f578)


* /max_deaths
  
[http://localhost:8080/max_deaths/](http://localhost:8080/max_deaths/)
It can find the  most deaths counts. If min_date and max_date are provided, finds the country with the most deaths between the specified range of dates.

![image](https://github.com/SaiNeeraj2503/4883-SoftwareTools-Neeraj/assets/81518238/9019950b-0f50-4cd3-aa75-5dddf3ee3978)

[http://localhost:8080/max_deaths/?min_date=2020-01-01&max_date=2022-01-01](http://localhost:8080/max_deaths/?min_date=2020-01-01&max_date=2022-01-01)

![image](https://github.com/SaiNeeraj2503/4883-SoftwareTools-Neeraj/assets/81518238/ec893782-097d-4f56-9122-477db72aa070)


* /min_deaths

  It will fetch the countries with low deaths
  [http://localhost:8080/min_deaths](http://localhost:8080/min_deaths/)
![image](https://github.com/SaiNeeraj2503/4883-SoftwareTools-Neeraj/assets/81518238/e9bc0040-4777-4922-a4fa-a2826995d536)


* /avg_deaths

[http://localhost:8080/avg_deaths/](http://localhost:8080/avg_deaths/). Finds the average number of deaths between all countries.

![image](https://github.com/SaiNeeraj2503/4883-SoftwareTools-Neeraj/assets/81518238/16ee3741-91ac-47bb-95b0-f4f2409e47b5)




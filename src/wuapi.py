## 
## Created By: Gabriel Gonzalez (contact me at gabeg@bu.edu) 
## 
## 
## NAME:
## 
##     wuapi.py
## 
## 
## SYNTAX: 
## 
##     python wuapi.py [ ZIPCODE ] [ HOURS ]
## 
## 
## PURPOSE:
## 
##     Weather Underground API which gives useful information on the
##     current weather conditions in a given zipcode. Used in the 
##     main "weather" script to get the current weather conditions.
## 
## 
## KEYWORDS:
## 
##     ZIPCODE - zipcode of the location where the user wants weather information
##     HOURS   - an integer from 1-36 representing the weather information for this 
##               number of hours in the future to display
## 
## 
## FUNCTIONS:
## 
##     check_zip_code  - Check if zip code corresponds to an actual location
## 
##     get_website     - Get URL for Weather Underground API
##     get_hours       - Get number of hours to print future weather
## 
##     current_weather - Display current weather information
##     future_weather  - Display future weather information
## 
##     main            - Display weather information
## 
## 
## FILE STRUCTURE:
## 
##     * Import Modules
##     * Check Zipcode
##     * Weather Information Retrieval
##     * Print Weather Data
##     * Compile Weather Information
##     * Display Weather Information
## 
## 
## MODIFICATION HISTORY:
## 	
##     gabeg Sep 29 2013 <> created
## 
##     gabeg Jul 11 2014 <> added more Wunderground databases
## 
## **********************************************************************************


## ##########################
## ##### IMPORT MODULES #####
## ##########################

from sys import argv
import urllib2 
import json 



## #########################
## ##### CHECK ZIPCODE #####
## #########################

## Check if the input zipcode corresponds to an actual location
def check_zip_code(parsed_json):
    try:
        error = parsed_json['response']['error']['type']
        if 'querynotfound' in error: 
            print "ERROR: No cities matching that zipcode"
            exit()
    except:
        pass



## #########################################
## ##### WEATHER INFORMATION RETRIEVAL #####
## #########################################

## Return the website containing all the Wunderground data
def get_website():

    ## Script input parameters
    zipcode = argv[1]
        
    ## Website to access all the databases
    ws = 'http://api.wunderground.com/api/30e9ab88be150d93/alerts/astronomy/conditions/geolookup/hourly/q/'
    ext = '.json'
    url = "%s%s%s" % (ws, zipcode, ext)
        
    ## Return the website
    return url



## Get number of hours to print future weather
def get_hours():
    ## Check script parameters
    try:        
        ## Number of hours into the future to display
        num = int(argv[2])
    except:
        ## No future display requested
        return 0
    
    
    ## Check that future hours input is correct
    if (num < 0) or (num > 36):
        print "ERROR: Invalid number of hours '%s' entered." % num
        exit()
        
    
    ## Return number of hours
    return num



## ##############################
## ##### PRINT WEATHER DATA #####
## ##############################

## Display current weather information
def current_weather(parsed_json):
    
    ## City and state
    city = parsed_json['location']['city']
    state = parsed_json['location']['state']
    
    ## Current weather information
    temp = parsed_json['current_observation']['temp_f']
    feels = parsed_json['current_observation']['feelslike_f']
    weather = parsed_json['current_observation']['weather']
    precip = parsed_json['current_observation']['precip_today_in']
    time = parsed_json['current_observation']['observation_time']
    
    ## Sunrise time
    risehr = parsed_json['sun_phase']['sunrise']['minute']
    risemin = parsed_json['sun_phase']['sunrise']['hour'].zfill(2)
    sunrise = "%s:%s" % (risehr, risemin)
    
    ## Sunset time
    sethr = parsed_json['sun_phase']['sunset']['hour']
    setmin = parsed_json['sun_phase']['sunset']['minute'].zfill(2)
    sunset = "%s:%s" % (sethr, setmin)
    
    ## Miscellaneous information
    humidity = parsed_json['current_observation']['relative_humidity']
    windSpeed = parsed_json['current_observation']['wind_mph']
    windChill = parsed_json['current_observation']['windchill_f']
    elevation = parsed_json['current_observation']['observation_location']['elevation']
    solarrad = parsed_json['current_observation']['solarradiation']
    
    ## Display information
    print \
            """\
            City ~ %s
            State ~ %s
            Temp ~ %s
            Feels ~ %s
            Weather ~ %s
            Precipitation ~ %s in
            Humidity ~ %s
            Wind Speed ~ %s mph
            Wind Chill ~ %s
            Elevation ~ %s
            Solar Radiation ~ %s
            Time ~ %s \
            """ \
            % (city, state, temp, feels, weather, precip, \
               humidity, windSpeed, windChill, elevation, solarrad, time) 



## Display future weather information
def future_weather(parsed_json, num):
    
    ## Future weather information    
    for i in range(0, num):
        future_temp = parsed_json['hourly_forecast'][i]['temp']['english']
        future_feels = parsed_json['hourly_forecast'][i]['feelslike']['english']
        future_weather = parsed_json['hourly_forecast'][i]['condition']
        future_prob = parsed_json['hourly_forecast'][i]['pop']
        future_time = parsed_json['hourly_forecast'][i]['FCTTIME']['pretty']
        
        print \
            """
            Future Temp ~ %s
            Future Feels ~ %s
            Future Weather ~ %s
            Future Precip. Prob. ~ %s%%
            Future Time ~ %s \
            """ \
            % \
            (future_temp, future_feels, future_weather, future_prob, future_time) 



## #######################################
## ##### COMPILE WEATHER INFORMATION #####
## #######################################

## Main function
def main():
    
    ## Get the website with all the weather data
    url = get_website()
    
    ## Open the Wunderground API
    api = urllib2.urlopen(url)
    
    ## Wunderground weather information
    json_string = api.read() 
    parsed_json = json.loads(json_string) 
    
    
    ## Check if input zip code corresponds to an actual location
    check_zip_code(parsed_json)
    
    ## Get number of hours in the future to display future weather
    num = get_hours()
    
    ## Display current weather information
    current_weather(parsed_json)    
    
    ## Display future weather information
    future_weather(parsed_json, num)
    
    
    ## Close the Wunderground API
    api.close()



## ---------------------------------------
## ----- DISPLAY WEATHER INFORMATION ----- 
## ---------------------------------------

main()

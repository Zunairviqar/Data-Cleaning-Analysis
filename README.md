# Homework 02

## About the Data

1. Title: Crime in Context, 1975-2015.

2. Link to Data: https://www.kaggle.com/marshallproject/crime-rates

3. Source / Origin: 
    * Author or Creator: FBI Uniform Crime Reporting program's "Offenses Known and Clearances by Arrest"
    * Publication Date: 18 August 2016
    * Publisher: Gabriel Dance, Tom Meagher, and Emily Hopkins of The Marshall Project
    * Version or Data Accessed: Version 1 (29th September 2020)
    
4. License: Unknown

5. Can You Use this Data Set for Your Intended Use Case? 
Yes, since I am not reproducing the data and only performing an analysis on it, adhering similarly to the data set that we used in workshop 2.

## Format

### Overview

Format: csv
Size: 266KB
Number of Records: 2830

### Sample of Data

report_year,agency_code,agency_jurisdiction,population,violent_crimes,homicides,rapes,assaults,robberies,months_reported,crimes_percapita,homicides_percapita,rapes_percapita,assaults_percapita,robberies_percapita
1975,NM00101,"Albuquerque, NM",286238,2383,30,181,1353,819,12,832.52,10.48,63.23,472.68,286.13
1975,TX22001,"Arlington, TX",112478,278,5,28,132,113,12,247.16,4.45,24.89,117.36,100.46
1975,GAAPD00,"Atlanta, GA",490584,8033,185,443,3518,3887,12,1637.44,37.71,90.3,717.1,792.32
1975,CO00101,"Aurora, CO",116656,611,7,44,389,171,12,523.76,6,37.72,333.46,146.58
1975,TX22701,"Austin, TX",300400,1215,33,190,463,529,12,404.46,10.99,63.25,154.13,176.1
1975,MD00301,"Baltimore County, MD",642154,1259,25,137,347,750,12,196.06,3.89,21.33,54.04,116.79

### Fields or Column Headers

* Field/Column 1: Name = report_year, Type = integer.
* Field/Column 1: Name = agency_code, Type = string.
* Field/Column 1: Name = agency_jurisdiction, Type = string.
* Field/Column 1: Name = population, Type = integer.
* Field/Column 1: Name = violent_crimes, Type = integer.
* Field/Column 1: Name = homicides, Type = integer.
* Field/Column 1: Name = rapes, Type = integer.
* Field/Column 1: Name = assaults, Type = integer.
* Field/Column 1: Name = robberies, Type = integer.
* Field/Column 1: Name = months_reported, Type = integer.
* Field/Column 1: Name = crimes_percapita, Type = integer.
* Field/Column 1: Name = homicides_percapita, Type = integer.
* Field/Column 1: Name = rapes_percapita, Type = integer.
* Field/Column 1: Name = assaults_percapita, Type = integer.
* Field/Column 1: Name = robberies_percapita, Type = integer.

## Questions

### Question 1: 

Maximum number of robberies in a year in a state in the US from 1975 to 2015?

* Who (population): The people in an individual US state.
* What (subject, discipline): The number of robberies
* Where (location): In each state of the US
* When (snapshot, longitudinal): any year from 1975 to 2015
* How much data do you need to do the analysis/work: The crime data for each individual state in the US from 1975 to 2015.

### Question 2: 

The average number of violent crimes committed in the US from 1975 to 2015?

* Who (population): The population in the United States.
* What (subject, discipline): Average number of violent crimes.
* Where (location): In the entirety of the United States.
* When (snapshot, longitudinal): Cumulative from 1975 to 2015
* How much data do you need to do the analysis/work: The yearly crime data for each state in the US from 1975 to 2015.

### Who Might Collect Relevant Data / What Articles or Publications Cite a Relevant Data Set?

Government Organisations (such as FBI for this particular dataset), Businesses and Industries, NGOs, as well as Researchers. Scholarly Articles and Data Publications/ Repositories/ Portals cite a relevant data set. 

## Analysis

### Central Tendency

* The average value of population is 795698.0891304348
* The average value of violent_crimes is 8946.377043225571
* The average value of homicides is 124.89506172839506
* The average value of rapes is 416.27886710239653
* The average value of assaults is 4405.146022520887
* The average value of robberies is 4000.2450980392155
### Dispersion

* The range of population is 8450098
* The range of violent_crimes is 174388
* The range of homicides is 2244
* The range of rapes is 3884
* The range of assaults is 71015
* The range of robberies is 107392


* The standard deviation of population is 1012450.5695786542
* The standard deviation of violent_crimes is 15862.946876191885
* The standard deviation of homicides is 203.12916115302104
* The standard deviation of rapes is 479.81193412483015
* The standard deviation of assaults is 6977.293768858712
* The standard deviation of robberies is 8653.902964516823
### Outliers

* The max value in population is 8550861
* The max value in violent_crimes is 174542
* The max value in homicides is 2245
* The max value in rapes is 3899
* The max value in assaults is 71030
* The max value in robberies is 107475

### Other

* The highest number of robberies in the US occured in the year 1981 in the state of NewYorkCity
* The average number of violent crimes committed in the US from 1975 to 2015 are 8946

##Verification

### With Excel:

- All the answers for the "population" columns match as shown in the screenshot "verify_pop" attached. I copied the entire column of population to another excel sheet where i removed all the blank spaces in order to make it similar to how my code functions. Then I calculated the values for max, mean(average), range(max-min) and Standard Deviation.
- All the answers for the "violent_crimes" columns match as shown in the screenshot "verify_vc" attached. I copied the entire column of violent_crimes to another excel sheet where i removed all the blank spaces and extra values that are not required in order to make it similar to how my code functions. Then I calculated the values for max, mean(average), range(max-min) and Standard Deviation.
- All the answers for the "homicides" columns match as shown in the screenshot "verify_hc" attached. I copied the entire column of homicides to another excel sheet where i removed all the blank spaces and extra values that are not required in order to make it similar to how my code functions. Then I calculated the values for max, mean(average), range(max-min) and Standard Deviation.
- All the answers for the "rapes" columns match as shown in the screenshot "verify_rp" attached. I copied the entire column of rapes to another excel sheet where i removed all the blank spaces in order to make it similar to how my code functions. Then I calculated the values for max, mean(average), range(max-min) and Standard Deviation.
- All the answers for the "assaults" columns match as shown in the screenshot "verify_at" attached. I copied the entire column of assaults to another excel sheet where i removed all the blank spaces in order to make it similar to how my code functions. Then I calculated the values for max, mean(average), range(max-min) and Standard Deviation.
- All the answers for the "robberies" columns match as shown in the screenshot "verify_rb" attached. I copied the entire column of robberies to another excel sheet where i removed all the blank spaces in order to make it similar to how my code functions. Then I calculated the values for max, mean(average), range(max-min) and Standard Deviation.

## Conclusion

The results of my calculations were certainly able to answer my questions. The questions were very specific and the dataset used also precisely answered them in the manner that was required. However, a few hindrances were the missing data for the state of 'Louisville, KY' which had to be removed from the calculations eventually not allowing the data to be very exact, and hence to be an approximation.
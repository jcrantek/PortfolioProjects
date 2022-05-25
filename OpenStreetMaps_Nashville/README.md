# Project: Wrangle OpenStreetMap Data

Name: Jeremy Crantek

## Map Area

Nashville, TN, United States

https://www.openstreetmap.org/relation/

I chose Nashville due to currently living here and knowing the general area. I am familiar with some of the local naming conventions of the streets so exploring the data should help me pick out anything that
might be wrong. Then I can correct any problems with some python scripts, export the cleaned data to csv files and ultimately load the data into a new SQL database. From there we can explore the data more 
using SQL commands.

## Data about Nashville Map

I decided to take a sample of the original osm file (nashville.osm). I sampled down the data on 3 different occasions (k=85, k=50, k=15) to try to maximize the errors found in the data. The 
data for the map was categorized using the ElemenTree library. Here we can see an overall count (tag_count.py) of various pieces of the sampled OSM file (nashville_sample.osm).

```
{'osm': 1,
'node': 22642,
'tag': 10399,
'way': 3019,
'nd': 26064,
'relation': 34,
'member': 1914}
```
## Problems Encountered with the Nashville Map

Even after sampling down the data (sample.py), I did not run into a lot of issues with this dataset. Overall, the data was
very clean (street names, postal codes, etc.) due to a lot of users helping to clean it up. It seems that the users for
Nashville’s map data have been very busy!

I processed the map (process_map.py) data using 3 regular expressions to find any problem characters:

1. lower – lowercase letters and valid
2. lower_colon – lowercase letters that are valid tags with a colon
3. problemchars – tags with problematic characters

Figure 1 - process map function that will categorize the street data into 4 categories.

Once we processed the map, I did not find any problem characters in the map data:
{'lower': 7110, 'lower_colon': 3076, 'other': 213, 'problemchars': 0}

I did see some abbreviated street names suffixes in the data. For example, Rosa L Parks Blvd should be Rosa L Parks Boulevard. So that is where most of the effort was focused.

## Abbreviated Street Names

I used a regular expression in an audit function (audit.py) to find those streets with incorrect suffixes and replace them with the more formal usage using an update function (audit.py). 
Figure 2: mapping of abbreviated names to formal suffixes After the update function we now have the correct suffix for our example street: Rosa L Parks Blvd => Rosa L Parks Boulevard 
Now to create 5 csv files and segregate the data to store them in each csv. The file sizes are listed below including our original osm file (nashville.osm) and the sample file (nashville_sample.osm) taken from the original osm file.
Next up we created a new SQL database using the sqlite3 python library named nashville_osm.db with a file size of 2928 KB.

Now we can answer some questions about the data and the area of Nashville using SQL commands.

Number of Nodes
sqlite > SELECT COUNT(*) FROM NODES;
22642

Number of Ways
sqlite > SELECT COUNT(*) FROM WAYS;
3019

Number of Unique Users
sqlite > SELECT COUNT(DISTINCT(e.uid))
FROM (SELECT uid FROM nodes UNION ALL SELECT uid FROM ways) e;
1044


Top 10 Contributing Users
sqlite> SELECT e.user, COUNT(*) as num
FROM (SELECT user FROM nodes UNION ALL SELECT user FROM ways) e
GROUP BY e.user
ORDER BY num DESC
LIMIT 10;

```
Gedwards724 | 10706
wward | 3135
woodpeck_fixbot | 726
bobby22 | 637
Tom_Holland | 629 <= Spiderman?
greggerm | 381
ChesterKiwi | 361
maxerickson | 360
42429 | 312
Rub21 | 254
```
Top 10 Amenities in Nashville
sqlite> SELECT value, COUNT(*) as num
FROM nodes_tags
WHERE key='amenity'
GROUP BY value
ORDER BY num DESC
LIMIT 10;

```
place_of_worship | 40 <= Not a surprise here in the Southern U.S.
restaurant | 10 <= Also not a surprise as Nashville is a major foodie city.
school | 8
cafe | 7
fast_food | 6
fountain | 5
bench | 5
bar | 5
fuel | 4
pub | 2
```
## Conclusion

Overall, the data in the Nashville open streets map was clean. The main points of the addresses (names, suffixes, postal codes, etc.) were updated well and consistently with only a few abbreviated name issues that arose during this exercise.
Nashville is often labeled as an ‘it’ city but if you looked at its open street map data you would not be able to tell. The lack of amenities is the biggest letdown for this data. Things like ‘drinking fountain’ and ‘toilet’ listed as amenities show 
that the data for Nashville still has a long way to go for accuracy and truthfulness. Other online maps (bing, google, apple) list much more in the amenities field for this city.

## Suggestions

One could potentially import data from those more fleshed out maps using their APIs (if provided) or at the very least manual input to attempt to update the amenity data. Obviously, using the API is the better route but could lead to some
trouble in linking the OPM data with that from other map sources. Manual input would be tedious and could lead to user errors but could also help link the data better since human eyes would be able to match the amenities correctly.

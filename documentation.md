# Documentation for GBAD APIs
Friday December 16, 2022


## Introduction
Read the read me to understand how to run the API locally if you are trying to test local fixes


## dataportal
Run this by going to either
1. http://localhost:9000/dataportal/
or
2. http://gbadske.org:9000/dataportal/


## GBADsTables
This API returns a list of tables in the GBADs database.  It is used by the dataportal to generate the list of tables that are available for the user to query.

You can access this API by going to either
1. http://localhost:9000/GBADsTables/public?format=html
or
2. http://gbadske.org:9000/GBADsTables/public?format=html

The only elements you can change about this api is the format which can be set to either *html* or *text*


## GBADsTable
This API returns the contents of a specific table in the GBADs database.  It is used by the dataportal to generate the list of tables that are available for the user to query.

You can access this API by going to either
1. http://localhost:9000/GBADsTable/public?table_name=livestock_production_faostat&format=html
or
2. http://gbadske.org:9000/GBADsTable/public?table_name=livestock_production_faostat&format=html

The only elements you can change about this api is the format which can be set to either *html* or *text*


## GBADsPublicQuery
This API returns the contents of a specific query performed on a specific table in the GBADs database.

An example to hit the endpoint is as follows:
1. http://localhost:9000/GBADsPublicQuery/livestock_production_faostat?fields=country,year,species,population&query=year=2017%20AND%20species=%27Goats%27&format=html
or
2. http://gbadske.org:9000/GBADsPublicQuery/livestock_production_faostat?fields=country,year,species,population&query=year=2017%20AND%20species=%27Goats%27&format=html

The elements that can be changed for this API are:

**Required Fields**
1. table_name - this is the name of the table you want to query.
    1. You can get a list of the tables by going to 
2. fields - this is the list of columns you want to return.
3. query - this is the query you want to run on the table (ex. Query: year=2017 AND species='Goats').

**Optional Fields**

4. join - this is the join you want to run on another table.
5. order - this is the order you want to return the results in.
6. format - this is the format you want the results returned in (html or text/csv).
7. count - If set to anything other than no, returns the number of rows returned by the query.
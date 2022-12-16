# API_GBADsPublic
RDS library routines and API functions to access the public GBADs database tables on AWS RDS

To install and run this application you need to install FastAPI and other Python modules
 -  pip (or pip3) install fastapi
 -  pip (or pip3) install uvicorn
 -  pip (or pip3) install pandas
 -  pip (or pip3) install typing
 -  pip (or pip3) install pathlib
 -  pip (or pip3) install psycopg2

Then you can run the API main on port 9000 (the port number is on the last line of main.py):

python3 main.py

This will need to be backgrounded to stay running and let you use the shell.  It will also
print out error messages to the console so you should pipe these into a log file for now.
It is good to use nohup to ensure that the process is not interrupted.

To access the API in your web browser start with the command:
http://localhost:9000/dataportal/

Improvements made:
1. Clean up file created by the API
2. Improved logging
3. Added parameterized queries to prevent SQL injection attacks
4. Send error messages to the user and not just to the console
4. Add * to fields to generate all fields for the general query capability
   - fields=* does work but it does not retrieve the field names
   - need to add a subroutine to fetch field names - the following code will do this:

cur.execute(f"""SELECT * FROM {table_name} ;""")

rows = cur.fetchone()

column_names = [desc[0] for desc in cur.description]


Improvements that need to be made:
2. Clean up code and document
3. Add test harness


## Notes

- You will need a file called secure_rds.py to run the RDS commands but that file contains
password information so you must request it from Deb Stacey


## Example Calls From each API
1. ```http://localhost:9000/GBADsTables/public?format=html```
2. ```http://localhost:900/GBADsTable/public?table_name=livestock_production_faostat&format=html```
3. ```http://localhost:9000/GBADsPublicQuery/livestock_production_faostat?fields=country,year,species,population&query=year=2017%20AND%20species=%27Goats%27&format=html```
4. ```http://localhost:9000/GBADsLivestockPopulation/oie?year=*&country=Canada&species=Cattle&format=html```
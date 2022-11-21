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

Improvements that need to be made:
1. Improve the logging
2. Clean up file created by the API
3. Send error messages to the user and not just to the console
4. Check to make sure that sql injection is not a problem
5. Clean up code and document
6. Add * to fields to generate all fields for the general query capability
   - fields=* does work but it does not retrieve the field names
   - need to add a subroutine to fetch field names - the following code will do this:
         
cur.execute(f"""SELECT * FROM {table_name} ;""")
         
rows = cur.fetchone()
         
column_names = [desc[0] for desc in cur.description]



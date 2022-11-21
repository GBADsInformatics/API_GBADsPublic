#
# Connect to the public GBADs database
#
#    Connection parameters include:
#       host = database location in AWS which is gbadske-database-public-data.cp73fx22weet.ca-central-1.rds.amazonaws.com
#       dbname = name of the database which is publicData_1 since this database will contain public data
#       user = main database user (and currently the only database user) which is the default user "postgres"
#       password = password for the database user
#
#    Author: Deb Stacey
#
#    Date of last update: August 4, 2021
#
#    Usage: from secure_connect import connect_public
#
#
# Libraries
#
import psycopg2 as ps
#
def connect_public():
#
# Create connection and cursor
#
    conn = ps.connect("host=gbadske-database-public-data.cp73fx22weet.ca-central-1.rds.amazonaws.com dbname=publicData_1 user=postgres password=gbadske2021!")
#
# Return connection information
#
    return conn
#
# End of function connect_public()
#


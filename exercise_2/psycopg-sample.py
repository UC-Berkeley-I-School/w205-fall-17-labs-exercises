#Sample code snippets for working with psycopg


import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

# Connect to the database
conn = psycopg2.connect(database="postgres", user="postgres", password="pass", host="localhost", port="5432")

#Create the Database

try:
    # CREATE DATABASE can't run inside a transaction
    conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    cur = conn.cursor()
    cur.execute("CREATE DATABASE tcount")
    cur.close()
    conn.close()
except:
    print "Could not create tcount"

#Connecting to tcount

conn = psycopg2.connect(database="tcount", user="postgres", password="pass", host="localhost", port="5432")

#Create a Table
#The first step is to create a cursor. 

cur = conn.cursor()
cur.execute('''CREATE TABLE tweetwordcount
       (word TEXT PRIMARY KEY     NOT NULL,
       count INT     NOT NULL);''')
conn.commit()


#Running sample SQL statements
#Inserting/Selecting/Updating

#Rather than executing a whole query at once, it is better to set up a cursor that encapsulates the query, 
#and then read the query result a few rows at a time. One reason for doing this is
#to avoid memory overrun when the result contains a large number of rows. 

cur = conn.cursor()

#Insert
cur.execute("INSERT INTO tweetwordcount (word,count) \
      VALUES ('test', 1)");
conn.commit()

#Using variables to update
uCount=5
uWord="test"
cur.execute("UPDATE tweetwordcount SET count=%s WHERE word=%s", (uCount, uWord))
conn.commit()

#Select
cur.execute("SELECT word, count from tweetwordcount")
records = cur.fetchall()
for rec in records:
   print "word = ", rec[0]
   print "count = ", rec[1], "\n"
conn.commit()

conn.close()

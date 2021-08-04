# Database Connection

import psycopg2 as pg2

conn = pg2.connect(database='loginsystem',user='postgres',password='password')
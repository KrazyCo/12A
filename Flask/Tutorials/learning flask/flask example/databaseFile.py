import sqlite3

def readDatabase(sql):
  with sqlite3.connect("movie.db")as db:
    cursor = db.cursor()
    cursor.execute(sql)
    
    result = cursor.fetchall()
    return result

def writeDatabase(sql):
  with sqlite3.connect("movie.db")as db:
    cursor = db.cursor()
    cursor.execute(sql)
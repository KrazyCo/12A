import sqlite3


def readDatabase():
  sql = input("SQL: ")
  with sqlite3.connect("movie.db")as db:
      cursor = db.cursor()
      cursor.execute(sql)

      result = cursor.fetchall()

      for each in result:
          print(each)


def writeDatabase():
  sql = input("SQL: ")
  with sqlite3.connect("movie.db")as db:
      cursor = db.cursor()
      cursor.execute(sql)

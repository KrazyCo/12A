import sqlite3
from pathlib import Path
from tabulate import tabulate


def showAllFilms():
    currDir = str(Path(__file__).parent.absolute()).replace("\\", "/")
    db = sqlite3.connect(currDir+"/movie.db")
    cursor = db.cursor()
    cursor.execute("SELECT * FROM film")
    result = cursor.fetchall()
    db.commit()
    db.close()
    return result


def writeDatabase():
    sql = input("SQL: ")
    with sqlite3.connect("movie.db")as db:
        cursor = db.cursor()
        cursor.execute(sql)


if __name__ == "__main__":
    exit = False
    print("Film database\n"
        "==============\n"
        "")
    while exit == False:
        userInput = int(input("Please select an option\n"
                    "\n"
                    "1 - Add a new film\n"
                    "2 - Delete a film\n"
                    "3 - Show all films\n"
                    "4 - Find films by year\n"
                    "5 - Exit\n"
                    "\n"
                    ">>> "))
        match userInput:
            case 1:
                print("1")
            case 2:
                pass
            case 3:
                films = showAllFilms()
                print(tabulate(films, headers=["ID", "Title", "Year"]))
            case 4:
                pass
            case 5:
                exit = True
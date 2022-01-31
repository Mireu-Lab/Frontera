import sqlite3

class write:
    def file(kakaoid, file, times):
        sqldata = sqlite3.connect("Data/Diary_API.sqlite3")
        data = sqldata.cursor()
        sqlline = """INSERT INTO file_time (kakaoid, filehash, times) VALUES (?, ?, ?);"""
        data.execute(sqlline, (kakaoid, file, times))
        sqldata.commit()
        data.close()
        sqldata.close()

class read:
    def file(kakaoid):
        sqldata = sqlite3.connect("Data/Diary_API.sqlite3")
        data = sqldata.cursor()
        sqlline = """select filehash, times from file_time where kakaoid='{}';""".format(kakaoid)
        data.execute(sqlline)
        sqljson = data.fetchall()
        return sqljson
        sqldata.close()

class delete:
    def file(kakaoid):
        sqldata = sqlite3.connect("Data/Diary_API.sqlite3")
        data = sqldata.cursor()
        sqlline = """delete from file_time where filehash = '{}';""".format(kakaoid)
        data.execute(sqlline)
        sqldata.commit()
        data.close()
        sqldata.close()
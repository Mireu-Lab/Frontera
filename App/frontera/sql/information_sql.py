import sqlite3

class write:    
    def user_info(kakaoid, nickname, realname, profile_picture, hobby, job, zone, sex, birthday, times):
        sqldata = sqlite3.connect("Data/Diary_API.sqlite3")
        data = sqldata.cursor()
        sqlline = """INSERT INTO userdb (kakaoid, nickname, realname, profile_picture, hobby, job, zone, sex, birthday, times) VALUES (?, ?, ?, ?, ?, ?, ?, ? ,?);"""
        data.execute(sqlline, (kakaoid, nickname, realname, profile_picture, hobby, job, zone, sex, birthday, times))
        sqldata.commit()
        data.close()
        sqldata.close()

class read:
    def user_info(kakaoid):
        sqldata = sqlite3.connect("Data/Diary_API.sqlite3")
        data = sqldata.cursor()
        sqlline = """select nickname, realname, profile_picture, hobby, job, zone, sex, birthday, times from user_information where kakaoid='{}';""".format(kakaoid)
        data.execute(sqlline)
        sqljson = data.fetchall()
        return sqljson
        sqldata.close()

class delete:
    def user_info(kakaoid):
        sqldata = sqlite3.connect("Data/Diary_API.sqlite3")
        data = sqldata.cursor()
        sqlline = """delete from user_information where kakaoid = ?;"""
        data.execute(sqlline, (kakaoid))
        sqldata.commit()
        data.close()
        sqldata.close()
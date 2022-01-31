import sqlite3

sqlset1 ="""
        CREATE TABLE userdb (
          id integer not null primary key autoincrement,
          user varchar(255) null,
          password varchar(255) null,
          email varchar(255) null,
          phone varchar(255) null,
          hash varchar(255) null
        );
        """

sqlset2 = """ 
          CREATE TABLE file_time (
            id integer not null primary key autoincrement,

            idhash varchar(255) null,

            filehash varchar(255) null,

            times varchar(255) null
          );
        """

sqlset3 = """
          CREATE TABLE user_information (
            id integer not null primary key autoincrement,

            -- 사용자 해쉬 ID
            userid varchar(255) null,
            
            -- 사용자 이메일
            email varchar(255) null,

            -- 사용자 닉네임
            nickname varchar(255) null,

            -- 사용자 본명
            realname varchar(255) null,

            -- 사용자 프로필사진
            profile_picture varchar(255) null,

            -- 사용자 취미
            hobby varchar(255) null,

            -- 사용자 직업
            job varchar(255) null,

            -- 사용자 지역
            zone varchar(255) null,

            -- 사용자 성별
            sex varchar(255) null,

            -- 사용자 생일
            birthday varchar(255) null,

            -- 사용자 가입일자
            times varchar(255) null
          );
          """
    
with sqlite3.connect("Data/Diary_API.sqlite3") as sqlfile:
  sqlfile.executescript(sqlset1)
  sqlfile.executescript(sqlset2)
  sqlfile.executescript(sqlset3)
  sqlfile.commit()
  
  # sqlfile.execute("INSERT INTO userdb (user, password, email, phone, hash) VALUES ('string', 'string', 'string', 'string', 'string');")
  # sqlfile.commit()

print("clear")
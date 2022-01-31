from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel
from frontera import account, file
import uvicorn

app = FastAPI()

class account_info(BaseModel):
    email : str = None
    password : str = None
    phone:str = None
    name : str = None

class information_info(BaseModel):
    userid : str = None
    name : str = None
    
class diary_data(BaseModel):
    text : str

@app.get("/")
def read_root():
    return None

@app.post("/account/singin", tags=["account"])
async def singin(account_info:account_info):
    """
    # 로그인
    """
    return {"message":account.signin(account_info.email, str(account_info.phone), account_info.password)}

@app.post("/account/signup", tags=["account"])
async def signup(account_info:account_info):
    """
    # 회원가입
    """
    return {"message" : account.signup(account_info.email, account_info.name)}

@app.post("/account/secession", tags=["account"])
async def secession(account_info:account_info):
    """
    # 탈퇴
    """
    return {"message":account.secession(account_info.email, account_info.name, str(account_info.phone), account_info.password)}

# ////////////////////////////////////////////////////////////////
# ////////////////////////////////////////////////////////////////
# ////////////////////////////////////////////////////////////////

@app.post("/information/write", tags=["information"])
async def singin(account_info:account_info):
    """
    # 사용자 정보 쓰기
    """
    return {"message":account.signin(account_info.email, str(account_info.phone), account_info.password)}

@app.post("/information/read", tags=["information"])
async def signup(account_info:account_info):
    """
    # 사용자 정보 읽기
    """
    return {"message" : account.signup(account_info.email, account_info.name)}

# ////////////////////////////////////////////////////////////////
# ////////////////////////////////////////////////////////////////
# ////////////////////////////////////////////////////////////////

@app.post("/diary/{userid}/list/", tags=["diary"])
async def read_item(userid: str):
    """
    # 사용자 서비스 일기장 데이터 리스트
    """
    file.userid = userid
    return file.list()

@app.post("/diary/{userid}/create", tags=["diary"])
async def read_item(userid : str, diary_data : diary_data):
    """
    # 사용자 서비스 일기장 생성
    """
    file.userid = userid
    return file.add(diary_data.text)

@app.post("/diary/{fileid}/delete", tags=["diary"])
async def read_item(fileid : str):
    """
    # 사용자 서비스 일기장 삭제
    """
    return {"message":file.delete(fileid)}

@app.post("/diary/{fileid}/read/{type}", tags=["diary"])
async def read_item(fileid : str, type : bool):
    """
    # 사용자 서비스 일기장 읽기

    type : type는 JSON, XML을 변환을 요청을 확인하는 수단입니다.
    아래와 같이 준비가 되어있습니다

    True : JSON

    False : XML
    
    """
    return file.file_read(fileid, type)

if __name__ == "__main__":
    uvicorn.run(app, host='0.0.0.0', port=80)
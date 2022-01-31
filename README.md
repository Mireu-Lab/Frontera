# Main API Docs

### 로그인

로그인은 아래와 같은 데이터가 필요하다
```json
{
    //사용자 이메일 계정
    "email": "string",
  
    //사용자 이름
    "name": "string",

    //사용자 카카오 SDK ID 이름
    "kakaoid": "string"

}
```

API는 아래와 같은 CURL로 준비되어있습니다.
```curl
curl -X 'POST' \
  'http://api.mireu.xyz/account/singin' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "email": "string",
  "name": "string",
  "kakaoid": "string"
}'
```

해당 코드의 작동결과는 아래와 같습니다
```json
// 로그인 성공시
{
  "message": "몰?루"
}

// 로그인 실패시
{
  "message": false
}
```

---

### 회원가입

회원가입은 아래와 같은 데이터가 필요하다
```json
{
    //사용자 이메일 계정
    "email": "string",
      
    //사용자 이름
    "name": "string",

    //사용자 카카오 SDK ID 이름
    "kakaoid": "string"
}
```

API는 아래와 같은 CURL로 준비되어있습니다.
```curl
curl -X 'POST' \
  'http://api.mireu.xyz/account/signup' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "email": "string",
  "name": "string",
  "kakaoid": "string"
}'
```

해당 코드의 작동결과는 아래와 같습니다
```json
// 회원가입 성공시
{
  "message": "몰?루"
}

// 회원가입 실패시
{
  "message": "No such account"
}
```

---

### 탈퇴

탈퇴은 아래와 같은 데이터가 필요하다
```json
{
    //사용자 이메일 계정
    "email": "string",
  
    //사용자 이름
    "name": "string",
    
    //사용자 카카오 SDK ID 이름
    "kakaoid": "string"
}
```

API는 아래와 같은 CURL로 준비되어있습니다.
```curl
curl -X 'POST' \
  'http://api.mireu.xyz/account/singin' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "email": "string",
  "name": "string",
  "kakaoid": "string"
}'
```

해당 코드의 작동결과는 아래와 같습니다
```json
// 탈퇴 성공시
{
  "message": true
}

// 탈퇴 실패시
{
  "message": false
}
```

### 일기장 파일 리스트

API는 아래와 같은 CURL로 준비되어있습니다.
```curl
curl -X 'POST' \
  'http://api.mireu.xyz/diary/<Kakao> ID>/list/' \
  -H 'accept: application/json' \
  -d ''
```

해당 코드의 작동결과는 아래와 같습니다
```json
// 일기장 파일 리스트 성공시
{
  []
}

// 일기장 파일 리스트 실패시
{
  []
}
```

---

### 일기장 파일 생성

일기장 파일 생성은 아래와 같은 데이터가 필요하다
```json
{
    // 사용자 일기장 내용
    "text": "string"
}
```

API는 아래와 같은 CURL로 준비되어있습니다.
```curl
curl -X 'POST' \
  'http://api.mireu.xyz/diary/<FILE> ID>/create' \
  -H 'accept: application/json' \
  -d '{
  "text": "string"
}'
```

해당 코드의 작동결과는 아래와 같습니다
```json
{
  "<p>string</p>"
}
```

---

### 일기장 파일 삭제

일기장 파일 생성은 아래와 같은 데이터가 필요하다
```json
{
    // 사용자 일기장 내용
    "text": "string"
}
```

API는 아래와 같은 CURL로 준비되어있습니다.
```curl
curl -X 'POST' \
  'http://api.mireu.xyz/diary/<FILE> ID>/delete' \
  -H 'accept: application/json' \
  -d ''
```

해당 코드의 작동결과는 아래와 같습니다
```json
//파일 삭제 성공
{
  "message": true
}

//파일 삭제 실패
{
  "message": false
}
```

---

### 일기장 파일 읽기

API는 아래와 같은 CURL로 준비되어있습니다.
```curl
curl -X 'POST' \
  'http://api.mireu.xyz/diary/<FILE ID>/read/<TYPE>' \
  -H 'accept: application/json' \
  -d ''
```

해당 코드의 작동결과는 아래와 같습니다
```json
// 파일 읽기 XML 성공시
"<?xml version=\"1.0\" encoding=\"utf-8\"?>\n<p>\n\t<_value>string</_value>\n</p>"

// 파일 일기 JSON 성공시
{
  "p": [
    {
      "_value": "string"
    }
  ]
}

// 파일 읽기 실패시
{
  "message": false
}
```
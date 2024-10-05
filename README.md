<img width="100%" src="https://github.com/user-attachments/assets/486b88f9-c65e-4d41-bc39-4d149b689087"/>
<br>
<div align="center">
  <a href="https://store.steampowered.com/app/2609390/Temporis_Arts/">
    <img width="3%" src="https://github.com/user-attachments/assets/19a862e2-4348-4c4a-9c98-aa6dc8189a30"/>
  </a> &nbsp;
  <a href="https://awesome-woodwind-237.notion.site/Temporis-Arts-Backend-e5e0529541c649dda8e2581e487239b9">
    <img width="3%" src="https://github.com/user-attachments/assets/c2569156-f4fa-4833-82b2-c308a8e6ac2c"/>
  </a> &nbsp;
  <a href="https://discord.com/invite/JSyTr3psnb">
    <img width="3%" src="https://github.com/user-attachments/assets/6ec582ce-3e05-4c6a-aea1-2043dbb78aae"/>
  </a> &nbsp;
  <a href="https://x.com/ChronosSyndrome?t=x-nqB5ltzv3fyx_4m4UeTw&s=32">
    <img width="3%" src="https://github.com/user-attachments/assets/366f5d11-658d-4a34-be64-b0cf691860fb"/>
  </a>
</div>
<br/><br/><br/><br/><br/>








## 🗨️ About Temporis Arts
<div align="center">
  <img width="70%" src="https://github.com/user-attachments/assets/19c6a1e9-b3d5-4ab1-87d5-41bd313e64e4"/>
</div>
<br /><br />
Temporis Arts는 원판 위를 회전하는 판정선을 따라, 그리고 음악에 맞춰 키를 누르는 게임입니다.<br /> <br />
지정된 키 중 어느 키를 눌러도 됩니다 - 다만 갯수만 맞다면요!<br /><br />
특이한 방식의 판정으로 인해, 일반적인 리듬게임을 즐기던 사람이어도 충분히 새로운 경험을 할 수 있습니다.<br /><br />
40곡 이상, 80개 이상의 패턴이 준비되어 있습니다!<br /><br /><br />
처음에 잠겨 있는 곡이나 패턴은 "메모리얼"을 통해 해금할 수 있습니다.<br /><br />
밤하늘에 펼쳐진 별들을 발견하고, 새로운 곡을 획득해보세요!  
<br /><br /><br /><br /><br />

## ⚙️ System Architecture  




<img width="800px" src='https://github.com/user-attachments/assets/e0689aab-7f42-44c8-800d-b9d2da4f4d62'/>  
<br /><br />

## 🛠️ 기술 스택

**BE**

Language: `Python 3.8`

Tools: `VS code`

Framework: `FastAPI 0.112.2`

---

**DB**

SYSTEM : `PostgreSQL 15.8`

---

**INFRA**

Cloud : `AWS EC2`

Reverse Proxy, Secure : `Nginx`

CI/CD : `Docker 24.0.5`

<br />
Python, FastAPI의 의존성 패키지는 requirements.txt 참조.
<br /><br /><br /><br /><br />

## 📁 폴더구조

```bash
📦Temporis-Arts-Backend-1
 ┣ 📂database
 ┃ ┣ 📜connection.py
 ┃ ┗ 📜__init__,py
 ┣ 📂models
 ┃ ┣ 📂responses
 ┃ ┃ ┣ 📜auths.py
 ┃ ┃ ┣ 📜charts.py
 ┃ ┃ ┣ 📜datetime.py
 ┃ ┃ ┣ 📜message.py
 ┃ ┃ ┗ 📜__init__.py
 ┃ ┣ 📜auths.py
 ┃ ┣ 📜charts.py
 ┃ ┣ 📜musics.py
 ┃ ┣ 📜records.py
 ┃ ┣ 📜users.py
 ┃ ┗ 📜__init__,py
 ┣ 📂routes
 ┃ ┣ 📜auths.py
 ┃ ┣ 📜charts.py
 ┃ ┣ 📜records.py
 ┃ ┣ 📜users.py
 ┃ ┗ 📜__init__,py
 ┣ 📂services
 ┃ ┣ 📜auths.py
 ┃ ┗ 📜__init__.py
 ┣ 📂test
 ┃ ┣ 📜conftest.py
 ┃ ┣ 📜test_auth.py
 ┃ ┣ 📜test_charts.py
 ┃ ┣ 📜test_records.py
 ┃ ┣ 📜test_users.py
 ┃ ┗ 📜__init__.py
 ┣ 📜config.py
 ┣ 📜main.py
 ┣ 📜pytest.ini
 ┣ 📜README.md
 ┗ 📜requirements.txt
```

# GitHub에서 원격 저장소 만들기

1. 오른쪽 상단 `+` 토글 클릭

![캡처](https://user-images.githubusercontent.com/108647806/178030722-eb0a36b7-a4f7-472f-bcae-75cc0e41156c.png)

2. New Repositiory

3. repository 이름 설정하고 저장소 생성

4. ```bash
   $ git remote add origin https://github.com/github username/.git
   ```

   *깃아 원격저장소 추가해줘 origin으로*

5. 원격저장소 확인

   ```bash
   $git remote -v
   ```

6. 원격 저장소 활용 명령어 - push

   ```bash
   $git push origin master
   ```

   ```bash
   $git pull origin master
   ```


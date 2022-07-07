# GitHub에서 원격 저장소 만들기

1. 오른쪽 상단 `+` 토글 클릭

[](https://github.com/avocad06/TIL/blob/master/git/GitHub%EC%97%90%EC%84%9C%20%EC%9B%90%EA%B2%A9%20%EC%A0%80%EC%9E%A5%EC%86%8C%20%EB%A7%8C%EB%93%A4%EA%B8%B0.assets/%EC%BA%A1%EC%B2%98.png?raw=true)

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


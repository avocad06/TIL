# GitHub에서 원격 저장소 만들기

1. 오른쪽 상단 `+` 토글 클릭

![image-20220707042703523](GitHub에서 원격 저장소 만들기.assets/image-20220707042703523.png)

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


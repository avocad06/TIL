# modified 와 $ git restore의 활용



## modified

- 이전부터 버전으로 관리되고 있으면서(Tracked)

- 변경되었지만 커밋 되지않은 파일 (Changes not staged for commit)



1. modified.txt를 생성 후 Staging area에 Add = Staged 상태

```bash
$ touch modified.txt
$ git add modified.txt

$ git status
On branch master
Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        new file:   modified.txt
```



2. modified.txt를 수정 후 git status 확인 Staging Area에 있는 파일 2개

![수정](https://user-images.githubusercontent.com/108647806/178030269-6ab32dc6-c314-4c95-a321-e2d2e46d1946.PNG)

```bash
$ git status
On branch master
Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        new file:   modified.txt

Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   modified.txt
```



3. modified.txt를 처음 상태로 수정 후 git status 확인 = 1번 상태와 동일하게 Staging Area에 있는 파일은 1개 = <u>**수정되지 않았다고 보는 것**</u>

   ![다시](https://user-images.githubusercontent.com/108647806/178030324-c4e0421f-406a-492d-a1a1-393aba3cd3c0.PNG)

   ```bash
   $ git status
   On branch master
   Changes to be committed:
     (use "git restore --staged <file>..." to unstage)
           new file:   modified.txt
   ```



4. 이 상태로 commit 하면 정상적으로 commit 됨

   ```bash
   $ git commit -m 'modified 이해하기'
   [master eb2af5b] modified 이해하기
    1 file changed, 0 insertions(+), 0 deletions(-)
    create mode 100644 modified.txt
    
    $ git log -1 --oneline
   eb2af5b (HEAD -> master) modified 이해하기
   ```



💡 즉, **git**은 가장 최근 저장 유무에 따른 변화를 감지하는 게 아니라, 해당 파일의 <u>상태 자체를 기준으로</u> 변화를 추적함을 알 수 있음.
파일명의 변경은 Untracked Files로 봄.



## git restore

> Staging Area에 있는 파일 중 commit 하고 싶지 않은 파일이 있을 때



1. a/b/c.txt 파일을 생성 후 Staging Area에 Add

```bash
$ touch a.txt b.txt c.txt
$ git add .

$ git status
On branch master
Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        new file:   a.txt
        new file:   b.txt
        new file:   c.txt
```



2. -1) a/b.txt 생성에 대한 commit만 하고 싶은 경우

   1. $ git restore c.txt

   ```bash
   $ git restore --staged c.txt
   
   $ git status
   On branch master
   Changes to be committed:
     (use "git restore --staged <file>..." to unstage)
           new file:   a.txt
           new file:   b.txt
   
   Untracked files:
     (use "git add <file>..." to include in what will be committed)
           c.txt
   ```

   c. txt 가 Untracked files 상태인 것을 확인

   

   2. $ git commit

   ```bash
   $ git commit -m 'Add a,b.txt'
   [master bac60f6] Add a,b.txt
    2 files changed, 0 insertions(+), 0 deletions(-)
    create mode 100644 a.txt
    create mode 100644 b.txt
    
    $ git log -1 --oneline
   bac60f6 (HEAD -> master) Add a,b.txt
   ```

 2. -2) b.txt 수정 후 c.txt 생성에 대한 commit

    1. $ git Add

       ```bash
       $ git add .
       
       $ git status
       On branch master
       Changes to be committed:
         (use "git restore --staged <file>..." to unstage)
               modified:   b.txt
               new file:   c.txt
       ```

       b.txt 수정과 c. txt가 정상적으로 Add 되는 것을 확인

       

    2. commit

       ```bash
       $ git commit -m 'Add c.txt b.txt(modified)'
       [master a983139] Add c.txt b.txt(modified)
        2 files changed, 1 insertion(+)
        create mode 100644 c.txt
        
        $ git log -1 --oneline
       a983139 (HEAD -> master) Add c.txt b.txt(modified)
       ```

       정상적으로 commit 되는 것을 확인

       

💡 즉, 커밋은 파일 단위로 이루어지는 게 아니고, <u>행위에 대한 버전 기록</u>임을 다시 이해할 수 있음.


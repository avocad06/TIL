# Git 커밋 만들기

0. 사전설정

   ```bash
   $git config --global user.name 'GitHub ID'
   $git config --global user.email 'GitHub Email'
   ```

1. git 저장소 만들기

   ```bash
   $ git init
   Initialized empty Git repository in C:/Users/user/Desktop/0706/.git/
   ```

2. 커밋을 만든다

   ```bash
   $ git status
   On branch master
   
   No commits yet
   
   Untracked files:
     (use "git add <file>..." to include in what will be committed)
           1day/
   
   nothing added to commit but untracked files present (use "git add" to track)
   ```

   ```bash
   $ git add .
   $ git commit -m 'example'
   ```

   ```bash
   $ git log
   commit 1a375d2047daa0f9b69178dff7838b94925f7d88 (HEAD -> master)
   Author: avocad06 <miggo2704@gmail.com>
   Date:   Thu Jul 7 02:34:40 2022 +0900
   
       example
   ```

   ```bash
   $ git status
   On branch master
   nothing to commit, working tree clean
   ```

   
### Kate Macias
### Software Engineering 1
### Fall 2026

Last login: Sun Nov 15 17:23:17 on ttys001
katemacias@Kates-MacBook-Air ~ % cd documents
katemacias@Kates-MacBook-Air documents % git init challenge81
cd challenge81
Initialized empty Git repository in /Users/katemacias/Documents/challenge81/.git/
katemacias@Kates-MacBook-Air challenge81 % git add README.md
git commit -m "Added README"
fatal: pathspec 'README.md' did not match any files
On branch main

Initial commit

nothing to commit (create/copy files and use "git add" to track)
katemacias@Kates-MacBook-Air challenge81 % touch README.md  
katemacias@Kates-MacBook-Air challenge81 % ls
README.md
katemacias@Kates-MacBook-Air challenge81 % git add README.md
git commit -m "Added README"
[main (root-commit) e2559ed] Added README
 1 file changed, 0 insertions(+), 0 deletions(-)
 create mode 100644 README.md
katemacias@Kates-MacBook-Air challenge81 % git log
commit e2559edc8c5b5280f292bb4c5c0ba14ba633d13b (HEAD -> main)
Author: Kate Macias <kebohning@gmail.com>
Date:   Mon Nov 16 10:52:02 2026 -0800

    Added README
katemacias@Kates-MacBook-Air challenge81 % git switch --detach e2559edc8c5b5280f292bb4c5c0ba14ba633d13b
HEAD is now at e2559ed Added README
katemacias@Kates-MacBook-Air challenge81 % git branch newbranch
git switch newbranch
Switched to branch 'newbranch'
katemacias@Kates-MacBook-Air challenge81 % git merge main
Already up to date.
katemacias@Kates-MacBook-Air challenge81 % git branch newbranch
git switch newbranch

## Question: After the merge, where do the main and newbranch branches point?

Both branches point to the same commit.

## Question: After the merge, which branch is HEAD pointing to?

HEAD is still pointing to the newbranch branch.

## Question: What conditions were true such that this was a fast-forward merge?

The newbranch branch was already up to date with the main branch.

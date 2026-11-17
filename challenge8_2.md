### Kate Macias
### Software Engineering 1
### Fall 2026

## Output of git log after the merge is completed

katemacias@Kates-MacBook-Air testrepofile % git log
commit 306c470a4c6ab1d7475842b464e0f60daf6431d1 (HEAD -> newbranch)
Author: Kate Macias <kebohning@gmail.com>
Date:   Tue Nov 17 10:38:09 2026 -0800

    problem

commit 4a3a010cef32dd8da700ef99a138c3f3f0fe4c4b (main)
Author: Kate Macias <kebohning@gmail.com>
Date:   Tue Nov 17 10:34:37 2026 -0800

    second

commit a41b67321a37e9f80fee52874ee2bb1852eeda68
Author: Kate Macias <kebohning@gmail.com>
Date:   Tue Nov 17 10:32:37 2026 -0800

    comitted
katemacias@Kates-MacBook-Air testrepofile % 

## Question: Why aren't main and newbranch pointing to the same commit?

because we detached newbranch from main and made commits on that branch.

## Question: If you merge newbranch into main, will it be a fast-forward merge? Why or why not?

no, because newbranch isn't a decendant of main.

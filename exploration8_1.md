### Kate Macias
### Software Engineering 1
### Fall 2026

## Describe what a branch is and how it differs from a collection of related commits.
A branch is a separate line of development that allows you to work on a feature or bug fix without affecting the main codebase. You can do anything you want to it, and someone has to approve the merge with main before that can be done. 

## Discuss why a git pull must, as part of its processing, perform a merge.

a git pull must perform a merge so the origin and the local branch match and you gather any work that others have done and merged. 

## What's the difference between a fast-forward merge and a normal merge? Under what circumstances can you perform a fast-forward merge?

A fast-forward merge is a merge that does not create a merge commit, while a normal merge does. You can perform a fast-forward merge when the branch you are merging into is up-to-date with the branch you are merging from.

## When you are switched to branch main, and you git merge somebranch, does that merge somebranch's changes into main? Or does it merge main's changes into somebranch?

somebranch becomes main. they've been united and are now the "main" code base. 

## Can a merge conflict occur with a fast forward merge? Why or why not?

No, a fast-forward merge does not create a merge commit, so conflicts cannot occur. It moves the local pointer to the same commit as the remote branch, so any changes that need to be merged are already present.

## Outline the process you have to go through in Git to resolve a merge conflict.

git merge 
open the files and find the conflicting lines
resolve the conflicts by editing the files
git add and git commit to save the changes
if all else fails, ask Beej to help untangle your git rats nest

## In the Collaboration Across Branches chapter, which of the three workflows presented most appeals to you in general? Why?

I like the feature branch workflow. It seems very straightforward. Each person gets a branch and the master of the project allows the merges.

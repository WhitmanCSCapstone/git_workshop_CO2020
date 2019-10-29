This activity is intended for groups of two. Each partner should follow along on a seperate computer. Note that the `$` character marks the start of the command prompt, while subsequent lines are printed by the command.

Part 1: Cloning the repository
------------------------------

A Git repository is a directory in which a Git project lives. These repositories can be stored on the GitHub server. We call this version of the repository the "remote" repository. Our first step is to copy a repository to our local machine. This type of repository is called the "local" repository. 

- Click on the green "Clone or download" button above and copy the URL to your
  clipboard.
- Open a terminal and `cd` to a directory that you want to work in.
- Clone the repository with `git clone` followed by the URL from earlier.

```
$  git clone https://github.com/WhitmanCSCapstone/git_workshop_CO2020.git
Cloning into 'git_workshop_CO2020'...
remote: Enumerating objects: 3, done.
remote: Counting objects: 100% (3/3), done.
remote: Compressing objects: 100% (2/2), done.
remote: Total 3 (delta 0), reused 0 (delta 0), pack-reused 0
Unpacking objects: 100% (3/3), done.
```

The `clone` command copies a remote repository to your local machine. Note that `clone` is only used to initialize the repository on your local machine, there are other commands to update your local repository once you already have it cloned. 

Next we enter our local repository and run the following commands:

```
$ cd git_workshop_CO2020/
$ git status
On branch master
Your branch is up to date with 'origin/master'.

nothing to commit, working tree clean

$ python3 main.py
Hello world!
```
The `status` command allows you to see where you are within your repository. From this output, we see that we are in the master branch of our repository (which we will dive into deeper later). Additionally, we are told that there is "nothing to commit," meaning that our current local version of the repository matches the remote version of the repository. 


Now we have local access to the repository. We're able to run and test the main
script and see that it works.

Part 2: Documenting a need
--------------------------

When you find that a shared project needs to be changed, it's best to make a
ticket to inform others of the need you've noticed. On GitHub, these tickets
are called issues. In a browser, open the GitHub Issues tab for our
repository. Create a new issue that calls for the addition of a new text file.

![new ticket](/images/new-ticket.png)

Since you'll be resolving your own issue, you can assign it to yourself using
the "Assignees" section on the right. This signals to your teammates that
you have this issue handled.

![assignees](/images/assignees.png)

Part 3: Making a change
-----------------------

It's good practice to create a new branch whenever work begins on an issue. A branch is a series of changes. The main branch is called `master`, and other branches contain changes that `master` doesn't have yet. This feature lets us save our progress on one issue when switching to work on another. 

![diagram](/images/diagram.png)

We'll make a new branch for our changes. A branch is normally named after a
bug or feature, but we want to make sure our branch names don't conflict with one
another. For this exercise, name your branch something arbitrary that's unique
within this class:

```
$ git checkout -b tulips-feature
Switched to a new branch 'tulips-feature'
```

`git checkout` changes the repository to reflect a branch. The `-b` flag says
that the named branch doesn't exist yet and must be created. `git status` will
tell us that the branch has been created and we've checked it out.

```
$ git status
On branch tulips-feature
nothing to commit, working tree clean
```

Now we've made our branch, but it only exists locally. We need to make a
matching branch on GitHub and send our changes to it. The command `push`, with the flag `--set-upstream`,  does just that! We include the name of our upstream, followed by the name of our new branch. In this case, that is `origin tulips-feature`. 

```
$ git push --set-upstream origin tulips-feature
Counting objects: 3, done.
Delta compression using up to 4 threads.
Compressing objects: 100% (2/2), done.
Writing objects: 100% (3/3), 297 bytes | 297.00 KiB/s, done.
Total 3 (delta 0), reused 0 (delta 0)
remote:
remote: Create a pull request for 'tulips-feature' on GitHub by visiting:
remote:      https://github.com/WhitmanCSCapstone/git_workshop_CO2020/pull/new/tulips-feature
remote:
To github.com:WhitmanCSCapstone/git_workshop_CO2020.git
 * [new branch]      tulips-feature -> tulips-feature
Branch 'tulips-feature' set up to track remote branch 'tulips-feature' from 'origin'.
```

Others can now `checkout` our branch to see our changes in the filepath `origin/tulips-feature`. 

Now that we have our feature branch we can make changes to the project files.
Create a new file with any editor and write a line of text. Save the file in
the project directory with your name and the `.txt` extension.

If we check the branch status, we see that the new file isn't being tracked
by Git. To fix this, we use the `add` command followed by the name of the file we want to add. Let's do this and check this status of our repository again. Notice that if you want to add more files at once, the  `add .` command allows you to stage all untracked files.

```
$ git status
On branch tulips-feature
Untracked files:
  (use "git add <file>..." to include in what will be committed)

        tulip.txt

nothing added to commit but untracked files present (use "git add" to track)
$ git add tulip.txt
$ git status
On branch tulips-feature
Changes to be committed:
  (use "git reset HEAD <file>..." to unstage)

        new file:   tulip.txt
```




As the status message says, our file is ready for "commit". A commit is a version of the project that we want to save as its own state. We typically create new commits whenever we make changes to our project. Since we can always revert back to previous commits, frequent commiting is advised. To commit, we use the `commit` command. We also need to use the `-m` flag to specify a commit message. This reminds developers what changes were made in each commit. 

```
$ git commit -m "Add an important new thing"
[tulips-feature a5d0dd0] Add an important new thing
 1 file changed, 1 insertion(+)
 create mode 100644 tulip.txt
```


Since our feature is finished, we want to merge it into the `master` branch. Control-click on the GitHub link in the terminal to create a new pull request in your browser. Create the pull request, but don't merge it yet – We want to get a second opinion to make sure your changes are good.

Part 4: Code review
-------------------

To check your changes for quality and correctness, you and your partner will review one another's code.

First, request a review from your partner using the "Reviewers" section on the right. Assign yourself under "Assignees", since you'll be responsible for making revisions.

![sidebar](/images/sidebar.png)

Once your partner has requested your review, find their pull request in the
"Pull requests" tab. Right below the title, we can see the name of the branch
being merged. Copy the name of your partner's feature branch to be used next.

![PR header](/images/pr-header.png)

Our local repository doesn't know about new branches on the remote repository, so we need to fetch the latest list of branches. `git fetch` will inform the local repository of the remote's latest changes without yet modifying any files.

```
$ git fetch
remote: Enumerating objects: 4, done.
remote: Counting objects: 100% (4/4), done.
remote: Compressing objects: 100% (2/2), done.
remote: Total 3 (delta 0), reused 3 (delta 0), pack-reused 0
Unpacking objects: 100% (3/3), done.
From github.com:WhitmanCSCapstone/git_workshop_CO2020
 * [new branch]      tulips-feature -> origin/partners-feature
```

Now that our repository knows about the latest remote changes, we can checkout the new branch.

```
$ git checkout partners-feature
Branch 'partners-feature' set up to track remote branch 'partners-feature' from 'origin'.
Switched to a new branch `partners-feature'
```

One of the purposes of a code review is to check the correctness of the new code. We can run the `main` script again, but this time it should print the contents of our partner's file.

```
$ python3 main.py
Hello, world!
```

We aren't seeing the contents of our partner's file. Go back to the pull request and comment on this discrepancy.

Part 5: Revision
----------------

As your partner said, your file contents aren't getting printed. We need to fix that before we can resolve the pull request.

Check out your own branch with `git checkout`. We don't need the `-b` flag this time, as the branch already exists.

```
$ git checkout tulips-feature
Switched to branch 'tulips-feature'
Your branch is up to date with 'origin/tulips-feature'.
```

Open up `main.py` to find the issue.

```
def main():
    # Part 5: Copy this line to call `print_file` on your own file.
    print_file('beszel.txt')

def print_file(path):
    f = open(path, 'r')
    for line in f:
        print(line, end='')

if __name__ == '__main__':
    main()
```

It looks like only files passed into `print_file` are getting printed. Call `print_file` on your own text file in `main`.

```
def main():
    # Part 5: Copy this line to call `print_file` on your own file.
    print_file('beszel.txt')
    print_file('tulip.txt')

def print_file(path):
    f = open(path, 'r')
    for line in f:
        print(line, end='')

if __name__ == '__main__':
    main()
```

Now we can test the change to see if it works:

```
$ python3 main.py
```

The script should print both "Hello, world!" and the contents of your file.

Now that we know the change is working, let's stage and commit it. We also need to push the commit so our partner can see that it's fixed.

```
$ git add main.py
$ git commit -m "Fix the important new thing"
[tulips-feature a5d0dd0] Add an important new thing
 1 file changed, 1 insertion(+)
 create mode 100644 main.py
$ git push
```

Finally, we can re-request our partner's review. Go back to your own pull request and use the "Reviewers" section on the right to re-request their review.

Part 6: Code review again
-------------------------

Once your partner is ready for you to re-review their code, we can checkout their branch again. Even though it says we're up to date, we need to `pull` to get the latest changes.

```
$ git checkout partners-feature
Switched to branch `partners-feature'
Your branch is up to date with 'origin/partners-feature'.

$ git pull
remote: Enumerating objects: 5, done.
remote: Counting objects: 100% (5/5), done.
remote: Compressing objects: 100% (2/2), done.
remote: Total 3 (delta 0), reused 3 (delta 0), pack-reused 0
Unpacking objects: 100% (3/3), done.
From github.com:WhitmanCSCapstone/git_workshop_CO2020
   a5d0dd0..6bbb571  partners-feature -> origin/partners-feature
Updating a5d0dd0..6bbb571
Fast-forward
 main.py | 1 +
 1 file changed, 1 insertion(+)
```

Now we can see if the script prints files like it should.

```
python3 main.py
```

Now it should say both "Hello, world!" and the contents of your partner's file. Success!

Go back to your partner's pull request and approve the changes.

Part 7: Merging
---------------

Once your partner approves your pull request, you can finalize it by merging it into `master`. Go back to your own pull request and click "Merge pull request", then "Confirm merge". Your changes are now reflected in the `master` branch, and your feature is complete! If your issue isn't yet closed, go ahead and close it now.

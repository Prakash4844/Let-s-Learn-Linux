This project aims to be alternative/backup of LinuxJourney. 

If you are looking to make contribution, follow the steps below.

#### If you don't have git on your machine, [install it](https://docs.github.com/en/get-started/quickstart/set-up-git).

<img align="right" width="300" src="https://i.imgur.com/NXhmCnq.png" alt="fork this repository" />

## Fork this repository

Fork this repository by clicking on the fork button on the top of this page.
This will create a copy of this repository in your account.



## Clone the repository

<img align="right" width="300" src="https://i.imgur.com/ZkVEU6g.png" alt="clone this repository" />

Now clone the forked repository to your machine. Go to your GitHub account, open the forked repository, click on the code button and then click the _copy to clipboard_ icon.

Open a terminal and run the following git command:


### To clone Use following Method 

### 1. By Git Submodule init and Update method 

```bash
$ git clone https://github.com/Prakash4844/Let-s-Learn-Linux
$ git submodule init
$ git submodule update
```

## OR

### 2. Git Submodule init and update alternative

```bash
$ git clone --recurse-submodules https://github.com/Prakash4844/Let-s-Learn-Linux
```

> **Warning**
> If you get any SSH error while cloning submodule, change the submodule link in .gitmodules file to https one from SSH one like this:

`url = git@github.com:Prakash4844/hugo-theme-relearn.git` to `url = https://github.com/Prakash4844/hugo-theme-relearn.git`


<img align="right" width="300" src="https://i.imgur.com/FuBbWhe.png" alt="copy URL to clipboard" />

## Create a branch

Change to the repository directory on your computer (if you are not already there):

```
cd Let-s-Learn-Linux
```

Now create a branch using the `git switch` command:

```
git switch -c your-new-branch-name
```

For example:

```
git switch -c command-line-pages
```

## Make necessary changes and commit those changes

Now open `Contributors.md` file in a text editor, add your name in table by adding two lines:

```html
  <td align="center"><a href="your profile link"><img src="your profile avatar pic(github profile pic)" width="100px;" alt=""/><br /><sub><b>your_username</b></sub></a><br />
  <a href="#question-your_username" title="Answering Questions">💬</a> <a href="https://github.com/Prakash4844/Let-s-Learn-Linux/commits?author=your_username" title="Documentation">📖</a>
```

between ```<tr></tr>``` tags 

<img align="right" width="450" src="https://firstcontributions.github.io/assets/Readme/git-status.png" alt="git status" />

If you go to the project directory and execute the command `git status`, you'll see there are changes.

Add those changes to the branch you just created using the `git add` command:

```
git add modified_files
```
Now commit those changes using the `git commit` command:

```
git commit -m "Add a good commit messeage"
```

## Push changes to GitHub

Push your changes using the command `git push`:

```
git push -u origin your-branch-name
```

replacing `your-branch-name` with the name of the branch you created earlier.

<details>
<summary> <strong>If you get any errors while pushing, click here:</strong> </summary>

- ### Authentication Error
     <pre>remote: Support for password authentication was removed on August 13, 2021. Please use a personal access token instead.
  remote: Please see https://github.blog/2020-12-15-token-authentication-requirements-for-git-operations/ for more information.
  fatal: Authentication failed for 'https://github.com/<your-username>/first-contributions.git/'</pre>
  Go to [GitHub's tutorial](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account) on generating and configuring an SSH key to your account.

</details>

## Submit your changes for review

If you go to your repository on GitHub, you'll see a `Compare & pull request` button. Click on that button.

<img style="float: right;" src="https://firstcontributions.github.io/assets/Readme/compare-and-pull.png" alt="create a pull request" />

Now submit the pull request.

<img style="float: right;" src="https://firstcontributions.github.io/assets/Readme/submit-pull-request.png" alt="submit pull request" />

Soon I'll be merging all your changes into the main branch of this project. You will get a notification email once the changes have been merged.

Congrats! You just contributed using a forking workflow _fork -> clone -> edit -> pull request_

Thank-you for your contribution.
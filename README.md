<H1 align="center">Let's Learn Linux</H1>


Ready to take the plunge into the world of Linux? Let's Learn Linux is the perfect starting point! This user-friendly website offers a wealth of resources for beginners, on Linux basics, automation, bash, POSIX, systemd, and more. With Let's Learn Linux, you'll gain the skills and confidence you need to navigate this powerful operating system like a pro. So why wait? Checkout the website now!!! be a Linux learners today and unlock your full potential!


> **Note**
> This Project needs contributors to pull content from Linux Journey to Let's Learn Linux. Only basic knowledge of HTML, Markdown and Hugo is needed for contribution. please help us out if you can.


#### Note: The Linux Journey site is now online again, so development of this project might be slow.


## Website is Currently Live at: [Let's Learn Linux](https://letslearnlinux.tech)

[![Deploy Let's Learn Linux site to Github Pages](https://github.com/Prakash4844/Let-s-Learn-Linux/actions/workflows/hugo.yml/badge.svg?branch=main)](https://github.com/Prakash4844/Let-s-Learn-Linux/actions/workflows/hugo.yml)


## Want to read offline?

### 1. Using Docker 

```bash
$ docker pull prakash4844/let-s-learn-linux:1.0
$ docker run -p 1313:1313 -it let-s-learn-linux:1.0
```

See Docker Repository: [Docker Repo](https://hub.docker.com/repository/docker/prakash4844/let-s-learn-linux/general)

![Site Screenshot](Site-Home.png)
### To clone Use following Method 

### 1. By Git Submodule init and Update method 

```bash
$ git clone https://github.com/Prakash4844/Let-s-Learn-Linux
$ git submodule init
$ git submodule update --progress
```

## OR

### 2. Git Submodule init and update alternative

```bash
$ git clone --recurse-submodules https://github.com/Prakash4844/Let-s-Learn-Linux
```

To run the server offline execute the following command

```bash
$ hugo server
```
Browse to http://localhost:1313/Let-s-Learn-Linux/ and you should see the website at your localhost.

> **Warning**
> If you get any SSH error while cloning submodule, change the submodule link in .gitmodules file to https one from SSH one or visa-versa like this:

`url = git@github.com:Prakash4844/hugo-theme-relearn.git` to `url = https://github.com/Prakash4844/hugo-theme-relearn.git`
OR</br>
`url = https://github.com/Prakash4844/hugo-theme-relearn.git` to `url = git@github.com:Prakash4844/hugo-theme-relearn.git`


## Contriubution:
- For info on How to contribute See this [CONTRIBUTING.md](https://github.com/Prakash4844/Let-s-Learn-Linux/tree/main/Contribute/Contributing)
- For a list of Contributors See this [Contributors.md](https://github.com/Prakash4844/Let-s-Learn-Linux/tree/main/Contribute/Contributors)

## Locale Status:

1. [x] English
2. [ ] Hindi
3. [ ] German

## Resources:
- Content is forked from [LinuxJourney](https://github.com/cindyq/linuxjourney)
- Use Hugo version 0.128.2
- Hugo Relearn Theme, [Check it out](https://github.com/McShelby/hugo-theme-relearn)
- Font Linux [Check it out](https://github.com/lkundrak/font-linux)
- Hugo QuizDown [Check it out](https://github.com/bonartm/hugo-quiz)
- Docker [Check it out](https://www.docker.com/)

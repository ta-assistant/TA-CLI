Client version 1.0.0
<h1 align="center"> Admin-CLI </h1>

<p align="center">This program is about checking students work in your computer and send students score to server by CLI</p>

## Documentation
* [Installation](#installation)
* [Getting start](#getting-start)
  - [Available Commands](#available-commands)
  - [Login](#login)
  - [Init work directory](#init-work-directory)
  - [Start checking work](#start-checking-work)
* [TA item](#ta-item)
  - [API-KEY](#api-key)
  - [workId](#workid)
* [ETC](#etc)
  - [Custom your own draft](#custom-your-own-draft)
## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install

### Library we use that are not in python standard library
```
$ pip install requests
```
Let's start the installation process first you need to install library that we mention 
then we will clone this repository into your local computer

ssh 
> $ git clone git@github.com:ta-assistant/TA-CLI.git

https 
> $ git clone https://github.com/ta-assistant/TA-CLI.git
and you need to goto TA-CLI directory to install CLI.


Goto TA-CLI directory 
```bash
$ cd TA-CLI
```
install CLI ( for more infomation -> [CLI](https://github.com/ta-assistant/TA-CLI/tree/master/ta_cli#readme) )

```bash
$ pip install --editable .
```
> If you use Window os you need to open terminal as adminstrator
> 
Now you have completed the installation process.

## Getting start
#### Available Commands
  1. init    [Init TA's work directory Args: workID (str): Work's ID]
  2. login   [Login]
  3. start   [Start working on TA directory]
  4. submit  [Submit]

#### Login
first let login we login with apikey that you need to ask server manager to get it then assume that your apikey is `1234567890`
then type command ta login --apikey 1234567890
```bash
$ ta login --apikey `yourapikey`
```
then you should get this massage
```bash
~\User\key has been created
~\User\key\taconfig.json has been created.
```
now your apikey will kept in your User directory
```bash
~/user/key/taconfig
```
So now you have apikey that in your computer next if you want to check students work you must create new directory that have students work in it when you use our command you must use it in that directory path. In this example I will call it work_directory.
#### Init work directory
let's start. I will assume that you already have lot of students work files in your work directory. then type command (this command you need to have work id if you don't know what is work id -> [work_id](#workid))
```bash
$ ta init --workid `work id`
```
if everything successful, you will receive this message.
```
[*] ~\Users\dir\work_directory makeing work directory
 |-[/] Creating workDirectory ~\Users\dir\work_directory
 |-[/] Creating `config.json`
 |-[/] Checking API-KEY
 |-[/] fetching draft.json ...
 |  |-[/]   API Request

  * statusCode : 200
  * message : Success
  * requestId : *****************
  * workDraft : {'outputDraft': ['studentId', 'param1', 'param2', 'comment', 'score', 'scoreTimestamp'], 'fileDraft': '{studentId}_test.zip'}

 |
[/] ~\Users\dir\work_directory is ready
```
if you don't know what workDraft for -> [work draft]

now you will have
```bash
$ ./work_directory
       ├── stuwork1
       ├── stuwork2
       ├── stuwork3
             .
             .
             .
       └── ta
            ├──  draft.json
            └── config.json
             
```
#### Start checking work
if everything is ready now you can use `ta start` ( if something is't ready ta start will send you what is missing )
```
ta start
```
then you will receive this message
```
Do you want to open vscode?(y/n): n
```
in this example I choose no but you can choose yes if you want to open student work by vscode.
```
[*] starting...
 |-[/] checking config.json
 |-[/] checking draft.json
Do you want to use draft from draft.json or fetch from the server
(R)ead from file or (F)etch from server: r
 |-[*] Your workId is 'workId'
 |-[*] draft has been written to work.json
 |-[/] ~\Users\dir\work_directory\ta\work.json created
 |
 |-[/] 5 file has processed
[/] finish
```
> (R)ead from file or (F)etch from server: r
> 
> in this line you can choose read or fetch up to you
fetch is for fetching updated draft form server
read is for reading draft.json from ta directory

(In this example I have 5 file in my working directory)

Now let's check it!
( it will run every work that follow the draft )
```
===========================
studentId: stuwork1
===========================
Enter param1: test
Enter param2: test
Enter comment: test
Enter score: 10
{'scoreTimestamp': 1626962297679, 'studentId': 'stu1', 'param1': 'test', 'param2': 'test', 'comment': 'test', 'score': 10.0} 
has been written down in ~\Users\dir\work_directory\ta\work.json
```
when check is done and you want to sent it to the server use command ta submit
```
ta submit
```
> !!! ALL COMMENT IS USE ON WORK DIRECTORY PATH!!!
## TA item
you need to have 2 thing to start the work
- apikey
- workid

### API-KEY
Apikey is use to indentify user when they send to the server that they have permission to check that work or not

> Where can I get an apikey?

apikey come from our server if you don't have it you need to contact our server manager

> If you do not have apikey can you start working process.

No you can't.

### WORKID
Workid is use for telling server that what work we are reviewing. So the draft will depent on workid

You can get workid from our website or if you can't find it you can contact server manager

## ETC
You can custom you own draft but if it not follow draft on server you can't submit it
```{"outputDraft": ["studentId","score"], "fileDraft": "{studentId}_something.zip"}```
#### Custom your own draft
draft is requried on fileDraft is `studentId` and in outputDraft is `score` if you don't have two property in your draft the program wont run

Let's get start on fileDraft

filedraft is a draft for checking student file that is valid or not you need to write in `{}`

outputDraft is a draft for you to put data in it but if the fileDraft already have it. The program will automatic put the data in it.
outputDraft you need to write in form of string `"studentId"`

then if you done with custom your draft when you use command `ta start`
in this line you need to choose R/r to read from your draft, you can also fetch draft from the server your draft will not be delete but work.json will be reset.
```
(R)ead from file or (F)etch from server: r
```
____
Contributions, issues, and feature requests are welcome!
Give a ⭐️ if you like this project!

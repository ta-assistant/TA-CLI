Client 1.0.0
<h1 align="center"> Admin-CLI </h1>


<p align="center">This program is about checking students work in ta's computer and send students score to server by CLI</p>

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install

### library we use that are not in python standard library
$ pip install requests

$ pip install -U click

Let's start the installation process first you need to install library that we mention 
then we will clone this github into your local computer

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

Now you have completed the installation process.

## How to use
Nowaday we have 4 command that can use.
  1. init    [Init TA's work directory Args: workID (str): Work's ID]
  2. login   [Login]
  3. start   [Start working on TA directory]
  4. submit  [Submit]

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

let's start. I will assume that you already have lot of students work files in your work directory. then type command (this command you need to have work id if you don't know what is work id -> [work_id])
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
> in this line you can choose read or fetch upto you
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

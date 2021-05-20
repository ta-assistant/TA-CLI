## FILE MANAGEMENT

Author Vitvara

This libary is about manage file and directory you can import those module to use by
```
from file_management_lib import module name
```
if you want to use only 1 method you can do it by
```
method = Object().method
method(parameter)
```
Or if you use more than 1 method you should create an variable to keep those Object
```
object1 = Object1()

object1.method1()
object1.method2(parameter)
```

To be clear about those parameter
### `path`
in FileEditor use path of directory that you want to create file 

`"this\is\path" `

In DirManagement you should put directory name that you want in to the back of the path

`"this\is\path\dirname"`

### `filename` need to be filename and its extension and have backslash in front of file name
"filename.txt"
"filename.json"

if there is anything in doubt, you can mention me in discord

WorkEditor
=================================================================================================================
work editor is about work.json
its have method that can edit work.json and it already handle case that not have work.json or already have work.json
path need to be ta dir

example:
### init work.json
`work = WorkEditor("\this\is\path")`
// it will autometic create work.json and read draft.json (if you want to use this module make sure that you check draft.json that already exits)
### get work.json
`filework = work.read_file("\work.json") -> dict`
### writting work.json
`work.write_work({'student_id': '6310546066', 'name': 'vitvara', 'ex': 'ex1', 'score1': '12', 'score2': '13', 'comment': 'nice work'})`


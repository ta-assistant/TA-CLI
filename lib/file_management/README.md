Author Vitvara

### This libary is about manage file and directory you can import those module to use by

from file_management_lib import module name

### if you want to use only 1 method you can do it by

method = Object().method
method(parameter)

### or if you use more than 1 method you should create an variable to keep those Object

object1 = Object1()

object1.method1()
object1.method2(parameter)

### to be clear about those parameter
### `path` on window path can't directly use by themself you need to add r in font of the path string to avoid backslash error
r"this\is\path" 
### in DirManagement you should put directory name that you want in to the back of the path
r"this\is\path\dirname" 

### anyone whio uses macOS, please give me some information that what is the format of the path ###

### `filename` need to be filename and its extension and have backslash in front of file name
"filename.txt"
"filename.json"

### if there is anything in doubt, you can mention me in discord
"""
Author vitvara
=================================================================================================================
work editor is about work.json
its have method that can edit work.json and it already handle case that not have work.json or already have work.json
path need to be ta dir

example use:
### init work.json
work = WorkEditor(r"\this\is\path)
// it will autometic create work.json and read draft.json (if you want to use this module make sure that you check draft.json that already exits)
### get work.json
filework = work.read_file(r"\work.json") -> dict
### writting work.json
work.write_work({'student_id': '6310546066', 'name': 'vitvara', 'ex': 'ex1', 'score1': '12', 'score2': '13', 'comment': 'nice work'})
"""
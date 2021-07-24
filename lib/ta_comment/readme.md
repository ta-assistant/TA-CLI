# TA COMMENT

Because we have a problem that when the students were deducted and wondered where they were deducted, then the 
students asked ta one by one, causing difficulty in answer question. So we came up with this idea.

This feature started out when we saw on github that when we reviewing the code we could tell which line of 
code were bugs to the person that respomsible for that project. So we think this the way to solved that problem. But we can't
do exactly like github. Then we have to change somthing to make it compatible with our projects.

## Examples of use
### how to write comment
```python
#>>> :start:

### YOUR CODE ###

#>>> :end: comment=good job
```

### how to read comment
```python
from ta_comment.main import ta_comment
print(ta_comment(workpath)
```

### what you will get
you will get comments in form of json follow this order studentId -> filename -> comment, lines
```
{
   "123456789": [
      {
         "1.py": [
            {
               "comment": "good job",
               "lines": {
                  "15-23": "def create_ta_dir(path):\n    ta_path = os.path.join(path, \"ta\")\n    if os.path.exists(ta_path):\n        return False\n    else:\n        DirManagement().create_dir(ta_path,out=False)\n        return True\n"
               }
            },
            {
               "comment": "good job",
               "lines": {
                  "55-60": "def init_work_directory(path, workid) -> bool:\n    config_path = os.path.join(path, \"ta\", \"config.json\")\n    ta_path = os.path.join(path, \"ta\")\n    draft_path = os.path.join(path, \"ta\", \"draft.json\")\n"
               }
            }
         ]
      }
 }
```
- we need to write down comment to student file
- we have our own syntax (you can't change it)
- all comment in student file will be read and send to server when we use `ta submit` (in case that you didn't use this feature on our project ignore this line)


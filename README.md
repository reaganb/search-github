# Machine Problem: GitHub API

#### You need to create a CLI application which takes in a search term and searches GitHub repositories for that term. It should output the results in CSV format.

#### Requirements:
1. The application takes in a search term as the command line argument
2. It should output a CSV file containing the name of the project, the description, the URL of the repository, the programming language used and the date where it was last updated
3. The application should output up to up to 1000 search results if possible
4. Commit your code to GitHub and past the link of your repository here. Repository name is: search-github

## The search_github script

The script requires the keyword for searching repositories in Github. It will list all available repositories related to the given keyword with a maximum of 1000 results per minute.

### Prerequisites
1. Windows/Linux OS
2. Python 3

### Usage
The script will work as long as there is Python 3 installed in the system.
Check if it is installed by executing the command:
```
$ python --version
```

### Examples

```
$ python search_github.py python out.txt
PAGE 1: 100 results
PAGE 2: 100 results
PAGE 3: 100 results
PAGE 4: 100 results
PAGE 5: 100 results
PAGE 6: 100 results
PAGE 7: 100 results
PAGE 8: 100 results
PAGE 9: 100 results
PAGE 10: 100 results
Github API request limit exceeded!
```
Running the command with the default arguments: keyword "python" and output file "out.txt".
Once executed, it will search the Github server in an unauthorized manner. Limiting the results up to 1000 every minute only.
It will output to the console the current page and the number of results that are being written to the output file.
```
$ cat out.txt

Name, Description, URL, Programming Language, Date of last update
"TheAlgorithms/Python", "All Algorithms implemented in Python", "https://github.com/TheAlgorithms/Python", "Jupyter Notebook", "2019-08-16T07:55:30Z"
"geekcomputers/Python", "My Python Examples", "https://github.com/geekcomputers/Python", "Python", "2019-08-16T06:41:31Z"
"Show-Me-the-Code/python", "Show Me the Code Python version.", "https://github.com/Show-Me-the-Code/python", "HTML", "2019-08-16T04:21:59Z"
"injetlee/Python", "Python脚本。模拟登录知乎， 爬虫，操作excel，微信公众号，远程开机", "https://github.com/injetlee/Python", "Python", "2019-08-16T07:30:17Z"
"TwoWater/Python", "Python 入门教程：【草根学 Python （基于Python3.6）】", "https://github.com/TwoWater/Python", "None", "2019-08-16T07:12:49Z"
"kubernetes-client/python", "Official Python client library for kubernetes", "https://github.com/kubernetes-client/python", "Python", "2019-08-16T06:51:34Z"
"xxg1413/python", "Python学习", "https://github.com/xxg1413/python", "Python", "2019-08-15T12:46:39Z"
"jakevdp/PythonDataScienceHandbook", "Python Data Science Handbook: full text in Jupyter Notebooks", "https://github.com/jakevdp/PythonDataScienceHandbook", "Jupyter Notebook", "2019-08-16T08:06:12Z"
"poise/python", "THIS COOKBOOK IS DEPRECATED – Chef cookbook to install Python and related tools", "https://github.com/poise/python", "Python", "2019-08-13T14:58:52Z"
```
Reading the output file shows the available repositories related to the given keyword. The output shown is trimmed from the original.
```
$ python search_github.py python out.txt
PAGE 1: 100 results
PAGE 2: 100 results
Github API request limit exceeded!
```
Running the script without waiting for another minute will not fully receive the 1000 results.




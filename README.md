# HomeJeopardy
A basic Django App to create a home jeopardy game based off a CSV of categories and clues
Requires python and pip (used to install libraries)

# Windows User Guide
make sure django and markdown2 is installed using pip
"pip install django"
"pip install markdown2"

open command prompt and navigate to directory of code
e.g. "cd Downloads/HomeJeopardy-master/HomeJeopardy-master"

to launch the server run "python manage.py runserver"
This should launch the server at 127.0.0.1:8000

In a web browser navigate to 127.0.0.1:8000 or wherever the server was launched according to the terminal 

# Writing Question Bank
2 example tsv's are included to use as an example for how to format. The file saved as "JeopardyTest.tsv" in the entries folder will be read. So either change the file name of the bank you want to use to that or in "views.py" change line 18 to the new file name

# password-manager

the application is developed using tkinter module , IDE - Pycharm and saves the data in json format.
Functionality - 
a) Generate a super safe password
b) save all your passwords in a json file
c) search through the json file for existing passwords. 

Note : if the json file already exists , but is empty then it usually generates an error because json.load doesn't support empty file read , that error is handled when the application
begins by scanning the json file using os module , and it deletes the file if filesize is 2 bytes or lower. 

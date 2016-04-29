#Main Menu options--where users pick file to analyze 
fileOptions = """\033[1;34mWelcome! Select a file to get started!\033[1;m 
\033[1;32mA\033[1;m - Organization One Data File 
\033[1;32mB\033[1;m - Organization Two Data File
\033[1;32mC\033[1;m - Organization Three Data File
\033[1;32mD\033[1;m - Enter a New Data File
Type \033[1;31mexit\033[1;m anytime to quit the program
Type \033[1;31mhelp\033[1;m anytime for additional program instructions"""

#Data Analysis Options--appears after user selects file from Main Menu.  
options = """\033[1;34mPlease select one of the options below.\033[1;m
\033[1;32m1\033[1;m - Return to Main Menu
\033[1;32m2\033[1;m - Search for Member's Information By Username  
\033[1;32m3\033[1;m - Table Showing Number of Members in Each Job Title
\033[1;32m4\033[1;m - Table Showing Number of Members Working for Each Company
\033[1;32m5\033[1;m - Average Salary Calculator 
\033[1;32m6\033[1;m - Visual Data Printout of Number of Members from Each State
\033[1;32m7\033[1;m - Domain Visual Data Printout Creator"""

#Average Calculator Options--appears after user selects Average Salary Calculator 
#from Data Analysis Options 
avgOptions = """\033[1;32ma\033[1;m - Total Average Salary
\033[1;32mb\033[1;m - Avg. Salary by Gender
\033[1;32mc\033[1;m - Avg. Salary by Position"""
from options import *


def fileSelection():
# this function prints the fileOptions text? and then allows the user to select which file they would like to work with.
# once the user has selected a file to work with, it is then open, read, and stored into a new global variable.   
# include try/except here? if one of the file options is not chosen? 
  try: 
    print(fileOptions)
    file = input("\033[1;38mSelect a file:\033[1;m")
    if file == "A" or file == "a":
      print("\033[1;33mYou have selected Organization One's data file\033[1;m")
      fname = "organization1.csv"
    elif file == "B" or file == "b":
      print("\033[1;33mYou have selected Organization Two's data file\033[1;m")
      fname = "organization2.csv" 
    elif file == "C" or file == "c":
      print("\033[1;33mYou have selected Organization Three's data file\033[1;m")
      fname = "organization3.csv"
    elif file == "D" or file == "d": 
      print("\033[1;33mYou have selected to enter your own file\033[1;m")
      fname = input("Enter file name:")
    elif file == "help" or file =="HELP" or file == "Help":
      helpfunction()
    
    global fhand
    fhand = open(fname) 
    global selectedFile
    selectedFile = fhand.readlines()
    
  except:
    if file == "exit":
      print("goodbye")
    else:
      print("Please select a file")
      fileSelection()
      
def helpfunction():
#this function contains the help text for the program.  Whenever this function is called (when the user types "help") the help text is printed.  
  print("\033[1;31mThis program allows you to analyze your organization's membership information.  You can use one of the files already uploaded, or upload a file of your own.  Each option analyzes the data in different ways.  Detailed information on each information is provided once you have selected a file.  You can type 'exit' anytime to quit the program.\033[1;m")
  fileSelection()


def option2():
#this option allows users to search for a username and returns all corresponding information for that username 
  #stores column headings from file into list
  columnHeadings = []
  columnHeadings = selectedFile[0]
  columnHeadings = columnHeadings.split(",")
  columnHeadings[13] = columnHeadings[13].rstrip()
  print("\033[1;33mYou selected option 2\033[1;m")
  UserNameInput = input("\033[1;38mPlease enter a username:\033[1;m")
  d = list()  
  for line in selectedFile: 
    line = line.split(",")
    username = line[1]
    if UserNameInput == username: 
      starter = 0 
      newLine = {}
      for i in line:
        newLine[columnHeadings[starter]] = i
        starter += 1 
        
      newLine['salary'] = newLine['salary'].rstrip()
      
      newLineList = list(newLine.keys())
      newLineList.sort()
      for key in columnHeadings:
          # d = list()
          d = ("\033[1;38m" + key + "\033[1;m", str(newLine[key]))
          # print(d)
          print(": ".join(d))  
      # print(newLine)
    else:
      continue

  if not d: 
   print("\033[1;31mNo matches found\033[1;m")

def option3():
#this function counts the number of people associated with each job title/position found in the organization's membership data file
#and returns a table with job positions in alphabetical order and the number of people in the organization who work in that position 
  print("\033[1;33mYou selected option 3\033[1;m")
  print("\033[1;34mNumber of Members in Each Job Title\033[1;m")
  jobCounter = dict()
  for line in selectedFile:
    # print(line)
    line = line.split(",")
    # print(line)
    job_title = line[9]
    # print(company)
    if job_title not in jobCounter:
      jobCounter[job_title] = 1
    else: 
      jobCounter[job_title] += 1
  # print(jobCounter)
  jobCounterList = list(jobCounter.keys())
  jobCounterList.sort()
  for key in jobCounterList:
    if key == "job_title":
      continue
    else:
      b = dict()
      b = ("\033[1;38m" + key + "\033[1;m", "\033[1;34m" +str(jobCounter[key]) + "\033[1;m")
      # print(b)
      print("\t".join(b))
  
  
def option4():
#this function counts the number of people working for each company and then 
#prints a table in alphabetical order by company and the number of people working at that company
  print("\033[1;33mYou selected option 4\033[1;m")
  print("\033[1;34mNumber of Members at Each Company\033[1;m")
  companyCounts = dict()
  for line in selectedFile:
    # print(line)
    line = line.split(",")
    # print(line)
    company = line[8]
    # print(company)
    if company not in companyCounts:
      companyCounts[company] = 1
    else: 
      companyCounts[company] += 1
  # print(companyCounts)
  companyCountsList = list(companyCounts.keys())
  companyCountsList.sort()
  for key in companyCountsList:
    if key == "company_name":
      continue
    else:
      a = dict()
      a = ("\033[1;38m" + key + "\033[1;m", "\033[1;34m" +str(companyCounts[key]) + "\033[1;m")
      # print(a)
      print("\t".join(a))


def option5():
#this function calculates average salary depending on option the user selects.
#option A returns the average salary for all members
#option B returns the average salary for males and females 
#option C returns the average salary for the job title entered by the user 
  total = 0
  totalFemale = 0
  totalMale = 0 
  count = 0 
  female = 0
  male = 0 
  jobCount = 0 
  jobSalary = 0
  print(avgOptions)
  x = input("\033[1;38mWhat is your choice?\033[1;m")
  if x =="a" or x =="A":
    for line in selectedFile:
      line = line.split(",")
      if line[13] == "salary\n": 
        continue
      else:
        salary = line[13]
        # print(salary)
        salary = salary.rstrip()
        # print(salary)
        salary = int(salary)
        total = salary + total 
        count = count + 1
    
    average = total / count 
    print("\033[1;32mAverage Salary:\033[1;m","$",average)
    
  elif x == "b" or x == "B":
    for line in selectedFile:
      line = line.split(",")
      if line[13] == "salary\n": 
        continue
      elif line[5] == "Female":
        salary = line[13]
        salary = salary.rstrip()
        salary = int(salary)
        totalFemale = salary + totalFemale 
        female = female + 1
      elif line[5] == "Male":
        salary = line[13]
        salary = salary.rstrip()
        salary = int(salary)
        totalMale = salary + totalMale 
        male = male + 1
    averageFemale = round(totalFemale/female, 2)
    averageMale = round(totalMale/male, 2) 
    print("\033[1;32mFemale Average Salary:\033[1;m","$",averageFemale)
    print("\033[1;32mMale Average Salary:\033[1;m", "$",averageMale)
  elif x == "c" or x == "C":
    job = input("\033[1;38mEnter job title:\033[1;m")
    try:
      for line in selectedFile:
        line = line.split(",")
        if line[13] == "salary\n": 
          continue
        elif job == line[9]: 
          salary = line[13]
          salary = salary.rstrip()
          salary = int(salary)
          jobSalary = jobSalary + salary 
          jobCount = jobCount + 1
      avgJobSalary = round(jobSalary/jobCount, 2)
      print("\033[1;32m" + job +"\033[1;m", "\033[1;32mAverage Salary:\033[1;m","$",avgJobSalary)
    except:
      print("\033[1;31mNo matches found\033[1;m")

def option6():
#returns a visual data printout of the number of members from each state 
  print("\033[1;33myou selected option 6\033[1;m")
  states = dict()
  for line in selectedFile:
    line = line.split(",")
    state = line[11]
    if state not in states:
      states[state] = 1
    else: 
      states[state] += 1 
  # print(states)
  statesList = list(states.keys())
  statesList.sort()
  for key in statesList:
    if key == "state":
      continue
    else:
      a = states[key]
      print("\033[1;38m" + key + "\033[1;m", "\033[1;34m" + (a * '*') +"\033[1;m", "\033[1;38m" + str(a) + "\033[1;m")

def option7():
#this funcion allows users to enter as many domains as they would like to 
#create a visual data printout to compare the number of people with email addresses
#with the domains listed.  
  print("\033[1;33mYou selected option 7\033[1;m")
  print("\033[1;34mCreate a visual data printout for domains you want to see.\033[1;m")
  domainList = dict()
  for line in selectedFile:
    # print(line)
    line = line.split(",")
    # print(line)
    email= line[7].split("@")
    # print(email)
    if len(email) >= 2:
      domain = email[1]
      # print(domain)
      if domain not in domainList:
        domainList[domain] = 1
      else: 
        domainList[domain] += 1
  
  # print(domainList)
  print("\033[1;34mEnter as many domains as you would like to compare below.  Make sure to separate each domain by a space.\033[1;m")
  print("\033[1;38mexample:\033[1;m \033[1;38mmysql.com\033[1;m \033[1;38mexaminer.com\033[1;m \033[1;38mberkeley.edu\033[1;m \033[1;38mgoodreads.com\033[1;m")
  userRequest = input("\033[1;38mEnter domains here: \033[1;m")
  userRequest =userRequest.split(" ")
  # print(userRequest)
  notFound = list()
  notFound.append("\033[1;31mThe following domain(s) were not found in the system:\033[1;38m")
  test = "no"
  print("\033[1;38mHorizontal Histogram-Number of People with the Following Domain(s)\033[1;38m")
  for key in userRequest:
    try: 
      value = domainList[key]
      print("\033[1;32m" + key +"\033[1;m", "\033[1;38m" + (value * '*') + "\033[1;m")
    except:
      notFound.append("\033[1;30m" + key + "\033[1;m")
      test = "yes"
  # print("The following domain(s) were not found in the system:") 
  if test =="yes":
    for i in notFound:
      print(i)
  
    
  
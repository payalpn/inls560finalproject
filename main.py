fileOptions = """Welcome! Select a file to get started! 
A - organization one 
B - organization two
C - organization three
D - Enter a new file"""

options = """1 - Main Menu
2 - Option 2
3 - Option 3
4 - Option 4"""

def fileSelection():
#include try/except here? if one of the file options is not chosen? 
  print(fileOptions)
  file = input("Select a file:")
  if file == "A" or "a":
    print("You are now using organization one's membership data file")
    fname = "organization1.csv"
  elif file == "B" or "b":
    print("You are now using organization two's membership data file")
    fname = "organization2.csv" 
  elif file == "C" or "c":
    print("You are now using organization three's membership data file")
    fname = "organization3.csv"
  elif file == "D" or "d": 
    print("user file")
    fname = input("Enter file name:")
  else:
    print("Please select a file")
  global fhand
  fhand = open(fname) 
  global selectedFile
  selectedFile = fhand.readlines()
  
fileSelection()

#stores column headings from file into list, columnHeadings --used laterin option 4 
columnHeadings = []
columnHeadings = selectedFile[0]
columnHeadings = columnHeadings.split(",")
# print(columnHeadings) 


def option2():
  print("You selected option 2")
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
      a = (key, str(companyCounts[key]))
      # print(a)
      print("\t".join(a))

def option3():
  print("You selected option 3")
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
      b = (key, str(jobCounter[key]))
      # print(b)
      print("\t".join(b))


def option4():
  print("You selected option 4")
  UserNameInput = input("Enter username:")
  for line in selectedFile: 
    line = line.split(",")
    username = line[1]
    if UserNameInput == username: 
      starter = 0 
      for i in line:
        newLine = {columnHeadings[starter], i}
        print(newLine)
        starter += 1 
    else:
      continue
  
going = True

while going:
  print(options)
  choice = input("what is your choice? ")
  if choice == "1":
    fileSelection()
  elif choice == "2":
    option2()
  elif choice == "3": 
    option3()
  elif choice == "4":
    option4() 
  elif choice == "exit":
    going = False
    
# This only happens if you exit.
print("Goodbye.")

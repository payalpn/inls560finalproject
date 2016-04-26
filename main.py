from options import * 
 
def fileSelection():
#include try/except here? if one of the file options is not chosen? 
  print(fileOptions)
  file = input("Select a file:")
  
  if file == "A" or file == "a":
    print("organization ONE")
    fname = "organization1.csv"
  elif file == "B" or file == "b":
    print("organization TWO")
    fname = "organization2.csv" 
  elif file == "C" or file == "c":
    print("organization THREE")
    fname = "organization3.csv"
  elif file == "D" or file == "d": 
    print("user file")
    fname = input("Enter file name:")
  else:
    print("Please select a file")
  
  global fhand
  fhand = open(fname) 
  global selectedFile
  selectedFile = fhand.readlines()
 
    
def option4():
  print("You selected option 4")
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


def option2():
  print("You selected option 2")
  UserNameInput = input("Enter username:")
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
          d = list()
          d = (key, str(newLine[key]))
          # print(d)
          print(": ".join(d))  
      # print(newLine)
    else:
      continue


def option5():
  total = 0
  totalFemale = 0
  totalMale = 0 
  count = 0 
  female = 0
  male = 0 
  jobCount = 0 
  jobSalary = 0
  print(avgOptions)
  x = input("Enter something:")
  if x =="a":
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
    print("Average Salary:","$",average)
  elif x == "b":
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
    print("Female Average Salary:","$",averageFemale)
    print("Male Average Salary:", "$",averageMale)
  elif x == "c":
    job = input("Enter job title:")
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
    print(job, "Average Salary:","$",avgJobSalary)

def option6():
  print("you selected option 6")
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
      print(key, a * '*', "(", a, ")")
    

fileSelection() 
 
going = True
#stores column headings from file into list, columnHeadings --used laterin option 4 
columnHeadings = []
columnHeadings = selectedFile[0]
columnHeadings = columnHeadings.split(",")
columnHeadings[13] = columnHeadings[13].rstrip()
# print(columnHeadings) 

#general demograhics option--count by gender, race, etc? 

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
  elif choice == "5":
    option5()
  elif choice == "6":
    option6()
  elif choice == "exit":
    going = False
    
# This only happens if you exit.
print("Goodbye.")

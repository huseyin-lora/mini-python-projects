
print(
      """ 
      --STUDENT QUESTION GENERATOR--
      • Using this application, you can manage students and questions.
      • You can also select a random question for a random student.
      
      
      """
      )

def showExistingStudents(studentList):
    if(len(studentList) == 0):
        print('\tNo students yet.')
    else:
        print('Existing students:')
        counter = 1
        for student in studentList:
            print(str(counter) + "." + student)
            counter += 1
    print('\t')

def showExistingQuestions(questionList):
    if(len(questionList) == 0):
        print('\tNo questions yet.')
    else:
        print('Existing questions:')
        counter = 1
        for question in questionList:
            print(str(counter) + "." + question)
            counter += 1
    print()

def program():
    print('Choose one of the actions:')
    print('AS -> Add Student')
    print('MS -> Move the student up in the list')
    print('RS -> Remove student by name')
    print('RLS -> Remove the last student')
    print('--------------------------------------')
    print('AQ -> Add question')
    print('RQ -> Remove question by item number')
    print('RLQ -> Remove the last question')
    print('RANDQ -> Randomly assign a question to a student')
    print('Q -> Quit the application')
    
    questions = []
    students = []
    validActions = ['as', 'ms', 'rs', 'rls', 'aq', 'rq', 'rlq', 'randq', 'q']
    while True: 
        try:
            selectedAction = input('Please choose an action: ').lower()
            if(selectedAction not in validActions):
                print('Please make a valid choice.')
                continue
        except:
            print('Invalid input.')
        # as: Add new student
        if (selectedAction == 'as'):
            studentToBeAdded = input('Enter the student name to be added: ')
            students.append(studentToBeAdded)
            print('New student is added.')
            showExistingStudents(students)
            
        # ms: Move the student
        elif (selectedAction == 'ms'):
            # içinde iki element varsa range(1,3) = [1, 2]
            rangeOfStudents = list(range(1, (len(students) + 1)))
            showExistingStudents(students)
            while True:
                try:
                    studentNumberToBeMovedUp = int(input('Enter the item number to move up: '))
                    
                    while (studentNumberToBeMovedUp not in rangeOfStudents):
                        print('Please enter an integer between ' + str(rangeOfStudents))
                        studentNumberToBeMovedUp = int(input('Enter the item number to move up: '))
            
                    while(studentNumberToBeMovedUp == 1):
                        studentNumberToBeMovedUp = int(input('You cannot move up the 1st item of the list. Enter the item number to move up: '))
                    
                    selectedStudentIndex = studentNumberToBeMovedUp - 1

                    break
                except:
                    print('Please provide an integer!')
                    
            if((studentNumberToBeMovedUp in rangeOfStudents) and (selectedStudentIndex > 0)):
                # Move the student up in the list
                students.insert((selectedStudentIndex - 1), students.pop(selectedStudentIndex))
                print('New ordering:')
                showExistingStudents(students)
         
         # rs: Remove student
        
        # rs: Remove the student
        elif (selectedAction == 'rs'):
            studentToBeRemoved = input('Enter the student name to be removed: ')
            students.remove(studentToBeRemoved)
            print('The student is deleted.')
            print('New ordering:')
            showExistingStudents(students)
        
        # rsl: Remove the last student
        elif (selectedAction == 'rls'):
            lastIndex = len(students) - 1
            students.pop(lastIndex)
            print('The last student in the list is deleted.')
            print('New ordering:')
            showExistingStudents(students)
        
        # aq: Add new question
        elif (selectedAction == 'aq'):
            questionToBeAdded = input('Enter a question to be added: ')
            questions.append(questionToBeAdded)
            print('New student is added.')
            showExistingQuestions(questions)
        
        # rq: Remove the question by item id
        elif (selectedAction == 'rq'):
            print()
        
        """
        elif (selectedAction == 'rlq'):
            print()
        elif (selectedAction == 'randq'):
            print()
        elif (selectedAction == 'q'):
            print() 
        """
program()
    
    
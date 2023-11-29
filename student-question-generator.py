import random

# ! Note: I have changed some action names for clarity.
# ? Example: Add Question action was 'a', I made it 'AQ'. 

def showListItems(listName, itemName):
    if(len(listName) == 0):
        print(f'\tNo {itemName}s yet.')
    else:
        print(f'Existing {itemName}s:')
        counter = 1
        for itemName in listName:
            print(f"{counter}. {itemName}")
            counter += 1
    print('\t')

def program():
    # Printing Initial window
    messageList = ['\n--STUDENT QUESTION GENERATOR--', '• Using this application, you can manage students and questions.', '• You can also select a random question for a random student. \n', 'Choose one of the actions:', 'AS -> Add Student', 'MS -> Move the student up in the list', 'RS -> Remove student by name', 'RLS -> Remove the last student' , '--------------------------------------', 'AQ -> Add question', 'RQ -> Remove question by item number' , 'RLQ -> Remove the last question', 'G -> Randomly assign a question to a student' , 'Q -> Quit the application']
    for message in messageList:
        print(message) 
    
    # Initializing the lists
    questions = []
    students = []
    validActions = ['as', 'ms', 'rs', 'rls', 'aq', 'rq', 'rlq', 'g', 'q']
    while True: 
        # Getting action
        selectedAction = str(input('Please choose an action: ')).lower()
        # Validating action
        while(selectedAction not in validActions):
            print('WARNING: Action does not exist.')
            selectedAction = input('Please choose one of the listed actions: ').lower()
        
        # as: Add new student
        if (selectedAction == 'as'):
            # Note: Validation of this input is optional
            studentToBeAdded = str(input('Enter the student name to be added: '))
            
            # Optional Validation: Is the input numeric?
            while(studentToBeAdded.isnumeric()):
                print('WARNING: Numeric values are not accepted.')
                studentToBeAdded = str(input('Enter the student name to be added: '))
                
            students.append(studentToBeAdded) # Adding at the end of the list
            print('New student is added successfully.')
            showListItems(students, 'student')
            
        # ms: Move the student
        elif (selectedAction == 'ms'):
            # Note: range(1,3) = [1, 2]
            rangeOfStudents = list(range(1, (len(students) + 1)))
            showListItems(students, 'student')
            
            while True:
                try:
                    studentNumberToBeMovedUp = int(input('Enter the item number to move up: '))
                    
                    while (studentNumberToBeMovedUp not in rangeOfStudents):
                        print('WARNING: The item number can have the values in range of ' + str(rangeOfStudents))
                        studentNumberToBeMovedUp = int(input('Enter the item number to move up: '))
            
                    while(studentNumberToBeMovedUp == 1):
                        print('WARNING: You cannot move up the 1st item of the list.')
                        studentNumberToBeMovedUp = int(input('Enter an item number except 1: '))
                    
                    selectedStudentIndex = studentNumberToBeMovedUp - 1

                    break
                except:
                    print('WARNING: Please provide an integer!')
                    
            # Move the student up in the list
            students.insert((selectedStudentIndex - 1), students.pop(selectedStudentIndex))
            print('Selected student is moved up successfully.')
            print('New ordering:')
            showListItems(students, 'student')
         
        # rs: Remove the student
        elif (selectedAction == 'rs'):
            print('Current list:')
            showListItems(students, 'student')
            studentToBeRemoved = input('Enter the student name to be removed: ')
            
            # Validation of the input
            while (studentToBeRemoved not in students):
                print('WARNING: This student is not in the list.')
                studentToBeRemoved = input('Enter the student name to be removed: ')
            students.remove(studentToBeRemoved) # Removing by value
            print('The student is deleted successfully.')
            print('New ordering:')
            showListItems(students, 'student')
        
        # rsl: Remove the last student
        elif (selectedAction == 'rls'):
            lastIndex = len(students) - 1
            students.pop(lastIndex)
            print('The last student in the list is deleted.')
            print('New ordering:')
            showListItems(students, 'student')
        
        # aq: Add new question
        elif (selectedAction == 'aq'):
            questionToBeAdded = str(input('Enter a question to be added: '))
            
            # Optional Validation: Is the input contains only numeric values? 
            # (like '235', not '230 + 5 = ?', which is acceptable.)
            while(questionToBeAdded.isnumeric()):
                print('WARNING: Question cannot consist of fully numeric values!')
                questionToBeAdded = str(input('Enter a question to be added: '))
            questions.append(questionToBeAdded)
            print('New question is added successfully.')
            showListItems(questions, 'question')
        
        # rq: Remove the question by item id
        elif (selectedAction == 'rq'):
            showListItems(questions, 'question')
            rangeOfQuestions = list(range(1, (len(questions) + 1)))
            
            while True:
                try:
                    questionToBeRemoved = int(input('Enter the question number to be removed: '))
                    
                    while (questionToBeRemoved not in rangeOfQuestions):
                        print('The item number can have the values in range of ' + str(rangeOfQuestions))
                        questionToBeRemoved = int(input('Enter the question number to be removed: '))
                    
                    selectedQuestionIndex = questionToBeRemoved - 1
                    break
                except:
                    print('Please provide an integer!')
                    
            questions.pop(selectedQuestionIndex)
            print('The question is deleted successfully.')
            print('New ordering of the questions:')
            showListItems(questions, 'question')
        
        # rlq: Remove the last question
        elif (selectedAction == 'rlq'):
            lastIndex = len(questions) - 1
            questions.pop(lastIndex)
            print('The last question in the list is deleted successfully.')
            print('New ordering of the questions:')
            showListItems(questions, 'question')
        
        # g: Randomly assign a question to a student
        elif (selectedAction == 'g'):
            randQuestion = random.choice(questions)
            randStudent = random.choice(students)
            print(f"'{randQuestion}' is asked for {randStudent} ")
        
        # q: Quit
        elif (selectedAction == 'q'):
            print('Goodbye')
            break 

program()

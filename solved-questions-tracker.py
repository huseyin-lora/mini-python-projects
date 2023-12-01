# (work_and_energy, work_and_energy_solvedQuestions, 67)
def questionTracker(subject, listOfSolvedQuestions, questionNumber):
    
    subject = list(range(1, (questionNumber + 1)))
    notSolvedQuestions = []
    solvedQuestions = []
    for question in subject:
        if question in listOfSolvedQuestions:
            solvedQuestions.append(question)
        else:
            notSolvedQuestions.append(question)
            """ print(f'NOT SOLVED: {question}') """
    print(f'SOLVED: {solvedQuestions} ')
    print('')
    print(f'NOT SOLVED: {notSolvedQuestions} ')
          
circular_motion = ''
circular_motion_solvedQuestions =[1,2,3,4,5,7,8,9,10,11,12,13,14,15,17,18,19,21,25,28,29,31,32,33,35,37,38,39,40,43,44,45,46,47,48,49,50 ]
print('\n\n\n\n---5. CIRCULAR MOTION; GRAVITATION---')
print('\t')
questionTracker(circular_motion, circular_motion_solvedQuestions, 90 )

  
work_and_energy = ''
work_and_energy_solvedQuestions =[1,2,3,4,5,6,7,9,13,14 ]
print('\n\n---6. WORK AND ENERGY---\n')
questionTracker(work_and_energy, work_and_energy_solvedQuestions, 93 )

linear_momentum = ''
linear_momentum_solvedQuestions =[]
print('\n\n---7. LINEAR MOMENTUM---\n')
questionTracker(linear_momentum, linear_momentum_solvedQuestions, 86 )



#! python3
# randomQuizGenerator.py - Creates quizzes with questions and answers in
# random order, along with the answer key.

import random
# The quiz data. Keys are states and values are their capitals.
capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix',
'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver',
'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee',
'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois':
'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas':
'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine':
'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 'Michigan':
'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 'Missouri':
'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada':
'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton', 'New Mexico':
'Santa Fe', 'New York': 'Albany', 'North Carolina': 'Raleigh','North Dakota': 'Bismarck',
'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City','Oregon': 'Salem', 'Pennsylvania':
'Harrisburg', 'Rhode Island': 'Providence','South Carolina': 'Columbia','South Dakota':
'Pierre', 'Tennessee':'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont':
'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia', 'West Virginia':
'Charleston', 'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}

#create 15 quizfiles and answer files
No_of_files = int(input('Enter the number files:'))
for num in range(No_of_files):
    quizfile = open('quizfile%s.txt' %(num+1),'w')
    answerfile = open('answerfile%s.txt' %(num+1),'w')
    #write the header for the quizfiles
    quizfile.write('Name:\n\nDate:\n\nClass:\n\n')
    quizfile.write((' '*20) + 'States and Capitals Quiz (Form %s)\n\n\n' %(num+1))
    #shuffle the order of the States
    states = list(capitals.keys())
    random.shuffle(states)
    #loop through all the states to get 50 questions
    for questionNum in range(50):
        #create right and wrong answers
        correctAnswer = capitals[states[questionNum]]
        wrongAnswer = list(capitals.values())
        wrongAnswer.remove(correctAnswer)
        wrongAnswer = random.sample(wrongAnswer,3)
        answerOptions = [correctAnswer] + wrongAnswer
        random.shuffle(answerOptions)
        #write the questions and answerOptions on the quizfile
        quizfile.write('%s.What is the capital of %s?\n' %(questionNum+1,states[questionNum]))
        for i in range(4):
            quizfile.write('   %s.%s\n' %('ABCD'[i],answerOptions[i]))
        quizfile.write('\n')
        #wire the answer in the answerfile
        answerfile.write('%s.%s\n' %(questionNum+1,'ABCD'[answerOptions.index(correctAnswer)]))
    quizfile.close()
    answerfile.close()
print('%s files created' %(No_of_files))

# 1. det(ective) - Determinant Detective 
A Matrix Determinant Calculator

### Features
- Calculates the determinant of any square matrix.
- Handles invalid inputs gracefully.
- Works with matrices of various sizes.
- Utilizes a recursive algorithm for determinant calculation.

### Getting Started
Before you start using the Determinant Detective, make sure you have the following prerequisites installed on your system:

- Python
- NumPy library**

You can install NumPy using pip:

```bash
'pip install numpy'
```

or Anaconda

```Anacondo Prompt
# Best practice, use an environment rather than install in the base env
conda create -n my-env
conda activate my-env
# If you want to install from conda-forge
conda config --env --add channels conda-forge
# The actual install command
conda install numpy
```

After you installed, activate your own environment and installed numpy via conda, go VSCode and press CTRL + Shift + P. Type:
```VSCode File Researcher
> Python: Select Interpreter
```
Then choose your own environment.
Now you can import and use NumPy.

### Usage
To use the Determinant Detective, follow these steps:

1. Run the program in your Python environment (e.g., VSCode).

2. You will be greeted with a welcome message and an introduction to the program.

3. Enter the number of rows and columns for your matrix when prompted. Ensure the following conditions are met:
   - The matrix must have at least one row and one column.
   - Row and column sizes should be positive integers.
   - The matrix should be square (i.e., rows equal columns).

4. Enter the values for each element of the matrix as prompted.

5. The program will calculate and display the determinant of the matrix.

### Example

Lets walk through an example of using the Determinant Detective to calculate the determinant of a 3x3 matrix:

```bash
1 2 3
4 5 6
7 8 9
```


1. Run the program and enter `3` for the number of rows and `3` for the number of columns.

2. Enter the values for each element as prompted.

3. The program will display the determinant, which should be `0` for this particular matrix.

### Algorithm

The Determinant Detective uses a recursive algorithm for determinant calculation. Here's how it works:

- For 2x2 matrices, it directly calculates the determinant using the formula:

```bash
determinant = (a * d) - (b * c)
```

- For larger matrices, it breaks down the problem into smaller submatrices. It calculates the determinant recursively by calculating the cofactors and submatrices.

<br><br>

# 2. det(ective)-limited
### Description
A limited version (actully first version) of det(ective), where you can calculate only 2x2, 3x3, and 4x4 matrices.

<br><br>

# 3. Student-Question Generator
### Description
This Python program, named Student Question Generator, is designed to manage students and questions interactively. It allows users to add or remove students and questions, move students up in the list, and randomly assign a question to a student. It's a simple yet effective tool for educators and facilitators in classroom or training settings.

### Features
- **Add Student (AS):** Add a new student to the list.
- **Move Student (MS):** Move a student up in the list.
- **Remove Student (RS):** Remove a student by name.
- **Remove Last Student (RLS):** Remove the last student in the list.
- **Add Question (AQ):** Add a new question to the list.
- **Remove Question (RQ):** Remove a question by its number in the list.
- **Remove Last Question (RLQ):** Remove the last question in the list.
- **Generate (G):** Randomly assign a question to a student.
- **Quit (Q):** Exit the application.

### Usage
1. **Start the Program:** Run the script to start the program.
2. **Select an Action:** Choose from the list of actions displayed on the screen. Actions are identified by their unique codes (e.g., `AS` for Add Student).
3. **Follow Prompts:** Enter the required information following each action's prompt.
4. **View Lists:** View updated lists of students and questions after each action.
5. **Random Assignment:** Use the `G` action to randomly assign a question to a student.
6. **Exit:** Use the `Q` action to quit the application.

### Notes
- The program handles basic input validation, ensuring appropriate user interaction.
- Numerical inputs are not accepted for student names and non-numeric questions.
- The action names have been updated for clarity (e.g., `AQ` for Add Question).

### Dependencies
- Python (version 3.x or above)
- No external libraries are required, except for the built-in `random` module.

<br><br>


# 4. Solved Questions Tracker
### Description
This Python program helps you track your progress in solving questions for various subjects. It provides a list of solved and unsolved questions for each subject.

### How to Use

1. Make sure you have Python installed on your system.
2. Open the program in your preferred code editor (e.g., VSCode).
3. Initialize the list of your topic, such as circular_motion = ''
4. Create topic_name_solved_questions list for your topic like circular_motion_solved_questions and enter the question numbers that you have solved.
5. Call the questionTracker(subject, liastOfSolvedQuestions, questionnumber) with proper arguments. 

### Use Case for Circular Motion and Gravitation

Subject: Circular Motion and Gravitation
``` Python
# Initializing the topic list
circular_motion = ''

# Creating the solved questions list
circular_motion_solved_questions =[1,2,3,4,5,7,8,9,10,11,12,13,14,15,17,18,19,21,25,28,29,31,32,33,35,37,38,39,40,43,44,45,46,47,48,49,50 ]

# Styling:
print('\n\n\n\n---5. CIRCULAR MOTION; GRAVITATION---')
print('\t')

# Calling the function: list of the topic, 
questionTracker(circular_motion, circular_motion_solved_questions, 90 )
```


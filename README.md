# Quiz Creator

The Quiz Creator is a Python program that allows you to create custom quizzes by entering questions and answers. It supports multiple-choice questions and true/false questions. The program shuffles the questions and answers (except for true/false questions) to create a randomized quiz. It also generates an answer key for the quiz.

## Features

- Create custom quizzes with multiple-choice and true/false questions
- Specify the correct answer for each question
- Shuffle questions and answers for a randomized quiz experience
- Generate an answer key for the quiz
- Save the quiz and answer key to separate files

## Requirements

- Python 3.x

## Usage

1. Clone the repository or download the `quiz_creator.py` file.

2. Open a terminal or command prompt and navigate to the directory where the `quiz_creator.py` file is located.

3. Run the program using the following command:
   ```
   python quiz_creator.py
   ```

4. Follow the prompts to enter your questions and answers:
   - Enter a question or press Enter to finish.
   - Enter the answers for each question (minimum 2 answers required).
   - Specify the correct answer for each question.
   - For true/false questions, provide only 2 answers.

5. After entering all the questions and answers, the program will create the quiz and shuffle the questions and answers.

6. The program will save the quiz to a file named `quiz.txt` and the answer key to a file named `answer_key.txt` in the same directory.

7. The quiz and answer key will be displayed in the console, and you will find the saved files in the program's directory.

## Example

Here's an example of how to use the Quiz Creator:

```
Welcome to the Quiz Creator!
Enter your questions and answers below.
For true/false questions, provide only 2 answers.

Enter a question (or press Enter to finish): What is the capital of France?
Enter answer 1 (or press Enter to skip): Paris
Is this the correct answer? (y/n): y
Enter answer 2 (or press Enter to skip): London
Is this the correct answer? (y/n): n
Enter answer 3 (or press Enter to skip): Berlin
Is this the correct answer? (y/n): n
Enter answer 4 (or press Enter to skip): Madrid
Is this the correct answer? (y/n): n
Enter a question (or press Enter to finish):

Creating quiz...
Shuffling questions and answers...
Saving quiz to file...
Saving answer key to file...

Quiz and answer key saved successfully!
Thank you for using the Quiz Creator!
```

After running the program, you will find the `quiz.txt` and `answer_key.txt` files in the program's directory.

## License

This project is licensed under the [MIT License](LICENSE).

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.

## Acknowledgements

This program was created as a learning exercise and is based on the concepts of quiz creation and file handling in Python.
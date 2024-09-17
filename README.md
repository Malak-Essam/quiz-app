# quiz-app

# Quiz Application

This is a Python-based quiz application built using **Tkinter**. The application reads questions and answers from a CSV file and allows users to:
- View a question, reveal the correct answer, and mark whether they got it correct or incorrect.
- Navigate between questions using "Next" and "Previous" buttons.
- Track their score as they progress through the quiz.
- Add new questions and answers to the quiz, which are saved to the CSV file.

The app is designed to be simple, and it can be packaged as a Windows executable using **PyInstaller**.

## Features

- **Load Questions from CSV**: Reads questions and answers from a `questions.csv` file.
- **Score System**: Users can mark their answers as correct or incorrect, and the score is tracked.
- **Add Questions**: Users can add new questions and answers, which are saved directly to the CSV file.
- **Show Answer**: The correct answer is hidden until the user clicks "Show Answer".
- **Responsive Navigation**: Users can navigate between questions using "Next" and "Previous" buttons.
- **Maximized Window**: The app launches in a maximized window with a pleasant background color.

## Screenshot

![Quiz App Screenshot](path_to_screenshot_image)

## Getting Started

### Prerequisites

To run this application, you'll need to have Python installed on your machine along with the following packages:
- `pandas`
- `tkinter`
- `pyinstaller` (if you plan to package the app as an executable)

You can install the required packages using `pip`:

```bash
pip install pandas
```

### Installing

1. Clone the repository:

```bash
git clone https://github.com/your-username/quiz-application.git
cd quiz-application
```

2. Ensure that your `questions.csv` file is placed in the root directory, with the following format:

```csv
Question,Answer
What is the capital of France?,Paris
Who wrote 'To Kill a Mockingbird'?,Harper Lee
```

3. Run the application:

```bash
python quiz_app.py
```

### Packaging as a Windows Executable

To package this application as a standalone Windows executable, use **PyInstaller**:

1. Install PyInstaller:

   ```bash
   pip install pyinstaller
   ```

2. Package the app:

   ```bash
   pyinstaller --onefile --windowed quiz_app.py
   ```

3. The executable will be available in the `dist` folder.

## Usage

- **Show Answer**: Click the "Show Answer" button to reveal the answer to the current question.
- **Correct/Incorrect**: Mark your answer as correct or incorrect using the respective buttons. Your score will update accordingly.
- **Next/Previous**: Navigate between questions using the "Next" and "Previous" buttons.
- **Add Questions**: Add new questions and answers using the input fields at the bottom of the app.

## CSV File Format

Ensure your `questions.csv` follows this format:

```csv
Question,Answer
What is the capital of France?,Paris
Who developed the theory of relativity?,Albert Einstein
```

The app will automatically load new questions from this file upon launch, and any new questions added through the app will be saved to this file.

## Contributing

Contributions are welcome! If you have any ideas or improvements, feel free to fork the repository and submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

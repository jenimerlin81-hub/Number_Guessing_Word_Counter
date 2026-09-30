# Number Guessing Game & Word Counter

A beginner-friendly Python CLI project that combines a random number guessing game with a file-based word counter and frequency analyzer.

## 📌 Project Overview

This project contains two simple Python tools:

1. **Number Guessing Game** – Guess a randomly generated number within a limited number of attempts.
2. **Word Counter** – Read a text file, count the total number of words, and analyze word frequency.

## ✨ Features

### 🎯 Number Guessing Game

* Generates a random number between 1 and 100
* Allows up to 7 attempts
* Shows "Too High" or "Too Low" hints
* Tracks the number of attempts
* Calculates a score

### 📝 Word Counter

* Reads words from a `.txt` file
* Counts the total number of words
* Calculates word frequency
* Ignores uppercase/lowercase differences
* Removes punctuation
* Handles missing files

## 🛠️ Technologies Used

* Python 3
* Random Module
* String Manipulation
* File Handling
* Dictionaries
* Exception Handling
* Command Line Interface (CLI)

## 📂 Project Structure

```text
Number_Guessing_Word_Counter/
│
├── main.py
├── sample.txt
└── README.md
```

## ▶️ How to Run

### 1. Check Python

```bash
python --version
```

### 2. Run the Program

```bash
python main.py
```

## 💻 Main Menu

```text
========================================
 NUMBER GUESSING GAME & WORD COUNTER
========================================

1. Number Guessing Game
2. Word Counter
3. Exit

Enter your choice:
```

## 🎯 Sample Guessing Game

```text
I have selected a number between 1 and 100.
Try to guess the number!

Enter your guess: 50
Too low!

Enter your guess: 75
Too high!

Enter your guess: 63
Congratulations! You guessed the correct number.

Number of attempts: 3
Your score: 50
```

## 📝 Sample Word Counter

```text
Enter text file name: sample.txt

Total number of words: 19

===== Word Frequency =====
easy : 2
is : 3
python : 4
```

## 🧠 Concepts Learned

* Random number generation
* `while` loops
* Conditional statements
* Functions
* Counters and scoring
* File handling
* String manipulation
* Dictionaries
* Exception handling
* User input validation

## 🚀 Future Improvements

* Add difficulty levels
* Add multiple game rounds
* Save high scores
* Support multiple text files
* Display the most frequent words
* Add a graphical user interface

## 👩‍💻 Author

**Jeni Merlin**

AI & Data Science Student

## 📄 License

This project is created for educational and learning purposes.

#!/usr/bin/env python
# coding: utf-8

# In[1]:


import tkinter as tk
from tkinter import messagebox
import pandas as pd

# Load the questions from the CSV file
def load_questions():
    try:
        return pd.read_csv('questions.csv')
    except FileNotFoundError:
        messagebox.showerror("File Not Found", "The file 'questions.csv' was not found.")
        return pd.DataFrame({'Question': [], 'Answer': []})  # Return an empty DataFrame if the file is not found

# Save the updated questions DataFrame to CSV
def save_questions():
    df.to_csv('questions.csv', index=False)

# Load initial dataset
df = load_questions()

# Initialize variables
current_question = 0
score = 0

# Function to show the next question
def next_question():
    global current_question
    if current_question < len(df) - 1:
        current_question += 1
        update_question()
        hide_answer()

# Function to show the previous question
def prev_question():
    global current_question
    if current_question > 0:
        current_question -= 1
        update_question()
        hide_answer()

# Function to update the question
def update_question():
    question_label.config(text=df.iloc[current_question, 0])
    hide_answer()

# Function to hide the answer
def hide_answer():
    answer_label.config(text="Answer: ???", fg='blue')

# Function to show the answer
def show_answer():
    answer_label.config(text=f"Answer: {df.iloc[current_question, 1]}", fg='blue')

# Function to mark as correct and increase score
def mark_correct():
    global score
    score += 1
    score_label.config(text=f"Score: {score}")
    messagebox.showinfo("Correct", "Good job!")
    next_question()

# Function to mark as incorrect
def mark_incorrect():
    messagebox.showinfo("Incorrect", f"The correct answer is: {df.iloc[current_question, 1]}")
    next_question()

# Function to add a new question and answer
def add_question():
    question = question_entry.get()
    answer = answer_entry.get()

    if question and answer:
        global df
        new_data = pd.DataFrame({'Question': [question], 'Answer': [answer]})
        df = pd.concat([df, new_data], ignore_index=True)
        save_questions()  # Save the updated DataFrame to the CSV
        messagebox.showinfo("Success", "Question added successfully!")
        question_entry.delete(0, 'end')
        answer_entry.delete(0, 'end')
    else:
        messagebox.showwarning("Input Error", "Please enter both the question and the answer.")

# Create the main window
root = tk.Tk()
root.title("Quiz Application")

# Maximize the window
root.state('zoomed')

# Set background color
root.config(bg='#D6EAF8')

# Frame for the question and answer display
display_frame = tk.Frame(root, padx=10, pady=10, bg='#D6EAF8')
display_frame.pack(pady=20)

# Add question label
question_label = tk.Label(display_frame, text=df.iloc[current_question, 0], wraplength=800, font=('Helvetica', 20), fg='black', bg='#D6EAF8')
question_label.pack(pady=10)

# Show answer button
btn_show_answer = tk.Button(display_frame, text="Show Answer", font=('Helvetica', 14), command=show_answer)
btn_show_answer.pack(pady=10)

# Add answer label, initially hidden
answer_label = tk.Label(display_frame, text="Answer: ???", wraplength=800, font=('Helvetica', 16), fg='blue', bg='#D6EAF8')
answer_label.pack(pady=10)

# Score label
score_label = tk.Label(root, text=f"Score: {score}", font=('Helvetica', 18), bg='#D6EAF8')
score_label.pack(pady=20)

# Buttons for "Correct" and "Incorrect"
btn_frame = tk.Frame(root, bg='#D6EAF8')
btn_frame.pack(pady=10)

btn_correct = tk.Button(btn_frame, text="Correct", font=('Helvetica', 14), command=mark_correct)
btn_correct.pack(side='left', padx=10)

btn_incorrect = tk.Button(btn_frame, text="Incorrect", font=('Helvetica', 14), command=mark_incorrect)
btn_incorrect.pack(side='left', padx=10)

# Buttons for Next and Previous question
nav_frame = tk.Frame(root, bg='#D6EAF8')
nav_frame.pack(pady=10)

btn_prev = tk.Button(nav_frame, text="Previous Question", font=('Helvetica', 14), command=prev_question)
btn_prev.pack(side='left', padx=10)

btn_next = tk.Button(nav_frame, text="Next Question", font=('Helvetica', 14), command=next_question)
btn_next.pack(side='left', padx=10)

# Separator between display and question adding section
separator = tk.Label(root, text="----------------------------------------------------", bg='#D6EAF8')
separator.pack(pady=10)

# Frame for adding new questions
add_frame = tk.Frame(root, padx=10, pady=10, bg='#D6EAF8')
add_frame.pack(pady=10)

# Entry for new question
question_entry_label = tk.Label(add_frame, text="New Question:", font=('Helvetica', 12), bg='#D6EAF8')
question_entry_label.grid(row=0, column=0, padx=10, pady=5)
question_entry = tk.Entry(add_frame, width=40, font=('Helvetica', 12))
question_entry.grid(row=0, column=1, padx=10, pady=5)

# Entry for new answer
answer_entry_label = tk.Label(add_frame, text="New Answer:", font=('Helvetica', 12), bg='#D6EAF8')
answer_entry_label.grid(row=1, column=0, padx=10, pady=5)
answer_entry = tk.Entry(add_frame, width=40, font=('Helvetica', 12))
answer_entry.grid(row=1, column=1, padx=10, pady=5)

# Button to add new question and answer
btn_add_question = tk.Button(add_frame, text="Add Question", font=('Helvetica', 12), command=add_question)
btn_add_question.grid(row=2, columnspan=2, pady=10)

# Start the application
root.mainloop()


# In[ ]:





# -*- coding: utf-8 -*-
"""Untitled0.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1CxTv73yxocuBlApCXFW1NgkLbdYxQF9y
"""

import pandas as pd
import matplotlib.pyplot as plt

# Create a DataFrame manually
data = {
    'studentId': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],
    'rollno': ['A001', 'A002', 'A003', 'A004', 'A005', 'A006', 'A007', 'A008', 'A009', 'A010',
               'A011', 'A012', 'A013', 'A014', 'A015', 'A016', 'A017', 'A018', 'A019', 'A020'],
    'name': ['John', 'Ram', 'Mohit', 'Sophia', 'Rahul', 'Ayushi', 'James', 'Avansh', 'Benjamin', 'Ishi',
             'Henry', 'Shyam', 'Alexander', 'Virat', 'Daniel', 'Aman', 'Matthew', 'Elexa', 'Jos', 'Harprit'],
    'branch': ['CSE', 'ECE', 'ME', 'CSE', 'ECE', 'ME', 'CSE', 'ECE', 'ME', 'CSE',
               'ECE', 'ME', 'CSE', 'ECE', 'ME', 'CSE', 'ECE', 'ME', 'CSE', 'ECE'],
    'subject1_marks': [75, 82, 91, 63, 77, 88, 79, 85, 92, 78, 86, 74, 80, 84, 69, 81, 88, 72, 79, 83],
    'subject2_marks': [80, 85, 89, 76, 78, 92, 74, 81, 87, 83, 76, 68, 84, 90, 77, 75, 83, 88, 91, 79],
    # ... add more subject columns if needed
}

df = pd.DataFrame(data)

# (a) Insert new column
df['total_marks'] = df.iloc[:, 4:].sum(axis=1)

# (b) Calculate min, max, count on numerical data
min_marks = df.iloc[:, 4:].min().to_frame(name='min_marks')
max_marks = df.iloc[:, 4:].max().to_frame(name='max_marks')
count_students = df.shape[0]

# (c) Visualize the data using Barplot and Lineplot
df.plot(x='name', y=['subject1_marks', 'subject2_marks'], kind='bar')
plt.title('Subject Marks for Students')
plt.xlabel('Students')
plt.ylabel('Marks')
plt.show()

df.plot(x='name', y='total_marks', kind='line', marker='o')
plt.title('Total Marks for Students')
plt.xlabel('Students')
plt.ylabel('Total Marks')
plt.show()


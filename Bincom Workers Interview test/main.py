from cgitb import html
import sqlite3
from optparse import Values
import random as rd
from collections import Counter
from itertools import count
import re
from statistics import mean, median, mode, variance
from turtle import color


HTML = '''<html>
<head>
<title>Our Python Class exam</title>

<style type="text/css">

	body{
		width:1000px;
		margin: auto;
	}
	table,tr,td{
		border:solid;
		padding: 5px;
	}
	table{
		border-collapse: collapse;
		width:100%;
	}
	h3{
		font-size: 25px;
		color:green;
		text-align: center;
		margin-top: 100px;
	}
	p{
		font-size: 18px;
		font-weight: bold;
	}
</style>

</head>
<body>
<h3>TABLE SHOWING COLOURS OF DRESS BY WORKERS AT BINCOM ICT FOR THE WEEK</h3>
<table>

	<thead>
		<th>DAY</th><th>COLOURS</th>
	</thead>
	<tbody>
	<tr>
		<td>MONDAY</td>
		<td>GREEN, YELLOW, GREEN, BROWN, BLUE, PINK, BLUE, YELLOW, ORANGE, CREAM, ORANGE, RED, WHITE, BLUE, WHITE, BLUE, BLUE, BLUE, GREEN</td>
	</tr>
	<tr>
		<td>TUESDAY</td>
		<td>ARSH, BROWN, GREEN, BROWN, BLUE, BLUE, BLEW, PINK, PINK, ORANGE, ORANGE, RED, WHITE, BLUE, WHITE, WHITE, BLUE, BLUE, BLUE</td>
	</tr>
	<tr>
		<td>WEDNESDAY</td>
		<td>GREEN, YELLOW, GREEN, BROWN, BLUE, PINK, RED, YELLOW, ORANGE, RED, ORANGE, RED, BLUE, BLUE, WHITE, BLUE, BLUE, WHITE, WHITE</td>
	</tr>
	<tr>
		<td>THURSDAY</td>
		<td>BLUE, BLUE, GREEN, WHITE, BLUE, BROWN, PINK, YELLOW, ORANGE, CREAM, ORANGE, RED, WHITE, BLUE, WHITE, BLUE, BLUE, BLUE, GREEN</td>
	</tr>
	<tr>
		<td>FRIDAY</td>
		<td>GREEN, WHITE, GREEN, BROWN, BLUE, BLUE, BLACK, WHITE, ORANGE, RED, RED, RED, WHITE, BLUE, WHITE, BLUE, BLUE, BLUE, WHITE</td>
	</tr>

	</tbody>
</table>

<p>Examine the sequence below very well, you will discover that for every 1s that appear 3 times, the output will be one, otherwise the output will be 0.</p>
<p>0101101011101011011101101000111 <span style="color:orange;">Input</span></p>
<p>0000000000100000000100000000001 <span style="color:orange;">Output</span></p>
<p>
</body>
</html>'''

# Which color of shirt is the mean color?
# Using Regular Expressions (RE) to find a list containing all colours
all_colours = re.findall('[A-Z]+', HTML)
colours = [colour for colour in all_colours]
color_counts = Counter(colours)

mean_colours = max(color_counts, key=colours.count)
print('Question: Which color of shirt is the mean color?',
      '\n Answer:', mean_colours)

# Which color is mostly worn throughout the week?
mode_colours = (mode(colours))
print('Question: Which color is mostly worn throughout the week?',
      '\n Answer:', mode_colours)

# Which color is the median?
sorted_colors = sorted(all_colours)
median_color = median(sorted_colors)
print('Which color is the median?',
      '\n Answer:', median_color)

# Get the variance of the colors
frequencies = list(color_counts.values())
variance_color = variance(frequencies)
print('Get the variance of the colors',
      '\n Answer:', variance_color)


# if a colour is chosen at random, what is the probability that the color is red?
total_colors = sum(color_counts.values())
red = ((color_counts['RED']))
probability_red = red / total_colors
print('if a colour is chosen at random, what is the probability that the color is red?',
      '\n Answer:', probability_red)

conn = sqlite3.connect('colors.db')
cursor = conn.cursor()

# Save the colours and their frequencies in postgresql database
cursor.execute('''
CREATE TABLE IF NOT EXISTS color_frequencies (
    color TEXT PRIMARY KEY,
    frequency INTEGER
)
''')
for color, frequency in color_counts.items():
    cursor.execute('''
    INSERT OR REPLACE INTO color_frequencies (color, frequency)
    VALUES (?, ?)
    ''', (color, frequency))
conn.commit()
cursor.execute('SELECT * FROM color_frequencies')
rows = cursor.fetchall()

print("Colors and their frequencies stored in SQLite database:")
for row in rows:
    print(f"{row[0]}: {row[1]}")
conn.close()

# write a recursive searching algorithm to search for a number entered by user in a list of numbers.
mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def search(my_list, val):
    try:
        return 'number is in the list in index:', my_list.index(val)
    except ValueError:
        return "number not found"


x = int(input("Enter number to check in the list:"))
print(search(mylist, x))

# Write a program that generates random 4 digits number of 0s and 1s and convert the generated number to base 10
binary_number = ''.join(rd.choice('01') for _ in range(4))
decimal_number = int(binary_number, 2)
print("Generated 4-digit binary number:",
      {binary_number}, " Converted to decimal (base 10):", {decimal_number})


# Write a program to sum the first 50 fibonacci sequence
# fibonacci sequence generator code
n = 50
num1 = 0
num2 = 1
sum_fib = 0
count = 1

while count <= n:
    sum_fib += num1
    num1, num2 = num2, num1 + num2
    count += 1

print("Sum of the first 50 Fibonacci numbers:", sum_fib)

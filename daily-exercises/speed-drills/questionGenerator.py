import json
import random
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

"""
NumPy Speed Drill Notebook Generator

This script generates a Jupyter notebook (.ipynb) containing a random set of
NumPy practice drills selected from a predefined question bank.

Main features
-------------
• Randomly selects questions from the drill bank.
• The number of questions is controlled by NUM_QUESTIONS.
• Each run uses a randomly generated seed so the exact drill set can be reproduced.
• The seed is embedded in the notebook filename.

Example output:
    numpy_speed_drill_seed_4839201.ipynb

Notebook structure
------------------
The generated notebook contains:

1. A start cell that:
   - starts a timer
   - initializes session metadata
   - prepares stats tracking

2. A NumPy import cell.

3. A sequence of drill questions:
   - each question is a markdown cell
   - followed by an empty code cell where the user writes the solution

4. A final cell that:
   - stops the timer
   - calculates total session time
   - appends the session statistics to a shared JSON file

Statistics tracking
-------------------
Session statistics are stored in a shared file:

    drill_stats.json

Each completed notebook session appends an entry containing:
    - seed used to generate the drill set
    - number of questions
    - total time taken
    - finished status

Example entry:

{
  "seed": 4839201,
  "questions": 30,
  "total_time_seconds": 1420,
  "finished": true
}

If the final cell is not executed, the session is considered unfinished
and no entry is written.

Purpose
-------
This tool is meant for fast repetition and muscle-memory training for
common NumPy operations such as indexing, slicing, broadcasting,
sorting, searching, aggregation, and conditional operations.

The generator allows repeated practice with varied drill sets while
keeping performance statistics across sessions.
"""

# -----------------
# SETTINGS
# -----------------

SEED = random.randint(0, 10_000_000)   # auto seed
random.seed(SEED)

NUM_QUESTIONS = 20

OUTPUT_FILE = BASE_DIR / f"numpy_speed_drill_seed_{SEED}.ipynb"
STATS_FILE = "C:/Users/fbase/All_vscode_projects/numpyGithubRepo/daily-exercises/speed-drills/drill_stats.json"

# -----------------
# QUESTION SETS
# -----------------

sets = {

"set1": [
"Given A = np.arange(1,26).reshape(5,5), extract the entire 4th column.",
"Given A = np.arange(1,26).reshape(5,5), extract the last two rows.",
"Given A = np.arange(1,26).reshape(5,5), extract the middle 3x3 block.",
"Given A = np.arange(1,26).reshape(5,5), extract first 3 rows but columns 2–4.",
"Given A = np.arange(1,26).reshape(5,5), reverse the row order.",
"Given A = np.arange(1,26).reshape(5,5), reverse the column order.",
"Given A = np.arange(1,26).reshape(5,5), extract all even numbers using boolean indexing.",
"Given A = np.arange(1,26).reshape(5,5), replace values >15 with 0.",
"Given A = np.arange(1,26).reshape(5,5), extract the four corner elements.",
"Given A = np.arange(1,26).reshape(5,5), extract the diagonal elements."
],

"set2": [
"Given A = np.arange(-10,15), extract all positive numbers.",
"Given A = np.arange(-10,15), replace negative numbers with 0.",
"Given A = np.arange(-10,15), replace numbers between 5 and 10 with 99.",
"Given A = np.arange(-10,15), count how many numbers are even.",
"Given A = np.arange(-10,15), extract numbers divisible by 3.",
"Given A = np.arange(-10,15), create an array where values >5 become 1 else 0.",
"Given A = np.arange(-10,15), compute the sum of positive numbers.",
"Given A = np.arange(-10,15), find indices where value < -5.",
"Given A = np.arange(-10,15), clip values to [-3,7].",
"Given A = np.arange(-10,15), replace odd numbers with -1."
],

"set3": [
"Given A = np.array([8,3,15,1,9,12,7,5]), sort ascending.",
"Given A = np.array([8,3,15,1,9,12,7,5]), sort descending.",
"Given A = np.array([8,3,15,1,9,12,7,5]), get indices that would sort the array.",
"Given A = np.array([8,3,15,1,9,12,7,5]), find index of largest value.",
"Given A = np.array([8,3,15,1,9,12,7,5]), find index of smallest value.",
"Given A = np.array([8,3,15,1,9,12,7,5]), get the 3 largest values.",
"Given A = np.array([8,3,15,1,9,12,7,5]), get the 3 smallest values.",
"Given A = np.array([8,3,15,1,9,12,7,5]), find positions where value > 8.",
"Given A = np.array([8,3,15,1,9,12,7,5]), count elements greater than the mean.",
"Given A = np.array([8,3,15,1,9,12,7,5]), find unique elements."
],

"set4": [
"Given A = np.arange(12).reshape(4,3), add 5 to every element.",
"Given A = np.arange(12).reshape(4,3), multiply all elements by 2.",
"Given A = np.arange(12).reshape(4,3), subtract row means from each row.",
"Given A = np.arange(12).reshape(4,3), normalize the array to 0-1 range.",
"Given A = np.arange(12).reshape(4,3), add vector [10,20,30] to each row.",
"Given A = np.arange(12).reshape(4,3), multiply columns by [1,2,3].",
"Given A = np.arange(12).reshape(4,3), compute row sums.",
"Given A = np.arange(12).reshape(4,3), compute column means.",
"Given A = np.arange(12).reshape(4,3), convert values >6 to 1 else 0.",
"Given A = np.arange(12).reshape(4,3), square every element."
],

"set5": [
"Given A = np.random.randint(0,20,(5,5)), count elements greater than 10.",
"Given A = np.random.randint(0,20,(5,5)), find max value in each row.",
"Given A = np.random.randint(0,20,(5,5)), find min value in each column.",
"Given A = np.random.randint(0,20,(5,5)), compute total sum.",
"Given A = np.random.randint(0,20,(5,5)), compute column means.",
"Given A = np.random.randint(0,20,(5,5)), count how many numbers are even.",
"Given A = np.random.randint(0,20,(5,5)), get indices of the max value.",
"Given A = np.random.randint(0,20,(5,5)), compute standard deviation.",
"Given A = np.random.randint(0,20,(5,5)), compute diagonal sum.",
"Given A = np.random.randint(0,20,(5,5)), count elements equal to row mean."
],

"set6": [
"Given A = np.arange(1,13), reshape into 3x4.",
"Reshape A into 2x6.",
"Convert A into a column vector.",
"Convert A into a row vector.",
"Flatten a 3x4 reshaped version of A.",
"Use ravel to convert reshaped A back to 1D.",
"Reshape into 4x3 then transpose.",
"Reverse the flattened array.",
"Reshape into 3x4 then extract the second row.",
"Reshape into 3x4 then extract the last column."
],

"set7": [
"Given A = np.arange(-6,10), replace negatives with 0 using np.where.",
"Replace values >5 with 100 using np.where.",
"Create array where positives become 1 else 0.",
"Extract indices of even numbers using np.where.",
"Replace multiples of 3 with -3.",
"Convert numbers between 2 and 6 into 50.",
"Extract values < -2 using a mask.",
"Replace odd numbers with their negative.",
"Square values >0 otherwise leave unchanged.",
"Replace numbers divisible by 4 with 999."
],

"set8": [
"Given A = np.arange(1,21).reshape(4,5), compute row sums.",
"Compute column sums.",
"Find row index containing maximum value.",
"Extract elements greater than overall mean.",
"Replace values >15 with row mean.",
"Compute difference between each element and column mean.",
"Normalize each row by its row sum.",
"Extract anti-diagonal.",
"Find positions of multiples of 5.",
"Replace entire third column with zeros."
]

}

# -----------------
# FLATTEN BANK
# -----------------

question_bank = []
for s in sets.values():
    question_bank.extend(s)

selected = random.sample(question_bank, NUM_QUESTIONS)

# -----------------
# NOTEBOOK BUILD
# -----------------

cells = []

cells.append({
"cell_type": "markdown",
"metadata": {},
"source": [
"# NumPy Speed Drill\n",
f"Random seed used for this notebook: **{SEED}**\n",
"If you want to reproduce this exact drill set, run the generator with this seed."
]
})

cells.append({
"cell_type": "code",
"metadata": {},
"execution_count": None,
"outputs": [],
"source": [

"import time, json\n",
"from pathlib import Path\n",
"\n",
f"SEED = {SEED}\n",
f"NUM_QUESTIONS = {NUM_QUESTIONS}\n",
f'STATS_FILE = \"{STATS_FILE}\" \n',
"\n",
"start_time = time.time()\n",
"print('Timer started')\n"
]
})

cells.append({
"cell_type": "code",
"metadata": {},
"execution_count": None,
"outputs": [],
"source": ["import numpy as np"]
})

for i, q in enumerate(selected, 1):

    cells.append({
        "cell_type": "markdown",
        "metadata": {},
        "source": [f"### Question {i}\n{q}"]
    })

    cells.append({
        "cell_type": "code",
        "metadata": {},
        "execution_count": None,
        "outputs": [],
        "source": [""]
    })

cells.append({
"cell_type": "markdown",
"metadata": {},
"source": ["## RUN THE NEXT CELL WHEN YOU FINISH ALL QUESTIONS"]
})

cells.append({
"cell_type": "code",
"metadata": {},
"execution_count": None,
"outputs": [],
"source": [

"end_time = time.time()\n",
"total_time = end_time - start_time\n",
"\n",
"stats_file = Path(STATS_FILE)\n",
"\n",
"data = []\n",
"if stats_file.exists():\n",
"    data = json.loads(stats_file.read_text())\n",
"\n",
"entry = {\n",
"    'seed': SEED,\n",
"    'questions': NUM_QUESTIONS,\n",
"    'total_time_seconds': total_time,\n",
"    'finished': True\n",
"}\n",
"\n",
"data.append(entry)\n",
"stats_file.write_text(json.dumps(data, indent=2))\n",
"\n",
"print('Session complete')\n",
"print(f'Total time: {total_time/60:.2f} minutes')\n"
]
})

notebook = {
"cells": cells,
"metadata": {},
"nbformat": 4,
"nbformat_minor": 5
}

with open(OUTPUT_FILE, "w") as f:
    json.dump(notebook, f)

print(f"Created {OUTPUT_FILE} with {NUM_QUESTIONS} drills")
print(f"Seed used: {SEED}")
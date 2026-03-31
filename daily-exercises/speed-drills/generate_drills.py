"""
NumPy Speed Drill Notebook Generator

This script generates a Jupyter notebook (.ipynb) containing a random set of
NumPy practice drills selected from question banks stored in a separate folder.

Main features
-------------
• Automatically loads all question files from the `question-banks` directory.
• Any Python file in that folder can define one or more lists ending with `_QUESTIONS`.
• Questions are grouped by topic based on their filename.
• Randomly selects questions from the combined question pool.
• The number of questions is controlled by NUM_QUESTIONS.
• Each run uses a randomly generated seed so the exact drill set can be reproduced.
• The seed is embedded in the notebook filename.

Example output
--------------
numpy_speed_drill_seed_4839201.ipynb


Notebook structure
------------------
The generated notebook contains:

1. A start cell that:
   - starts a timer
   - initializes session metadata
   - prepares statistics tracking

2. A NumPy import cell.

3. A sequence of drill questions:
   - each question is a markdown cell
   - followed by an empty code cell where the user writes the solution

4. A final cell that:
   - stops the timer
   - calculates total session time
   - calculates average seconds per question
   - appends session statistics to a shared JSON file


Statistics tracking
-------------------
Session statistics are stored in a shared file:

    drill_stats.json

Each completed drill session appends an entry containing:

    - session date
    - random seed used
    - number of questions
    - total session time
    - average seconds per question
    - topic distribution of selected questions
    - attempted_all flag (indicates the session was completed)

Example entry:

{
  "date": "2026-03-11T20:14:21",
  "seed": 4839201,
  "questions": 20,
  "total_time_seconds": 1320,
  "avg_seconds_per_question": 66,
  "topics": {
      "indexing": 5,
      "sorting": 4,
      "broadcasting": 3
  },
  "attempted_all": true
}

If the final notebook cell is not executed, no entry is written to the
statistics file, which implicitly indicates the drill session was abandoned.


Purpose
-------
This tool is designed for fast repetition and muscle-memory training of
common NumPy operations such as:

    - indexing
    - slicing
    - broadcasting
    - sorting
    - searching
    - aggregation
    - reshaping
    - conditional operations

Over time, the accumulated statistics can be analyzed (EDA) to observe
practice patterns, speed improvements, topic distribution, and session history.
"""

import json
import random
import importlib.util
import subprocess
import sys
from datetime import datetime
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
QUESTION_BANK_DIR = BASE_DIR.parents[1] / "question-banks"
NOTEBOOK_DIR = BASE_DIR / "notebooks"

NOTEBOOK_DIR.mkdir(exist_ok=True)

STATS_FILE = BASE_DIR / "drill_stats.json"

# -----------------
# SETTINGS
# -----------------

NUM_QUESTIONS = 15
SEED = random.randint(0, 10_000_000)
random.seed(SEED)

OUTPUT_FILE = NOTEBOOK_DIR / f"numpy_speed_drill_seed_{SEED}.ipynb"


# -----------------
# LOAD QUESTION BANKS
# -----------------

question_bank = []

for file in QUESTION_BANK_DIR.glob("*.py"):

    topic = file.stem.replace("_questions", "")

    spec = importlib.util.spec_from_file_location(file.stem, file)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)

    for attr in dir(module):

        if attr.endswith("_QUESTIONS"):

            for q in getattr(module, attr):

                question_bank.append((topic, q))


if len(question_bank) < NUM_QUESTIONS:

    raise ValueError(
        f"Not enough questions in bank ({len(question_bank)}) for {NUM_QUESTIONS} drills"
    )


selected = random.sample(question_bank, NUM_QUESTIONS)


# -----------------
# TOPIC COUNTS
# -----------------

topic_counts = {}

for topic, _ in selected:

    topic_counts[topic] = topic_counts.get(topic, 0) + 1


# -----------------
# NOTEBOOK BUILD
# -----------------

cells = []

cells.append({
"cell_type": "markdown",
"metadata": {},
"source": [
"# NumPy Speed Drill\n",
f"Seed: **{SEED}**\n",
f"Questions: **{NUM_QUESTIONS}**\n"
]
})


cells.append({
"cell_type": "code",
"metadata": {},
"execution_count": None,
"outputs": [],
"source":[

"import time, json\n",
"from pathlib import Path\n",
"from datetime import datetime\n",
"from datetime import datetime\n"

f"SEED = {SEED}\n",
f"NUM_QUESTIONS = {NUM_QUESTIONS}\n",
f"STATS_FILE = r\"{STATS_FILE}\"\n",
f"TOPIC_COUNTS = {topic_counts}\n",

"\nstart_time = time.time()\n",
"\nstart_timestamp = datetime.now()\n"
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


for i, (topic, q) in enumerate(selected, 1):

    cells.append({
        "cell_type": "markdown",
        "metadata": {},
        "source": [f"### Question {i} ({topic})\n{q}"]
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
"source":[

"end_time = time.time()\n",
"end_timestamp = datetime.now()\n"
"total_time = end_time - start_time\n",
"avg_time = total_time / NUM_QUESTIONS\n",

"\nstats_file = Path(STATS_FILE)\n",

"data = []\n",
"if stats_file.exists():\n",
"    data = json.loads(stats_file.read_text())\n",

"\nentry = {\n",
"    'date': datetime.now().isoformat(),\n",
"    'start_time':start_timestamp.isoformat(),\n",
"    'end_time':end_timestamp.isoformat(),\n",
"    'seed': SEED,\n",
"    'questions': NUM_QUESTIONS,\n",
"    'total_time_seconds': total_time,\n",
"    'avg_seconds_per_question': avg_time,\n",
"    'topics': TOPIC_COUNTS,\n",
"    'attempted_all': True\n",
"}\n",

"\ndata.append(entry)\n",
"stats_file.write_text(json.dumps(data, indent=2))\n",

"\nprint('Session complete')\n",
"print(f'Total time: {total_time/60:.2f} minutes')\n",
"print(f'Avg seconds/question: {avg_time:.2f}')\n"

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


print(f"Created {OUTPUT_FILE}")
print(f"Seed used: {SEED}")
print(f"Questions available: {len(question_bank)}")


# -----------------
# OPEN NOTEBOOK
# -----------------

try:

    subprocess.Popen(["code", str(OUTPUT_FILE)])

except FileNotFoundError:

    print("Jupyter not found in PATH — open notebook manually.")
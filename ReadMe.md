# ET3 Assignment

I chose **Option 3** for this submission. If more time becomes available, I’ll implement the other options and update this repository accordingly.

---

## Requirements

- Accepts a **path to a text file** (via user prompt).
- **Ignores punctuation and case** while counting.
- Displays the **top 10 most frequent words** with their counts.

## Bonus

- Handles **large files efficiently** by streaming line-by-line (no full file read into memory).
- Generates a **simple bar chart** of the top words using `matplotlib`.

---

## Prerequisites

- Python
- (For plotting) `matplotlib`


## Step-by-Step Setup

1. Clone the repository:
    ```bash
    git clone https://github.com/ANBadawy/ET3.git
    ```
2. Create and activate a virtual environment:
    ```bash
    # Windows
    python -m venv env
    env\Scripts\activate

    # Linux/Mac
    python3 -m venv env
    source env/bin/activate
    ```
3. Install required packages:
    ```bash
    pip install -r requirements.txt
    ```

4. Basic script (requirements only)
    ```bash
    python version_1_no_bonus.py
    ```

    When prompted, paste the path to your .txt file (e.g., D:\Ze_Env\ET3\Option_3\file_1.txt).

    **Output**: Prints a list of the top 10 words with counts.


5. Large-file + Plot script (requirements + bonus)
    ```bash
    python version_2_bonus.py
    ```

    - Streams the file line by line (good for huge files).

    - Shows a bar chart of the top 10 words.
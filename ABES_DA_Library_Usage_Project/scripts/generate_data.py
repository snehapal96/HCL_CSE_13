"""Reference script: shows the structure of the Library Usage dataset.
   The actual raw data is provided in data/raw/library_usage.xlsx.
   This script documents what columns exist and their intended distributions.
"""
import numpy as np
import pandas as pd

# ── Dataset dimensions ────────────────────────────────────────────────────────
# 250 real records + 5 intentional duplicates = 255 rows
# 11 columns

# ── Column distributions (approximate) ───────────────────────────────────────
# Member_Type  : Student 55%, Research Scholar 20%, Staff 15%, Faculty 10%
# Department   : CSE 30%, ECE 20%, Mechanical 20%, Management 20%, Civil 10%
# Preferred_Genre: Fiction, Technical, Self-Help, Competitive Exams, Reference
# Membership_Plan: Basic 65%, Premium 35%
# Age          : mostly 17–60 (intentional outliers: -21 and 150 added)
# Visits_Per_Month: 1–15
# Avg_Stay_Minutes: 10–120
# Distance_From_Home_Km: 0.3–15 km
# Books_Borrowed_Per_Month: 0–9

# ── Intentional data quality problems ────────────────────────────────────────
# 1. Missing values in: Preferred_Genre (5), Age (5),
#                       Avg_Stay_Minutes (5), Distance_From_Home_Km (5),
#                       Visit_Date (1)
# 2. Impossible Age values: -21 and 150
# 3. Inconsistent Department text: 'management', ' Management ', 'MECHANICAL', '  CSE', 'Management '
# 4. 5 duplicate rows appended at the end

print("Library Usage Dataset – structure reference loaded.")
print("See data/raw/library_usage.xlsx for the actual data.")

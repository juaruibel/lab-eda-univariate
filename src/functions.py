# Librerías

import sys
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from pathlib import Path


# Path

BASE_DIR = Path(__file__).resolve().parent.parent

DATA_DIR = BASE_DIR / "data"

# Carga

def load_data(file1):
    """
    Carga los datos del proyecto desde data_raw/
    """
    path = DATA_DIR / file1
    return pd.read_csv(path)

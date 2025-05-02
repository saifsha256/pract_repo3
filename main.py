import numpy as np
import pandas as pd

def main():

    arr = np.array([1, 2, 3, 4, 5, 6])
    print("Original NumPy Array:", arr) 

    s = pd.Series([10, 20, 30, 40, 50], name="MySeries")
    print("Pandas Series:\n", s)

    print("I'm not surprised motherf**kers!")

if __name__ == "__main__":
    main()
import numpy as np
import pandas as pd

def main():

    arr = np.array([1, 2, 3, 4, 5, 6])
    print("Original NumPy Array:", arr) 

    s = pd.Series([10, 20, 30, 40, 50], name="MySeries")
    print("Pandas Series:\n", s)

    print("I'm not surprised motherf**kers!")
    print("I love this shit. I can do this for my whole and it will never get boring.")

if __name__ == "__main__":
    main()
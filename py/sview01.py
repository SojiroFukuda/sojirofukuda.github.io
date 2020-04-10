# import package
from sviewgui import sview as sv
import pandas as pd

# sample code 1
sv.buidGUI()

# sample code 2
df = pd.DataFrame() 
sv.buildGUI(df)

# sample code 3
path = "User/Document/data.csv"
sv.buildGUI(path)

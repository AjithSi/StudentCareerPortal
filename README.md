# StudentCareerPortal

# Lets starts with simple Plots

# installing required libraries
from pip._internal import main
main(['install','numpy'])

from pip._internal import main
main(['install','pandas'])

from pip._internal import main
main(['install','matplotlib'])

from pip._internal import main
main(['install','openpyxl'])

# importing libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# 
response_main = pd.read_excel(C:\Temp\TechLabs (Responses).xlsx)

# viewing the first 5 rows
print(response_main.head())

# grouping and creating new dataframes

response_abitur = df[df['Was machen Sie zurzeit?'] == 'Abitur']
response_bachelor= df[df['Was machen Sie zurzeit?'] == 'Bachelor Studium']
response_master = df[df['Was machen Sie zurzeit?'] == 'Master Studium']

#Participants=P
P1 = "Number of Highschool students: " + str(response_abitur.shape[0])
P2 = "Number of Bachelor students: " + str(response_bachelor.shape[0])
P3 = "Number of Master students: " + str(response_master.shape[0])
print(P1 + " \n" + P2 + " \n" + P3 )

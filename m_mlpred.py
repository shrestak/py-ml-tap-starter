# Click on Packages - search and install sklearn-pandas

# input environment policy
# input Ethical Investment

import pandas as pd
from sklearn.naive_bayes import GaussianNB

criteria = {
"1111" : "Invest ESG",
"1110" : "Monitor ESG",
"0001" : "Prof Non ESG",
"0010" : "No Prof No ESG",
"0011" : "Prof Non ESG",
"0101" : "Prof Non ESG",
"0111" : "Prof Non ESG",
"1001" : "Prof Non ESG",
"1011" : "Prof Non ESG",
"1101" : "Prof Non ESG",
"0000" : "No Prof No ESG",
"0100" : "No Prof No ESG",
"0110" : "No Prof No ESG",
"1000" : "No Prof No ESG",
"1100" : "No Prof No ESG",
"0000" : "No Prof No ESG",
"1010" : "No Prof No ESG"
           }

ESGType = {
  1: "Invest_ESG",
  2: "Monitor_ESG",
  3: "Prof_Non_ESG",
  4: "No_Prof_No_ESG"
}

df = pd.read_csv("ESG-less-data.csv")
print(df.head())

# Update : Feature and label

print("*** Extracted features and label ***")

# Update : Train the model
print("**** Training Gaussian NB *****")


print("**** Training complete *****")

# Loop to accept user input and predict ESG status
while 1==1:
  print("Input Criteria with 1 or 0 in the following format:")
  print("Environmental_Policy, Ethical_Investment, Diverse_Board, Profitable")
  print("No commas, or Spaces. Example: 1011")
  combo_input = input("Enter criteria (EP EI DB PR) - ")
  combo_input = combo_input.replace(" ", "")  # Remove any spaces
  
  # Column Names should match the training data
  data = {
  "EP" : combo_input[0],
  "EI" : combo_input[1],
  "DB" : combo_input[2],
  "PR" : combo_input[3]  
  }
  
  column_names = ["EP","EI","DB","PR"]
  
  # Update Line - Create DataFrame for prediction
  
  # Update Line - Predict
  
  # Update line for manual prediction
  print("\n**** Status ****")
  print(f"ESG status Manual: ")
  # Update line for GausNB prediction
  print(f"ESG status GausNB: ")

  print("\n","-"*20)

  
  
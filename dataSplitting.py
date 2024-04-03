import pandas as pd
import random

# Read the CSV file into a pandas DataFrame
df = pd.read_csv('Song_Lyrics_For_Top_100_Songs_2014_to_2023.csv')

# Filter rows with 'true' in the 'LyricStatus' column
filtered_df = df[df['LyricsStatus'] == 'TRUE']

# get column names
colNames = ['Top100Year','SongTitle','Artist','LyricsStatus','Lyrics','ReleaseYear','Genre']#pd.DataFrame(df).columns

# set empty data frames for the 3 data sets
training = pd.DataFrame(columns=colNames)
validating = pd.DataFrame(columns=colNames)
testing = pd.DataFrame(columns=colNames)

# Defining the percentages for training, validation, and testing sets
train = 0.76
valid = 0.11
testi = 0.13

for i in range(2014, 2024):
    #print(i)
    # get one specific year
    year_df = filtered_df[filtered_df['Top100Year'] == str(i)]
    # randomize the order
    year_df = year_df.sample(frac=1).reset_index(drop=True)

    # Calculate the number of rows for each set based on percentages
    num_rows = len(year_df)
    train_size = int(num_rows * train)
    valid_size = int(num_rows * valid)
    testi_size = int(num_rows * testi)

    # Split the DataFrame into training, validation, and testing sets
    train_df = year_df[:train_size]
    valid_df = year_df[train_size:train_size + valid_size]
    testi_df = year_df[train_size + valid_size:]

    # append the new values
    training = pd.concat([training, train_df], ignore_index=True)
    validating = pd.concat([validating, valid_df], ignore_index=True)
    testing = pd.concat([testing, testi_df], ignore_index=True)


# Save the output to new CSV files
training.to_csv('trainingSet.csv', index=False)
validating.to_csv('validatingSet.csv', index=False)
testing.to_csv('testingSet.csv', index=False)

numTr = len(training)
numVa = len(validating)
numTe = len(testing)

print(f'training set has {numTr} rows')
print(f'validating set has {numVa} rows')
print(f'testing set has {numTe} rows')

print(f'total rows: {numTr+numVa+numTe}')

# -*- coding: utf-8 -*-
"""
Created on Jun 25 00:00:13 2023

@author: 0legs Borodins

My account: 
    https://github.com/DrOlegsBorodins/

Project: 
    https://github.com/DrOlegsBorodins/Transpose_Rearrange.git

PLEASE USE:
    CITATION.cff file as a citation if my work contributed to your publication.


Description:
    
In data arrangement, the transpose operation is used to convert the 
orientation of a table or matrix. More specifically, it flips the rows
and columns of the data, resulting in a new arrangement where the original
columns become rows and the original rows become columns.

The transpose operation is particularly useful in data management for several 
reasons:

 1. Reshaping Data: Transposing a table allows for a different perspective on 
    the data. It can be helpful when the original orientation of the data 
    doesn't suit the desired analysis or presentation format. By rearranging 
    the rows and columns, the data can be organized in a more convenient way.

 2. Statistical Analysis: Some statistical procedures require data to be in a 
    specific format. Transposing the data may be necessary to meet the 
    requirements of certain analysis techniques. For example, in multivariate 
    statistics, transposing data may be necessary to perform certain types of 
    factor analysis or clustering.

 3. Data Comparison: Transposing data can facilitate the comparison of 
    variables or observations. By switching the rows and columns, similar 
    variables or measurements can be aligned, making it easier to identify 
    patterns, similarities, or discrepancies across different entities or time 
    periods.

 4. Data Presentation: In certain cases, the transposed format can enhance the 
    presentation of data. For instance, when dealing with a large number of 
    variables or categories, transposing the data can make the table narrower 
    and easier to read by reducing the width of each row.

Overall, transposing data offers flexibility in data management, analysis, and 
presentation by reorienting the table's structure. It allows for different 
perspectives on the data and can improve its usability for various purposes.    
    
Information:
    We will use the randomly generated data 
    provied by Tabel_Raw.csv 
    (you also can find it in my GitHub).

Important web sources:

"""


#%%  Import all necessary packages

#Packages to find the packages

import pandas as pd
print("pandas")
print(pd.__version__)

import os
print("os")


#%%  Import data

# Show where is the data 
folder_path = r'C:\Users\0.13\Desktop'

# Set the file name
file_name = "Tabel_Raw"
filr_format = ".csv"

# Create the complete file path
RawData = os.path.join(folder_path, file_name+filr_format)

# Use the file path as needed
print("File path:", RawData)


# Read the table and now it will become a data frame (Index command to zero indicates that the first column in your table will be set as index)
# To remove it from the index type False in the command or if you need other columns as an index set it by putting the number of the column of your wish)

Data = pd.read_csv(RawData, low_memory=False, index_col=0)

# Print the first 3 lines 
print(Data.head(3))


#%%  Now we simply use the transpose function to change spaces between the rows and columns ( so now our columns become raw and vice versa) 

Result = Data.transpose()


#%% Let's save the table 

# Choose the format 
table_format = '.csv' 
New_file_name = "_transpose"

table_to_save = os.path.join(folder_path, file_name+New_file_name+table_format)

# Use the file path as needed
print("File path:", table_to_save)

# Save it
Result.to_csv(table_to_save)

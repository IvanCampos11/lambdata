# lambdata

https://test.pypi.org/project/lambdata-ivan/

##What it does and what's in it.
This package helps seeing and cleaning null values and adds the ability
to eaisly add new lists to the DataFrame as a column!

-nullReport: This just gets all the null values into one number and prints how many there are. Includes variation in grammar if theres only one NaN or multiple as well if they're absent!

-listToColumn: Give this a list and a name and it'll turn it into a series and add it as a new column.

-nullClean: This finds commonly used placeholders for NaN's and replces them to a real numpy NaN then it drops all rows containing them, cleaning the data.

##Getting Started

To get started using this package, you'll need pandas and numpy.

This package is based around DataFrames, use the DFMod(insert DataFrame) and you'll be all set in using all of its funcionality!

code to use: DFMod(insert DataFrame)

##nullReport
This usefull function searches the entire dataframe and reports if there are any null values (This does not show which columns have these null values!)

code to use: DFMod.nullReport()

##nullClean
This will search the entire dataframe and converts commonly used NaN types into a more
computer friendly, np.nan value! After, it will clean the data by dropping all of the rows containg them and then telling you how many null values it found and removed

code to use: DFMod.nullClean()

##listToColumn
This simply takes a given list and converts it into a pd.Series then adds this new series into the dataframe as a new column.

code to use: DFMod.listToColumn(insert list, "name of new list")


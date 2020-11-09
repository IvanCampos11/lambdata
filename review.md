# DFMod

So i know the assignment said make a class but classes that dont really rely on attributes a whole lot(of have self.dataframe) are better
off being functions. So as far ass god practice these should be functions but as far as the assignment grat job.

# NullReport

I like the .sum().sum(). I'm being picky but (there isn't anything glaringly wrong so i think im forced to) what you print out in the if
statements i would instead use f-strings as i prefer them but again im being picky.

# List to Column

You say lists.copy but you don't save it anywhere. Also since the list isn't being returned or sliced you don't need to copy it like you would a dataframe
when cleaning. You store the new column in the instance dataframe but also return it. Is there a reason for this? I man feasably sure lets save it in the object
and give it to the user but idk it's strange.

# Null clean
 First line is too long, no sure if it isn't pep compliant because im looking at it on github but it can be shorter. The replace method for dataframes
 can accept a dictionary so i would maybe try something like this
     df.replace({
         '?': np.nan, 'nan': np.nan,
         'etc': "etc"
     })
 # Extra
 Couldn't pip install ): unlucky.
 Because of this i'll have to say a 1 wich sucks everything was good with minor polishing but I couldn't install.
 Nonetheless great job man

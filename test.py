
import sklearn
import numpy as np

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_selection import SelectPercentile, chi2

cv=CountVectorizer(min_df=0.0, analyzer='word', ngram_range=(3, 4))


#from sklearn.feature_extraction.text import TfidfVectorizer
#tf=TfidfV
#ectorizer()

result=cv.fit_transform([file('/Users/Louis/Desktop/PJL2013/testdonne').read()])

sct = SelectPercentile(score=chi2, percentile=16)

X=[]

result1=sct.transform(result)

result.shape

print result
#print cv.vocabulary_

# import glob
#permet d'acceder a une liste des fichiers python
# t=glob.glob('./*.py') t[0] donne le premier fichier python

#count_vect = CountVectorizer()
#>>> X_train_counts = count_vect.fit_transform(twenty_train.data)
#>>> X_train_counts.shape

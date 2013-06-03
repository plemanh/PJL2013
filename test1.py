import sklearn
import numpy as np

from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer

cv=CountVectorizer()

X=cv.fit_transform([file('/Users/Louis/Desktop/PJL2013/testdonne1.txt').read(),file('/Users/Louis/Desktop/PJL2013/testdonne1.txt').read()])


tf=TfidfTransformer(use_idf=False).fit(X)

Y=tf.transform(X)


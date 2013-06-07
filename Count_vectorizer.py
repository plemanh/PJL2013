# import glob
#permet d'acceder a une liste des fichiers python
# t=glob.glob('./*.py') t[0] donne le premier fichier python


import glob
import sklearn
import numpy as np

from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer

# Creation de la liste des stop words
fich = open('/Users/paullemanh/Documents/Telecom/M1/PJL/stop_words')
y = []
for line in fich:
    y.append(line[0:-1])
pass

cv=CountVectorizer(min_df=0.0, analyzer='word', ngram_range=(1, 3), stop_words = y)

# Test countvectorizer sur plusieurs fichiers:
fichiers=glob.glob('/Users/paullemanh/Documents/Telecom/M1/PJL/Art_history/*')
sumdata=[]

# pour mettre tous les textes dans un seul
# fonctionne
for x in fichiers:
	sumdata.append(file(x).read())
pass

X=cv.fit_transform(sumdata)


#Utilisation de Tfidftransformer
tf=TfidfTransformer(use_idf=False).fit(X)
Y=tf.transform(X)


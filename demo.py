# Author : Alexandre Gramfort, alexandre.gramfort@telecom-paristech.fr
# License BSD

import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline 
from sklearn.pipeline import FeatureUnion
from sklearn.feature_selection import SelectPercentile, chi2
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cross_validation import cross_val_score

# Ne pas considerer tous les mots mais que ceux qui apparaissent avec une frequence faible
select = SelectPercentile(score_func=chi2, percentile=16)

#choix du classifieur: regression logistique
clf = LogisticRegression(tol=1e-8, penalty='l2', C=10., intercept_scaling=1e3)

# Ne considere que les mots qui apparaissent avec la frequence la plus faible
countvect_char = TfidfVectorizer(ngram_range=(1, 5), analyzer="char", binary=False)
countvect_word = TfidfVectorizer(ngram_range=(1, 3), analyzer="word", binary=False, min_df=3)

ft = FeatureUnion([("chars", countvect_char), ("words", countvect_word)])
clf = Pipeline([('vect', ft), ('select', select), ('logr', clf)])

X = []
y = []
with open('train.csv') as f:
    for line in f:
        y.append(int(line[0]))
        X.append(line[5:-6])

y = np.array(y)
scores = cross_val_score(clf, X, y, cv=2)

print scores

clf.fit(X, y)

X = []
with open('test.csv') as f:
    for line in f:
        X.append(line[3:-6])

y_test = np.loadtxt('answers.txt')
print np.mean(clf.predict(X) == y_test)

# -*- coding: utf-8 -*-
"""
Created on Wed Aug  1 14:52:43 2018

@author: user
"""

from sklearn.model_selection import train_test_split
from keras import preprocessing
import os

import pandas as pd
from sklearn.svm import SVC
from sklearn.metrics import confusion_matrix,classification_report

##################################################

import datetime


prefix = "1000"

data_path = "C:\\Users\\afy\\PycharmProjects\\AnalizeProject\\other\\data\\"
model_path = "C:\\Users\\afy\\PycharmProjects\\AnalizeProject\\other\\result\\"
main_folder_name = model_path + str(datetime.datetime.now()).replace(":", "_") + "\\"

def read_adjust_data():
    df = pd.read_csv(data_path + prefix + "_types.zip", delimiter=' ', header=None ,compression="zip")
    df[0] = df[0].astype('category')
    cat = df[0].cat
    df[0] = df[0].cat.codes
    y = df[0].values

    return y

def run_analize(X, y, kernel, file_name):

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # train classifier
    clf = SVC(probability=True, kernel= kernel)
    clf.fit(X_train, y_train)

    # predict and evaluate predictions
    predictions = clf.predict_proba(X_test)

    matrix = confusion_matrix(y_test, predictions.argmax(axis=1))
    report = classification_report(y_test, predictions.argmax(axis=1))

    cm_file = open(main_folder_name + file_name + "\\Confisuon_matrix_" + str(kernel), "w")
    cm_file.write(str(matrix))
    cm_file.write("\n\n")
    cm_file.write(report)
    cm_file.close()
    print(matrix)
    print(report)

# os.makedirs(main_folder_name + prefix)

df = pd.read_csv(data_path + prefix + "_calls.zip", delimiter=' ', header=None,compression="zip" )
D = df.values
ds_tmp = D[:, 0].tolist()
ds = []
for v in ds_tmp:
    ds.append(v.split(','))

maxlen = 342
X = preprocessing.sequence.pad_sequences(ds, maxlen=maxlen)
print(X.shape)


os.makedirs(main_folder_name)


print("-------------------basliyor------------")
file_name2 = "deneme"
os.makedirs(main_folder_name + "\\" + file_name2)

y = read_adjust_data()
run_analize(X, y, "rbf", file_name2)





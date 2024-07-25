# -*- coding: utf-8 -*-
"""Project-1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1IRaiaf14Pt-ZsvvA2H9PCLs5SPXAxX1s
"""

#import library yang akan digunakan untuk membersihkan data
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#import data yang akan dibersihkan
data = pd.read_csv('Employee.csv')
data.head()

#melihat informasi dari data
data.info()

#mencari nilai kosong pada dataset
missing_value = data.isnull().sum()
print(missing_value)

#karena tidak terdapat data kosong, maka lanjut ke proses selanjutnya mencari nilai duplikat
duplidata = data.duplicated().sum()
print('Jumlah data duplikat:', duplidata)

#terdapat 1889 data yang akan dibersihkan

#pembersihan data duplikat
data = data.drop_duplicates()
print(data)

#cek kembali jumlah data duplikat
duplidata = data.duplicated().sum()
print('Jumlah data duplikat:', duplidata)

#setelah data bersih dari duplikat lalu di cek nilai outlier/pencilannya
#kolom JoiningYear
plt.figure(figsize=(6, 4))
sns.boxplot(x=data['JoiningYear'])
plt.title('Plot Kolom JoiningYear')
plt.show()
#kolom PaymentTier
plt.figure(figsize=(6, 4))
sns.boxplot(x=data['PaymentTier'])
plt.title('Plot Kolom PaymentTier')
plt.show()
#kolom Age
plt.figure(figsize=(6, 4))
sns.boxplot(x=data['Age'])
plt.title('Plot Kolom Age')
plt.show()
#kolom ExperienceInCurrentDomain
plt.figure(figsize=(6, 4))
sns.boxplot(x=data['ExperienceInCurrentDomain'])
plt.title('Plot Kolom ExperienceInCurrentDomain')
plt.show()
#kolom LeaveOrNot
plt.figure(figsize=(6, 4))
sns.boxplot(x=data['LeaveOrNot'])
plt.title('Plot Kolom LeaveOrNot')
plt.show()

#berdasarkan plot yang digunakan untuk mencari nilai pencilan, dinyatakan bahwa tidak terdapat pencilan pada data
#karena tidak terdapat nilai kosong, tidak terdapat pencilan/outlier, dan sudah dilakukan pembersihan duplikasi pada data
#selanjutnya data siap untuk diekspor dan dianalisis
setelah_bersih = 'Clean_Employee.csv'
data.to_csv(setelah_bersih, index=False)
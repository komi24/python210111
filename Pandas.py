#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd

df = pd.read_csv("train.csv")


# In[2]:


df


# In[3]:


df["Age"]


# In[4]:


df["Age"] * 2


# In[5]:


df["Age x 2"] = df["Age"] * 2


# In[6]:


df


# In[7]:


df.to_csv("titanic.csv")


# In[8]:


df.describe()


# In[9]:


df.count()


# In[10]:


len(df)


# In[11]:


df["Age"].mean()


# In[19]:


df["Age"].min() * 12


# In[13]:


df["Age"].max()


# In[20]:


df["Embarked"].unique()


# In[21]:


df.columns


# In[22]:


df.loc[4:10]


# In[26]:


df["Age"] > 30


# In[28]:


df[(df["Age"] > 30) & (df["Sex"] == "male")]


# In[29]:


df[(df["Age"] > 30) & (df["Sex"] == "male")].loc[4:10]


# In[30]:


df[(df["Age"] > 30) & (df["Sex"] == "male")].iloc[4:10]


# In[38]:


# trouver le pourcentage d'hommes qui ont survécu par rapport aux nobmre total d'hommes
print(len(df[(df["Survived"] == 1) & (df["Sex"] == "male")]) / len(df[df["Sex"] == "male"]))

# trouver le pourcentage de femmes qui ont survécu par rapport aux nobmre total de femmes
print(len(df[(df["Survived"] == 1) & (df["Sex"] == "female")]) / len(df[df["Sex"] == "female"]))

# moyenne d'age des survivants
print(df[(df["Survived"] == 1)]["Age"].mean())
# moyenne d'age des disparus
print(df[(df["Survived"] == 0)]["Age"].mean())


# In[39]:


df["Age"].hist()


# In[41]:


df[(df["Survived"] == 0)]["Age"].hist(color="r", alpha=0.5)
df[(df["Survived"] == 1)]["Age"].hist(color="g", alpha=0.5)
      


# In[42]:


df.plot.scatter("Age", "Fare")


# In[45]:


df["Sex"] = df["Sex"].map({"female": 1, "male": 0})


# In[48]:


# Faire la même chose pour embarked
df["Embarked"] = df["Embarked"].map({"S": 0, "C": 1, "Q": 2})
# df["Embarked"].unique()


# In[52]:


df.drop(columns=["Cabin"], inplace=True)
# df = df.drop(columns=["Cabin"]) # même chose


# In[54]:


df.drop(columns=["Age x 2"], inplace=True)


# In[55]:


df.count()


# In[58]:


df.dropna(subset=["Age"], inplace=True)
df.count()


# In[59]:


df.dropna(subset=["Embarked"], inplace=True)
df.count()


# In[69]:


import re

# implémenter une regex dans convert_name pour capturer uniquement les titres dans les noms

def convert_name(name):
    return re.findall(", ([^\.]+)\.", name)[0]

df["Title"] = df["Name"].map(convert_name)
# convert_name("Braund, Mr. Owen Harris")


# In[70]:


df


# In[71]:


df["Title"].unique()


# In[72]:


import numpy as np

v = np.array([1,4,8])
v


# In[73]:


v + 2


# In[76]:


l = [1, 4, 8]
l + [2]


# In[81]:


from sklearn.svm import SVC
# import numpy as np

training_features = pd.DataFrame([
    {"age": 30, "taille": 180, "isChild": 0},
    {"age": 32, "taille": 170, "isChild": 0},
    {"age": 28, "taille": 190, "isChild": 0},
    {"age": 42, "taille": 178, "isChild": 0},
    {"age": 10, "taille": 120, "isChild": 1},
    {"age": 8, "taille": 110, "isChild": 1},
    {"age": 7, "taille": 130, "isChild": 1},
    {"age": 6, "taille": 120, "isChild": 1},
])

training_features
# training_enfants
# training_y = 

clf = SVC()

clf.fit(training_features[["age", "taille"]], training_features["isChild"])


# In[85]:


clf.predict([[29, 180], [2, 110]])


# In[119]:


import numpy as np

# test_Y = np.random.rand()

# help(np.random.rand)
# help(np.random.randint)
test_Y = np.random.randint([0,100],[80,200], size=(1000,2))
test_Y


# In[121]:


# clf.predict(test_Y)


# In[123]:


import matplotlib.pyplot as plt

plt.scatter(test_Y[:,0],test_Y[:,1], c=clf.predict(test_Y), cmap="Set1")


# In[113]:


# test_Y[4:10,0]
test_Y = np.random.randint(0,100, size=(10,10))
test_Y


# In[117]:


# récupérer la première colonne
test_Y[:,0]

# récupérer la première ligne
test_Y[0,:]

# récupérer les colonnes de 2 à 5
test_Y[0,2:5]

# récupérer les lignes de 4 à 6
test_Y[4:6,:]

# récupérer le carré délimité par les lignes de 4 à 8 et les colonne de 3 à 6
test_Y[4:8,3:6]


# In[ ]:


# Sélectioner les colonnes Pclass, Sex, Age, Embarked, Parch, SibSp, Fare pour l'apprentissage dans train_X

# Sélectionner la colonne survived pour l'apprentissage dans train_Y

# Lancer l'apprentissage d'un SVC sur train_X et train_Y

# Faite un scatter qui affiche la prédiction en fonction de Age et Fare (en colorant différemment les survivants et les disparus)


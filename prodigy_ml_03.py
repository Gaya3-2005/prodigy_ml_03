# -*- coding: utf-8 -*-
"""prodigy_ml_03.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Cw6Ky-4R_m5MUsjyaWDx1Mtegf6K5EK2
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('/content/drive/MyDrive/cats_vs_dogs.csv')

display(df.head(10))
print(df.info())
print('\nShape of the DataFrame (rows/columns):', df.shape)

df_sum = df[['n_dog_households', 'n_cat_households']].sum()

plt.figure(figsize=(12, 8))
plt.pie(df_sum, startangle=90)
plt.title('Number of Cats/Dogs Households', fontweight='bold')
plt.axis('equal')

total_sum = df_sum.sum()
plt.text(0, -1.2, f'Total: {total_sum}', fontsize=12, ha='center', fontweight='bold')

dog_label_x = -0.5
cat_label_x = 0.5
label_y = -0.1

plt.text(dog_label_x, label_y, f'Dogs: {df_sum["n_dog_households"]}', fontsize=20, fontweight='bold', ha='center', color='white', verticalalignment='center')
plt.text(cat_label_x, label_y, f'Cats: {df_sum["n_cat_households"]}', fontsize=20, fontweight='bold', ha='center', color='white', verticalalignment='center')

plt.show()

print('\nSUM of households with cats/dogs:', total_sum)
print('n_pet_households:', df['n_pet_households'].sum())

sns.histplot(df['percent_dog_owners'], bins = 20, kde = True)
plt.show()

sns.histplot(df['percent_cat_owners'], bins = 20, kde = True)
plt.show()

top_10_states_dogs = df.sort_values(by='percent_dog_owners', ascending=False).head(10)
last_10_states_dogs = df.sort_values(by='percent_dog_owners', ascending=False).tail(10)

dogs_combined = pd.concat([top_10_states_dogs, last_10_states_dogs])

# palette
custom_palette = ["#00FF00" if index < 10 else "#FF0000" for index in range(len(dogs_combined))]

# Create the bar plot
plt.figure(figsize=(12, 8))
sns.barplot(data=dogs_combined, x='percent_dog_owners', y='state', palette= custom_palette)
plt.xlabel('Percentage of Dog Owners', fontweight='bold' )
plt.ylabel('State', fontweight='bold')
plt.title('States with the Highest and Lowest Percentage of Dog Owners', fontweight='bold')


plt.grid(True, color = 'grey', linestyle = '--', alpha = 0.3)
plt.tight_layout()
plt.show()
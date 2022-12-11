# -*- coding: utf-8 -*-
"""
Created on Sat Nov 26 20:42:42 2022

@author: Yashomadhav Mudgal
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats

def getdata(file,ind):
    """
    

    Returns
    -------
    df : TYPE
        DESCRIPTION.
    df2 : TYPE
        DESCRIPTION.

    """
    df = pd.read_csv(file,skiprows=(4),index_col=(False)) # Reading csv file 
    df = df.loc[:, ~df.columns.str.contains('Unnamed')] # To remove unnamed column
    
    df = df.loc[df['Country Name'].isin(countries)] 
    df = df.loc[df['Indicator Code'].eq(ind)]
    df2 = df.melt(id_vars=['Country Name','Country Code','Indicator Name','Indicator Code'], var_name='Years')
    del df2['Country Code'] # Deleting column 
    df2 = df2.pivot_table('value',['Years','Indicator Name','Indicator Code'],'Country Name').reset_index() # Resetting index
    return df, df2

countries= ['Australia', 'United States', 'China', 'United Kingdom']


#Line Plot


df,df2 = getdata('API_19_DS2_en_csv_v2_4700503.csv','SP.POP.GROW') # Extracting data from files   
    
plt.figure(dpi=144) # Plotting the figure
df2 = df2[(df2['Years']>="1990") & (df2['Years']<="2020")] # Selecting years 
df2['Years'] = pd.to_numeric(df2['Years'])
df2.plot("Years", countries, title ='Population Growth (annual %)',legend ='leftbottom')
plt.ylabel('Growth percentage') # Showing growth percentage on y axis
plt.legend(loc = 'center left', bbox_to_anchor =(1, 0.5))
plt.show()




# Pie chart

 
df, df2 = getdata('API_19_DS2_en_csv_v2_4700503.csv','EN.ATM.CO2E.SF.ZS')# Extracting data from files
df2.dropna()  

aus = np.sum(df2['Australia'])
usa = np.sum(df2['United States'])
chi = np.sum(df2['China'])
uk = np.sum(df2["United Kingdom"])

total = aus + usa + chi + uk

australia = aus/ total*100
united_states = usa/ total*100
china = chi/ total*100
united_kingdom = uk/ total*100 # Taking each percentage before plotting 

methane_emission = np.array([australia, united_states, china, united_kingdom])


plt.figure(dpi=144)
plt.pie(methane_emission, labels = countries, shadow = True, autopct = ('%1.1f%%'))# We used autopct for showing percantages on piechart
plt.title("Co2 emissions from solid fuel consumption (% of total)") # This function is for showing title of data
plt.show()


skew = stats.skew(df2[countries]) # For determining skewness of  Co2 emission 
print("Skewness", skew)



# Bar chart



df, df2 = getdata('API_19_DS2_en_csv_v2_4700503.csv','SP.POP.TOTL')# Extracting data from files
df2 = df2.loc[df2['Years'].isin(['2000','2001','2002','2003','2004'])]
df2.dropna()


num = np.arange(5)
width = 0.2
years = df2['Years'].tolist() # Used (tolist) to convert array values to list

  
plt.figure()
plt.title('Total Population ')
plt.bar(num,df2['Australia'], width, label ='Australia')
plt.bar(num+0.2, df2['United States'], width, label ='United States')
plt.bar(num-0.2, df2['China'], width, label='China')

plt.xticks(num, years) # This is for showing years in x asis
plt.xlabel('Years')
plt.ylabel('Total population')
plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
plt.show()

mean = df2[countries].mean() # Determining mean of total population

print("Mean", mean)


# Pie chart

df, df2 = getdata('API_19_DS2_en_csv_v2_4700503.csv','EN.ATM.NOXE.KT.CE')# Extracting data from files
df2.dropna()

aus = np.sum(df2['Australia'])
usa = np.sum(df2['United States'])
chi = np.sum(df2['China'])
uk = np.sum(df2["United Kingdom"])

total = aus + usa + chi  + uk

australia = aus/ total*100
united_states = usa/ total*100
china = chi/ total*100
united_kingdom = uk/ total*100  # Taking each percentage before plotting

ele_production = np.array([australia, united_states, china, united_kingdom])
explode =(0.1,0.0,0.0,0.2) 

plt.figure(dpi = 144)
plt.pie(ele_production, labels = countries, shadow = True, explode = explode, autopct = ('%1.1f%%'))# We used autopct for showing percantages on piechart
plt.title("Nitrous Oxide emissions") # This function is for showing title of data
plt.show()



#skew = stats.skew(df2[countries]) # For determining skewness of nitrous oxide emission 
#print("Skewness", skew)



#line plot


df, df2 = getdata('API_19_DS2_en_csv_v2_4700503.csv','EG.FEC.RNEW.ZS')# Extracting data from files

plt.figure(dpi = 144) # For plotting the figure 
df2['Years'] = pd.to_numeric(df2['Years'])
df2.plot("Years", countries, title ='Renewable energy consumption',legend ='leftbottom')
plt.ylabel('Energy consumption') # Showing energy consumption on y axis
plt.xlim(1990, 2020)
plt.legend(loc = 'center left', bbox_to_anchor = (1, 0.5))
plt.show()


# Bar chart 

df, df2 = getdata('API_19_DS2_en_csv_v2_4700503.csv','AG.LND.FRST.K2')# Extracting data from files
df2 = df2.loc[df2['Years'].isin(['2010','2011','2012','2013','2014'])]
df2.dropna()


num= np.arange(5)
width = 0.2
years = df2['Years'].tolist() # Used (tolist) to convert array values to list

  
plt.figure()
plt.title('Forest Area (square Kilometer)')
plt.bar(num,df2['Australia'], width, label='Australia')
plt.bar(num+0.2, df2['United States'], width, label='United States')
plt.bar(num-0.2, df2['China'], width, label='China')
plt.xticks(num, years) # This is for showing years in x asis
plt.xlabel('Years')
plt.ylabel('Sq,Km')
plt.legend(loc = 'center left', bbox_to_anchor = (1, 0.5))
plt.show()

mean = df2[countries].mean()# Determining mean of forest area

print("Mean", mean)
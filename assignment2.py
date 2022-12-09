# -*- coding: utf-8 -*-
"""
Created on Sat Nov 26 20:42:42 2022

@author: Yashomadhav Mudgal
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


def getdata(file,ind):
    """
    

    Returns
    -------
    df : TYPE
        DESCRIPTION.
    df2 : TYPE
        DESCRIPTION.

    """
    df= pd.read_csv(file,skiprows=(4),index_col=(False))
    df= df.loc[:, ~df.columns.str.contains('Unnamed')]
    #df= df.dropna()
    df = df.loc[df['Country Name'].isin(countries)] 
    df= df.loc[df['Indicator Code'].eq(ind)]
    df2 = df.melt(id_vars=['Country Name','Country Code','Indicator Name','Indicator Code'], var_name='Years')
    del df2['Country Code']
    df2 = df2.pivot_table('value',['Years','Indicator Name','Indicator Code'],'Country Name').reset_index()
    #print(df.describe())
    #df2= df.transpose()
    #df2.info()
    #df2= df.T
    df.dropna()
    df2.dropna()
    return df, df2

countries= ['Australia', 'United States', 'China', 'India', 'United Kingdom']

df,df2= getdata('API_19_DS2_en_csv_v2_4700503.csv','SP.POP.GROW')
# df2 = df2.loc[df2['Indicator Code'].eq('SP.POP.GROW')]
#df2.to_csv('test_data6.csv')

#df3= pd.melt(df2, id_vars=988).drop('variable', axis=1).sort_values(0)
#df3.columns= list('Years')
#print(df3)
#Line Plot
    
plt.figure(dpi=144)
df2 = df2[(df2['Years']>="1990") & (df2['Years']<="2020")]
df2['Years'] = pd.to_numeric(df2['Years'])
df2.plot("Years", countries, title='Population Growth (annual %)',legend='leftbottom')
plt.xticks(rotation= 45.0)
#plt.xlim(1990, 2020)
plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
plt.show()



    
#pie chart

 
df, df2 = getdata('API_19_DS2_en_csv_v2_4700503.csv','EN.ATM.CO2E.SF.ZS')
df2.dropna()

aus= np.sum(df2['Australia'])
usa= np.sum(df2['United States'])
chi= np.sum(df2['China'])
ind= np.sum(df2['India'])
uk= np.sum(df2["United Kingdom"])

total= aus + usa + chi + ind + uk

australia= aus/ total*100
united_states= usa/ total*100
china= chi/ total*100
india= ind/ total*100
united_kingdom= uk/ total*100

methane_emission= np.array([australia, united_states, china, india, united_kingdom])


plt.figure(dpi=144)
plt.pie(methane_emission, labels= countries, shadow=True, autopct=('%1.1f%%'))# We used autopct for showing percantages on piechart
plt.title("Co2 emissions from solid fuel consumption (% of total)") # This function is for showing title of data
plt.show()






#bar chart
df, df2 = getdata('API_19_DS2_en_csv_v2_4700503.csv','EN.ATM.GHGT.ZG')
df2 = df2.loc[df2['Years'].isin(['2000','2001','2002','2003','2004'])]
df2.dropna()


num= np.arange(5)
width= 0.2
years = df2['Years'].tolist()

  
plt.figure()
plt.title('Total green house emission ')
plt.bar(num,df2['Australia'], width, label='Australia')
plt.bar(num+0.2, df2['United States'], width, label='United States')
plt.bar(num-0.2, df2['China'], width, label='China')
plt.bar(num+0.4, df2['India'], width, label='India')
plt.xticks(num, years) # This is for showing years in x asis
# plt.yticks(np.arange(0,110000,10000)) # This is for setting range and jump to get desired plot
plt.xlabel('Years')
plt.ylabel('Green house emission')
plt.legend()
plt.show()


#rolling (line plot) 

#df, df2 = getdata('API_19_DS2_en_csv_v2_4700503.csv','EG.ELC.RNWX.ZS')

#df2_rolling = df2.rolling(window=10).mean()
#df2_rolling.plot("Years", ["Australia", "United States", "China", "India"], title= 'Electricity production from renewable resources')
#plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
#plt.show()


#Pie chart

df, df2 = getdata('API_19_DS2_en_csv_v2_4700503.csv','EG.ELC.RNWX.ZS')
df2.dropna()

aus= np.sum(df2['Australia'])
usa= np.sum(df2['United States'])
chi= np.sum(df2['China'])
ind= np.sum(df2['India'])
uk= np.sum(df2["United Kingdom"])

total= aus + usa + chi + ind + uk

australia= aus/ total*100
united_states= usa/ total*100
china= chi/ total*100
india= ind/ total*100
united_kingdom= uk/ total*100

ele_production= np.array([australia, united_states, china, india, united_kingdom])


plt.figure(dpi=144)
plt.pie(ele_production, labels= countries, shadow=True, autopct=('%1.1f%%'))# We used autopct for showing percantages on piechart
plt.title("Electricity production from renewable resources") # This function is for showing title of data
plt.show()




#line plot 

df, df2 = getdata('API_19_DS2_en_csv_v2_4700503.csv','EG.FEC.RNEW.ZS')

plt.figure(dpi=144)
df2['Years'] = pd.to_numeric(df2['Years'])
df2.plot("Years", countries, title='Renewable energy consumption',legend='leftbottom')
plt.xticks(rotation= 45.0)
plt.xlim(1990, 2020)
plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
plt.show()


#bar chart 

df, df2 = getdata('API_19_DS2_en_csv_v2_4700503.csv','EG.USE.ELEC.KH.PC')
df2 = df2.loc[df2['Years'].isin(['2010','2011','2012','2013','2014'])]
df2.dropna()


num= np.arange(5)
width= 0.2
years = df2['Years'].tolist()

  
plt.figure()
plt.title('Electric Power Consumption ')
plt.bar(num,df2['Australia'], width, label='Australia')
plt.bar(num+0.2, df2['United States'], width, label='United States')
plt.bar(num-0.2, df2['China'], width, label='China')
plt.bar(num+0.4, df2['India'], width, label='India')
plt.xticks(num, years) # This is for showing years in x asis
# plt.yticks(np.arange(0,110000,10000)) # This is for setting range and jump to get desired plot
plt.xlabel('Years')
plt.ylabel('')
plt.legend()
plt.show()

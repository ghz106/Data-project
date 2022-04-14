from pandas_datareader import wb # import WB API
import pandas as pd
import matplotlib.pyplot as plt

#DATA PROEJCT

#--------------------------------------------------------------------------------------------------------
#RENEABLE ENERGY

#the code to clean up the dataframe for electricity production from renewable energy
def data_cleaning1(wb_rnwx):
    wb_rnwx = wb_rnwx.reset_index() #reset the index so EUU is first
    wb_rnwx.year = wb_rnwx.year.astype(int)
    wb_rnwx.country = wb_rnwx.country.astype('string')
    wb_rnwx = wb_rnwx.sort_values(['country','year']) #sorts by country and then year
    wb_rnwx.dropna() #drops all the values that says NaN
    return wb_rnwx

#Figure for renwable energy
import ipywidgets as widgets
def plot_wb1(wb_rnwx, country): 
    I = wb_rnwx['country'] == country
    ax = wb_rnwx.loc[I,:].plot(x='year', y='elec_prod_from_renewable_energy', style='-o', legend=False)
    ax.set_ylabel('% of total')
    ax.set_title('Figure 2.1:' ' ' 'Electricity production from renewable energy') 
    ax.set_xlim(1975, 2015)
    return 

#--------------------------------------------------------------------------------------------------------
#NUCLEAR ENERGY

#Data cleaning function for nuclear energy
def data_cleaning2(wb_nucl):
    wb_nucl = wb_nucl.reset_index() #reset the index so EUU is first
    wb_nucl.year = wb_nucl.year.astype(int)
    wb_nucl.country = wb_nucl.country.astype('string')
    wb_nucl = wb_nucl.sort_values(['country','year']) #sorts by country and then year
    wb_nucl.dropna() #drops all the values that says NaN
    return wb_nucl

#Figure for nuclear energy
def plot_wb2(wb_nucl, country): 
    I = wb_nucl['country'] == country
    ax=wb_nucl.loc[I,:].plot(x='year', y='elec_prod_from_nuclear_energy', style='-o', legend=False)
    ax.set_ylabel('% of total')
    ax.set_title('Figure 3.1:' ' ' 'Electricity production from nuclear energy') 
    ax.set_xlim(1975, 2015)
    
#--------------------------------------------------------------------------------------------------------
#FOSSIL FUELS

#Data cleaning function for fossil fuels
def data_cleaning3(wb_fosl):
    wb_fosl = wb_fosl.reset_index() #reset the index so EUU is first
    wb_fosl.year = wb_fosl.year.astype(int)
    wb_fosl.country = wb_fosl.country.astype('string')
    wb_fosl = wb_fosl.sort_values(['country','year']) #sorts by country and then year
    wb_fosl.dropna() #drops all the values that says NaN
    return wb_fosl

#Figure for fossil fuels
def plot_wb3(wb_fosl, country): 
    I = wb_fosl['country'] == country
    ax=wb_fosl.loc[I,:].plot(x='year', y='fosl', style='-o', legend=False)
    ax.set_ylabel('% of total')
    ax.set_xlim(1975,2015)
    ax.set_title('Figure 4.1: Energy production from fossil fuels 1975-2015')
    
#------------------------------------------------------------------------------------------------------    
#COMPARING THE SOURCES OF ELECTRICITY PRODUCTION

#Figure for comparision of fossil fuels and renewable energy
def plot_wb6(wb_fosl, country): 
    I = wb_fosl['country'] == country
    ax=wb_fosl.loc[I,:].plot(x='year', y='fosl', style='-o', legend=True)
    ax.plot(wb_eu.year, wb_eu.elec_prod_from_renewable_energy, color='green')
    ax.set_xlabel("year",fontsize=10)
    ax2=ax.twinx()
    ax2.plot(wb_fosl_eu.year, wb_fosl_eu.fosl, color='red')
    ax.set_ylabel('% share renewable sources')
    ax.set_xlabel('year')
    ax.set_xlim(1975,2015)
    ax.set_title('Figure 4.2: % Energy prod from renewable (green) vs fossil (red) sources')
    
    
#----------------------------------------------------------------------------------------------------------  
#MERGING THE DATASETS

#Figure showing the %-point difference for renewable- and nuclear energy
def plot_wb4(wb, country): 
    I = wb['country'] == country
    ax = wb.loc[I,:].plot(x='year', y='prod_diff', style='-o', legend=False)
    ax.set_ylabel('%-point difference of total production')
    ax.set_title('Figure 6.1:' ' ' '%-point difference in electricity production') 
    ax.set_xlim(1975, 2015)
    
#Figure showing the %-point difference between renewable energy and fossil fuels
def plot_wb5(wb2, country): 
    I = wb2['country'] == country
    ax = wb2.loc[I,:].plot(x='year', y='prod_diff2', style='-o', legend=False)
    ax.set_xlim(1975,2015)
    ax.set_title('Figure 6.2:' ' ' '%-point difference in electricity production') 
    ax.set_ylabel('%-point difference of total energy production')
    
#----------------------------------------------------------------------------------------------------------
#CLEANING THE DATASET OF RENEWABLE ENERGY IN KWH
    
#Function to clean the data for renewable energy in kwh
def data_cleaning4(wb_rnwx_kwh):
    wb_rnwx_kwh = wb_rnwx_kwh.reset_index() #reset the index so EUU is first
    wb_rnwx_kwh.year = wb_rnwx_kwh.year.astype(int)
    wb_rnwx_kwh.country = wb_rnwx_kwh.country.astype('string')
    wb_rnwx_kwh = wb_rnwx_kwh.sort_values(['country','year']) #sorts by country and then year
    wb_rnwx_kwh.dropna() #drops all the values that says NaN
    wb_rnwx_kwh['e_in_kwh_thousand'] = wb_rnwx_kwh['e_in_kwh']/1000000 #again because it's easier to read in the graph
    return wb_rnwx_kwh

#-----------------------------------------------------------------------------------------------------------
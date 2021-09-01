
#########MODULE#######
import yfinance as yf
import glob
import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st
import datetime



#######################################################################

st.header("#Backtest your hedging stategies (year 2020 data)")

st.sidebar.header('Enter date here for BANK NIFTY DATA')

########################################################
### NIFTY BANK CHART FOR 10 YEARS

tickerSymbol = '^NSEBANK'
#get data on this ticker
tickerData = yf.Ticker(tickerSymbol)
#get the historical prices for this ticker
tickerDf = tickerData.history(period='1d', start='2010-5-31', end=datetime.date.today())

st.write("""
## Closing Price **NIFTY BANK**
""")
st.line_chart(tickerDf.Close)
################################################################

###IMPORTING PATH

file0=['Expiry 02nd July','Expiry 04th June','Expiry 07th May','Expiry 09th July','Expiry 11th June','Expiry 16th July','Expiry 16th May','Expiry 18th June']
file1 = st.selectbox('Select date of expiry of BANKNIFTY WEEKLY CONTRACTS',file0)
st.write('You selected this :', file1)


n= 'https://github.com/emailatmukesh/Backtest-your-hedging-strategies/tree/main/may%20to%20july/'
l=file1.replace(' ','%20')
m="/1"
PATH= n+l+m
st.write(PATH)
#PATH=r'v'
#PATH =r'C:\Users\mukesh\Music\JAN to apr data\Expiry 16th January\CSV 30-12-19 to 16-01-20 (Expiry Day)'
filenames = glob.glob(PATH + "/*.csv")


st.write(filenames)
#################################
#######################################################################





st.sidebar.write('#PUT DATES BELOW TO KNOW MONEYNESS OF CONTRACT' )

d = st.sidebar.date_input("Enter a start date for your banknifty data",datetime.date(2020, 1, 1))


e = st.sidebar.date_input("Enter a end date for your banknifty data",datetime.date(2020, 1, 12))




tickerDf2 = tickerData.history(period='1d', start=d, end=e)
pd.DataFrame.reset_index(tickerDf2,inplace=True)
st.sidebar.write(tickerDf2[["Close","Date"]])
####################################################################################
#print(filenames)
collect=pd.DataFrame()

#p='700'
#p = list(m


j={}

collect=pd.DataFrame()

optionlist=[]

#p = list(map(str, input("Enter a multiple value with ce/pe: ").split()))
for filename in filenames:
          x=filename.split('BANKNIFTY')[-1]
          y=x.split('.')[0]
          y=str(y[-7:])
          optionlist.append(y)
          

#p = [x.upper() for x in p]
options = st.multiselect('Select the OPTION CONTRACT',optionlist,[optionlist[5],optionlist[-6],optionlist[8],optionlist[10]])
st.write('You selected:', options)



    
    
   
liso=[lambda x: x for x in options]




for g in range(len(liso)):
    et=options[g]
    for filename in filenames:
          x=filename.split('BANKNIFTY')[-1]
          y=x.split('.')[0]
          lll=str(y[-7:])
          
          if str(lll)==str(et):
                  df = pd.read_csv(filename)
                  qq=str(y[-7:])
                  col=['banknify data','date','time','open','high','low',qq,'lot1']
                  df.columns=col
                
                  df['time-date']=pd.to_datetime(df['date'] + ' ' + df['time'])
                  df3=df.drop(['banknify data','date','time','open','high','low','lot1'],axis=1)
                  df4=df3.set_index('time-date')
                  #st
                  
                  ud = df.date.unique()
                  #st.write(f'**{et}** contract of BANKNIFTY')
                  df22= df.drop(['time','high','lot1'],axis=1)
                  dfo=df22.groupby("date").mean()
                  dfol=dfo[qq]
                  
                  
                  
                  
                 
                 
                  collect=pd.concat([collect,dfol],axis=1)
                  #st.line_chart(dfol)
                  
st.subheader('Data for your option strategy backtesting')                  
collect    
st.write("""
## Plot of your selected option contracts
""")
st.line_chart(collect)     

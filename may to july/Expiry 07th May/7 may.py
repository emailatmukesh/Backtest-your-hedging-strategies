# -*- coding: utf-8 -*-
"""
Created on Sat Dec 26 10:08:42 2020

@author: mukesh
"""

# -*- coding: utf-8 -*-
"""
Created on Sat Dec 26 09:52:02 2020

@author: mukesh
"""

# -*- coding: utf-8 -*-
"""
Created on Sat Dec 26 09:44:23 2020

@author: mukesh
"""

# -*- coding: utf-8 -*-
"""
Created on Sat Dec 26 09:38:12 2020

@author: mukesh
"""







import glob
import pandas as pd
import matplotlib.pyplot as plt

PATH =r'C:\Users\mukesh\Music\may to july\Expiry 07th May\CSV 20-04-20 to 07-05-20 (Expiry day)'
filenames = glob.glob(PATH + "/*.csv")



#print(filenames)
collect=pd.DataFrame()

#p='700'
#p = list(m


e=['200','500','700','000']
j={}

collect=pd.DataFrame()


#p = list(map(str, input("Enter a multiple value with ce/pe: ").split()))

#p = [x.upper() for x in p]


for et in range(len(e)):
    p=e[et]
   # p='22000PE'
    for filename in filenames:
          x=filename.split('BANKNIFTYWK')[-1]
          y=x.split('.')[0]
          z=y[2: -2]
          if str(z)==str(p):
                  df = pd.read_csv(filename)
                  
                  col=[y,'date','time','open','high','low','close','lot1']
                  df.columns=col
                  df
                  df['time-date']=pd.to_datetime(df['date'] + ' ' + df['time'])
                  df3=df.drop([y,'date','time','open','high','low','lot1'],axis=1)
                  
                  ud = df.date.unique()
                  try:
                      list2=[ud[-4], ud[-3],ud[-2],ud[-1]]
                      for i in range(len(list2)):
                            grouped = df.groupby(df.date)
        
                            Tanya = grouped.get_group(list2[i])
                            
                            #print(Tanya)
                            k=list2[i]
                            j[i]=grouped.get_group(list2[i])
                            h = k.replace("/", "-")
                            l1=h+y+".png"
                            l2=(list2[i]+' '+y)
                            #plt.plot(Tanya['time-date'],Tanya['close'],label=l2)
                      
                  
                      figure, axes = plt.subplots(nrows=2, ncols=2,facecolor='grey')
                      figure.suptitle(y)
                            
                      axes[0, 0].plot(j[0]['time-date'], j[0]['close'],label=list2[0],color='yellow')
                            
                      axes[0, 0].legend()
                      axes[0, 0].grid()
                      axes[0, 0].set_facecolor('grey')
                      
                      axes[0, 1].plot(j[1]['time-date'], j[1]['close'],label=list2[1],color='yellow')
                      axes[0, 1].legend()
                      axes[0, 1].grid()
                      axes[0, 1].set_facecolor('grey')
                      
                      axes[1, 0].plot(j[2]['time-date'], j[2]['close'], label=list2[2],color='yellow')
                      axes[1, 0].legend()
                      axes[1, 0].grid()
                      axes[1, 0].set_facecolor('grey')
                      
                      axes[1, 1].plot(j[3]['time-date'], j[3]['close'], label=list2[3],color='yellow')
                      axes[1, 1].legend()
                      axes[1, 1].grid()
                      axes[1, 1].set_facecolor('grey')
                            
                            
                      figure.tight_layout()                   
                      
                                                   
                      plt.rcParams["figure.figsize"] = (24,11)
                                            #ax = plt.gca()
                                            #ax.set_facecolor('black')
                            #plt.grid()
                      plt.savefig(y+' date.png',dpi=300,bbox_inches='tight')
                      
                  except:
                      pass
                      
                      
                      
                  
                      
                        # -*- coding: utf-8 -*-

# -*- coding: utf-8 -*-

# -*- coding: utf-8 -*-


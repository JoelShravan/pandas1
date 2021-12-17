import pandas as pd

class A:
   def rea(self,file):
      file=pd.read_csv(file)
      return (file)
   
   def sum_jan(self,file):
      file=pd.read_csv(file)
      sj=file['jan_2021'].sum()
      print("jan_sum:")
      return(sj)
    
   def sum_feb(self,file):
      file=pd.read_csv(file)
      sj=file['feb_2021'].sum()
      print("feb_sum:")
      return(sj)   
      
   def sum_mar(self,file):
      file=pd.read_csv(file)
      sj=file['mar_2021'].sum()
      print("mar_sum:")
      return(sj)
   
   def sum_rows(self,file):  
    file=pd.read_csv(file)
    for i in range(0,len(file)):
          s=file['jan_2021'][i]+file['feb_2021'][i]+file['mar_2021'][i]
          print(file['name'][i]+":")
          print(s)
         

file='data.csv'
a=A()
#print(a.rea(file))

jan_sal=a.sum_jan(file)
print(jan_sal)

feb_sal=a.sum_feb(file)
print(feb_sal)

mar_sal=a.sum_mar(file)
print(mar_sal)

a.sum_rows(file)

print("percentage diff b/w jan and feb:")
pcdjf=((feb_sal-jan_sal)/jan_sal)*100
print(pcdjf)

print("percentage diff b/w feb and mar:")
pcdfm=((feb_sal-mar_sal)/feb_sal)*100
print(pcdfm)
#(1) Creating a DataFrame from scratch -----------------------------

import pandas as pd

data = [[1,2,3],
        [4,5,6]]

df_1 = pd.DataFrame(data,columns=["A","B","C"])
df_1


#(2) Creating a dataframe from a dictionary -----------------------------
import pandas as pd

data = {"A":[1,2], "B":[3,4] }
df_2 = pd.DataFrame(data)
df_2

#(3) Merging Dataframes -----------------------------
import pandas as pd

df_a = pd.DataFrame([[1,"A"],
                    [2,"B"]],
                    columns= ["column_1","column_2"])

df_b = pd.DataFrame([["A",3],
                    ["B",4]],
                    columns= ["column_2","column_3"])                        
#Lets merge the 2 dataframes
Data_AB = pd.merge(df_a,df_b, on = "column_2", how="inner")


#(4) Lets sort the dataframe -----------------------------
df = pd.DataFrame([[4,"A"],
                    [2,"B"],
                    [1,"C"],
                    [3,"D"]],
                    columns=["column_1","column_2"])        
df.sort_values(by="column_1")                          


#(5) concatenating Dataframes -----------------------------
df_x = pd.DataFrame([[1,"Sady"],
                      [2, "Eliana"],
                      [3,"Natalia"],
                      [4,"Carlos"],
                      [5, "Francisco"],
                      [6, "Rex"]],
                      
                      columns=["Id","Member_Name"])

df_y = pd.DataFrame([[1,"Mario"],
                      [2, "Marta"],
                      [3,"Larry"],
                      [4,"Empi"],
                      [5, "Palta"],
                      [6, "Marcus"]],
                      
                      columns=["Id","Member_Name"])                  
                      
df_x_y =  pd.concat((df_x, df_y), axis= 1)                     
                      


#(6) rename a column
df_x.rename(columns= {"Member_Name":"Name_of_member"})         
df_x          

#(7) add new column 
df_x["Region"] = df_x["Id"] +20
df_x


#(8) Drop column by position in dataframe de atras para adelante
N=3
new_df_x_y = df_x_y.iloc[:,:-2]


#(9) Group by data
df_z = pd.DataFrame([[1,"Stgo"],
                      [2, "TX"],
                      [3,"Stgo"],
                      [4,"CA"],
                      [5, "CA"],
                      [6, "TX"]],
                      
                      columns=["Id","City"]) 

df_z
        #Lets merge
df_z_2 =  pd.merge(new_df_x_y, df_z, on ="Id", how="inner")


#(10) Group by City count how many ppl are in the same city
df_z_3 = df_z_2.groupby("City").count()
df_z_3


df_z_3 = df_z_2.groupby(by=["City"]).size().reset_index(name="counts")
df_z_3


#(10) Unique Values in each column
df_z_2.nunique()

#(11) fill NAN values
import pandas as pd
import numpy as np

df_C = pd.DataFrame([[1,"Sady"],
                      [2, np.nan],
                      [3,"Natalia"],
                      [4,np.nan],
                      [5, "Francisco"],
                      [6, "Rex"]],
                      
                      columns=["Id","Member_Name"])

df_C.Member_Name.fillna("get_name", inplace =True)
df_C


# (12) Apply a function on a column:
import pandas as pd

def f(number):
        return number + 2000
df = pd.DataFrame([[1,"Audi"],
                   [2,"BMW"]],
                    columns=["Id","Brand"]
                                )
df["year"] = df.Id.apply(f)
df

#(13) Drop duplicates "the columns needs to be exactly the same"
import pandas as pd

df = pd.DataFrame([[1,"Audi"],
                   [2,"BMW"],
                   [2,"BMW"],
                   [4,"Audi"],
                   [4,"Toyota"]],
                    columns=["Id","Brand"]
                                )
df = df.drop_duplicates()                               
df
df.shape
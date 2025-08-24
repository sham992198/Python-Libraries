import pandas as pd
# creation of data frames
a = {
    "Name":["sham","ram"],
    "age":[20,34],
    "salary":[200000 ,34000]
    }
df=pd.DataFrame(a)
print(df)

# #exploring data
data = pd.read_excel("mymoviedb.xlsx")
print(data)
print(pd.head(10))
print(pd.tail(10))
print(data.info())
print(data.describe())
print(data.isnull().sum())

#dealing with duplicate values
data = pd.read_csv("offices.csv")
print(data)
print(data["Eid"].duplicated())  # find row wise duplicate value
print(data.drop_duplicates("Eid"))

#Exploring with missing data
data = pd.read_csv("offices.csv")
print(data)
print(data.isnull().sum())
print(data.dropna())

#column transformation
data = pd.read_excel("mymoviedb.xlsx")
data.loc[(data["bonus %"]==0),"getbonus"]="no bonus"
data.loc[(data["bonus %"]==0),"getbonus"]="bonus"
print(data.head(10))



data = pd.read_excel("mymoviedb.xlsx")
data["full name"]=data["first name"] + " " + data["last name"]
print(data)


data = {
    "Name":["sham","ram"],
    "sirname":["kolekar","nalge"],
    "age":[20,34],
    "salary":[200000 ,34000]
    }
a=pd.DataFrame(data)
print(a)
a["full name"]=a["Name"].str.capitalize()+" "+a["sirname"].str.capitalize()
print(a)

#Group by
gp=data.groupby("Name").agg({"salary"})
print(gp)

merge join and concatenate
data = {
    "EID":["E1","E2","E3","E4"],
    "Name":["sham","ram","rahul","panda"],
    "age":[20,34,23,35],
    }
data1 = {
    "EID":["E1","E2","E3","E4"],
    "salary":[25000,30000,45000,50000]
}
a=pd.DataFrame(data)
b=pd.DataFrame(data1)
print(a)
print(b)
print(pd.merge(a,b,on = "EID"))
print(pd.merge(a,b,on = "EID",how="right"))

data = {
    "EID":["E1","E2","E3","E4"],
    "Name":["sham","ram","rahul","panda"],
    "age":[20,34,23,35],
    }
data1 = {
    "EID":["E5","E6","E7","E8"],
    "Name":["yam","champ","mail","jhon"],
    "salary":[25000,30000,45000,50000]
}
a=pd.DataFrame(data)
b=pd.DataFrame(data1)
print(a)
print(b)
print(pd.concat([a,b]))

compare dataframe
d={
    "Fruit":["mango","banana","papaya"],
    "price":[100,50,30],
    "quantaty":[10,15,5]
 }
a=pd.DataFrame(d)
print(a)
b=a.copy()
print(b)
b.loc[0,"price"]=150
b.loc[1,"price"]=100
b.loc[2,"price"]=50
b.loc[0,"quantaty"]=15
b.loc[1,"quantaty"]=22
b.loc[2,"quantaty"]=10
print(a.compare(b))

#pivoting and melting dataframes
dict={
    "keys":["k1","k2","k3","k4"],
    "names":["rahul","sham","champ","dada"],
    "houses":["red","green","blue","yellow"],
    "grades":["1th","2nth","3rd","4th"]
}
a=pd.DataFrame(dict)
print(a)
print(a.pivot(index="keys",columns="names",values=["houses","grades"]))

dict={
    "keys":["k1","k2","k3","k4"],
    "names":["rahul","sham","champ","dada"],
    "houses":["red","green","blue","yellow"],
    "grades":["1th","2nth","3rd","4th"]
}
a=pd.DataFrame(dict)
print(a)
print(pd.melt(a,id_vars=["names"],value_vars=["houses","grades"],var_name="house&grades"))
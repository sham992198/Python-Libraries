import matplotlib.pyplot as plt
#Barplot
y=[10,20,30,60,90]
x=["mark1","mark2","mark3","mark4","mark5"]
colors=["red","blue","pink","green","black"]
plt.bar(x,y,color=colors,edgecolor="black")
plt.ylabel("mark of student",fontsize=15)
plt.xlabel("names of students",fontsize=15)
plt.title("Marks informations",fontsize=20)
plt.show()

#Lineplot
x=["day1","day2","day3","day4"]
y=[20,44,35,10]
y1=[40,50,30,32]
plt.plot(x,y ,marker="o",ls="--",color="red",label="wek1")
plt.plot(x,y1 ,marker="o",ls=":",color="green",label="wek2",alpha=0.5)
plt.legend()
plt.show()
import pandas as pd
data=pd.read_excel("C:/Fullpython/Expense.xlsx")
d=pd.DataFrame(data)
print(d)

#scatter plot
import numpy as np
x= np.random.randint(1,10,50)
y= np.random.randint(10,100,50)
plt.scatter(x,y,marker="*",color="red")
plt.show()

#piechart
brands=["samsung","apple","nokia","redmi"]
x=[30,50,20,3]
c=["red","pink","green","yellow"]
ex=[0,0,0,0.1]
plt.pie(x,labels=brands,colors=c,explode=ex,shadow=True,autopct= "%.2f")
plt.show()

#boxplot
l=[1,2,3,4,5,6,8,9,7,55,33,45,67,44,66]
plt.boxplot(l)
plt.show()

#histogram
x=[1,2,3,4,5,6,44,55,66]
plt.hist(x,bins=15,color="blue",edgecolor="black")
plt.show()

#violin plot
x=[11,22,33,44,33,44,3,22,88]
plt.violinplot(x,showmedians=True)
plt.show()

#stem plot
x=[11,22,33,44,33,44,3,22,88]
plt.stem(x,linefmt="--",markerfmt="*",bottom=1)
plt.show()

#stackplot
x=[1,2,3,4,5]
p=[10,20,30,40,50]
p1=[12,33,55,44,3]
p2=[30,44,50,66,77]
plt.stackplot(x,p,p1,p2,labels=["week1","week2","week3"])
plt.legend()
plt.show()

#stepplot
x=["d1","d2","d3","d4","d5"]
p=[10,20,30,40,50]
plt.step(x,p,where="mid")
plt.show()

#legend
x=[1,2,3,4,5]
y=[11,22,33,44,55]
y1=[99,88,77,66,78]
plt.figure(figsize=[5,3])
plt.plot(x,y,label="male")
plt.plot(x,y1,label="female")
plt.legend()
plt.show()

# subplot
x=[1,2,3,4,5]
y=[11,22,33,44,55]
plt.subplot(1,2,1)
plt.plot()

x=[5,6,7,8,9]
y=[10,20,30,55,66]
plt.subplot(1,2,2)
plt.savefig("subplot.png")
plt.show()
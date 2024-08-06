
#pie chart
import matplotlib.pyplot as p
us=[12,32,16,45]
la=[12,32,16,45]
e=[0,0,0,0.04]
c=["blue","cyan","red","yellow"]
p.pie(us,labels=la,startangle=270,explode=e,colors=c,autopct="%1.2g%%")
p.show()
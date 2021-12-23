import numpy as np
import matplotlib.pyplot as plt
import mlpy
np.random.seed(0)
mean1,con1,n1=[1,5],[[1,1],[1,2]],200
x1=np.random.multivariate_normal(mean1,con1,n1)


print(x1.shape)
mean2,con2,n2=[2.2,2.5],[[1,0],[0,1]],300
x2=np.random.multivariate_normal(mean2,con2,n2)

mean3,con3,n3=[5,5],[[0.5,0],[0,0.5]],200
x3=np.random.multivariate_normal(mean3,con3,n3)

x=np.concatenate((x1,x2,x3),axis=0)

# plot2=plt.scatter(x[:,0],x[:,1])

cls,means,steps=mlpy.kmeans(x,k=3,plus=True)


print(cls,means,steps)
fig=plt.figure(1)
plot1=plt.scatter(x[:,0],x[:,1],c=cls,alpha=0.75)
plot2=plt.scatter(means[:,0],means[:,1],c=np.unique(cls),s=128,marker='d')
plt.show()
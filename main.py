import numpy as np
import matplotlib.pyplot as plt

data1 = np.genfromtxt("D:\Python3_Projects\Lab_1_Tpr\\lab1_A0_A60.csv", delimiter=";", names=["a","Q1","Q2"])


Q1 = np.array(data1["Q1"][1:]).T
Q2 = np.array(data1["Q2"][1:]).T
A = np.empty(shape=60,dtype="U3",)
for i in range(len(A)):
    A[i] = "A"+str(i+1)

print(Q1,Q2,A)


def Pareto(arr1,arr2,Aarr):
    res = np.empty(shape=60, dtype="U3")

    for i in range(len(arr1)):
        for j in range(len(arr1)):
            if arr1[i] == arr1[j] and arr2[i] == arr2[j]:
                continue

            if arr1[i] >= arr1[j]:
                if arr2[i] >= arr2[j]:
                    if res[j] == "":
                        res[j] = Aarr[i]
                else:
                    continue
            continue
    return res

def Slayter(arr1,arr2,Aarr):
    res = np.empty(shape=60, dtype="U3")

    for i in range(len(arr1)):
        for j in range(len(arr1)):
            if arr1[i] > arr1[j]:
                if arr2[i] > arr2[j]:
                    if res[j] == "":
                        res[j] = Aarr[i]
                else:
                    continue
            continue
    return res


par = Pareto(Q1,Q2,A)
print(par)
slay = Slayter(Q1,Q2,A)
print(slay)


plt.xlabel("Q1")
plt.ylabel("Q2")
plt.scatter(data1["Q1"],data1["Q2"], color ="darkcyan")

check = []
mov = 0.2
for i in range(len(Q1)):
    if str(Q1[i])+str(Q2[i]) in check:
        plt.annotate("="+A[i], (Q1[i], Q2[i]), (Q1[i]+0.27, Q2[i] + mov),fontsize=7)
        mov = mov+0.02
        continue
    plt.annotate(A[i], (Q1[i], Q2[i]),(Q1[i], Q2[i]+0.2),fontsize=7)
    check.append(str(Q1[i])+str(Q2[i]))

x_point = []
y_point = []
for i in range(len(Q1)):
    if slay[i] == "":
        x_point.append(Q1[i])
        y_point.append(Q2[i])


plt.plot(x_point,y_point)

plt.show()




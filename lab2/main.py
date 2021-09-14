Arr1 = [5,4,33,99,34,19,15,35,87,53,69,50,87,2,37,62,89,10,5,60]
Arr2 = [4,11,57,29,3,16,92,21,22,5,43,79,61,28,78,47,51,45,82,87]
Arr3 = [99,51,89,86,53,26,48,94,36,6,7,92,17,64,21,20,80,66,94,54]
Arr4 = [5,4,33,99,34,19,15,35,87,53,69,50,87,2,37,62,89,10,5,60,4,11,57,29,3,16,92,21,22,5,43,79,61,28,78,47,51,45,82,87,99,51,89,86,53,26,48,94,36,6,7,92,17,64,21,20,80,66,94,54]


def is_higher_sum(arr, num,mode = False):
    sum = 0
    for i in arr:
        sum += i
    if mode == False:
        if sum + num > 100:
            return True
    else:
        return sum


def min_containers_num(arr, C):
    sum = 0
    for i in arr:
        sum += i
    return sum/C


def NFA(arr):
    res = [[]]
    j = 0
    cnt = 0
    for i in range(len(arr)):
        if i == 0:
            res[j].append(arr[i])
            continue
        cnt += 1
        if is_higher_sum(res[j], arr[i]) != True:
            res[j].append(arr[i])
        else:
            res.append([])
            j += 1
            res[j].append(arr[i])
    print(res,"Complexity = ",cnt," Num of containers = ",len(res))


def FFA(arr):
    res = [[]]
    j = 0
    cnt = 0
    l = len(arr)
    for i in range(l):
        check = False
        if i == 0:
            res[j].append(arr[i])
            continue
        cnt += 1
        if is_higher_sum(res[j], arr[i]) != True:
            res[j].append(arr[i])
        else:
            for b in res:
                cnt += 1
                if is_higher_sum(b,arr[i]) != True:
                    b.append(arr[i])
                    check = True
                    break
            if check == False:
                res.append([])
                j += 1
                res[j].append(arr[i])

    print(res,"Complexity = ",cnt," Num of containers = ",len(res))


def WFA(arr):
    res = [[]]
    j = 0
    cnt = 0
    l = len(arr)
    for i in range(l):
        check = False
        if i == 0:
            res[j].append(arr[i])
            continue
        cnt += 1
        if is_higher_sum(res[j], arr[i]) != True:
            res[j].append(arr[i])
        else:
            min = is_higher_sum(res[0],arr[i],True)
            Tmp_arr = res[0]
            for b in res:
                num = is_higher_sum(b,arr[i],True)
                if num < min:
                    min = num
                    Tmp_arr = b
                cnt += 1
            if is_higher_sum(Tmp_arr, arr[i]) != True:
                res[res.index(Tmp_arr)].append(arr[i])
            else:
                res.append([])
                j += 1
                res[j].append(arr[i])
    print(res, "Complexity = ", cnt," Num of containers = ",len(res))

def BFA(arr):
    res = [[]]
    j = 0
    cnt = 0
    l = len(arr)
    for i in range(l):
        check = False
        if i == 0:
            res[j].append(arr[i])
            continue
        cnt += 1
        if is_higher_sum(res[j], arr[i]) != True:
            res[j].append(arr[i])
        else:
            d = {}
            for b in res:
                h = is_higher_sum(b,arr[i],True)
                d[h] = b
            for v in sorted(d,reverse=True):
                cnt += 1
                if is_higher_sum(d.get(v),arr[i]) != True:
                    res[res.index(d.get(v))].append(arr[i])
                    check = True
                    break
            if check ==  False:
                res.append([])
                j += 1
                res[j].append(arr[i])
    print(res, "Complexity = ", cnt," Num of containers = ",len(res))


print("Array1 NFA original")
NFA(Arr1)
print("NFA LH sorted")
NFA(sorted(Arr1))
print("NFA HL sorted")
NFA(sorted(Arr1,reverse=True))
print("\n")


print("FFA original")
FFA(Arr1)
print("FFA LH sorted")
FFA(sorted(Arr1))
print("FFA HL sorted")
FFA(sorted(Arr1,reverse=True))
print("\n")

print("WFA original")
WFA(Arr1)
print("WFA LH sorted")
WFA(sorted(Arr1))
print("WFA HL sorted")
WFA(sorted(Arr1,reverse=True))
print("\n")

print("BFA original")
BFA(Arr1)
print("BFA LH sorted")
BFA(sorted(Arr1))
print("BFA HL sorted")
BFA(sorted(Arr1,reverse=True))
print("------------------------------------------------------")
print("Array2 NFA original")
NFA(Arr2)
print("NFA LH sorted")
NFA(sorted(Arr2))
print("NFA HL sorted")
NFA(sorted(Arr2,reverse=True))
print("\n")


print("FFA original")
FFA(Arr2)
print("FFA LH sorted")
FFA(sorted(Arr2))
print("FFA HL sorted")
FFA(sorted(Arr2,reverse=True))
print("\n")

print("WFA original")
WFA(Arr2)
print("WFA LH sorted")
WFA(sorted(Arr2))
print("WFA HL sorted")
WFA(sorted(Arr2,reverse=True))
print("\n")

print("BFA original")
BFA(Arr2)
print("BFA LH sorted")
BFA(sorted(Arr2))
print("BFA HL sorted")
BFA(sorted(Arr2,reverse=True))
print("------------------------------------------------------")
print("Array3 NFA original")
NFA(Arr3)
print("NFA LH sorted")
NFA(sorted(Arr3))
print("NFA HL sorted")
NFA(sorted(Arr3,reverse=True))
print("\n")


print("FFA original")
FFA(Arr3)
print("FFA LH sorted")
FFA(sorted(Arr3))
print("FFA HL sorted")
FFA(sorted(Arr3,reverse=True))
print("\n")

print("WFA original")
WFA(Arr3)
print("WFA LH sorted")
WFA(sorted(Arr3))
print("WFA HL sorted")
WFA(sorted(Arr3,reverse=True))
print("\n")

print("BFA original")
BFA(Arr3)
print("BFA LH sorted")
BFA(sorted(Arr3))
print("BFA HL sorted")
BFA(sorted(Arr3,reverse=True))
print("------------------------------------------------------")
print("Array4 NFA original")
NFA(Arr4)
print("NFA LH sorted")
NFA(sorted(Arr4))
print("NFA HL sorted")
NFA(sorted(Arr4,reverse=True))
print("\n")


print("FFA original")
FFA(Arr4)
print("FFA LH sorted")
FFA(sorted(Arr4))
print("FFA HL sorted")
FFA(sorted(Arr4,reverse=True))
print("\n")

print("WFA original")
WFA(Arr4)
print("WFA LH sorted")
WFA(sorted(Arr4))
print("WFA HL sorted")
WFA(sorted(Arr4,reverse=True))
print("\n")

print("BFA original")
BFA(Arr4)
print("BFA LH sorted")
BFA(sorted(Arr4))
print("BFA HL sorted")
BFA(sorted(Arr4,reverse=True))
print("------------------------------------------------------")




print("\nMin num of containers for first line = ",min_containers_num(Arr1,100))
print("\nMin num of containers for second line = ",min_containers_num(Arr2,100))
print("\nMin num of containers for third line = ",min_containers_num(Arr3,100))
print("\nMin num of containers for forth line = ",min_containers_num(Arr4,100))
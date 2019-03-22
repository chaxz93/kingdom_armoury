import math

def arrangeEquipments(equipments):
    num = equipments[0]
    equipments.pop(0)
    arr = equipments
    print(arr)
    k = math.ceil(num/2)
    arr.sort()
    armory = []
    head = arr[k-1]
    armory.append(head)
    arr.remove(head)
    n = len(arr)
    for i in range(n - 1):
        if (i % 2 == 0 and arr[i] > arr[i + 1]):

            temp = arr[i]
            arr[i]= arr[i + 1]
            arr[i + 1]= temp

        if (i % 2 != 0 and arr[i] < arr[i + 1]):

            temp = arr[i]
            arr[i]= arr[i + 1]
            arr[i + 1]= temp

    for i in range(0, len(arr) - 1, 2):
        arr[i], arr[i + 1] = arr[i + 1], arr[i]
    armory.extend(arr)
    return (armory)

if __name__== "__main__":
    arr = [4, 1, 2, 3, 4]
    kingdom = arrangeEquipments(arr)
    print (kingdom)

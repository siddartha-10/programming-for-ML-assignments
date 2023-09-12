def q1():
    name = input("Please enter your name: ")
    age = int(input("Please enter your age: "))
    print(f"My name is {name} and I am {age}")
    return (name,age)

# print(q1())


def q2():
    name, age = q1()
    fruits = input("please input your favorite fruit: ").split(" ")
    info = {"name": name, "age": age, "fruits": fruits}
    #print(len(info))
    for key, value in info.items():
        print(key + ":", value)
#q2()


def q3():
    import numpy as np
    np.random.seed(1)
    a = np.random.randint(0, 10, size=5)  # Create 5 random integers
    b = np.random.randint(0, 10, size=5)  # Create 5 random intergers
    a = a.tolist() # converting numpy array to list
    b = b.tolist() # converting numpy array to list
    list1 = a + b
    #print(list1)
    union = []
    intersection = []
    for i in list1:
        if i not in union:
            union.append(i)
    for i in a:
        if i in b:
            intersection.append(i)
    print("a intersect b = ", intersection)
    print("a union b = ",union)

#q3()


def q4(n):
    if n == 0:
        print("1")
        return [1]

    prev_row = q4(n - 1)
    row = [1]

    for i in range(1, n):
        row.append(prev_row[i - 1] + prev_row[i])

    row.append(1)

    for num in row:
        print(num, end=" ")
    print()

    return row

n = int(input("Please enter a number: "))
print(q4(n))





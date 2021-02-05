def reverse():
	num=int(input("Enter the number to be reversed: "))
	outNum=0
	while num != 0:
		outNum=  outNum*10 + num%10
		num=num/10
		num =int(num)
	print("The reversed number is ")
	print(outNum)

def average():
	n=int(input("Enter the number of elements for average: "))
	print("Enter the elements: ")
	sum=0
	for i in range(n):
		add=int(input())
		sum=sum+add
	print(sum/n)


def array():
    toStop = False
    arr = []
    while not toStop: 
        print("\t\tOptions")
        print("1. Insert at position")
        print("2. Append")
        print("3. Remove element at given position")
        ch = int(input("Enter an option: "))

        if ch == 1:
            ele = int(input("Enter the element to insert: "))
            pos = int(input("Enter the position to enter: "))

            if pos > len(arr) or pos < 0:
                print("Invalid position")
                continue

            arr.insert(pos, ele)

        elif ch == 2:
            ele = int(input("Enter the element to append: "))
            arr.append(ele)

        elif ch == 3:
            pos = int(input("Enter the position of element to be removed: "))
            
            if pos < 0 or pos >= len(arr):
                print("Invalid position")
                continue

            if pos == 0:
                arr = arr[1: ]
            elif pos == len(arr) - 1:
                arr = arr[:pos]
            else:
                arr = arr[ : pos] + arr[pos+1 : ]

        print("Array is :  ")
        print(arr)
        
        toStop = not bool(int(input("Continue? (Enter 1 to continue, 0 to stop)")))


def main():
    print("Choose")
    print("1. Average of N numbers")
    print("2. Reverse of a number") 
    print("3. Insert an element to a desired position in a list, Append an element to the list, remove element from desired position in a list")
    cho = int(input())

    if cho == 1:
        average()
    elif cho == 2:
        reverse()
    elif cho == 3:
        array()


main()
    
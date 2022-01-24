def bin_to_gray():
    n = input('Enter binary code: ')

    # List comprehension to split the binary code into separate digits
    b_array = [int(x) for x in str(n)]
    # Most Significant Bit(msb) will be first element of the b_array
    msb = b_array[0]

    # Array to store the elements of the gray code
    # First element is the Most Significant Bit
    g_array = [msb]

    # Compare consecutive bits to determine gray code
    for i in range(len(b_array)):
        k = i + 1
        if k == len(b_array):
            break

        if b_array[i] == b_array[i + 1]:
            g_array.append(0)
        else:
            g_array.append(1)

    # Convert integer list to string list
    g_array_str = [str(i) for i in g_array]

    # Join list items using join()
    gray_code = int("".join(g_array_str))

    print(f'Gray code: {gray_code}')


def gray_to_bin():
    n = input('Enter gray code: ')

    # List comprehension to split gray code into separate digits
    g_array = [int(x) for x in str(n)]
    # Most Significant Bit(msb) will be first element of the array
    msb = g_array[0]

    # Array to store the elements of the binary code
    # First element is the Most Significant Bit
    b_array = [msb]

    # Compare consecutive bits to determine binary code
    for i in range(len(g_array)):
        k = i + 1
        if k == len(g_array):
            break

        if b_array[i] == g_array[i + 1]:
            b_array.append(0)
        else:
            b_array.append(1)

    # Convert integer list to string list
    b_array_str = [str(x) for x in b_array]

    # Join list items using join()
    binary_code = int("".join(b_array_str))

    print(f'Binary code: {binary_code}')


if __name__ == '__main__':
    print("***********************************")
    print("Choose operation: ")
    print("\t [1] Binary to Gray code \n"
          "\t [2] Gray to Binary code")
    choice = int(input("Enter choice here: "))

    if choice == 1:
        bin_to_gray()
    elif choice == 2:
        gray_to_bin()
    else:
        print("[!] Enter viable choice.")

import base64
import zlib

string = "vDCP591g1WP75I/kROQLhJhxKk6z9DCThi3EOV3Pkw=="


def highest_product_of_three(list_of_ints):
    """ Takes a list of integers and returns the highest product of three of the integers. The input list_of_ints will always have at least three integers.
    >>> highest_product_of_three([1,2,3,4,5])
    60
    >>> highest_product_of_three([1,2,3,4,-5])
    24
    >>> highest_product_of_three([-10,-10,1,3,2])
    300
    >>> highest_product_of_three([10,2,5])
    100
    >>> highest_product_of_three([5,4,3,2,1])
    60
    """

    # Runtime: O(n)
    # Spacetime: O(1)

    highest_product = list_of_ints[0] * list_of_ints[1] * list_of_ints[2]
    highest = list_of_ints[0]
    lowest = list_of_ints[0]
    highest_two = list_of_ints[0] * list_of_ints[1]
    lowest_two = list_of_ints[0] * list_of_ints[1]

    if len(list_of_ints) == 3:
        return highest_product


    for i in range(2,len(list_of_ints)-1):
        product = list_of_ints[i] * list_of_ints[i + 1]
        current_num = list_of_ints[i]

        if current_num > highest:
            highest = current_num
            if product > highest_two:
                highest_two = product
        elif current_num < lowest:
            lowest = current_num
            if product < lowest_two:
                lowest_two = product

    if highest_two * highest > lowest_two * lowest:
        highest_product = highest_two * highest
    elif highest_two * highest < lowest_two * lowest:
        highest_product = lowest_two * lowest
    elif highest_two * lowest < lowest_two * highest:
        highest_product = lowest_two * highest
    else:
        highest_product = highest_two * lowest

    return highest_product

def valid_parens_perms(num):

    result = []

    def recurse(substr, left, right):
        if left == 0 and right == 0:
            result.append(substr)
            return

        elif left == 0:
            recurse(substr + ')', left, right - 1)

        elif left < right:
            recurse(substr + '(', left - 1, right)
            recurse(substr + ')', left, right - 1)

        elif left == right:
            recurse(substr + '(', left - 1, right)

    recurse('', num, num)

    return result

def xor(data, key): 
	return bytearray(a^b for a, b in zip(*map(bytearray, [data, key]))) 
def prime():
	prime_nums = []
	for num in range(500):
		if num > 1:
			for i in range(2, num):
				if (num % i) == 0:
					break
			else:
				prime_nums.append(num)
	return prime_nums

res = prime()
key = str.encode(chr(highest_product_of_three([-10,-10,1,3,2]))*2) + str.encode('*'.join(chr(i*10) for i in res)) +  str.encode('-'.join(valid_parens_perms(2)))

#base64.b64encode(self.xor(zlib.compress(self.logger), self.key)).decode("utf-8") 

print(zlib.decompress(xor(base64.b64decode(string), key)))
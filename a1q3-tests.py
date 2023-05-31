print("""
Name: Hatem Alfarra
NSID: Hma194
Student #: 11291988
Section: 145-01
""")


from a1q3 import game_loop




# Test 1: Ex-Input1

file = 'Ex-Input1.txt'
input = "Ex-Input1.txt"
expected = 'Same as Ex-Output1.txt'
result = 'Same as Ex-Output1.txt'
# passed



# Test 2: Ex-Input2

file = 'Ex-Input2.txt'
input = "Ex-Input2.txt"
expected = 'Ex-Output2.txt'
result = 'Same as Ex-Output2.txt'
# passed



# Test 3: Ex-Input3

file = 'Ex-Input3.txt'
input = "Ex-Input3.txt"
expected = 'Ex-Output3.txt'
result = 'Same as Ex-Output3.txt'
# passed



# Test 4: Ex-Input1-1
# Running Ex-Input1 through another iteration

file = 'Ex-Input1-1.txt'
input = "Ex-Input1-1.txt"
expected = 'Ex-Output1-1.txt'
result = 'Same as Ex-Output1-1.txt'
# passed




# Test 5: Ex-Input1-2
# Running Ex-Input1-1 through another iteration

file = 'Ex-Input1.txt'
input = "Ex-Input1.txt"
expected = 'Ex-Output1.txt'
result = 'Same as Ex-Output1.txt'
# Inputted as '3x3_updated.txt'
# passed



# Test 6: Ex-Input1-2

file = 'Ex-Input1-2.txt'
input = "Ex-Input1-2.txt"
expected = 'Ex-Output1-2.txt'
result = 'Same as Ex-Output1-2.txt'
# Inputted as '3x3_updated.txt'
# passed


# Test 7: Ex-Input4
# Completely empty file

file = 'Ex-Input4.txt'
input = "Ex-Input4.txt"
expected = 'error message'
result = 'error message'
# passed



# Test 8: Ex-Input5
# Width and length of inputted file are not equal
file = 'Ex-Input5.txt'
input = "Ex-Input5.txt"
expected = 'Message: Please use a square array (width equals height) instead'
result = 'same message as expected'
# passed


# Test 9: Ex-Input6
# Wrong symbols

file = 'Ex-Input6.txt'
input = "Ex-Input6.txt"
expected = 'Error'
result = 'Error'
# passed

test_string = '1w3e4rt5jkdnh6ljh86mjb99'
actual = ''.join(filter(lambda i: i.isdigit(), test_string))
print("The digit string is: " + str(actual))

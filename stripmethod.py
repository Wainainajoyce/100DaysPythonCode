#The strip method is used to remove whitespace characters by default
#removes hyphens and dollar signs from the start and end of the string. In the third example, it removes leading and trailing zeros from the string.
new_string = "  My name is Joyce   "
newer_string = new_string.strip()
print(newer_string)
#You can use lstring and rstring to remove leading characters and trailing characters respectively
newest_string = "& My name is joyce"
newest_string1 = newer_string.lstrip()
print(newest_string1)



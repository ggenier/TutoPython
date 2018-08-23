# -*-coding:Latin-1 -*
import re

regexp = re.search(r"abc", "abcdef")
print(regexp)

regexp = re.search(r"^0[0-9]([ .-]?[0-9]{2}){4}$", "0631961990")
print(regexp)

regexp = re.search(r"^0[0-9]([ .-]?[0-9]{2}){4}$", "06-31-96-19-90")
print(regexp)



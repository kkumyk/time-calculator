# This entrypoint file to be used in development. Start by reading README.md
from time_calculator import add_time
from unittest import main


print(add_time("11:06 PM", "2345:02"))
#print(add_time("1:06 PM", "2233:02"))
# print(add_time("4:05 PM", "34:02"))
# print(add_time("6:06 AM", "332:02"))


# Run unit tests automatically
main(module='test_module', exit=False)
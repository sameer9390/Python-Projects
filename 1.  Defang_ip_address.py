''' A user’s IP address is defanged to prevent the user from clicking on a malicious link. The problem with Defanginig IP addresses is one of the common coding interview questions for someone who is planning data science. In this , I will tell you how to defang an IP address using Python.


 
Solving the problem of changing an IP address is good for someone who is a newbie for practising the concept of string manipulation. It is very easy to understand because it is only based on the concepts of replacing and join. There are so many unique ways to solve this problem, which is why this is one of the favourite questions for interview coding.

Defanging IP Address: Problem Statement
To convert an IP address to a defanged IP address, we need to replace “.” with “[.]”. During coding interviews, a standard problem for changing an IP address is that you receive a valid IP address, you must return a defanged version of that IP address.

 You just need to replace every “.” with “[.]”.

Defang IP Address using Python
Now let’s see how to write a program to defang an Ip address using Python. Here you simply need to treat “.” as a separator and split the string. Then you have to rejoin an empty string and select “[.]” as the new separator:
'''

 
def ip_address(address):
    new_address = ""
    split_address = address.split(".")
    separator = "[.]"
    new_address = separator.join(split_address)
    return new_address
ipaddress = ip_address("1.1.2.3")
print(ipaddress)
view rawdefang.py hosted with ❤ by GitHub
This is how easy it is to defang an Ip address using Python. If you are planning to use C++ for your coding interviews then below is how to defang an IP address using the C++ programming language:


def ip_address(address):
    new_address = ""
    split_address = address.split(".")
    separator = "[.]"
    new_address = separator.join(split_address)
    return new_address
ipaddress = ip_address("1.1.2.3")
print(ipaddress)

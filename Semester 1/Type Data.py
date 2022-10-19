from colorama import Fore, Back, Style
data_int = 8
print(Fore.RED,"Data = ", data_int, "type",type(data_int))

data_float = float(data_int)
data_bool = bool(data_int)
data_str = str(data_int)
print(Fore.MAGENTA,"data = ", data_float, "type", type(data_float))
print(Fore.BLACK,"data = ", data_bool, "type", type(data_bool))
print(Fore.CYAN,"data =", data_str, "type", type(data_str))

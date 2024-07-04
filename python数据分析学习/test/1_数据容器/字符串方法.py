#split方法
my_str = "hello czy work hard"
my_str_list = my_str.split(" ")
print(f"切割后得到:{my_str_list}")

#strip方法
my_str = "  hello czy work hard  "
new_str_list = my_str.strip() #没有参数，默认去除空格
print(f"切割后得到:{new_str_list}")

my_str = "12hello czy work hard21"
new_str_list = my_str.strip("12") 
print(f"切割后得到:{new_str_list}")
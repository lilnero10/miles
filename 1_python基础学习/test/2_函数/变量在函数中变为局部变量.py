num = 200

def test_a():
    print(f"test_a:{num}")

def test_b():
    num = 500 #局部变量
    print(f"test_b:{num}")

test_a()
test_b()
print(num)
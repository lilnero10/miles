class Solution(object):
    def average(self, salary):
        # 找到最小值和最大值
        min_salary = min(salary)
        max_salary = max(salary)

        # 计算去掉最小值和最大值后的剩余工资总和
        total_salary = sum(salary) - min_salary - max_salary

        # 剩余工资的数量
        count = len(salary) - 2

        # 计算平均值
        average_salary = total_salary / count

        # 输出保留小数点后四位
        return format(average_salary, ".4f")


salary = [48000,59000,99000,13000,78000,45000,31000,17000,39000,37000,93000,77000,33000,28000,4000,54000,67000,6000,1000,11000]
print(Solution().average(salary))
class Solution(object):
    def Change(self, bills):
        # 初始化手头的各种面额的钞票数量
        five_count = 0
        ten_count = 0
        twenty_count = 0

        # 遍历每一位顾客的支付
        for bill in bills:
            if bill == 5:
                five_count += 1
            elif bill == 10:
                if five_count > 0:
                    five_count -= 1
                    ten_count += 1
                else:
                    return False
            elif bill == 20:
                if ten_count > 0 and five_count > 0:
                    ten_count -= 1
                    five_count -= 1
                    twenty_count += 1
                elif five_count >= 3:
                    five_count -= 3
                    twenty_count += 1
                else:
                    return False
            elif bill == 50:
                if twenty_count > 0 and five_count >= 1:
                    twenty_count -= 1
                    five_count -= 1
                elif ten_count >= 1 and five_count >= 3:
                    ten_count -= 1
                    five_count -= 3
                elif five_count >= 9:
                    five_count -= 9
                else:
                    return False
            elif bill == 100:
                if twenty_count >= 2 and five_count >= 1:
                    twenty_count -= 2
                    five_count -= 1
                elif ten_count >= 1 and twenty_count >= 1 and five_count >= 1:
                    ten_count -= 1
                    twenty_count -= 1
                    five_count -= 1
                elif ten_count >= 3 and five_count >= 1:
                    ten_count -= 3
                    five_count -= 1
                elif five_count >= 19:
                    five_count -= 19
                else:
                    return False
            elif bill == 1000:
                if twenty_count >= 49 and five_count >= 1:
                    twenty_count -= 49
                    five_count -= 1
                elif ten_count >= 99 and five_count >= 1:
                    ten_count -= 99
                    five_count -= 1
                elif five_count >= 199:
                    five_count -= 199
                else:
                    return False

        return True
    def Change2(self, bills):
        # 贪心算法
        # 初始化手头的钞票数量
        change = {5: 0, 10: 0, 20: 0}

        # 遍历每一位顾客的支付
        for bill in bills:
            if bill == 5:
                change[5] += 1
            elif bill == 10:
                if change[5] > 0:
                    change[5] -= 1
                    change[10] += 1
                else:
                    return False
            elif bill == 20:
                if change[10] > 0 and change[5] > 0:
                    change[10] -= 1
                    change[5] -= 1
                    change[20] += 1
                elif change[5] >= 3:
                    change[5] -= 3
                    change[20] += 1
                else:
                    return False
            else:
                # 计算找零金额
                change_needed = bill - 5
                # 按照贪心算法，优先使用面额大的钞票进行找零
                for denomination in [20, 10, 5]:
                    while change_needed >= denomination and change[denomination] > 0:
                        change_needed -= denomination
                        change[denomination] -= 1
                if change_needed > 0:
                    return False
                change[bill] += 1

        return True

# 示例
bills = [5, 5, 5, 10, 20, 50, 100, 1000]
print(Solution().Change2(bills))
# 輸入一個列表
a = input("輸入由逗號分隔的數字列表: ")
# 將輸入的字符串轉換為整數列表
nums = list(map(int, a.split(',')))

def missing_number(nums):
    n = len(nums)
    # 計算理論總量
    total = n * (n + 1) // 2
    # 計算實際總數
    actual_sum = sum(nums)
    # 返回缺少的數字
    return total - actual_sum

# 呼叫函數並打印結果
#test 1
print(missing_number([0,1,2,3,5]))  # 輸出: 4
#test 2
print(missing_number([0,5,7,9,8,4,3,2,1]))  # 輸出: 6
#print result of input(a)
print(f"缺少的數字是:: {missing_number(nums)}")
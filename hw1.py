from typing import List, Tuple
# 根據圖像中紅色突出顯示的鍵聲明一個字母變量
alphabet: List[List[str]] = [
    ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')'],  # 第一行
    ['Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P'],  # 第二行
    ['A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L'],       # 第三行
    ['Z', 'X', 'C', 'V', 'B', 'N', 'M','<','>','?']      # 第四行
]
# 此函數根據需要的位置找到key
def getResult(queries: List[Tuple[str, int]]) -> List[str]:
    results = []
    for s, k in queries:
        found = False
        for i in range(len(alphabet)):
            if s in alphabet[i]:
                j = alphabet[i].index(s)
                found = True
                
                if k == 1:    #上
                    results.append(alphabet[i - 1][j] if i > 0 else alphabet[-1][j])
                elif k == 2:  #下
                    results.append(alphabet[i + 1][j] if i < len(alphabet) - 1 else alphabet[0][j])
                elif k == 3:  #右
                    results.append(alphabet[i][j + 1] if j < len(alphabet[i]) - 1 else alphabet[i][0])
                elif k == 4:  #左
                    results.append(alphabet[i][j - 1] if j > 0 else alphabet[i][-1])
                break
        
        if not found:
            results.append('-1')

    return results

#例如
test_queries = [('K', 4), ('E', 1), ('*', 2)]
output = getResult(test_queries)
print(output)

test_queries = [('M', 3)]
output = getResult(test_queries)
print(output)
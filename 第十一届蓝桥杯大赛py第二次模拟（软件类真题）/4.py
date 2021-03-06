class Solution:
    def generateParenthesis(self, n: int) :
        if n <= 0: return []
        res = []

        def nQueen(paths, left, right):
            if left > n or right > left: return
            if len(paths) == n * 2:  # 因为括号都是成对出现的
                res.append(paths)
                return

            nQueen(paths + '(', left + 1, right)  # 生成一个就加一个
            nQueen(paths + ')', left, right + 1)

        nQueen('', 0, 0)
        return res

s=Solution()
print(s.generateParenthesis(4))
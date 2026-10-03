class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        m=0
        n=-1
        for i in range(len(mat)):
            a=sum(mat[i])
            if a>n:
                n=a
                m=i
        return [m,n] 

        
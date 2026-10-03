class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        m=0
        n=[0,0]
        for i in range(len(mat)):
            a=sum(mat[i])
            if a>m:
                n=[i,a]
                m=a
        return n 

        
class Solution(object):
    def isValid(self, s):
        st=[]
        p={")":"(","}":"{","]":"["}
        for c in s:
            if c in "({[":
                st.append(c)
            else:
                if not st:
                    return False
                if st[-1]!=p[c]:
                    return False
                st.pop()
        return len(st)==0
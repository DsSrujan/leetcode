class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        
        """
        a=[]
        p=path.split('/')
        for n in p:
            if n =="" or n==".":
                continue 
            elif n=="..":
                if a:
                    a.pop()
            else:
                a.append(n)
        return "/"+"/".join(a)




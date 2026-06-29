class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s=list(s)
        t=list(t)
        if len(s)!=len(t):
            return False
        else:
            for let in s:
                if let in t:
                    t.remove(let)
            if not t:
                return True
            else:
                return False

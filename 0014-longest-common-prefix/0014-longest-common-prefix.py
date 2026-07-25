class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs)==0:
            return ""
        prefix=strs[0]
        for i in range(1,len(strs)):
            curr=strs[i]
            j=0
            while j<min(len(prefix),len(curr)):
                if prefix[j]==curr[j]:
                    j+=1
                else:
                    break
            prefix=prefix[0:j]       
        return prefix       
        
class Solution:

    def encode(self, strs: List[str]) -> str:
        joined = ""
        for i in strs:
            i.replace('%', '%40')
            joined += i + "%20"
        return joined

    def decode(self, s: str) -> List[str]:
        
        splited = s.split('%20')
        for i in splited:
            i = i.replace('%', '%40')
        splited.pop()
        return splited

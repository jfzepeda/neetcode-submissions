class Solution:

    def encode(self, strs: List[str]) -> str:
        joined = ""
        for i in strs:
            joined += i + ",}*"
        return joined

    def decode(self, s: str) -> List[str]:
        splited = s.split(',}*')
        splited.pop()
        return splited

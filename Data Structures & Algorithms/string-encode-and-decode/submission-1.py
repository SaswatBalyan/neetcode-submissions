class Solution:
    def encode(self, strs: List[str]) -> str:
        if not strs:
            return ''
        size,res=[],[]
        for s in strs:
            size.append(len(s))
        for sz in size:
            res.append(str(sz))
            res.append(',')
        res.append('#')
        res.extend(strs)
        return ''.join(res)
    def decode(self, s: str) -> List[str]:
        if not s:
            return []
        size,res,i=[],[],0
        while s[i] != '#':
            j = i
            while s[j] != ',':
                j += 1
            size.append(int(s[i:j]))
            i = j + 1
        i += 1
        for sz in size:
            res.append(s[i:i+sz])
            i += sz
        return res


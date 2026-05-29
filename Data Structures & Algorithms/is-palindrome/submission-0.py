class Solution:
    def isPalindrome(self, s: str) -> bool:
        lower = s.lower()
        no_spaces = lower.replace(" ", "")
        clean_text = re.sub(r'[^a-zA-Z0-9]', '', no_spaces)
        i = 0
        j = len(clean_text)-1

        while (i<=j):
            if (clean_text[i] != clean_text[j]):
                return False    
            i+=1
            j-=1

        return True;

            



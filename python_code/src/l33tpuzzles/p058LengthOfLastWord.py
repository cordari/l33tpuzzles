class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        seen_letter = False
        word_length = 0
        for i in range(len(s) - 1, -1, -1):
            if s[i] == " ":
                if seen_letter:
                    return word_length
            else:
                seen_letter = True
                word_length += 1
        return word_length
    
def main():
    word = "Hello World"
    word = "   fly me   to   the moon  "
    word = "abcdefghijk"
    sol = Solution()

    print(sol.lengthOfLastWord(word))

if __name__ == "__main__":
    main()

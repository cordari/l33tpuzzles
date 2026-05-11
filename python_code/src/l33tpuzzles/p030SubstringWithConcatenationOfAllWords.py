
from typing import Dict, List

"""
30. Substring with Concatenation of All Words

Hard

You are given a string s and an array of strings words. All the strings of words are of the same length.

A concatenated string is a string that exactly contains all the strings of any permutation of words concatenated.

For example, if words = ["ab","cd","ef"], then "abcdef", "abefcd", "cdabef", "cdefab", "efabcd", and "efcdab" are all concatenated strings. "acdbef" is not a concatenated string because it is not the concatenation of any permutation of words.
Return an array of the starting indices of all the concatenated substrings in s. You can return the answer in any order.

 

Example 1:

Input: s = "barfoothefoobarman", words = ["foo","bar"]

Output: [0,9]

Explanation:

The substring starting at 0 is "barfoo". It is the concatenation of ["bar","foo"] which is a permutation of words.
The substring starting at 9 is "foobar". It is the concatenation of ["foo","bar"] which is a permutation of words.

Example 2:

Input: s = "wordgoodgoodgoodbestword", words = ["word","good","best","word"]

Output: []

Explanation:

There is no concatenated substring.

Example 3:

Input: s = "barfoofoobarthefoobarman", words = ["bar","foo","the"]

Output: [6,9,12]

Explanation:

The substring starting at 6 is "foobarthe". It is the concatenation of ["foo","bar","the"].
The substring starting at 9 is "barthefoo". It is the concatenation of ["bar","the","foo"].
The substring starting at 12 is "thefoobar". It is the concatenation of ["the","foo","bar"].

 

Constraints:

1 <= s.length <= 10^4
1 <= words.length <= 5000
1 <= words[i].length <= 30
s and words[i] consist of lowercase English letters.
"""
class Solution:
    """
    this is the naive approach that times out on some edge cases.
    """
    def __findSubstring(self, s: str, words: List[str]) -> List[int]:
        wlen = len(words[0])
        wcount = len(words)
        ans: List[int] = []

        ref_freq: Dict[str, int] = {}
        for word in words:
            if word in ref_freq:
                ref_freq[word] = ref_freq[word] + 1
            else:
                ref_freq[word] = 1

        w_freq: Dict[str, int] = {}


        for x in range(0, wlen):
            
            i = x
            while i < len(s):
                for word in words:
                    w_freq[word] = 0
                error = 0
                j = 0
                while j < wcount:
                    start = i + wlen * j
                    end = start + wlen
                    if end <= len(s):
                        subs_word = s[start: end]
                        if subs_word in w_freq:
                            if w_freq[subs_word] < ref_freq[subs_word]:
                                w_freq[subs_word] = w_freq[subs_word] + 1
                            else:
                                error = 1
                                break
                        else:
                            error = 2
                            break
                    else:
                        error = 2
                        break
                    j += 1
                if error == 0:
                    ans.append(i)
                if error == 2:
                    i = i + wlen * (j + 1)
                else:
                    i += wlen

        return ans
    
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        word_size = len(words[0])
        word_count = len(words)
        substr_size = word_size * word_count
        anchor_right_bound = len(s) - substr_size
        mover_right_bound = len(s) - word_size

        ref_freq: Dict[str, int] = {}
        subs_freq: Dict[str, int] = {}

        ans: List[int] = []

        for word in words:
            subs_freq[word] = 0
            if word in ref_freq:
                ref_freq[word] = ref_freq[word] + 1
            else:
                ref_freq[word] = 1

        print(f"ref_freq:{ref_freq}")

        # state = 1

        for x in range(0, word_size):
            for word in subs_freq.keys():
                subs_freq[word] = 0
            state = 1
            anchor = x
            print(f"anchor: {anchor}, state: {state}")
            while anchor <= anchor_right_bound:
                print(f"begin anchor loop anchor {anchor}")
                if state == 1:
                    mover = anchor
                # else:
                #     mover += word_size
                print(f"mover: {mover}, anchor: {anchor}, substr_size: {substr_size}")
                state = 0
                while mover < anchor + substr_size:
                    if mover > mover_right_bound:
                        print(f"mover:{mover} out of mover_right_bound")
                        state = 1
                        break
                    ext_word = s[mover:mover + word_size]
                    print(f"ext_word:{ext_word}")
                    if ext_word not in ref_freq:
                        state = 1
                        break
                    subs_freq[ext_word] = subs_freq[ext_word] + 1
                    mover += word_size

                print(f"end mover loop mover:{mover}, subs_freq:{subs_freq}, anchor:{anchor}")
                if state == 0:
                    all_match = True
                    for word in ref_freq.keys():
                        if ref_freq[word] != subs_freq[word]:
                            all_match = False
                            break
                    if all_match:
                        ans.append(anchor)

                    prev_word = s[anchor:anchor + word_size]
                    print(f"prev_word:{prev_word}")
                    subs_freq[prev_word] = subs_freq[prev_word] - 1
                    anchor += word_size
                    print(f"state 0, anchor:{anchor}, subs_freq:{subs_freq}")
                else:
                    for w in subs_freq.keys():
                        subs_freq[w] = 0
                    anchor = mover + word_size
                    print(f"state 1, anchor: {anchor}, subs_freq: {subs_freq}")


        return ans


                




    
def main():
    # s = "aaaaaaaaaaaaaa"
    # words = ["aa","aa"]
    s = "cvecqxjemfumiqgppzqadaduhzxwymeahkdzhodtvyhfqouipmitmlpvmmsmayniishpglkbltgbhclxptsdgjzvxrhxpufxmpouaavltdodgaaxvuccdbxauezlbhipwykwahjulxxtzzsvtuzyywasczefgovenfapmjjzjiukhmfchecfcczhedmmsjrhotwdfieqqzaalgeumhzrlzapemewwxfmqerxmwnevoggulbiuczfdbxiodgmaoasssqgqdklrtrnguwaxxfczekphrdjfdczxsfnvrypkscqoasnyaqzeaootrxawbzwtejrykiickbsltgltwmawaqstnsrpsnkyxdwjlhlykfldlwzhibgkryfgqwxkmkjlnhuzohzymkeygffqincznhhgfhqrrbcejyfxfeysoeqwjxornqsazbgfizyzadgjbljhsjzinrfwqtpdmjelkmqvlpumsaxtoicgrbqeuvclrtqdcwopjhkwwekqhklxsofkrvqorvbiornrobgzisxgyiyfskcmahytdphwkkgactrswzthrqnsaoxuychalfvqwdoipujrpclocevvxkpzypuyrdyeiuxhznroiaizftpjakgzvwyvlsuevskgohppvggfjogojwxlgdkdbjzmbvqznbfekwvhcbmlrvbdryozezffigujbkkqnpuylsfqtudnpfqifehjdorlulxvxhmlzilmascwogjdlzlsfvcjjvueitbfbpsayfmayrwmxhskifcocgxmdtslnvtqllsjrglrxifwpxiaflohtnvxgnkvldnwrfhkmsbjcgiugquldiuxvqwdfibqmomfuvpioqtqybkeservomulcsrhbsapgouckjmyzgqzjdgbjxzylvlpoczruzgdnahxjuxkcqjltppcnqcanoqbqpunoasdabdlxcvzsfnlucojsskfgcjzrdohggmgjpshspgkutyrxocrgmxpqiohncqtkdctswcmllzggxzenbvvoukgeaqscgnojpkenmszzrhgqgkfhhbxcleimuaqaqhmhrsvfmufgbnyjxeqgfoissrgotxqjeerxwoelilrlypuxvkecaovuhbibabmgfffetkpdxioyxkvvvbxxqssxwcawdnflskpoweruogslqpinrgnhafgyjhxpucaompcjvwfjcxwumfkfnxmnevmncjeyleoztrkqnpzroyndfziswxfcstsuewurbirwbdnqtohjmxmrwvjvurxmmpirmckpmblohyeanolzlytjveepxedktndhrnwdrirygwavmlxzjqigwpxutaeonjwgwukpcbnlzngnzfmkvxrumoohruvgdtnboxrqaedcumpvrefpbyjppxwirrowldxzcordtvhnjwkaarpdqashxorqifmvlkwnynqtkxitwswyklccoulnlcetjsouckidzaymahfwbbwnpyrdvcqggwbsprmtbwyczxozgwxjztzosqtpvmvbiytzpitsgtufsleahbkgxjxrbsgwedapbtoqdjikdcrxpwywzifwtenuwvrdyrszmgpsszexevutrsstczrvdhsbclgdeycqhukztoyzkstdllwpmqnrxfubqbeuzjmidxjylhyxatbngzcsppjoudsmewigfvoksyjfhjdhcguifzaxqlnnqfzxcidjftuztfebojksphcxgcuwpjlfplctvhcadyzwdfztpmngtpfbtbzillqawuttexthwufbzhvqtizmaentgmcrzut"
    words = ["hbkgxjxrbsgwedapbtoqdjikdc","rwbdnqtohjmxmrwvjvurxmmpir","qbeuzjmidxjylhyxatbngzcspp","mckpmblohyeanolzlytjveepxe","dktndhrnwdrirygwavmlxzjqig","abmgfffetkpdxioyxkvvvbxxqs","szexevutrsstczrvdhsbclgdey","wpxutaeonjwgwukpcbnlzngnzf","wumfkfnxmnevmncjeyleoztrkq","dohggmgjpshspgkutyrxocrgmx","lkwnynqtkxitwswyklccoulnlc","rxpwywzifwtenuwvrdyrszmgps","gqgkfhhbxcleimuaqaqhmhrsvf","rgnhafgyjhxpucaompcjvwfjcx","umpvrefpbyjppxwirrowldxzco","rdtvhnjwkaarpdqashxorqifmv","rxwoelilrlypuxvkecaovuhbib","zosqtpvmvbiytzpitsgtufslea","cqhukztoyzkstdllwpmqnrxfub","npzroyndfziswxfcstsuewurbi","bvvoukgeaqscgnojpkenmszzrh","sxwcawdnflskpoweruogslqpin","fzaxqlnnqfzxcidjftuztfeboj","pqiohncqtkdctswcmllzggxzen","mufgbnyjxeqgfoissrgotxqjee","etjsouckidzaymahfwbbwnpyrd","mkvxrumoohruvgdtnboxrqaedc","vcqggwbsprmtbwyczxozgwxjzt","joudsmewigfvoksyjfhjdhcgui"]
    sol = Solution()
    ans = sol.findSubstring(s, words)
    print(ans)

if __name__ == "__main__":
    main()


                


        
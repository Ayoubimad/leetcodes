class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        substrings = {}

        # {abc : 1 , b : 2}

        if len(s) == 0:
            return 0

        for i in range(len(s)):
            for j in range(i, len(s)):
              current_substring = s[i:j+1]
              if current_substring not in substrings:
                # We should check if there is any duplicate character whitin the substring here. How?
                if len(set(current_substring)) == len(current_substring:
                   substrings[current_substring] = len(current_substring)

        return max(substrings.values())
        """
        seen = set()  # qui mettiamo i caratteri unici visti nella sequenza
        left_index = 0  # indice sinistro della finestra
        max_len = 0  # lunghezza massima ottenuta per ora

        for right_index in range(len(s)):
            # incrementiamo l'indice destro e se troviamo
            # un carattere duplicato incrementiamo anche il sinistro
            while s[right_index] in seen:

                seen.remove(s[left_index])
                left_index += 1

            seen.add(s[right_index])
            max_len = max(max_len, right_index - left_index + 1)

        return max_len

from typing import List


class Solution:

    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        # Metto ogni carattere di t e s in hash_tables differenti {"carattere": occorrenza}.
        # Se sono uguali allora è un anagramma.

        s_hash_table = {}
        t_hash_table = {}

        for element in s:
            if element in s_hash_table:
                s_hash_table[element] = s_hash_table[element] + 1
            else:
                s_hash_table[element] = 1

        for element in t:
            if element in t_hash_table:
                t_hash_table[element] = t_hash_table[element] + 1
            else:
                t_hash_table[element] = 1

        return s_hash_table == t_hash_table

    # Funziona ma da time limit
    """
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        out = {}

        for s in strs:

            # Se il dizionario è vuoto
            if out == {}: 
                out[s] = [s]
                continue

            # controllo se è un anagramma delle chiavi

            added = False

            for key in out.keys():
                if self.isAnagram(key,s):
                    # Se è anagramma lo aggiungo
                    out[key].append(s)
                    added = True
                    break  

            # Se non è stato aggiunto come anagramma, lo aggiungo come chiave.
            if not added:
                out[s] = [s]

        return list(out.values())
        """

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        out = {}

        # Posso usare come chiave la forma canonica, basta che ordino la stringa corrente.
        # Ex: eat ate => la forma canonica è aet.
        for s in strs:

            key = tuple(sorted(s))
            # se la chiave non c'è la aggiungo
            if key not in out:
                out[key] = []
            # se aggiungo l'anagramma
            out[key].append(s)

        return list(out.values())

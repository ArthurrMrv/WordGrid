class Solution:
    list_found = []

    def decomp_words(self, list_words) -> dict:
        """
        Decompose the list of words in a dictionary of from 'length' -> 'beggining' -> 'caracter'
        """
        dico_decomp = {}
        for word in list_words:
            for i in range(0, len(word)):
                if i in dico_decomp:
                    if word[:i] in dico_decomp[i]:
                        dico_decomp[i][word[:i]] += word[i]
                    else:
                        dico_decomp[i][word[:i]] = word[i]
                else:
                    dico_decomp[i] = {word[:i] : word[i]}

        return dico_decomp

    def recc_search(self, board, words, dict_words, x, y, actual):
        
        for p in [(0, 1), (0, -1), (1, 0), (-1, 0)]:

            if ((-1 < x+p[0] < len(board[0]))  and (-1 < y+p[1] < len(board))):
                pass
            else:
                continue
            
            if actual + board[y+p[1]][x+p[0]] in words:
                self.list_found.append(actual + board[y+p[1]][x+p[0]])
            
            if (len(actual) not in dict_words) or (actual not in dict_words[len(actual)]) or (board[y+p[1]][x+p[0]] not in dict_words[len(actual)][actual]):
                continue
            
            self.recc_search(board, words, dict_words, x+p[0], y+p[1], actual+board[y+p[1]][x+p[0]])
        return self.list_found.copy()

                
    def search(self, board, words, dict_words):
        """
        Loop through each cell and activate the reccursive search if necessary
        """
        ans = []
        for y in range(0, len(board)):
            for x in range(0, len(board)):
                if board[y][x] in dict_words[0]['']:
                    ans = self.recc_search(board, words, dict_words, x, y, board[y][x])
        ans.sort()
        return ans

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        """
        Return a list of words matching between the input and the words in the grid
        """
        self.list_found.clear()
        
        return self.search(board, words, self.decomp_words(words))

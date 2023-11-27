from tqdm import tqdm
import string

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

    def recc_search(self, board, words, dict_words, x, y, actual, studied):
        """
        reccursive search of the words in the grid
        """
        
        for (i, j) in tuple((x, y) for x in range(-1, 2) for y in range(-1, 2) if (x, y) != (0, 0)):

            if not ((-1 < x+i < len(board[0]))  and (-1 < y+j < len(board))) or (x+i, y+j) in studied:
                continue

            if actual + board[y+j][x+i].lower() in words[actual[0]]:
                self.list_found.append(actual + board[y+j][x+i].lower())
            
            if (len(actual) not in dict_words) or (actual not in dict_words[len(actual)]) or (board[y+j][x+i].lower() not in dict_words[len(actual)][actual]):
                continue
            
            self.recc_search(board, words, dict_words, x+i, y+j, actual+board[y+j][x+i].lower(), studied + ((x+i, y+j),))
        return self.list_found.copy()

                
    def search(self, board, words, dict_words):
        """
        Loop through each cell and activate the reccursive search if necessary
        """
        ans = []
        #initiate a bar variable to be a tqdm loading bar
        bar = tqdm(total=len(board)*len(board[0]), desc="Searching words...", ascii=True)
        
        for y in range(0, len(board)):
            for x in range(0, len(board)):
                bar.update(1)
                if board[y][x].lower() in dict_words[0]['']:
                    ans = self.recc_search(board, words, dict_words, x, y, board[y][x].lower(), studied=((x, y)))
                    
        bar.close()
        ans.sort()
        return ans

    def findWords(self, board : list, words : tuple):
        """
        Return a list of words matching between the input and the words in the grid
        """
        
        self.list_found.clear()
        return set(self.search(board, 
                               {s : tuple(word for word in words if word[0] == s) for s in string.ascii_lowercase}, 
                               self.decomp_words(words)))

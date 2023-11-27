import random
from leetcode_word_search import Solution

class Grid():
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.grid = self.get_random_grid(width, height)
        self.answ = None
        
    def __str__(self):
        ans = ""
        for i in range(len(self.grid)):
            for j in range(len(self.grid[0])):
                ans += str(self.grid[i][j]) + " "
            ans += "\n"
        return ans

    def __getitem__(self, key):
        return self.grid[key]

    def __setitem__(self, key, value):
        self.grid[key] = value

    def get_width(self):
        return self.width

    def get_height(self):
        return self.height

    def get_grid(self):
        return self.grid
    
    def get_answers(self):
        if self.answ == None:
            self.answ = self.get_answers_grid(self.grid)
        return self.answ

    def get_cell(self, x, y):
        return self.grid[y][x]

    def set_cell(self, x, y, value):
        self.grid[y][x] = value

    def get_random_cell(self):
        x = random.randint(0, self.width - 1)
        y = random.randint(0, self.height - 1)
        return self.grid[y][x]

    def get_random_empty_cell(self):
        x = random.randint(0, self.width - 1)
        y = random.randint(0, self.height - 1)
        while self.grid[y][x] != 0:
            x = random.randint(0, self.width - 1)
            y = random.randint(0, self.height - 1)
        return self.grid[y][x]

    def get_random_cell_of_value(self, value):
        x = random.randint(0, self.width - 1)
        y = random.randint(0, self.height - 1)
        while self.grid[y][x] != value:
            x = random.randint(0, self.width - 1)
            y = random.randint(0, self.height - 1)
        return self.grid[y][x]

    def get_random_empty_cell_of_value(self, value):
        x = random.randint(0, self.width - 1)
        y = random.randint(0, self.height - 1)
        while self.grid[y][x] != 0 and self.grid[y][x] != value:
            x = random.randint(0, self.width - 1)
            y = random.randint(0, self.height - 1)
        return self.grid[y][x]

    def get_random_cell_of_values(self, values):
        x = random.randint(0, self.width - 1)
    
    @staticmethod
    def get_random_grid(width : int,
                        height : int,
                        occurences : str = "AAAAAAAAABBCCDDDEEEEEEEEEEEEEEEFFGGHHIIIIIIIIJKLLLLLMMMNNNNNNOOOOOOPPQRRRRRRSSSSSSTTTTTTUUUUUUVVWXYZ"):
        
        return tuple(tuple(random.choice(occurences) for x in range(width)) for y in range(height))
    
    @staticmethod
    def get_answers_grid(grid : list, 
                        words_database : str = "dico.txt"):
        
        with open(words_database, "r") as f:
            list_of_words = tuple(w.strip() for w in f.readlines())
            
        return Solution().findWords(grid, list_of_words)
        
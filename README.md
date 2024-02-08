# Word Search Grid Generator

## Overview

This Python script generates a random word search grid and finds all the words present in the grid using the LeetCode Word Search algorithm.

The script defines a `Grid` class responsible for generating random word search grids and finding words within them. It utilizes the `leetcode_word_search` module to perform the word search algorithm.

## Features

- **Grid Class**: Defines a `Grid` class to generate random word search grids and find words within them.
- **Random Grid Generation**: Generates random word search grids with specified dimensions and occurrence of letters.
- **Word Search Algorithm**: Utilizes the LeetCode Word Search algorithm to find words within the generated grid.

## Requirements

- Python 3.x
- pandas library

## Usage

1. **Import the Script**: Import the `Grid` class from the script.

   ```python
   from word_search_grid_generator import Grid
   ```

2. **Create a Grid Object**: Create a `Grid` object with the desired width, height, and optionally the occurrences of letters.

   ```python
   grid = Grid(width=10, height=10)
   ```

3. **Get the Grid and Answers**: Retrieve the generated grid and the words found within it.

   ```python
   generated_grid = grid.get_grid()
   found_words = grid.get_answers()
   ```

4. **Optional Configuration**: You can customize the random grid generation by specifying the width, height, and occurrences of letters.

   ```python
   grid = Grid(width=15, height=15, occurrences="ABCDE")
   ```

## Example

```python
from word_search_grid_generator import Grid

# Create a 10x10 word search grid
grid = Grid(width=10, height=10)

# Retrieve the generated grid and found words
generated_grid = grid.get_grid()
found_words = grid.get_answers()

print("Generated Grid:")
print(generated_grid)
print("Found Words:")
print(found_words)
```

## Contributing

Contributions are welcome! If you'd like to improve the script or add new features, feel free to submit a pull request.

---

# LeetCode Word Search Module Overview

This module provides functionality for searching words in a grid using the LeetCode Word Search algorithm.

## Usage

1. **Import the Module**: Import the `Solution` class from the module.

   ```python
   from leetcode_wordsearch import Solution
   ```

2. **Create an Instance**: Create an instance of the `Solution` class.

   ```python
   solver = Solution()
   ```

3. **Find Words**: Use the `findWords` method to find words in a given grid.

   ```python
   board = [['A','B','C','E'],
            ['S','F','C','S'],
            ['A','D','E','E']]

   words = ("ABCCED", "SEE", "ABCB")
   found_words = solver.findWords(board, words)
   ```

4. **Retrieve Results**: The `findWords` method returns a list of words found in the grid.

   ```python
   print(found_words)
   ```

## License

This module is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

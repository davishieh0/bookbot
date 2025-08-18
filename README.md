# 📚 BookBot

> A simple yet powerful book analysis tool that counts words and analyzes character frequency in text files.

## 🚀 Quick Start

### Prerequisites
- Python 3.6 or higher

### Usage

```bash
python3 main.py <path_to_book>
```

### Example

```bash
python3 main.py books/frankenstein.txt
```

**Output:**
```
77130 words found in the document

============ BOOKBOT ============
Analyzing book found at books/frankenstein.txt...
----------- Word Count ----------
Found 77130 total words
--------- Character Count -------
e: 46043
t: 30365
a: 26743
o: 25225
i: 24613
n: 24367
s: 21155
h: 19725
r: 18557
...
============= END ===============
```
## 🔧 How It Works

1. **Text Processing**: Reads the entire book file into memory
2. **Word Counting**: Splits text by whitespace and counts words
3. **Character Analysis**: Converts all characters to lowercase and counts frequency
4. **Sorting**: Orders characters by frequency (most common first)
5. **Filtering**: Shows only alphabetic characters in the final report

## 🎯 Functions Overview

### `main.py`
- `getBookText(pathToFile)` - Reads file contents
- `main()` - Main application logic

### `stats.py`
- `getNumWords(book)` - Counts total words
- `getCharsDict(text)` - Analyzes character frequency
- `sortCharacterCounts(characterCounts)` - Sorts characters by frequency

## 🛠️ Error Handling

BookBot gracefully handles common errors:

- **File Not Found**: Clear message when the specified file doesn't exist
- **Permission Denied**: Helpful error when file permissions are insufficient
- **Unexpected Errors**: Logs unknown errors for debugging

## 🤝 Contributing

We welcome contributions to BookBot! Here's a detailed guide on how to contribute to this project:

### 🔧 Getting Started

1. **Fork the Repository**
   ```bash
   # Click the "Fork" button on GitHub or use GitHub CLI
   gh repo fork davishieh0/bookbot --clone
   ```

2. **Clone Your Fork**
   ```bash
   git clone https://github.com/YOUR_USERNAME/bookbot.git
   cd bookbot
   ```

3. **Create a Branch**
   ```bash
   # Create a new branch for your feature/fix
   git switch -b feature/your-feature-name
   # or
   git switch -b fix/bug-description
   ```

### 💻 Making Changes

4. **Set Up Development Environment**
   ```bash
   # Test the current code works
   python3 main.py books/frankenstein.txt
   ```

5. **Make Your Changes**
   - Edit the code following the existing camelCase convention
   - Ensure your code is clean and well-commented
   - Test your changes thoroughly

6. **Test Your Changes**
   ```bash
   # Test with different books
   python3 main.py books/mobydick.txt
   python3 main.py books/prideandprejudice.txt

   # Test error handling
   python3 main.py nonexistent_file.txt
   ```

### 📝 Submitting Your Changes

7. **Commit Your Changes**
   ```bash
   # Add your changes
   git add .

   # Commit with a descriptive message
   git commit -m "Add: detailed description of your changes"
   ```

8. **Push to Your Fork**
   ```bash
   git push origin feature/your-feature-name
   ```

9. **Create a Pull Request**
   - Go to your fork on GitHub
   - Click "New Pull Request"
   - Select your branch and the main repository's main branch
   - Fill out the PR template:

   **PR Title:** `Add: Brief description of your changes`

   **PR Description:**
   ```markdown
   ## What does this PR do?
   Brief description of the changes

   ## How to test?
   Step-by-step instructions to test your changes

   ## Checklist
   - [ ] Code follows camelCase convention
   - [ ] All functions are properly documented
   - [ ] Changes have been tested
   - [ ] No breaking changes introduced
   ```
**Thank you for contributing to BookBot! 🎉**

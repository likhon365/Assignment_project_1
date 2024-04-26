def read_entire_file(file_name):
    with open(file_name, 'r') as file:
        content = file.read()
    return content

def insert_line(file_name, line, position):
    with open(file_name, 'r+') as file:
        lines = file.readlines()
        lines.insert(position, line + '\n')
        file.seek(0)
        file.writelines(lines)

def count_lines(file_name):
    with open(file_name, 'r') as file:
        lines = file.readlines()
        return len(lines)

def find_longest_words(file_name):
    with open(file_name, 'r') as file:
        words = file.read().split()
        longest_words = [word.strip(",.") for word in words if len(word.strip(",.")) == max(len(w.strip(",.")) for w in words)]
        return longest_words

def append_and_display(file_name, text):
    with open(file_name, 'a+') as file:
        file.write(text + '\n')
        file.seek(0)
        appended_content = file.read()
    return appended_content




# Example content provided
example_content = "India is the fastest-growing economy. India is looking for more investments around the globe. The whole world is looking at India as a great market. Most of the Indians can foresee the heights that India is capable of reaching."

# Write example content to the file
with open("notes.txt", "w") as file:
    file.write(example_content)

# Example usage of the functions:
file_name = "notes.txt"

# Read the entire text file
print("1) Entire content of the file:")
print(read_entire_file(file_name))
print()

# Insert a line in the text file
insert_line(file_name, "This is a new line.", 2)
print("2) After inserting a line:")
print(read_entire_file(file_name))
print()

# Count the number of lines in the text file
print("3) Number of lines in the file:", count_lines(file_name))
print()

# Find the longest words in the text file
print("4) Longest words in the file:")
print(find_longest_words(file_name))
print()

# Append text to the file and display the text
appended_text = "This is some additional text appended to the file."
print("5) After appending text:")
print(append_and_display(file_name, appended_text))
print()

# Append more text to the file and display the text
more_appended_text = "This is some more additional text appended to the file."
print("6) After appending more text:")
print(append_and_display(file_name, more_appended_text))

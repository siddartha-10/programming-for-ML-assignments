def count_words_in_file(input_file, output_file):
    try:
        with open(input_file, 'r') as file:
            text = file.read()
            word_count = 0

            words = text.split()  # Split text into words

            for word in words:
                word_count += 1

        with open(output_file, 'w') as output:
            output.write(f'The word count in the file "{input_file}" is: {word_count}')

        print(f'Word count has been written to {output_file}.')
        print(f'The word count in the file "{input_file}" is: {word_count}')
    except FileNotFoundError:
        print(f'The file "{input_file}" does not exist.')


user_input = input("Enter text: ")  # Take user input
input_file = 'input.txt'  # Name of the input text file to be counted
output_file = 'word_count.txt'  # Name of the output text file to store the word count

with open(input_file, 'w') as file:
    file.write(user_input)

count_words_in_file(input_file, output_file)

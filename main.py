from stats import get_num_words
from stats import get_char_count
from stats import sort_characters

def get_book_text(file_path):
	with open(file_path, 'r', encoding='utf-8') as f:
		return f.read()

def main():
	print("============ BOOKBOT ============")
	print("Analyzing book found at books/frankenstein.txt...")

	book_text = get_book_text('books/frankenstein.txt')
	
	print("----------- Word Count ----------")
	counter = get_num_words(book_text)
	print(f"Found {counter} total words")
	
	print("----------- Word Count ----------")
	char_dict = get_char_count(book_text)
	sorted_chars = sort_characters(char_dict)
	for entry in sorted_chars:
        	print(f"{entry['char']}: {entry['num']}")

	print("============= END ===============")
main()

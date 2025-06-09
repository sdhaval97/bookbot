from stats import get_num_words

def get_book_text(file_path):
	with open(file_path, 'r', encoding='utf-8') as f:
		return f.read()

def main():
	book_text = get_book_text('books/frankenstein.txt')
	counter = get_num_words(book_text)
	print(f"{counter} words found in the document")

main()

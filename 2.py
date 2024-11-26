
def process_library_data(book_records):
    
    book_dict = {}

    for record in book_records:
    
        title, days = record.split(" - ")
        days = int(days)  
        
        if title in book_dict:
            book_dict[title] += days
        else:
            book_dict[title] = days

    most_borrowed = max(book_dict, key=book_dict.get)
    least_borrowed = min(book_dict, key=book_dict.get)

    
    total_days = sum(book_dict.values())
    average_days = total_days / len(book_dict)

    unique_titles = set(book_dict.keys())

    sorted_books = sorted(book_dict.items(), key=lambda x: x[1], reverse=True)

    print("Most Borrowed Book:", most_borrowed, "-", book_dict[most_borrowed], "days")
    print("Least Borrowed Book:", least_borrowed, "-", book_dict[least_borrowed], "days")
    print("Average Borrowing Days:", average_days)
    print("Unique Book Titles:", unique_titles)
    print("Books Sorted by Borrowing Days:", sorted_books)

book_records = [
    "Data structure - 10",
    "Web design - 5",
    "Python Basics - 7",
    "Machine Learning - 3",
    "Data structure - 4"
]

process_library_data(book_records)
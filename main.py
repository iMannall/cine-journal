
# Cine Journal
# Your Personal Cinematic Archive

library = []


def display_menu():
    print("\n" + "=" * 40)
    print("           CINE JOURNAL")
    print("     Your Personal Cinematic Archive")
    print("=" * 40)
    print("1. Add a movie or series")
    print("2. View my library")
    print("3. Search my library")
    print("4. View favorites")
    print("5. Exit")


def add_title():
    title = input("\nEnter the title: ").strip()

    if not title:
        print("Title cannot be empty.")
        return

    if any(item["title"].lower() == title.lower() for item in library):
        print("This title is already in your library.")
        return

    category = input("Type (Movie / Series / Anime): ").strip()
    status = input("Status (Watched / Watchlist): ").strip()

    try:
        rating = float(input("Your rating (0-10): "))
        if not 0 <= rating <= 10:
            print("Rating must be between 0 and 10.")
            return
    except ValueError:
        print("Please enter a valid number.")
        return

    library.append({
        "title": title,
        "category": category,
        "status": status,
        "rating": rating,
        "favorite": False
    })

    print(f"\n'{title}' has been added to your Cine Journal!")


def view_library():
    print("\nYOUR CINEMATIC LIBRARY")

    if not library:
        print("Your library is currently empty.")
        return

    for number, item in enumerate(library, start=1):
        favorite = " ♥" if item["favorite"] else ""
        print(
            f"{number}. {item['title']} | "
            f"{item['category']} | "
            f"{item['status']} | "
            f"Rating: {item['rating']}/10{favorite}"
        )


def search_library():
    query = input("\nSearch for a title: ").strip().lower()

    results = [
        item for item in library
        if query in item["title"].lower()
    ]

    if results:
        print("\nSEARCH RESULTS")
        for item in results:
            print(f"- {item['title']} ({item['category']})")
    else:
        print("No matching titles found.")


def view_favorites():
    favorites = [item for item in library if item["favorite"]]

    print("\nMY FAVORITES")

    if not favorites:
        print("You haven't added any favorites yet.")
        return

    for item in favorites:
        print(f"- {item['title']} | Rating: {item['rating']}/10")


def main():
    while True:
        display_menu()
        choice = input("\nChoose an option (1-5): ").strip()

        if choice == "1":
            add_title()

        elif choice == "2":
            view_library()

        elif choice == "3":
            search_library()

        elif choice == "4":
            view_favorites()

        elif choice == "5":
            print("\nThank you for visiting Cine Journal. Goodbye!")
            break

        else:
            print("\nInvalid choice. Please select from 1 to 5.")


if __name__ == "__main__":
    main()

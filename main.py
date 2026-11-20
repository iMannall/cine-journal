
# ==========================================
# CINE JOURNAL
# Your Personal Cinematic Archive
# ==========================================

import json
from pathlib import Path

DATA_FILE = Path(__file__).with_name("library.json")


def load_library():
    """Load saved titles from the JSON file."""
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []


library = load_library()


def save_library():
    """Save the current library to the JSON file."""
    with open(DATA_FILE, "w", encoding="utf-8") as file:
        json.dump(library, file, indent=4, ensure_ascii=False)


def display_menu():
    print("\n" + "=" * 42)
    print("              CINE JOURNAL")
    print("       Your Personal Cinematic Archive")
    print("=" * 42)
    print("1. Add a title")
    print("2. View my library")
    print("3. Search my library")
    print("4. View favorites")
    print("5. Mark a title as favorite")
    print("6. Remove a title")
    print("7. Exit")
    print("=" * 42)


def add_title():
    title = input("\nEnter the title: ").strip()

    if not title:
        print("Title cannot be empty.")
        return

    if any(item["title"].lower() == title.lower()
           for item in library):
        print("This title is already in your library.")
        return

    category = input(
        "Category (Movie / Series / Anime): "
    ).strip().title()

    if category not in ["Movie", "Series", "Anime"]:
        print("Please enter Movie, Series, or Anime.")
        return

    status = input(
        "Status (Watched / Watchlist): "
    ).strip().title()

    if status not in ["Watched", "Watchlist"]:
        print("Please enter Watched or Watchlist.")
        return

    try:
        rating = float(input("Your rating (0-10): "))

        if not 0 <= rating <= 10:
            print("Rating must be between 0 and 10.")
            return

    except ValueError:
        print("Please enter a valid number.")
        return

    new_title = {
        "title": title,
        "category": category,
        "status": status,
        "rating": rating,
        "favorite": False
    }

    library.append(new_title)
    save_library()

    print(f"\n'{title}' added successfully!")


def view_library():
    print("\nMY CINEMATIC LIBRARY")

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

    print(f"\nTotal titles: {len(library)}")


def search_library():
    query = input("\nSearch for a title: ").strip().lower()

    if not query:
        print("Please enter a search term.")
        return

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
    favorites = [
        item for item in library
        if item["favorite"]
    ]

    print("\nMY FAVORITES")

    if not favorites:
        print("You haven't added any favorites yet.")
        return

    for item in favorites:
        print(
            f"- {item['title']} | "
            f"Rating: {item['rating']}/10"
        )


def mark_favorite():
    title = input(
        "\nEnter the title to mark as favorite: "
    ).strip()

    for item in library:
        if item["title"].lower() == title.lower():
            item["favorite"] = not item["favorite"]
            save_library()

            if item["favorite"]:
                print(f"{title} added to favorites!")
            else:
                print(f"{title} removed from favorites!")

            return

    print("Title not found in your library.")


def remove_title():
    title = input(
        "\nEnter the title to remove: "
    ).strip()

    for item in library:
        if item["title"].lower() == title.lower():
            library.remove(item)
            save_library()
            print(f"{title} removed successfully!")
            return

    print("Title not found in your library.")


def main():
    print("\nWelcome back to Cine Journal!")

    while True:
        display_menu()

        choice = input("\nChoose an option (1-7): ").strip()

        if choice == "1":
            add_title()

        elif choice == "2":
            view_library()

        elif choice == "3":
            search_library()

        elif choice == "4":
            view_favorites()

        elif choice == "5":
            mark_favorite()

        elif choice == "6":
            remove_title()

        elif choice == "7":
            print("\nYour cinematic memories are saved.")
            print("Thank you for using Cine Journal!")
            break

        else:
            print("\nInvalid choice. Please select from 1 to 7.")


if __name__ == "__main__":
    main()

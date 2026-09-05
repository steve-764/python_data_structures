# Contact Book Program

Build a command-line contact book that stores each contact as an entry in a dictionary, where the key is the name and the value is the phone number. The program should keep running in a loop and show a menu until the user chooses to quit.

## What your program needs to do

1. Create an empty dictionary called something like `contacts = {}` before the loop starts.
2. Use a `while True` loop that prints a menu with 5 options: Add, Search, Delete, Print all, Quit.
3. Read the user's menu choice with `input()`, then use `if`/`elif` to run the matching action.
4. **Add a contact**: ask for a name and phone number, then store them as `contacts[name] = phone`.
5. **Search a contact**: ask for a name and check if it exists with `if name in contacts`. Print the number if found, otherwise print a friendly "not found" message.
6. **Delete a contact**: check it exists first, then remove it with `del contacts[name]` (avoid crashing on a missing name).
7. **Print all contacts**: loop over `contacts.items()` and print each name and number, one per line.
8. **Quit**: use `break` to exit the while loop cleanly when the user picks the quit option.

## Example dictionary shape

\`\`\`python
contacts = {
    "Amina": "0712345678",
    "Brian": "0798765432"
}
\`\`\`

## Stretch goal (optional, still in scope)

Once the basics work, try adding one or two of these — they only use dictionaries, loops, and string methods you already know:

- Prevent duplicate names: if the name already exists, ask the user to confirm before overwriting the number.
- Make search case-insensitive by comparing `name.lower()` against the stored keys.
- Add a "contact count" option that prints `len(contacts)`.
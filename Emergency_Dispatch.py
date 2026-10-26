# Exercise 1 - Emergency Dispatch Record Search

LAST_NAME = "Bautista"
STUDENT_ID = "TUPM-26-1271"
SEED_DIGIT = 1
ID_SUM = 19

FAVORITE_ARTIST = input("Enter your favorite artist: ")

NAME_LENGTH = len(LAST_NAME)
ARTIST_LENGTH = len(FAVORITE_ARTIST)

# Convert artist letters to A=1, B=2, ..., Z=26
ARTIST_SUM = 0

for letter in FAVORITE_ARTIST .upper():
    if letter.isalpha():
        ARTIST_SUM += ord(letter) - ord('A') + 1

print("\n--- STUDENT-SPECIFIC ---")
print("Last Name:", LAST_NAME)
print("Student ID:", STUDENT_ID)
print("Favorite Artist:", FAVORITE_ARTIST)
print("Seed Digit", SEED_DIGIT)
print("ID Sum:", ID_SUM)
print("Name Length:", NAME_LENGTH)
print("Artist Length:", ARTIST_LENGTH)
print("Artist Sum:", ARTIST_SUM)
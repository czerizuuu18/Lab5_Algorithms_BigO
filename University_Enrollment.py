# Exercise 2 - University Enrollment Records

LAST_NAME = "Bautista"
STUDENT_ID = "TUPM-26-1271"

SEED_DIGIT = 1
ID_SUM = 19

FAVORITE_ARTIST = input("Enter your favorite artist: ")

NAME_LENGTH = len(LAST_NAME)
ARTIST_LENGTH = len(FAVORITE_ARTIST)

print("\n--- STUDENT-SPECIFIC INPUTS ---")
print("Last Name:", LAST_NAME)
print("Student ID:", STUDENT_ID)
print("Seed Digit:", SEED_DIGIT)
print("ID Sum:", ID_SUM)
print("Name Length:", NAME_LENGTH)
print("Artist Length:", ARTIST_LENGTH)

# DATA GENERATION RULES

# Dataset A: ascending values using SEED_DIGIT and ID_SUM
DATASET_SIZE = 10

dataset_a = []

start_a = SEED_DIGIT + ID_SUM

for i in range(DATASET_SIZE):
    dataset_a.append(start_a + i)

# Dataset B: ascending values using ARTIST_LENGTH and NAME_LENGTH
dataset_b = []

start_b = ARTIST_LENGTH + NAME_LENGTH

for i in range(DATASET_SIZE):
    dataset_b.append(start_b + 1)

print("\n--- GENERATED DATASETS ---")
print("Department A dataset:", dataset_a)
print("Department B dataset:", dataset_b)
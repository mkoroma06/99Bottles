# Loop to print the song to 99 Bottles of Beer on the Wall

print("Sing with me!")
print()

beer = 99
while beer <= 99 and beer > 1:
    print(f"{beer} bottles of beer on the wall, {beer} bottles of beer.")
    print(f"Take one down and pass it around, {beer - 1} bottles on the wall")
    beer = beer - 1
    print()

while beer == 1:
    print("1 bottle of beer on the wall, 1 bottle of beer")
    print("Take one down and pass it around, no more bottles of beer on the wall")
    beer = beer - 1
    print()

print("No more bottles of beer on the wall, no more bottles of beer")
print("Go to the store and buy some more, 99 bottles of beer on the wall")

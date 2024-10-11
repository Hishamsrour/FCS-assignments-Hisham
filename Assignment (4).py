Words = "Is this the real life? Is this just fantasy? Caught in a landslide,no escape from reality Open your eyes, look up to the skies and see I'm just a poor boy, I need no sympathy Because I'm easy come, easy go, little high,little low Any way the wind blows doesn't really matter to me, to me Mama, just killed a man Put a gun against his head, pulled my trigger, now he's dead Mama, life had just begun But now I've gone and thrown it all away Mama, ooh, didn't mean to make you cry If I'm not back again this time tomorrow Carry on, carry on as if nothing really matters Too late, my time has come Sends shivers down my spine, body's aching all the time Goodbye, everybody, I've got to go Gotta leave you all behind and face the truth Mama, ooh (any way the wind blows) I don't wanna die I sometimes wish I'd never been born at all I see a little silhouetto of a man Scaramouche, Scaramouche, will you do the Fandango? Thunderbolt and lightning, very, very frightening me (Galileo) Galileo, (Galileo) Galileo, Galileo Figaro, magnifico But I'm just a poor boy, nobody loves me He's just a poor boy from a poor family Spare him his life from this monstrosity."

int1 = int(input("Enter the first integer value: "))
int2 = int(input("Enter the second integer value: "))

if int1 >= int2:
    print("Invalid input")
elif int1 >= len(Words) or int2 >= len(Words):
    print("Index out of range")
else:
    for index in range(int1, int2+1):
        print(Words[index],end="")    





 
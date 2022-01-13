def game():
    return 76

score=game()
with open("highscore.txt","r") as f:
    highscoreval=(f.read())

if highscoreval=="":
    with open("highscore.txt","w") as f:
        f.write(str(score))

elif int(highscoreval)<score:
    with open("highscore.txt","w") as f:
        f.write(str(score))

import turtle
import pandas as pd
from show_state import State
from score import Score

screen = turtle.Screen()
screen.title("U.S. States Game")
screen.setup(800,600)
image = "blank_states_img.gif"

screen.addshape(image)

turtle.shape(image)


""" process to generate data in 50_states.csv
def get_mouse_click_coor (x, y):
    print (x, y)


turtle.onscreenclick(get_mouse_click_coor )

screen.mainloop()
"""
score = Score()

data = pd.read_csv("50_states.csv")
df = pd.DataFrame(data)

state_list_raw = df["state"].to_list()
state_list = [] ##list(map(str.lower,state_list_raw))

for i in state_list_raw:
    i = i.lower()
    state_list.append(i)

df["state lower case"] = df["state"].str.lower()




def run (answer):
    #answer = screen.textinput(title = "GUESS A STATE", prompt = "Name Another State")
    s = df[df["state lower case"] == answer]
    #print (s)
    x = int(s["x"].to_list()[0])
    y = int(s["y"].to_list()[0])
    #print(answer, " " , x, " ", y)
    state = State(x, y , s["state"].to_list()[0])
    state.display()
    score.add_score()
 

game_on = True

while game_on:
    answer = str(screen.textinput(title = "GUESS A STATE", prompt = "Name Another State, enter 'exit' to exit game.")).lower()
    #print("answer :", answer)
    if answer == "exit":
        break

    elif answer in state_list:
        run(answer)

        
    else:
        screen.textinput(title = "GUESS A STATE", prompt = "No state found, name another state")




#screen.exitonclick()
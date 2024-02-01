import turtle
import pandas
screen = turtle.Screen()
image = "blank_state.gif"
screen.addshape(image)
turtle.shape(image)
data = pandas.read_csv("28_states.csv")
all_states = data.state.to_list()
guess_states = []
while len(guess_states) < 29:
    ans = screen.textinput(title = f"{len(guess_states)}/29" ,
                             prompt = "what is another state ?").title()
    if ans == "Exit":
        missing_state = []
        for state in all_states:
            if state not in guess_states:
                missing_state.append(state)
        print(missing_state)
        break
    if ans in all_states:
        guess_states.append(ans)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == ans]
        t.goto(float(state_data.x), float(state_data.y))
        t.write(ans)
    


screen.exitonclick()



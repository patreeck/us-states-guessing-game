import turtle
import pandas
data = pandas.read_csv("50_states.csv")

screen = turtle.Screen()
screen.title("U.S Turtle Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
correct_guess = []
while len(correct_guess) < 50:
    answer = (
        screen.textinput(title=f"Guess the State {len(correct_guess)}/50", prompt="Whats another state name? ").title())
    all_states = data.state.to_list()
    if answer == 'Exit':
        missing_state = [state for state in all_states if state not in correct_guess]
        new_data = pandas.DataFrame(missing_state)
        new_data.to_csv("states_to_learn.csv")
        break
    if answer in all_states:
        correct_guess.append(answer)
        t = turtle.Turtle()
        t.penup()
        t.hideturtle()
        state_data = data[data.state == answer]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer)


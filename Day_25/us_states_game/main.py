import turtle

import pandas

from Day_25.us_states_game.state_name_display import StateNameDisplay
from Day_25.us_states_game.states_data import StatesData

screen = turtle.Screen()
screen.title("US STATES GAME")

image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

correct_answers = []
states_data = StatesData()
states_list = states_data.states_list

while len(correct_answers) < 50:

    answer_state = screen.textinput(title=f"{len(correct_answers)}/50 States Correct", prompt="What's another state's name?").title()

    if answer_state == "Exit":
        content = pandas.DataFrame()
        for state in states_list:
            if state not in correct_answers:
                print(states_data.data[states_data.data.state == state])

        break

    if answer_state in states_list and answer_state not in correct_answers:
        correct_answers.append(answer_state)

        state_coords = states_data.get_state_coords(answer_state)
        state_name_display = StateNameDisplay()
        state_name_display.display_name(state_coords, answer_state)

turtle.mainloop()

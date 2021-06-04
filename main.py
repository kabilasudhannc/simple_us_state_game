import turtle
import pandas

my_screen = turtle.Screen()
my_screen.title('U.S. States Game')
image = 'blank_states_img.gif'
my_screen.addshape(image)
turtle.shape(image)

jim = turtle.Turtle()
jim.penup()
jim.hideturtle()

data = pandas.read_csv('50_states.csv')
states = data['state'].to_list()

is_game_on = True
guessed_state = []

while len(guessed_state) < 50:
    user_input = my_screen.textinput(title=f'{len(guessed_state)}/ 50 States Correct',
                                     prompt="What's the next state").title()

    if user_input == 'Exit':
        missed_states = {
            'missed_states': [state for state in states if state not in guessed_state],
        }
        data_f = pandas.DataFrame(missed_states)
        data_f.to_csv('states_to_learn.csv')
        break
    if user_input in states and user_input not in guessed_state:
        for state in states:
            if user_input == state:
                x = int(data[data.state == user_input].x)
                y = int(data[data.state == user_input].y)
                print(x, y)
                jim.goto(x, y)
                jim.write(state)
                guessed_state.append(state)

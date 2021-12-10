import PySimpleGUI as sg
import random

faces = 6

def main():

    sg.theme('DarkAmber')

    dice_dict = {}

    layout = [  [sg.Text('Welcome to Dice generator', key='-WELCOME-')],
                [sg.Text('What kind of dice do you want to roll?'), sg.Input(size=4, default_text='6', key='-FACES-')],
                [sg.Text('How many dice do you need to roll?'), sg.Input(size=5, key='-DICE-')],
                [sg.Button('Roll those dice !!!', key='-ROLL_DICE-')],
                [sg.Text('The results are:', visible=False, key='-RESULT_TEXT-')],
                [sg.Listbox(dice_dict, size=(15,6), visible=False, key='-RESULTS-')]
                ]

    window = sg.Window('Dice Generator', layout)

    while True:
        event, values = window.read()
        
        if event == sg.WIN_CLOSED:
            break
        
        if values['-DICE-'].isdecimal() and values['-FACES-'].isdecimal():
            list_dice = roll_dice(int(values['-FACES-']), int(values['-DICE-']))
            dice_dict = create_dice_dict(int(values['-FACES-']))

            for result in list_dice:
                dice_dict[result] = dice_dict[result] + 1

            result_list = []
            index = 1
            for index in range(len(dice_dict)):
                #result_list = index + ": " + dice_dict[index]
                print("" + str(index) + " " + str(dice_dict[index]))

            window['-RESULT_TEXT-'].update(visible=True)
            window['-RESULTS-'].update(values=result_list, visible=True)
            print(dice_dict)
            
        else:
            sg.popup('The inputs are incorrect')
            window['-DICE-'].update(value='')
            window['-FACES-'].update(value='')

    window.close()

def roll_dice(nb_sides, nb_dice):
    list_dice = []
    
    for i in range(nb_dice):
        list_dice.append(random.randint(1, nb_sides))

    return list_dice

def create_dice_dict(nb_sides):
    dice_dict={}
    for i in range(nb_sides):
        dice_dict[i + 1] = 0
    return dice_dict

if __name__ == "__main__":
    main()

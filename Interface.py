import PySimpleGUI as Pg
from PyCalculator import calculator as Calc

Pg.theme('DarkGrey3')
default_font = ('Arial', 12, 'bold')

number_key = ['btn_1', 'btn_2', 'btn_3', 'btn_4', 'btn_5', 'btn_6', 'btn_7', 'btn_8', 'btn_9']

# layout

columnB = [
    [Pg.Button(key='btn_sum', button_text='+', pad=(0, 0), size=(1, 1), font=default_font), Pg.Button(key='btn_sub', button_text='-', pad=(0, 0), expand_x=True, font=default_font)],
    [Pg.Button(key='btn_div', button_text='/', pad=(0, 0), size=(1, 1), font=default_font), Pg.Button(key='btn_mult', button_text='x', pad=(0, 0), expand_x=True, font=default_font)],
    [Pg.Button(key='btn_mod', button_text='%', pad=(0, 0), size=(1, 1), font=default_font), Pg.Button(key='btn_back', button_text='←', pad=(0, 0), expand_x=True, font=default_font)],
    [Pg.Button(key='btn_equal', button_text='=', pad=(0, 0), expand_x=True, font=default_font)]
]

columnA = [
    [Pg.Button(key='btn_7', button_text='7', pad=(0, 0), expand_x=True, font=default_font), Pg.Button(key='btn_8', button_text='8', pad=(0, 0), expand_x=True, font=default_font), Pg.Button(key='btn_9', button_text='9', pad=(0, 0), expand_x=True, font=default_font)],
    [Pg.Button(key='btn_4', button_text='4', pad=(0, 0), expand_x=True, font=default_font), Pg.Button(key='btn_5', button_text='5', pad=(0, 0), expand_x=True, font=default_font), Pg.Button(key='btn_6', button_text='6', pad=(0, 0), expand_x=True, font=default_font)],
    [Pg.Button(key='btn_1', button_text='1', pad=(0, 0), expand_x=True, font=default_font), Pg.Button(key='btn_2', button_text='2', pad=(0, 0), expand_x=True, font=default_font), Pg.Button(key='btn_3', button_text='3', pad=(0, 0), expand_x=True, font=default_font)],
    [Pg.Button(key='btn_0', button_text='0', pad=(0, 0), font=default_font, expand_x=True)]
]

main_layout = [
    # line 1
    [Pg.Text(key='Panel', font=default_font, text='', background_color='#a34a28', size=(1,1), expand_x=True, justification='right', auto_size_text=True)],
    # line 2
    [Pg.Column(columnA, element_justification='c'), Pg.Column(columnB, element_justification='c')]
]

# window

window = Pg.Window('Calculator', main_layout, return_keyboard_events=True)

# events

Panel_Text = ''


def identify_buttonEvent_Operators(event=''):
    global Panel_Text

    if Panel_Text != 'Error':
        if event == 'btn_sum' and len(Panel_Text) > 0:
            Panel_Text = Panel_Text + '+'
        if event == 'btn_sub' and len(Panel_Text) > 0:
            Panel_Text = Panel_Text + '-'
        if event == 'btn_mod' and len(Panel_Text) > 0:
            Panel_Text = Panel_Text + '%'
        if event == 'btn_div' and len(Panel_Text) > 0:
            Panel_Text = Panel_Text + '/'
        if event == 'btn_mult' and len(Panel_Text) > 0:
            Panel_Text = Panel_Text + 'x'


def identify_buttonEvent_Numbers(event=''):
    global Panel_Text

    if event in number_key and Panel_Text == 'Error':
        Panel_Text = ''

    if event == 'btn_0' and len(Panel_Text) > 0:
        Panel_Text = Panel_Text + '0'
    if event in number_key:
        Panel_Text = Panel_Text + window[event].get_text()


while True:
    event, value = window.read(timeout=5)

    window['Panel'].update(Panel_Text)
    if event == Pg.WINDOW_CLOSED or event == 'Escape:9':
        break

    identify_buttonEvent_Numbers(event)
    identify_buttonEvent_Operators(event)

    if event == 'btn_back' and len(Panel_Text) > 0:
        if Panel_Text == 'Error':
            Panel_Text = ''
        else:
            Panel_Text = Panel_Text[:-1]
    if event == 'btn_equal' and len(Panel_Text) > 0:
        try:
            result = Calc(Panel_Text)
            if result == 'False':
                Panel_Text = "Error"
            else:
                Panel_Text = str(result)
        except:
            Panel_Text = "Error"

window.close()

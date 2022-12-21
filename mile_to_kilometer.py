from tkinter import *


def miles_to_km():
    miles = float(miles_input.get())
    km = round(miles * 1)
    kilometer_result_label.config(text=f"{km}")


window = Tk()
window.title("Miles to Kilometer Converter")
window.config(padx=20, pady=20)
'''código para criar a janela onde o sistema vai rodar, já atribuindo o título e a distância interna
o pad(enchimento), para as partes do código'''

miles_input = Entry(width=7)
miles_input.grid(column=1, row=0)

miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)
'''quando é só uma palavra pra constar, usa-se label'''
is_equal_label = Label(text="is equal to")
is_equal_label.grid(column=0, row=1)
'''o método grid server para posicionar o item na grade da janela,é como se dividisse a tela em quadrados, como
um excel. Também tem métodos para a posição exata x e y e outra para arrumar de maneira automática'''
kilometer_result_label = Label(text="0")
kilometer_result_label.grid(column=1, row=1)

calculate_button = Button(text="Calculate", command=miles_to_km)
"""quando é para inserir um botão, usa-se Button, não se esquecer de usar o text ou dará erro. Passa-se
a função como atributo para quando o botão for pressionado"""
miles_to_km()
window.mainloop()

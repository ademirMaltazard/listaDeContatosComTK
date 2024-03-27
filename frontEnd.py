import tkinter
from tkinter import *
import main
import psycopg2

host = 'localhost'
db_name = 'teste'
user = 'postgres'
password = '1234'
sslmode = 'required'

str_conn = 'host={0} dbname={1} user={2} password={3}'.format(host, db_name, user, password)

conn = psycopg2.connect(str_conn)
cursor = conn.cursor()

window = tkinter.Tk()

white = "#fff"
black = "#000"
purple = "#6A5ACD"
yellow = "#F0E68C"
blue = "#00BFFF"
red = "#DC143C"

fontText = "ARIAL 12"
fontTitle = "MONTSERRAT 20"
fontLine = "Ivy 1"
fontDesc = "ARIAL 8"

loged_user = {str}

window.title('contatos')
window.geometry('720x640')
window.configure(background=(purple))
window.resizable(width=False, height=False)

frame_up = Frame(window, width=720, height=70, bg=yellow, relief='flat')
frame_up.grid(column=0, row=0, pady=1, padx=0, sticky=NSEW)
frame_down = Frame(window, width=320, height=400, bg=white)
frame_down.grid(column=0, row=1, pady=1, padx=0, sticky=NS)


def login():
    dbName = eName.get()
    dbPassword = ePassword.get()
    print(main.select(cursor))
    print(dbName)
    user_data = main.selectByName(cursor, dbName)
    print(password, user_data)
    if dbName == user_data[0][0] and dbPassword == user_data[0][1]:
        print('logado')
        loged_user = {
            'user': user_data[0][0],
            'password': user_data[0][1],
            'name': user_data[0][2],
            'access': user_data[0][3],
            'phone': user_data[0][4],
            'email': user_data[0][5]
        }
        print(loged_user)


def registration():
    print('registration')

def registrtion_page():
    #Altera o titulo e limpa o frame_down
    l_name = Label(frame_up, text="Registro", height=1, anchor='ne', font=fontTitle, bg=yellow, fg=black)
    l_name.place(x=200, y=5)
    frame_down = Frame(window, width=320, height=400, bg=white)
    frame_down.grid(column=0, row=1, pady=1, padx=0, sticky=NS)

    #insira usuario, nome, senha, acesso
    lSetUser = Label(frame_down, text='Insira um nome de usuario:', height=1, font=fontText, bg=white, fg=black)
    lSetUser.place(x=10, y=5)
    eSetUser = Entry(frame_down, width=15, justify="lef", font=("", 12), highlightthickness=1,
                      relief="solid")
    eSetUser.place(x=10, y=35)
    lSetName = Label(frame_down, text='Insira seu nome:', height=1, font=fontText, bg=white, fg=black)
    lSetName.place(x=10, y=65)
    eSetName = Entry(frame_down, width=15, justify="left", font=("", 12), highlightthickness=1,
                     relief="solid")
    eSetName.place(x=10, y=95)
    lSetPassword = Label(frame_down, text='Insira sua senha:', height=1, font=fontText, bg=white, fg=black)
    lSetPassword.place(x=10, y=125)
    eSetPassword = Entry(frame_down, width=15, justify="left", show="*", font=("", 12), highlightthickness=1,
                      relief="solid")
    eSetPassword.place(x=10, y=155)
    box = Checkbutton(frame_down,text="admin?", height=1, onvalue="public", offvalue="private")
    box.place(x=10, y=185)

    confirm_btn = Button(frame_down, width=20, height=1, bg=blue, fg=black, text="Cadastrar", command=registration)
    confirm_btn.place(x=75, y=225)





#configuraç~çao do frame up - titulo
frame_up = Frame(window, width=720, height=70, bg=yellow, relief='flat')
frame_up.grid(column=0, row=0, pady=1, padx=0, sticky=NSEW)
frame_down = Frame(window, width=320, height=400, bg=white)
frame_down.grid(column=0, row=1, pady=1, padx=0, sticky=NS)
l_name = Label(frame_up, text="LOGIN", height=1, anchor='ne', font=fontTitle, bg=yellow, fg=black)
l_name.place(x=200, y=5)
l_line = Label(frame_up, width=315, text="", height=1, anchor='center', font=fontLine, bg='#f54256')
l_line.place(x=200, y=45)



#configuração do frtame down - conteudo da tela
lName = Label(frame_down, text="Login:", height=1, font=fontText, bg=white, fg=black)
lName.place(x=10, y=5)
eName = Entry(frame_down, width=25, justify="center", font=("", 12), highlightthickness=1, relief="solid")
eName.place(x=10, y=35)
lPassword = Label(frame_down, text='Senha:', height=1, font=fontText, bg=white, fg=black)
lPassword.place(x=10, y=70)
ePassword = Entry(frame_down, width=25, justify="center", show="*", font=("", 12), highlightthickness=1, relief="solid")
ePassword.place(x=10, y=100)

recover = Button(frame_down, text='Esqueceu sua senha?', height=1, font=fontDesc, bg=white, fg=red, relief='flat')
recover.place(x=10, y=135)

confirm_btn = Button(frame_down, width=20, height=1, bg=blue, fg=black, text="Entrar", command=login)
confirm_btn.place(x=75, y=170)

txt = Label(frame_down, text="Não tem um conta?", height=1, font=fontDesc, bg=white, fg=red)
txt.place(x=10, y=225)
new_user = Button(frame_down, text='criar conta',width= 20, height=1, fg=black, bg=yellow, command=registrtion_page)
new_user.place(x=10, y=250)

matriz = main.select(cursor)
#print(matriz)
#main.update(conn, cursor, 'maltazard', ePassword)
#matriz = main.select(cursor)
print(matriz)
window.mainloop()
cursor.close()

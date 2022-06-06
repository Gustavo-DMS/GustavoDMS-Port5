import sqlite3
import tkinter as tk

con = sqlite3.connect("Hospital.db")
cur = con.cursor()

def DropTable():
    cur.execute("""DROP TABLE IF EXISTS pacientes""")
    cur.execute("""DROP TABLE IF EXISTS atendimento""")
    cur.execute("""DROP TABLE IF EXISTS atendimento_servico""")
    cur.execute("""DROP TABLE IF EXISTS servico""")

def CriarPacientes ():
    cur.execute("""CREATE TABLE pacientes (
    ID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    Nome TEXT NOT NULL,
    RG VARCHAR(9) NOT NULL,
    CPF VARCHAR(11) NOT NULL,
    Nasc DATE NOT NULL,
    Sexo CHAR NOT NULL
    );
    """)

def CriarAtendimento():
    cur.execute("""CREATE TABLE atendimento (
    ID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    Paciente_ID INT NOT NULL,
    Data_Atendimento TEXT NOT NULL,
    Peso FLOAT NOT NULL,
    Altura FLOAT NOT NULL,
    Descricao TEXT NOT NULL,
    Codigo_Manchester INT,
    FOREIGN KEY (Paciente_ID) REFERENCES pacientes(ID)
    );
    """)

def CriarAtendimento_Servico():
    cur.execute("""CREATE TABLE atendimento_servico (
    Atendimento_ID INTEGER NOT NULL ,
    Servico_ID INTEGER NOT NULL,
    Data DATE NOT NULL,
    Valor_do_servico FLOAT,
    Medicos_ID INT NOT NULL,
    FOREIGN KEY (Medicos_ID) REFERENCES medicos(ID),
    FOREIGN KEY (Atendimento_ID) REFERENCES atendimento(ID),
    FOREIGN KEY (Servico_ID) REFERENCES servico(ID),
    PRIMARY KEY (Atendimento_ID,Servico_ID,Data)
    );
    """)

def CriarServico():
    cur.execute("""CREATE TABLE servico (
    ID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    Codigo_TUSS VARCHAR(45) NOT NULL,
    Descricao VARCHAR(45) NOT NULL,
    Valor FLOAT NOT NULL,
    Tipo_servico_ID INTEGER NOT NULL,
    FOREIGN KEY (Tipo_Servico) REFERENCES tipo_servico(ID)
    );
    """)

def CriarMedicoEspecialidades():
    cur.execute("""CREATE TABLE medicos_especialidades (
    Medicos_ID INTEGER NOT NULL,
    Especialidades_ID INTEGER NOT NULL,   
    FOREIGN KEY (Especialidades_ID) REFERENCES especialidades(ID),
    FOREIGN KEY (Medicos_ID) REFERENCES medicos(ID) 
    );
    """)

def CriarMedicos():
    cur.execute("""CREATE TABLE medico(
    ID INTEGER NOT NULL PRIMARY KEY AUTOCREMENT,
    Nome VARCHAR(100) NOT NULL,
    CRM VARCHAR(10)
    );
    """)

def CriarEspecialidades():
    cur.execute("""CREATE TABLE especialidades (
    ID INTEGER NOT NULL PRIMARY KEY AUTOCREMENT,
    Nome VARCHAR(45) NOT NULL,
    CID10_CAT VARCHAR(8) NOT NULL
    );
    """)
def AdicionarPacientes(nome,rg,cpf,nasc,sexo):
    cur.execute(""" INSERT INTO pacientes (nome,rg,cpf,nasc,sexo)
    VALUES (?,?,?,?,?)""",(nome,rg,cpf,nasc,sexo))
    con.commit()

def AdicionarAtendimentos(id_pac,data_at,peso,altura,desc,Manchester):
    cur.execute(""" INSERT INTO atendimento (Paciente_ID,Data_Atendimento,Peso,Altura,Descricao,Codigo_Manchester) 
    VALUES (?,?,?,?,?,?)""",(id_pac,data_at,peso,altura,desc,Manchester))
    con.commit()

def AdicionarAtendimentos_servico(at_id,serv_Id,data):
    cur.execute(""" INSERT INTO atendimento_servico (Atendimento_ID,Servico_ID,Data) 
    VALUES (?,?,?)""",(at_id,serv_Id,data))
    cur.execute("""UPDATE atendimento_servico 
    SET Valor_do_servico = (SELECT servico.Valor FROM servico WHERE servico.ID = atendimento_servico.Servico_ID)
    WHERE Atendimento_ID = ?
    AND Servico_ID = ?
    AND Data = (?);""",(at_id,serv_Id,data))
    con.commit()

def AdicionarServico(TUSS,Desc,Valor):
    cur.execute(""" INSERT INTO servico (Codigo_TUSS,Descricao,Valor) 
    VALUES (?,?,?)""",(TUSS,Desc,Valor))
    con.commit()

def LerTabela():
    print('Atendimentos -------------------------')
    cur.execute("""SELECT * FROM atendimento; """)
    for linha in cur.fetchall():
        print(linha)
    print('pacientes --------------------')
    cur.execute("""SELECT * FROM pacientes; """)
    for linha in cur.fetchall():
        print(linha)
    print('atendimento servico -----------------------')
    cur.execute("""SELECT * FROM atendimento_servico; """)
    for linha in cur.fetchall():
        print(linha)
    print('servico-------------------------------------')
    cur.execute("""SELECT * FROM servico; """)
    for linha in cur.fetchall():
        print(linha)

def ProduzirDados():
    DropTable()
    CriarAtendimento()
    CriarServico()
    CriarAtendimento_Servico()
    CriarPacientes()
    AdicionarPacientes('Regis','000000000','00000000000','1995-09-01','M')
    AdicionarPacientes('Aloisio','111111111','11111111111','1935-10-05','M')
    AdicionarPacientes('Bruna','222222222','22222222222','2001-06-22','F')
    AdicionarPacientes('Wladi','333333333','33333333333','1966-12-03','M')
    AdicionarAtendimentos(1,'2015-05-22',80,1.75,'O paciente fez xyz',1)
    AdicionarAtendimentos(1,'2019-10-26',90,1.80,'O paciente fez xyz',2)
    AdicionarAtendimentos(2,'2015-10-06',75,1.77,'O paciente fez xyz',2)
    AdicionarAtendimentos(3,'2018-19-06',65,1.65,'O paciente fez xyz',5)
    AdicionarAtendimentos(3,'2019-10-26',75,1.70,'O paciente fez xyz',3)
    AdicionarAtendimentos(4,'2020-10-26',75,1.70,'O paciente fez xyz',3)
    AdicionarAtendimentos(4,'2019-10-26',75,1.70,'O paciente fez xyz',2)
    AdicionarAtendimentos(4,'2019-10-26',75,1.70,'O paciente fez xyz',1)
    AdicionarServico(30310040,'Cirurgias fistulizantes com implantes valvulares',10)
    AdicionarServico(30213037,'Istmectomia ou nodulectomia - tireoide',100)
    AdicionarServico(30207045,'Redução de fratura de seio frontal',1000)
    AdicionarServico(30101875, 'Tratamento de escaras ou ulcerações com retalhos cutâneos locais',10000)
    AdicionarAtendimentos_servico(1,1,'2015-05-22') #m
    AdicionarAtendimentos_servico(1,2,'2015-05-22') #M
    AdicionarAtendimentos_servico(3,1,'2015-05-22') #m
    AdicionarAtendimentos_servico(4,4,'2019-05-22') #f
    AdicionarAtendimentos_servico(5,4,'2015-05-22') #f
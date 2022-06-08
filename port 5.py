import sqlite3
import tkinter as tk

con = sqlite3.connect("Hospital.db")
cur = con.cursor()

def DropTable():
    cur.execute("""DROP TABLE IF EXISTS pacientes""")
    cur.execute("""DROP TABLE IF EXISTS atendimento""")
    cur.execute("""DROP TABLE IF EXISTS atendimento_servico""")
    cur.execute("""DROP TABLE IF EXISTS servico""")
    cur.execute("""DROP TABLE IF EXISTS medicos_especialidades""")
    cur.execute("""DROP TABLE IF EXISTS medicos""")
    cur.execute("""DROP TABLE IF EXISTS especialidades""")
    cur.execute("""DROP TABLE IF EXISTS servicos_especialidades""")
    cur.execute("""DROP TABLE IF EXISTS tipo_servico""")
    cur.execute("""DROP TABLE IF EXISTS frequencias""")

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
    FOREIGN KEY (Tipo_servico_ID) REFERENCES tipo_servico(ID)
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
    cur.execute("""CREATE TABLE medicos(
    ID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    Nome VARCHAR(100) NOT NULL,
    CRM VARCHAR(10)
    );
    """)

def CriarEspecialidades():
    cur.execute("""CREATE TABLE especialidades (
    ID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    Nome VARCHAR(45) NOT NULL,
    CID10_CAT VARCHAR(8) NOT NULL
    );
    """)

def CriarServicosEspecialidades():
    cur.execute("""CREATE TABLE servicos_especialidades (
    Servico_ID INTEGER NOT NULL,
    Especialidades_ID INTEGER NOT NULL,
    FOREIGN KEY (Servico_ID) REFERENCES servico(ID),
    FOREIGN KEY (Especialidades_ID) REFERENCES especialidades(ID),
    PRIMARY KEY (Servico_ID,Especialidades_ID)
    );
    """)

def CriarFrequencias():
    cur.execute("""CREATE TABLE frequencias (
    Servico_ID int NOT NULL PRIMARY KEY,
    Sexo VARCHAR(1),
    QtdePeriodo INTEGER NOT NULL,
    PeriodoMeses INTEGER NOT NULL,
    IdadeMin INTEGER NOT NULL,
    IdadeMax INTEGER NOT NULL
    );
    """)

def CriarTipoServico():
    cur.execute("""CREATE TABLE tipo_servico (
    ID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    Tipo_Servico VARCHAR(45)
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

def AdicionarTipoServico(tipo_serv):
    cur.execute("""INSERT INTO tipo_servico (Tipo_servico) 
    VALUES (?);""",(tipo_serv,))
    con.commit()

def AdicionarAtendimentos_servico(at_id,serv_Id,data,med_id):
    cur.execute(""" INSERT INTO atendimento_servico (Atendimento_ID,Servico_ID,Data,Medicos_id) 
    VALUES (?,?,?,?)""",(at_id,serv_Id,data,med_id))
    cur.execute("""UPDATE atendimento_servico 
    SET Valor_do_servico = (SELECT servico.Valor FROM servico WHERE servico.ID = atendimento_servico.Servico_ID)
    WHERE Atendimento_ID = ?
    AND Servico_ID = ?
    AND Data = (?);""",(at_id,serv_Id,data))
    con.commit()

def AdicionarServico(TUSS,Desc,Valor,tipo_serv):
    cur.execute(""" INSERT INTO servico (Codigo_TUSS,Descricao,Valor,Tipo_servico_ID) 
    VALUES (?,?,?,?)""",(TUSS,Desc,Valor,tipo_serv))
    con.commit()

def AdicionarEspecialidade(nome,cid):
    cur.execute("""INSERT INTO especialidades (nome,CID10_CAT) 
    VALUES (?,?)""",(nome,cid))
    con.commit()

def AdicionarMedicos(nome,crm):
    cur.execute("""INSERT INTO medicos (Nome,CRM)
    VALUES (?,?)""",(nome,crm,))
    con.commit()

def AdicionarMedicoespecialidades(med_id,esp_id):
    cur.execute("""INSERT INTO medicos_especialidades (Medicos_ID,Especialidades_ID) 
    VALUES (?,?)""",(med_id,esp_id,))
    con.commit()

def AdicionarServicosEspecialidades(serv_Id,esp_id):
    cur.execute("""INSERT INTO servicos_especialidades (Servico_ID,Especialidades_ID)
    VALUES (?,?)""",(serv_Id,esp_id,))
    con.commit()

def AdicionarFrequencias(serv_Id,sexo,Qtd_per,periodo_mes,Idade_min,Idade_max):
    cur.execute("""INSERT INTO frequencias (Servico_ID,Sexo,QtdePeriodo,PeriodoMeses,IdadeMin,IdadeMax)
    VALUES (?,?,?,?,?,?)""",(serv_Id,sexo,Qtd_per,periodo_mes,Idade_min,Idade_max,))

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
    print('medicos_especialidades-------------------------------------')
    cur.execute("""SELECT * FROM medicos_especialidades; """)
    for linha in cur.fetchall():
        print(linha)
    print('medicos-------------------------------------')
    cur.execute("""SELECT * FROM medicos; """)
    for linha in cur.fetchall():
        print(linha)
    print('especialidades-------------------------------------')
    cur.execute("""SELECT * FROM especialidades; """)
    for linha in cur.fetchall():
        print(linha)
    print('servicos_especialidades-------------------------------------')
    cur.execute("""SELECT * FROM servicos_especialidades; """)
    for linha in cur.fetchall():
        print(linha)
    print('tipo_servicos-------------------------------------')
    cur.execute("""SELECT * FROM tipo_servico; """)
    for linha in cur.fetchall():
        print(linha)
    print('frequencias-------------------------------------')
    cur.execute("""SELECT * FROM frequencias; """)
    for linha in cur.fetchall():
        print(linha)

def ProduzirDados():
    DropTable()
    CriarAtendimento()
    CriarServico()
    CriarAtendimento_Servico()
    CriarPacientes()
    CriarMedicoEspecialidades()
    CriarMedicos()
    CriarEspecialidades()
    CriarServicosEspecialidades()
    CriarTipoServico()
    CriarFrequencias()
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
    AdicionarTipoServico('Exames de Diagnósticos Por Imagem')
    AdicionarTipoServico('Exames de Sangue')
    AdicionarTipoServico('Cirurgia de Alta Complexidade')
    AdicionarTipoServico('Consulta Médica')
    AdicionarTipoServico('Terapias')
    AdicionarServico(30310040,'Cirurgias fistulizantes com implantes valvulares',10,1)
    AdicionarServico(30213037,'Istmectomia ou nodulectomia - tireoide',100,2)
    AdicionarServico(30207045,'Redução de fratura de seio frontal',1000,3)
    AdicionarServico(30101875, 'Tratamento de escaras ou ulcerações com retalhos cutâneos locais',10000,3)
    AdicionarServico(20101074,'Avaliacao nutricional inclui consulta',500.50,5)
    AdicionarServico(30203023,'Tumor de lingua tratamento cirurgico',1500.25,1)
    AdicionarServico(30718015,'Amputacao ao nivel do braco tratamento cirurgico',1030.0,2)
    AdicionarEspecialidade('pediatria',1)
    AdicionarEspecialidade('Radiologia',2)
    AdicionarEspecialidade('Oncologia',3)
    AdicionarEspecialidade('Dermatologia',4)
    AdicionarMedicos('Walter',468754)
    AdicionarMedicos('Marcos',4463546)
    AdicionarMedicos('Roberto',45621676)
    AdicionarMedicos('Jandir Biroliro',6621615)
    AdicionarMedicoespecialidades(1,1)
    AdicionarMedicoespecialidades(1,2)
    AdicionarMedicoespecialidades(2,2)
    AdicionarMedicoespecialidades(3,3)
    AdicionarMedicoespecialidades(4,4)
    AdicionarServicosEspecialidades(1,1)
    AdicionarServicosEspecialidades(2,2)
    AdicionarServicosEspecialidades(3,3)
    AdicionarServicosEspecialidades(4,4)
    AdicionarServicosEspecialidades(5,1)
    AdicionarServicosEspecialidades(6,2)
    AdicionarFrequencias(1,'M',1,1500,15,30)
    AdicionarFrequencias(2,'M',1,30,1,10)
    AdicionarFrequencias(3,'A',1,1,0,120)
    AdicionarFrequencias(4,'F',1,10,30,80)
    AdicionarFrequencias(5,'F',1,50,12,30)
    AdicionarFrequencias(6,'A',1,0,100,900)
    AdicionarFrequencias(7,'M',1,5,5,120)
    AdicionarAtendimentos_servico(1,1,'2015-05-22',1) #m
    AdicionarAtendimentos_servico(2,3,'2015-05-22',3) #M
    AdicionarAtendimentos_servico(3,3,'2015-05-22',3) #m alosio ERRADO SEXO
    AdicionarAtendimentos_servico(4,4,'2019-05-22',4) #f bruna 
    AdicionarAtendimentos_servico(5,7,'2019-05-22',1) #f bruna ERRADO SEXO
    AdicionarAtendimentos_servico(7,5,'2015-05-22',4) #m wladi ERRADO ESP
    # LerTabela()

def FaltaRelação():
    cur.execute("""SELECT servico.ID 
    FROM servico LEFT JOIN servicos_especialidades
    ON servicos_especialidades.Servico_ID = servico.ID
    WHERE servicos_especialidades.Servico_ID is null """)
    print(cur.fetchall())

def ContServico():
    cur.execute("""SELECT COUNT(Servico_ID),servico.ID 
    FROM servico LEFT JOIN atendimento_servico
    ON servico.ID = atendimento_servico.Servico_ID
    GROUP BY (servico.ID) """)
    print(cur.fetchall())

def OverServico():
    cur.execute("""SELECT pacientes.Nome
    FROM pacientes INNER JOIN atendimento ON pacientes.ID = atendimento.Paciente_ID
    INNER JOIN atendimento_servico ON atendimento.ID = atendimento_servico.Atendimento_ID
    INNER JOIN servico ON servico.ID = atendimento_servico.Servico_ID
    INNER JOIN frequencias ON servico.ID = frequencias.Servico_ID
    WHERE frequencias.PeriodoMeses = 1500
    GROUP BY servico.ID
    HAVING COUNT(frequencias.Servico_ID) > 1    
    ;
    """)
    print(cur.fetchall())

def IncompatibilidadeSexo():
    cur.execute("""SELECT servico.ID,pacientes.Nome,pacientes.sexo,frequencias.sexo
    FROM pacientes INNER JOIN atendimento ON pacientes.ID = atendimento.Paciente_ID
    INNER JOIN atendimento_servico ON atendimento.ID = atendimento_servico.Atendimento_ID
    INNER JOIN servico ON servico.ID = atendimento_servico.Servico_ID
    INNER JOIN frequencias ON servico.ID = frequencias.Servico_ID
    WHERE frequencias.sexo <> pacientes.sexo AND frequencias.sexo <> 'A' """)
    print(cur.fetchall())

def ErroEspecialidade():
    cur.execute("""SELECT servico.ID,especialidades.Nome,MedEsp.Nome,medicos.nome
    FROM pacientes INNER JOIN atendimento ON pacientes.ID = atendimento.Paciente_ID
    INNER JOIN atendimento_servico ON atendimento.ID = atendimento_servico.Atendimento_ID
    INNER JOIN servico ON servico.ID = atendimento_servico.Servico_ID
    INNER JOIN servicos_especialidades ON servicos_especialidades.Servico_ID = servico.ID
    INNER JOIN especialidades ON servicos_especialidades.Especialidades_ID = especialidades.ID
    INNER JOIN medicos ON atendimento_servico.Medicos_ID = medicos.ID
    INNER JOIN medicos_especialidades ON medicos_especialidades.Medicos_ID = medicos.ID
    INNER JOIN especialidades as MedEsp on MedEsp.ID = medicos_especialidades.Especialidades_ID
    WHERE medicos_especialidades.Especialidades_ID NOT IN (servicos_especialidades.Especialidades_ID)
    """)
    print(cur.fetchall())

def main():
    # ProduzirDados()
    # LerTabela()
    # FaltaRelação()
    # ContServico()
    # OverServico()
    # IncompatibilidadeSexo()
    ErroEspecialidade()

main()
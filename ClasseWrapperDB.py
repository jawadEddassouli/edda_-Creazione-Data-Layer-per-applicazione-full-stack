#classe wrapper
#i più ci sono funzioni di connessione e di disconnessione
#le variabili di istanza sono le 4 variabili per la connessione
#invece la connessione è una variabile di classe 

#importo il modulo 
import pymssql

class WrapperDB:
    
    conn = 0
    
    #def __init__(self, server="192.168.40.16\\SQLEXPRESS", user="CRD2122", \
    def __init__(self, server="213.140.22.237\\SQLEXPRESS", user="CRD2122", \
               password="xxx123##", database="CRD2122"):
        self._server=server
        self._user=user
        self._password=password
        self._database=database
        
        
    def connessione(self):
	
        try:
            WrapperDB.conn = pymssql.connect(server = self._server, user = self._user, \
                        password = self._password, database = self._database)
            print("\nConnessione effettuata DB CRD2122!\n")
            return WrapperDB.conn	

        except:
            print("\nConnessione NON riuscita DB CRD2122!\n")
            return 0
        
            
    def disconnessione(self, co):
	
        try:
            co.close()
            print("\nCHIUSURA Connessione effettuata DB CRD2122!\n")
            
        except:
            print("\nCHIUSURA Connessione NON riuscita DB CRD2122!\n")
            return 0
        

    def visua(self):
        c = self.connessione()
        lista = []
        try:
            cur = c.cursor()
            istru = " select * from ACG_Persons "
            cur.execute(istru)
            lista = cur.fetchall()
            print("\nSELECT effettuata su DB CRD2122!\n")
        except:
            print("\nProblemi SELECT su DB CRD2122!\n")
        self.disconnessione(c)
        return lista

    def visuaMD(self):
        # UGUALE A visua, MA con lista di righe-dizionario, anziche 
        #	lista righe-tuple (CURSORE CREATO CON as_dict = True)
        c = self.connessione()
        lista = []
        try:
            cur = c.cursor(as_dict = True)
            istru = " select * from ACG_Persons "
            cur.execute(istru)
            lista = cur.fetchall()
            print("\nSELECT effettuata su DB CRD2122!\n")
        except:
            print("\nProblemi SELECT su DB CRD2122!\n")
        self.disconnessione(c)
        return lista
    
    def visuaParametrica(self, eta):
        c = self.connessione()
        lista = []
        try:
            cur = c.cursor()
            print("\nVisua cogn, nome e temperature delle pers. con una specifica eta' \n")
            istru = """
                select P.lastname , P.firstname , T.* 
                from ACG_Temperature1 AS T 
                join ACG_Persons AS P 
                on P.ID = T.IDPerson 
                WHERE P.age = %d   
                """
            cur.execute(istru,(eta))
            lista = cur.fetchall()
            print("\nSELECT effettuata su DB CRD2122!\n")
        except:
            print("\nProblemi SELECT su DB CRD2122!\n")
        self.disconnessione(c)
        return lista
    
    def creaSchemaTabella(self):
        # ACG_Temperature1(ID, dat, ora, minuti, temperatura, IDPerson)
        ok = 1
        c = self.connessione()
        try:
            ope = """
                IF NOT EXISTS ( 
                    Select * 
                     from sysobjects 
                     where xtype = 'U' and name = 'ACG_Temperature1' 
                    )
                CREATE TABLE ACG_Temperature1 (
                ID INT IDENTITY ( 1 , 1 ) NOT NULL , 
                DATAT VARCHAR ( 10 ) NOT NULL ,
                ORA INT NOT NULL ,
                MINUTI INT NOT NULL ,
                TEMPERATURA DECIMAL ( 5 , 2 ) NOT NULL ,
                IDPerson INT NOT NULL ,
                PRIMARY KEY ( ID ),
                FOREIGN KEY ( IDPerson ) REFERENCES ACG_PERSONS ( ID )
                     ON DELETE CASCADE 
                )          
                    """
            cursore= c.cursor()
            cursore.execute(ope)
            c.commit()
            print("\nCREATE effettuata (o la tabella esiste) su DB CRD2122!\n")
        
        except pymssql._mssql.MSSQLException as e:
            print("A MSSQLDatabaseException has been caught.")
            print('Number = ',e.number)
            print('Severity = ',e.severity)
            print('State = ',e.state)
            print('Message = ',e.message)  
            ok = 0
            
        """
        except pymssql._mssql.MssqlDatabaseException as e:
            print("A MSSQLDatabaseException has been caught.")
            print('Number = ',e.number)
            print('Severity = ',e.severity)
            print('State = ',e.state)
            print('Message = ',e.message)  
            ok = 0
        
        except pymssql._mssql.MssqlDriverException:
            print("A MSSQLDriverException has been caught.")
            ok = 0
        """
        """
        except pymssql.OperationalError as oe:
            print("\nOperationalError in CREATE su DB CRD2122!\n")
            print("number = " + str(oe.number) + "   severity=" + str(oe.severity) +"\n")
            ok = 0
        except pymssql.InternalError as ie:
            print("\nInternalError in CREATE su DB CRD2122!\n")
            ok = 0
        except pymssql.ProgrammingInternalError as pe:
            print("\nProgramminglError in CREATE su DB CRD2122!\n")
            ok = 0
        
        except:
            print("\nPROBLEMI CREATE effettuata su DB CRD2122\n")
            ok = 0
        """
        self.disconnessione(c)
        return ok
        
    
    def inserimenti(self, parametro):
        try:
            # Connessione
            #WrapperDB.conn = self.connetti() 
            c = self.connessione() 
            cursore = c.cursor()
            # NB %d anche per i DECIMAL!!!!!!!
            
            insertParametrica = " INSERT INTO ACG_Temperature1 VALUES (%s , %d , %d , %d, %d  ) "
            print(parametro)
            if  isinstance(parametro, tuple)  : # UNA sola riga
                print("E' UNA TUPLA")
                
                cursore.execute(insertParametrica, parametro)
                c.commit()
                print("INSERIMENTO RIGA AVVENUTO", parametro)
                self.disconnessione(c)
                return "OK"
            elif  isinstance(parametro, list)    : # piu righe
                print("E' UNA LISTA")
                cursore.executemany(insertParametrica, parametro)
                c.commit()
                print("INSERIMENTO RIGHE AVVENUTO", parametro)
                self.disconnessione(c)
                return "OK"
            else:
                # Disconnessione
                self.disconnessione(c)
                return "KO parametro"
            
        except:
            print("\nPROC Inserimento/i: PROBLEMA !")
            self.disconnessione(c)
            return "KO"
        
        
    
    def listaTabelle(self):
        pass
    
    def listaTabelleUtente(self):
        #
        c = self.connessione()
        lista = []
        try:
            cur = c.cursor(as_dict = True)
            istru = """
                select * from sysobjects  
                WHERE xtype = 'U'  
                """
            cur.execute(istru)
            lista = cur.fetchall()
            print("\nSELECT effettuata su DB CRD2122!\n")
        except:
            print("\nProblemi SELECT su DB CRD2122!\n")
        self.disconnessione(c)
        return lista
    
    def listaNomiTabelleUtente(self):
        #
        c = self.connessione()
        lista = []
        try:
            cur = c.cursor()
            istru = """
                select name from sysobjects  
                WHERE xtype = 'U'  
                order by name
                """
            cur.execute(istru)
            lista = cur.fetchall()
            print("\nSELECT effettuata su DB CRD2122!\n")
        except:
            print("\nProblemi SELECT su DB CRD2122!\n")
        self.disconnessione(c)
        return lista
    
    
    def listaCampiDiSysobjects(self):
        #
        c = self.connessione()
        lista = []
        try:
            cur = c.cursor(as_dict = True)
            istru = " select * from sysobjects "
            cur.execute(istru)
            listarighe = cur.fetchall()
            print("\nSELECT effettuata su DB CRD2122!\n")
            for k in listarighe[0]:
                lista.append(k)
        except:
            print("\nProblemi SELECT su DB CRD2122!\n")
        self.disconnessione(c)
        return lista
    
    
    def listaTipiDiSysobjects(self):
        #
        c = self.connessione()
        lista = []
        try:
            cur = c.cursor()
            istru = """ 
                select DISTINCT xtype from sysobjects  
               
                """
            cur.execute(istru)
            lista = cur.fetchall()
            print("\nSELECT effettuata su DB CRD2122!\n")
        except:
            print("\nProblemi SELECT su DB CRD2122!\n")
        self.disconnessione(c)
        return lista
    
    

	    
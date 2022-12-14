"""
Analizador Lexico
"""
import SubTipoToken
import TipoToken
import Token


class AnalizadorLexico:
    
    numLinea=1
    L=[]
    codigo=""
    palabras_reservadas=["FinMientras","Para","FinPara","Hasta","Con","Paso", "Verdadero","Leer","Escribir",
            "Si","Entonces","Sino","FinSi","Segun", "Regresar","Entero", "Repetir",
            "Real","Logico","Caracter","Falso","Hacer","Romper","Omision","Que",
            "FinSegun","Mientras", "Proceso","FinProceso","Funcion","FinFuncion"]
    

    def __init__(self,programa):
        
        archivo = open(programa, 'r') 
        lineas = archivo.readlines() 
        for linea in lineas: 
            self.codigo=self.codigo+linea
               
    
    def obtenerToken(self):
        
        if len(self.L)>0:
            return self.L.pop(0)
        
        return None
    
    def regresarToken(self,t):
        
        self.L.insert(0,t)

    def pruebas(c,numE,numR,index):
        print("c",c)
        print("numE y numR",numE,numR)
        print("index ",index)
        exit(0)   
    
    def esPalabraReservada(self,lexema):
        
        for i in self.palabras_reservadas:
            if lexema==i:
                return Token.Token(TipoToken.PALABRA_RESERVADA,lexema,lexema,self.numLinea)  
        return Token.Token(TipoToken.IDENTIFICADOR,SubTipoToken.NINGUNO,lexema,self.numLinea)  
            
    
    def crearLista(self):
        
        index=0
        nombreIden=""
        numero=""
        c=self.codigo[index]
        while (index<len(self.codigo)):
            c=self.codigo[index]

            if c.isspace():   # automata que detecta espacios
                if c=="\n":
                    self.numLinea=self.numLinea+1  
                    
                    
                index=index+1
                f=True
                while(index < len(self.codigo) and f):
                    c=self.codigo[index]
                    if(c.isspace()):
                        if c=="\n":
                            self.numLinea=self.numLinea+1 
                        index=index+1
                    else:
                        f=False

            elif c=="-" or c=="+" or c=="/" or c=="*" or c=="%":   #automata operadores aritmeticos 
                if c == "-":                   
                    t=Token.Token(TipoToken.OPERADOR_ARITMETICO,SubTipoToken.OPERADOR_RESTA,"-",self.numLinea)
                    self.L.append(t)
                if c == "+":                   
                    t=Token.Token(TipoToken.OPERADOR_ARITMETICO,SubTipoToken.OPERADOR_SUMA,"+",self.numLinea)
                    self.L.append(t)                    
                if c == "*":                   
                    t=Token.Token(TipoToken.OPERADOR_ARITMETICO,SubTipoToken.OPERADOR_MULTIPLICACION,"*",self.numLinea)
                    self.L.append(t)
                if c == "/":  # division o comentarios # create BY Elias silva
                    index = index + 1
                    if(index < len(self.codigo)):
                        c = self.codigo[index]
                        if (c == "/" or c == "*"):   # ENTRAN COMENTARIOS 
                            if (c == "/" ):
                                index = index + 1
                                while(index < len(self.codigo) and c != "\n"):
                                    c = self.codigo[index]
                                    if  c != "\n":
                                        index = index + 1
                            else:
                                c = self.codigo[index]
                                index = index + 1
                                if(index < len(self.codigo)):
                                    c = self.codigo[index]
                                    bandera = 0
                                    while(bandera ==0 and index < len(self.codigo)): 
                                        if c.isspace():
                                            if c=="\n":
                                                self.numLinea = self.numLinea + 1
                                        if c == "*":
                                            index = index + 1
                                            if(index < len(self.codigo)):        
                                                c = self.codigo[index]
                                                if c == "/":
                                                    bandera = 1
                                                    break
                                        index = index +1 
                                        if(index < len(self.codigo)):
                                            c = self.codigo[index]
                                    if   bandera == 0:
                                        print("En la linea ",self.numLinea,"no se cerro el comentario de bloque")                 
                        else:       
                            t=Token.Token(TipoToken.OPERADOR_ARITMETICO,SubTipoToken.OPERADOR_DIVISION,"/",self.numLinea)
                            self.L.append(t)
                if c == "%":                   
                    t=Token.Token(TipoToken.OPERADOR_ARITMETICO,SubTipoToken.OPERADOR_MODULO,"*",self.numLinea)
                    self.L.append(t)                                  
                index=index+1



            elif c==">" or c=="<":
                if c == ">":
                    index=index+1
                    if(index < len(self.codigo)):
                        c=self.codigo[index]
                        if c == "=":
                            index = index + 1
                            t=Token.Token(TipoToken.OPERADOR_RELACIONAL,SubTipoToken.OPERADOR_MAYOR_IGUAL,">=",self.numLinea)
                            self.L.append(t)
                        else:
                            t=Token.Token(TipoToken.OPERADOR_RELACIONAL,SubTipoToken.OPERADOR_MAYOR,">",self.numLinea)
                            self.L.append(t)
                    else:
                       print("Fin de archivo")          
                else:
                    index=index+1
                    if(index < len(self.codigo)):
                        c=self.codigo[index]
                        if c == "=":
                            t=Token.Token(TipoToken.OPERADOR_RELACIONAL,SubTipoToken.OPERADOR_MENOR_IGUAL,"<=",self.numLinea)
                            self.L.append(t)
                            index=index+1
                        else:
                            t=Token.Token(TipoToken.OPERADOR_RELACIONAL,SubTipoToken.OPERADOR_MENOR,"<",self.numLinea)
                            self.L.append(t)
                    else:       
                        print("Fin de archivo") 
            elif c == "(" or c == ")":
                if c== "(":
                    t=Token.Token(TipoToken.PARENTESIS,SubTipoToken.PARENTESIS_IZQUIERDO,c,self.numLinea)
                    self.L.append(t)
                else:
                    t=Token.Token(TipoToken.PARENTESIS,SubTipoToken.PARENTESIS_DERECHO,c,self.numLinea)
                    self.L.append(t)
                index=index+1
                 
            
            elif c.isalpha() or c=="_":#Tengo el automata de los identificadores
                nombreIden=c
                index=index+1
                f=True
                while(index < len(self.codigo) and f):
                    c=self.codigo[index]
                    if(c.isalpha() or c=="_" or c.isdigit()):
                        nombreIden=nombreIden+c
                        index=index+1
                    else:
                        f=False
                t=self.esPalabraReservada(nombreIden)  
                self.L.append(t)            
  
                    
                
            elif c == "\"":  # automata de cadenas create by Elias Silva
                    auxCA=c
                    index = index + 1
                    if(index < len(self.codigo)):
                        c =  self.codigo[index]
                        auxCA = auxCA + c 
                        while(c != "\""):
                         index = index + 1
                         if(index < len(self.codigo)):
                            c =  self.codigo[index]
                            auxCA = auxCA + c 
                         else:
                             print("La cadena No termina con \" "," en la linea ", self.numLinea)
                             break
                             exit
                        t = Token.Token(TipoToken.CADENA,SubTipoToken.NINGUNO,auxCA,self.numLinea)
                        self.L.append(t)
                    index = index + 1

                    #automata de numero enteros y reales by Elias 
            elif c.isdigit():
                numE = ""
                numR = ""
                while((index<len(self.codigo)) and (c.isdigit())):
                    index += 1
                    numE = numE + c
                    numR = numR + c
                    c =""
                    if(index < len(self.codigo)):
                        c = self.codigo[index]
                if c == ".":
                    numR = numE + c
                    index = index + 1
                    if(index < len(self.codigo)):
                        c = self.codigo[index]
                        if c.isdigit():
                            while(c.isdigit()):
                                index = index + 1
                                numR = numR + c
                                if(index < len(self.codigo)):
                                    c = self.codigo[index]
                            t=Token.Token(TipoToken.NUMERO, SubTipoToken.REAL, numR, self.numLinea)                  
                            self.L.append(t)                        
                        else:
                            print("Real no establecido correctamente.",numR, self.numLinea )
                            index = index + 1            
                else:
                    t=Token.Token(TipoToken.NUMERO, SubTipoToken.ENTERO, numE, self.numLinea)
                    self.L.append(t)      


                    
            elif c == "&" or c =="|" or c == "!":    #Operadores logicos by Elias silva 
                if c == "&":
                    index = index + 1
                    if(index<len(self.codigo)):
                        c = self.codigo[index]
                        if(c =="&"):
                            index = index + 1
                            t = Token.Token(TipoToken.OPERADOR_LOGICO,SubTipoToken.OPERADOR_Y,"&&",self.numLinea)
                            self.L.append(t)
                        else:
                            print("Operador incompleto &")   
                elif c == "|":
                    index = index + 1
                    if(index<len(self.codigo)):
                        c = self.codigo[index]
                        if(c == "|"):
                            index = index + 1
                            t = Token.Token(TipoToken.OPERADOR_LOGICO,SubTipoToken.OPERADOR_O,"||",self.numLinea)
                            self.L.append(t)
                        else:
                            print("Operador incompleto |")
                else:
                    index = index + 1
                    t = Token.Token(TipoToken.OPERADOR_LOGICO,SubTipoToken.NEGACION,"!",self.numLinea)
                    self.L.append(t)

            elif c=="'":
                index=index+1
                if(index<len(self.codigo)):
                    car=self.codigo[index]
                    index=index+1
                    if(index<len(self.codigo)):
                        c=self.codigo[index]
                        if c=="'":
                            t=Token.Token(TipoToken.SIMBOLO, SubTipoToken.NINGUNO,car,self.numLinea)
                            self.L.append(t)
                        else:
                            print ("Simbolo extranio char")
                        index=index+1
                        
                                                  
            elif c=="=":
                 index=index+1
                 if(index<len(self.codigo)):
                     c=self.codigo[index]
                     if c=="=":
                         index=index+1
                         t=Token.Token(TipoToken.COMPARACION,SubTipoToken.IGUALDAD,"==",self.numLinea)
                         self.L.append(t)
                     else:
                         t=Token.Token(TipoToken.ASIGNACION,SubTipoToken.NINGUNO,"=",self.numLinea)
                         self.L.append(t)                             
            elif c == "," or c==";" or c == ":":
                
                if c== ",":
                    t=Token.Token(TipoToken.SIGNO_DE_PUNTUACION,SubTipoToken.COMA,c,self.numLinea)
                    self.L.append(t)
                if c== ";":
                    t=Token.Token(TipoToken.SIGNO_DE_PUNTUACION,SubTipoToken.PUNTOYCOMA,c,self.numLinea)
                    self.L.append(t)
                if c== ":":
                    t=Token.Token(TipoToken.SIGNO_DE_PUNTUACION,SubTipoToken.DOSPUNTOS,c,self.numLinea)
                    self.L.append(t)     
                index=index+1


                
            else:
                
                print("Error, simbolo extranio "+c,c) 
                index=index+1        
                     
        print("Elementos: ",len(self.L))

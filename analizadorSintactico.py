import SubTipoToken
import AnalizadorLexico
import TipoToken


l=AnalizadorLexico.AnalizadorLexico("programa.txt")

l.crearLista()


def error(t1,t2,line):
   print("Se esperaba ",t1, "en linea ",line," se recibio ",t2)

#preanalisis es lo que espero
def seEspera(t,preanalisis):
   if(t!=None):
      if(t==preanalisis):
         return True;
   return False;      

def LISTA_FUNCIONES():
   FUNCION()
   
def TIPO():
        t = l.obtenerToken()
        if (t != None):
           if (not seEspera(t.getSubTipo(), SubTipoToken.ENTERO) and not seEspera(t.getSubTipo(), SubTipoToken.REAL) and  
            not seEspera(t.getSubTipo(), SubTipoToken.LOGICO) and not seEspera(t.getSubTipo(), SubTipoToken.CARACTER)):
              print("Error: Tipo incorecto Linea",t.getnumLinea())
        else:
            print("Se reconoce ",t)    
    
def FUNCION():
        TIPO()
        t=l.obtenerToken()
        if (t != None):
           if(not seEspera(t.getSubTipo(),SubTipoToken.FUNCION)):
              error(SubTipoToken.FUNCION,t.getSubTipo(),t.getnumLinea());
           else:
              print("Se reconoce FUNCION")       
 
        t=l.obtenerToken();
        if (t != None):          
           if(not seEspera(t.getTipo(),TipoToken.IDENTIFICADOR)):
               error(TipoToken.IDENTIFICADOR,t.getTipo(),t.getnumLinea())
           else:
               print("Se reconoce IDENTIFICADOR:",t.getlexema())
          
        t=l.obtenerToken()
        if (t != None): 
           if(not seEspera(t.getSubTipo(),SubTipoToken.PARENTESIS_IZQUIERDO)):
                   error(SubTipoToken.PARENTESIS_IZQUIERDO,t.getSubTipo(),t.getnumLinea());
           else:
              print("Se reconoce (")   
                   
        PARAMETROS()
               
        t=l.obtenerToken()
        if(t!=None):
           if(not seEspera(t.getSubTipo(),SubTipoToken.PARENTESIS_DERECHO)):
              error(SubTipoToken.PARENTESIS_DERECHO,t.getSubTipo(),t.getnumLinea());
           else:
              print("Se reconoce )")
                         
                  
        LISTA_OPERACIONES()
                      
        t=l.obtenerToken()
                
        if(t!=None):
           if(not seEspera(t.getSubTipo(),SubTipoToken.REGRESAR)):
              error(SubTipoToken.REGRESAR,t.getSubTipo(),t.getnumLinea());
           else:
              print("Se reconoce REGRESAR")
                    
        EXPRESION()
                    
        t=l.obtenerToken()
        if(t!=None):
           if(not seEspera(t.getSubTipo(),SubTipoToken.PUNTOYCOMA)):
              error(SubTipoToken.PUNTOYCOMA,t.getSubTipo(),t.getnumLinea());
           else:
              print("Se reconoce PUNTO Y COMA")
                     
        t=l.obtenerToken()
        if(t!=None):
           if(not seEspera(t.getSubTipo(),SubTipoToken.FINFUNCION)):
              error(SubTipoToken.FINFUNCION,t.getSubTipo(),t.getnumLinea());
           else:
              print("Se reconoce FINFUNCION")

def Operacion(t):
    if(seEspera(t.getSubTipo(),SubTipoToken.ENTERO)):
        return True
    elif(seEspera(t.getTipo(),TipoToken.IDENTIFICADOR)):
        return True
    else:
        return False                
        
             
def PARA():
    t = l.obtenerToken()
    if(not seEspera(t.getSubTipo(),SubTipoToken.PARA)):
        error(SubTipoToken.PARA,t.getSubTipo(),t.getnumLinea())
    else:   
        print("Se reconoce PARA")

    t = l.obtenerToken()
    if(not seEspera(t.getTipo(), TipoToken.IDENTIFICADOR)):
        error(TipoToken.IDENTIFICADOR,t.getTipo(),t.getnumLinea())
    else:
        print("Se reconoce IDENTIFICADOR")

    t = l.obtenerToken()
    if(not seEspera(t.getTipo(),TipoToken.ASIGNACION)):
        error(TipoToken.ASIGNACION,t.getTipo(),t.getnumLinea())
    else:
        print("Se reconoce ASIGNACION")

    t = l.obtenerToken()
    Operacion(t)
    if not Operacion:
        error("No se recibio ENTERO o IDENTIFICADOR",t.getnumLinea())  
    else:
        print("Se reconoce NUMERO o IDENTIFICADOR ")

    t = l.obtenerToken()
    if(not seEspera(t.getSubTipo(),SubTipoToken.HASTA)):
        error(SubTipoToken.HASTA,t.getSubTipo(),t.getnumLinea())  
    else:
        print("Se reconoce PALABRA RESERVADA HASTA")
    t = l.obtenerToken()
    Operacion(t)
    if not Operacion:
        error("No se recibio ENTERO o IDENTIFICADOR",t.getnumLinea())  
    else:
        print("Se reconoce NUMERO o IDENTIFICADOR")
    t = l.obtenerToken()

    if t.getSubTipo()== SubTipoToken.CON:
        if(not seEspera(t.getSubTipo(),SubTipoToken.CON)):
            error(SubTipoToken.CON,t.getSubTipo(),t.getnumLinea())
        else:
            print("Se reconoce PALABRA RESERVADA CON ") 
        t = l.obtenerToken()
        if(not seEspera(t.getSubTipo(),SubTipoToken.PASO)):
            error(SubTipoToken.PASO,t.getSubTipo(),t.getnumLinea())
        else:
            print("Se reconoce PALABRA RESERVADA PASO")
        t = l.obtenerToken()    
        Operacion(t)
        if not Operacion:
            error("No se recibio ENTERO o IDENTIFICADOR",t.getnumLinea())  
        else:
            print("Se reconoce NUMERO o IDENTIFICADOR")
        t = l.obtenerToken()
        if(not seEspera(t.getSubTipo(),SubTipoToken.HACER)):
            error(SubTipoToken.HACER,t.getSubTipo(),t.getnumLinea())
        else:
            print("Se reconoce PALABRA RESERVADA HACER")
        LISTA_OPERACIONES()
        t = l.obtenerToken()        
        if(not seEspera(t.getSubTipo(),SubTipoToken.FINPARA)):
            error(SubTipoToken.FINPARA,t.getSubTipo(),t.getnumLinea())
        else:
            print("Se reconoce PALABRA RESERVADA FINPARA")      
    elif t.getSubTipo()== SubTipoToken.HACER:
        if(not seEspera(t.getSubTipo(),SubTipoToken.HACER)):
            error(SubTipoToken.HACER,t.getSubTipo(),t.getnumLinea())
        else:
            print("Se reconoce PALABRA RESERVADA HACER")
        LISTA_OPERACIONES()        
        t = l.obtenerToken()        
        if(not seEspera(t.getSubTipo(),SubTipoToken.FINPARA)):
            error(SubTipoToken.FINPARA,t.getSubTipo(),t.getnumLinea())
        else:
            print("Se reconoce PALABRA RESERVADA FINPARA")
    else:
        error("No se cerro correctamente el para") 
                

            
          
               
def PARAMETROS():
    t = l.obtenerToken()
    if (t != None):
        if seEspera(t.getTipo(), TipoToken.IDENTIFICADOR):
            l.regresarToken(t)
            HAY_PARAMETROS()
        else:
            l.regresarToken(t)


def HAY_PARAMETROS():

   t=l.obtenerToken();
   if(not seEspera(t.getTipo(),TipoToken.IDENTIFICADOR)):
      error(TipoToken.IDENTIFICADOR,t.getTipo(),t.getnumLinea())
   else:
       print("Se reconoce IDENTIFICADOR:",t.getlexema())
   t=l.obtenerToken();
   if t!=None:
      if t.getSubTipo()== SubTipoToken.COMA:
          HAY_PARAMETROS()
      else:
          l.regresarToken(t)              
                   
def PROGRAMA():
   PROCESO()
   t=l.obtenerToken()
   if(t!=None): 
      l.regresarToken(t)
      LISTA_FUNCIONES()


def PROCESO():
   t=l.obtenerToken()
   if(not seEspera(t.getSubTipo(),SubTipoToken.PROCESO)):
      error(SubTipoToken.PROCESO,t.getSubTipo(),t.getnumLinea());
   else:
       print("Se reconoce PROCESO")
   t=l.obtenerToken()
   if(not seEspera(t.getTipo(),TipoToken.IDENTIFICADOR)):
      error(TipoToken.IDENTIFICADOR,t.getTipo(),t.getnumLinea())
   else:
       print("Se reconoce IDENTIFICADOR:",t.getlexema())
   LISTA_OPERACIONES()
   t=l.obtenerToken()
   if(t!=None):
      if(not seEspera(t.getSubTipo(),SubTipoToken.FINPROCESO)):
         error(SubTipoToken.FINPROCESO,t.getSubTipo(),t.getnumLinea());
      else:
         print("Se reconoce FINPROCESO")


def SI():
   t=l.obtenerToken()
   if(not seEspera(t.getSubTipo(),SubTipoToken.SI)):
      error(SubTipoToken.SI,t.getSubTipo(),t.getnumLinea());
   else:
       print("Se reconoce SI")
   t=l.obtenerToken()
   if(not seEspera(t.getSubTipo(),SubTipoToken.PARENTESIS_IZQUIERDO)):
      error(SubTipoToken.PARENTESIS_IZQUIERDO,t.getSubTipo(),t.getnumLinea());
   else:
       print("Se reconoce (")
   EXPRESION()
   t=l.obtenerToken()
   if(not seEspera(t.getSubTipo(),SubTipoToken.PARENTESIS_DERECHO)):
      error(SubTipoToken.PARENTESIS_DERECHO,t.getSubTipo(),t.getnumLinea());
   else:
       print("Se reconoce )")
   t=l.obtenerToken()
   if(not seEspera(t.getSubTipo(),SubTipoToken.ENTONCES)):
      error(SubTipoToken.ENTONCES,t.getSubTipo(),t.getnumLinea());
   else:
       print("Se reconoce ENTONCES")

   LISTA_OPERACIONES()

   t=l.obtenerToken()
   if t!=None:
      if t.getSubTipo()== SubTipoToken.SINO:
         LISTA_OPERACIONES()
         t=l.obtenerToken()
         if(not seEspera(t.getSubTipo(),SubTipoToken.FINSI)):
            error(SubTipoToken.FINSI,t.getSubTipo(),t.getnumLinea());
         else:
            print("Se reconoce FINSI")
      else:
         if(not seEspera(t.getSubTipo(),SubTipoToken.FINSI)):
            error(SubTipoToken.FINSI,t.getSubTipo(),t.getnumLinea());
         else:
            print("Se reconoce FINSI")


def LEER():

   t=l.obtenerToken()
   if(not seEspera(t.getSubTipo(),SubTipoToken.LEER)):
      error(SubTipoToken.LEER,t.getSubTipo(),t.getnumLinea());
   else:
       print("Se reconoce LEER")

   LISTA_LEER()
 
   t=l.obtenerToken()
   if(not seEspera(t.getSubTipo(),SubTipoToken.PUNTOYCOMA)):
      error(SubTipoToken.PUNTOYCOMA,t.getSubTipo(),t.getnumLinea());
   else:
       print("Se reconoce ;")  


def LISTA_LEER():

   t=l.obtenerToken();
   if(not seEspera(t.getTipo(),TipoToken.IDENTIFICADOR)):
      error(TipoToken.IDENTIFICADOR,t.getTipo(),t.getnumLinea())
   else:
       print("Se reconoce IDENTIFICADOR:",t.getlexema())
   t=l.obtenerToken();
   if t!=None:
      if t.getSubTipo()== SubTipoToken.COMA:
          LISTA_LEER()
      else:
          l.regresarToken(t)


def ESCRIBIR():

   t=l.obtenerToken()
   if(not seEspera(t.getSubTipo(),SubTipoToken.ESCRIBIR)):
      error(SubTipoToken.ESCRIBIR,t.getSubTipo(),t.getnumLinea());
   else:
       print("Se reconoce ESCRIBIR")

   LISTA_VALOR()

   t=l.obtenerToken()
   if(not seEspera(t.getSubTipo(),SubTipoToken.PUNTOYCOMA)):
      error(SubTipoToken.PUNTOYCOMA,t.getSubTipo(),t.getnumLinea());
   else:
       print("Se reconoce ;")  


def LISTA_VALOR():

   VALOR()
   t=l.obtenerToken();
   if t!=None:
      if t.getSubTipo()== SubTipoToken.COMA:
          LISTA_VALOR()
      else:
          l.regresarToken(t)


def VALOR():

   t=l.obtenerToken()
   if not t.getTipo()==TipoToken.CADENA:
      l.regresarToken(t)
      EXPRESION()
   else:
       print("Se reconoce STRING",t.getlexema())

def OPERACION():
   t=l.obtenerToken()
   #print("TOKEN::::::::"+t.getlexema())
   if t!= None:
       if t.getSubTipo()==SubTipoToken.SI:
           l.regresarToken(t)
           SI()
       elif t.getSubTipo()==SubTipoToken.LEER:
           l.regresarToken(t)
           LEER()        
       elif t.getSubTipo()==SubTipoToken.ESCRIBIR:
           l.regresarToken(t)
           ESCRIBIR()
       elif t.getSubTipo()==SubTipoToken.MIENTRAS:
           l.regresarToken(t)
           MIENTRAS()
       elif t.getSubTipo()==SubTipoToken.ENTERO:
           l.regresarToken(t)
           DECLARACION_ENTERO()
       elif t.getSubTipo()==SubTipoToken.CARACTER:
           l.regresarToken(t)
           DECLARACION_CARACTER()
       elif t.getSubTipo()==SubTipoToken.REAL:
           l.regresarToken(t)
           DECLARACION_REAL()
       elif t.getSubTipo()==SubTipoToken.LOGICO:
           l.regresarToken(t)
           DECLARACION_LOGICO()           
       elif t.getTipo()==TipoToken.IDENTIFICADOR:
           l.regresarToken(t)
           ASIGNACION()
       elif t.getSubTipo()==SubTipoToken.PARA:
           l.regresarToken(t)
           PARA()
       elif t.getSubTipo()==SubTipoToken.REPETIR:
           l.regresarToken(t)
           REPETIR()   

    
 
def ASIGNACION():

  t=l.obtenerToken()
  if(not seEspera(t.getTipo(),TipoToken.IDENTIFICADOR)):
     error(TipoToken.IDENTIFICADOR,t.getTipo(),t.getnumLinea())
  else:
     print("Se reconoce IDENTIFICADOR:",t.getlexema())
     
  t=l.obtenerToken()
  if(not seEspera(t.getTipo(),TipoToken.ASIGNACION)):
     error(TipoToken.ASIGNACION,t.getTipo(),t.getnumLinea())
  else:
     print("Se reconoce ASIGNACION:",t.getlexema())
     
  EXPRESION();     
  t=l.obtenerToken();
  
  #print("EL TOKEN QUE TENGO AHORA ES::::::::::::::::",t)
  
  if t!=None:
     if(not seEspera(t.getSubTipo(),SubTipoToken.PUNTOYCOMA)):
        error(SubTipoToken.PUNTOYCOMA,t.getSubTipo(),t.getnumLinea())
     else:
        print("Se reconoce PUNTO Y COMA:",t.getlexema())
    
def LISTA_OPERACIONES():
   OPERACION()
   t=l.obtenerToken()
   if (t!= None and
        t.getSubTipo()!=SubTipoToken.FINPROCESO and
        t.getSubTipo()!=SubTipoToken.FINSI and
        t.getSubTipo()!=SubTipoToken.FINMIENTRAS and
        t.getSubTipo()!=SubTipoToken.REGRESAR and 
        t.getSubTipo()!=SubTipoToken.HASTA and
        t.getSubTipo()!=SubTipoToken.QUE and
        t.getSubTipo()!=SubTipoToken.HACER and  
        t.getSubTipo()!=SubTipoToken.FINPARA):

        l.regresarToken(t)
        LISTA_OPERACIONES()
   elif t!= None and t.getSubTipo()==SubTipoToken.FINPROCESO:
      l.regresarToken(t)
   elif t!= None and t.getSubTipo()==SubTipoToken.FINSI:
      l.regresarToken(t)
   elif t!= None and t.getSubTipo()==SubTipoToken.FINMIENTRAS:
      l.regresarToken(t)
   elif t!= None and t.getSubTipo()==SubTipoToken.REGRESAR:
      l.regresarToken(t)
   elif t!= None and t.getSubTipo()==SubTipoToken.FINPARA:
      l.regresarToken(t)
   elif t!= None and t.getSubTipo()==SubTipoToken.HASTA:
      l.regresarToken(t)  
   elif t!= None and t.getSubTipo()==SubTipoToken.QUE:
      l.regresarToken(t)
   elif t!= None and t.getSubTipo()==SubTipoToken.HACER:
      l.regresarToken(t)      


def DECLARACION_ENTERO():
   t=l.obtenerToken()
   if(t!=None):
      if(not seEspera(t.getSubTipo(),SubTipoToken.ENTERO)):
         error(SubTipoToken.ENTERO,t.getSubTipo(),t.getnumLinea());
      else:
         print("Se reconoce palabra ENTERO")
      LISTA_ENTERO()
      t=l.obtenerToken()
      if(t!=None):
          if(not seEspera(t.getSubTipo(),SubTipoToken.PUNTOYCOMA)):
              error(SubTipoToken.PUNTOYCOMA,t.getSubTipo(),t.getnumLinea());
          else:
              print("Se reconoce ;")  
    
def DE():

   t=l.obtenerToken();
   if(t!=None):
      if(not seEspera(t.getTipo(),TipoToken.IDENTIFICADOR)):
          error(TipoToken.IDENTIFICADOR,t.getTipo(),t.getnumLinea())
      else:
          print("Se reconoce IDENTIFICADOR:",t.getlexema())
      t=l.obtenerToken();
      if t!=None:
          if t.getTipo()== TipoToken.ASIGNACION:
              print("Se reconoce =")
              t=l.obtenerToken();
              if(t!=None):
                 if(not seEspera(t.getSubTipo(),SubTipoToken.NUMERO_ENTERO)):
                    error(SubTipoToken.NUMERO_ENTERO,t.getSubTipo(),t.getnumLinea())
                 else:
                    print("Se reconoce ",t.getlexema())
              else:
                 print("Error se espera entero")
          else:
              l.regresarToken(t)
          
          
    
def LISTA_ENTERO():
   DE()
   t=l.obtenerToken();
   if(t!=None):
      if t.getSubTipo()== SubTipoToken.COMA:
          print("Se reconoce ,")
          LISTA_ENTERO()
      else:
          l.regresarToken(t)
   else:
       print("Error declaracion")
       
def DECLARACION_REAL():
   t=l.obtenerToken()
   if(t!=None):
      if(not seEspera(t.getSubTipo(),SubTipoToken.REAL)):
         error(SubTipoToken.REAL,t.getSubTipo(),t.getnumLinea());
      else:
         print("Se reconoce palabra REAL")
      LISTA_REAL()
      t=l.obtenerToken()
      if(t!=None):
          if(not seEspera(t.getSubTipo(),SubTipoToken.PUNTOYCOMA)):
              error(SubTipoToken.PUNTOYCOMA,t.getSubTipo(),t.getnumLinea());
          else:
              print("Se reconoce ;")  
    
def DR():

   t=l.obtenerToken();
   if(t!=None):
      if(not seEspera(t.getTipo(),TipoToken.IDENTIFICADOR)):
          error(TipoToken.IDENTIFICADOR,t.getTipo(),t.getnumLinea())
      else:
          print("Se reconoce IDENTIFICADOR:",t.getlexema())
      t=l.obtenerToken();
      if t!=None:
          if t.getTipo()== TipoToken.ASIGNACION:
              print("Se reconoce =")
              t=l.obtenerToken();
              if(t!=None):
                 if(not seEspera(t.getSubTipo(),SubTipoToken.NUMERO_REAL)):
                    error(SubTipoToken.NUMERO_REAL,t.getSubTipo(),t.getnumLinea())
                 else:
                    print("Se reconoce ",t.getlexema())
              else:
                 print("Error se espera entero")
          else:
              l.regresarToken(t)
          
          
    
def LISTA_REAL():
   DR()
   t=l.obtenerToken();
   if(t!=None):
      if t.getSubTipo()== SubTipoToken.COMA:
          print("Se reconoce ,")
          LISTA_REAL()
      else:
          l.regresarToken(t)
   else:
       print("Error declaracion")
       
def DECLARACION_LOGICO():
   t=l.obtenerToken()
   if(t!=None):
      if(not seEspera(t.getSubTipo(),SubTipoToken.LOGICO)):
         error(SubTipoToken.LOGICO,t.getSubTipo(),t.getnumLinea());
      else:
         print("Se reconoce palabra LOGICO")
      LISTA_LOGICO()
      t=l.obtenerToken()
      if(t!=None):
          if(not seEspera(t.getSubTipo(),SubTipoToken.PUNTOYCOMA)):
              error(SubTipoToken.PUNTOYCOMA,t.getSubTipo(),t.getnumLinea());
          else:
              print("Se reconoce ;")  
    
def DL():

   t=l.obtenerToken();
   if(t!=None):
      if(not seEspera(t.getTipo(),TipoToken.IDENTIFICADOR)):
          error(TipoToken.IDENTIFICADOR,t.getTipo(),t.getnumLinea())
      else:
          print("Se reconoce IDENTIFICADOR:",t.getlexema())
      t=l.obtenerToken();
      if t!=None:
          if t.getTipo()== TipoToken.ASIGNACION:
              print("Se reconoce =")
              t=l.obtenerToken();
              if(t!=None):
                 if(not (seEspera(t.getSubTipo(),SubTipoToken.VERDADERO) or seEspera(t.getSubTipo(),SubTipoToken.FALSO))):
                    error(SubTipoToken.LOGICO,t.getSubTipo(),t.getnumLinea())
                 else:
                    print("Se reconoce ",t.getlexema())
              else:
                 print("Error se espera logico")
          else:
              l.regresarToken(t)
          
          
    
def LISTA_LOGICO():
   DL()
   t=l.obtenerToken();
   if(t!=None):
      if t.getSubTipo()== SubTipoToken.COMA:
          print("Se reconoce ,")
          LISTA_LOGICO()
      else:
          l.regresarToken(t)
   else:
       print("Error declaracion")       

def DECLARACION_CARACTER():
   t=l.obtenerToken()
   if(t!=None):
      if(not seEspera(t.getSubTipo(),SubTipoToken.CARACTER)):
         error(SubTipoToken.CARACTER,t.getSubTipo(),t.getnumLinea())
      else:
         print("Se reconoce caracter")
      LISTA_CARACTER()
      t=l.obtenerToken()
      if(t!=None):
          if(not seEspera(t.getSubTipo(),SubTipoToken.PUNTOYCOMA)):
              error(SubTipoToken.PUNTOYCOMA,t.getSubTipo(),t.getnumLinea());
          else:
              print("Se reconoce ;")      
def DC():

   t=l.obtenerToken();
   if(t!=None):
      if(not seEspera(t.getTipo(),TipoToken.IDENTIFICADOR)):
          error(TipoToken.IDENTIFICADOR,t.getSubTipo(),t.getnumLinea())
      else:
          print("Se reconoce IDENTIFICADOR:",t.getlexema())
      t=l.obtenerToken();
      if t!=None:
          if t.getTipo()== TipoToken.ASIGNACION:
              print("Se reconoce =")
              t=l.obtenerToken();
              if(t!=None):
                  if(not seEspera(t.getTipo(),TipoToken.SIMBOLO)):
                     
                      error(TipoToken.SIMBOLO,t.getSubTipo(),t.getnumLinea())
                  else:
                      print("Se reconoce SIMBOLO ",t.getlexema())

              else:
                  print("Error se espera charater")
          else:
               l.regresarToken(t)
              
def LISTA_CARACTER():
   DC()
   t=l.obtenerToken();
   if(t!=None):
      if t.getSubTipo()== SubTipoToken.COMA:
          print("Se reconoce ,")
          LISTA_CARACTER()
      else:
          l.regresarToken(t)
   else:
       print("Error declaracion")

    
def DECLARACION_REAL():
   t=l.obtenerToken()
   if(t!=None):
      if(not seEspera(t.getSubTipo(),SubTipoToken.REAL)):
         error(SubTipoToken.REAL,t.getnumLinea());
      else:
         print("Se reconoce real")
      LISTA_REAL()
      t=l.obtenerToken()
      if(t!=None):
          if(not seEspera(t.getSubTipo(),SubTipoToken.PUNTOYCOMA)):
              error(SubTipoToken.PUNTOYCOMA,t.getnumLinea());
          else:
              print("Se reconoce ;")

def DR():

   t=l.obtenerToken();
   if(t!=None):
      if(not seEspera(t.getTipo(),TipoToken.IDENTIFICADOR)):
          error(TipoToken.IDENTIFICADOR,t.getnumLinea())
      else:
          print("Se reconoce IDENTIFICADOR:",t.getlexema())
      t=l.obtenerToken();
      if t!=None:
          if t.getTipo()== TipoToken.ASIGNACION:
              print("Se reconoce =")
              t=l.obtenerToken();
              if(t!=None):
                 if(not seEspera(t.getSubTipo(),SubTipoToken.NUMERO_REAL)):
                     error(SubTipoToken.NUMERO_REAL,t.getnumLinea())
                 else:
                     print("Se reconoce ",t.getlexema())
              else:
                 print("Error se espera real")
          else:
              l.regresarToken(t)

def LISTA_REAL():
   DR()
   t=l.obtenerToken();
   if(t!=None):
      if t.getSubTipo()== SubTipoToken.COMA:
          print("Se reconoce ,")
          LISTA_REAL()
      else:
          l.regresarToken(t)
   else:
       print("Error declaracion")

def REPETIR():
    t=l.obtenerToken()
    if not seEspera(t.getSubTipo(),SubTipoToken.REPETIR):
        error(SubTipoToken.REPETIR,t.getSubTipo(),t.getnumLinea())
    else:
        print("Se reconoce REPETIR")

    LISTA_OPERACIONES()
    t = l.obtenerToken()

    if not seEspera(t.getSubTipo(),SubTipoToken.HASTA):
        error(SubTipoToken.HASTA,t.getSubTipo(),t.getnumLinea())
    else:
        print("Se reconoce HASTA")
    t = l.obtenerToken()

    if not seEspera(t.getSubTipo(),SubTipoToken.QUE):
        error(SubTipoToken.QUE,t.getSubTipo(),t.getnumLinea())
        print(t.getlexema(),  t.getnumLinea() )
    else:
        print("Se reconoce QUE")
    t = l.obtenerToken()    

    if not seEspera(t.getSubTipo(),SubTipoToken.PARENTESIS_IZQUIERDO):
        error(SubTipoToken.PARENTESIS_IZQUIERDO,t.getSubTipo(),t.getnumLinea())
    else:
        print("Se reconoce  PARENTESIS_IZQUIERDO" )
    EXPRESION()
    t = l.obtenerToken()    
    if not seEspera(t.getSubTipo(),SubTipoToken.PARENTESIS_DERECHO):
        error(SubTipoToken.PARENTESIS_DERECHO,t.getSubTipo(),t.getnumLinea())
    else:
        print("Se reconoce  PARENTESIS_DERECHO")





def MIENTRAS():
    t=l.obtenerToken()
    if(t!=None):
        if(not seEspera(t.getSubTipo(),SubTipoToken.MIENTRAS)):
             error(SubTipoToken.MIENTRAS,t.getSubTipo(),t.getnumLinea())
        else:
            print("Se reconoce MIENTRAS:",t.getlexema())

    t=l.obtenerToken()
    if(t!=None):
        if(not seEspera(t.getSubTipo(),SubTipoToken.PARENTESIS_IZQUIERDO)):
            error(SubTipoToken.PARENTESIS_IZQUIERDO,t.getSubTipo(),t.getnumLinea())
        else:
            print("Se reconoce (")
    EXPRESION()
    t=l.obtenerToken()
    if(not seEspera(t.getSubTipo(),SubTipoToken.PARENTESIS_DERECHO)):
        error(SubTipoToken.PARENTESIS_DERECHO,t.getSubTipo(),t.getnumLinea())
    else:
        print("Se reconoce )")
    t=l.obtenerToken()
    if(not seEspera(t.getSubTipo(),SubTipoToken.HACER)):
        error(SubTipoToken.HACER,t.getSubTipo(),t.getnumLinea())
    else:
        print("Se reconoce HACER")

    LISTA_OPERACIONES()

    t=l.obtenerToken()

    if(not seEspera(t.getSubTipo(),SubTipoToken.FINMIENTRAS)):
        error(SubTipoToken.FINMIENTRAS,t.getSubTipo(),t.getnumLinea())
    else:
        print("Se reconoce FINMIENTRAS")


def EXPRESION():
    Y()
    EXPRESIONP()



def EXPRESIONP():
    t = l.obtenerToken()
    if (t != None):
        if seEspera(t.getSubTipo(), SubTipoToken.OPERADOR_O):
            Y()
            EXPRESIONP()
        else:
            l.regresarToken(t)


def Y():
    C()
    YP()


def YP():
    t = l.obtenerToken()
    if (t != None):
        if seEspera(t.getSubTipo(), SubTipoToken.OPERADOR_Y):
            C()
            YP()
        else:
            l.regresarToken(t)


def C():
    R()
    CP()


def CP():
    t = l.obtenerToken()
    if (t != None):
        if seEspera(t.getSubTipo(), SubTipoToken.IGUALDAD) or seEspera(t.getSubTipo(), SubTipoToken.DIFERENTE):
            R()
            CP()
        else:
            l.regresarToken(t)


def R():
    E()
    RP()


def RP():
    t = l.obtenerToken()
    if (t != None):
        if seEspera(t.getTipo(), TipoToken.OPERADOR_RELACIONAL):
            E()
            RP()
        else:
            l.regresarToken(t)


def E():
    T()
    EP()


def EP():
    t = l.obtenerToken()
    if (t != None):
        if seEspera(t.getSubTipo(), SubTipoToken.OPERADOR_SUMA) or seEspera(t.getSubTipo(), SubTipoToken.OPERADOR_RESTA):
            T()
            EP()
        else:
            l.regresarToken(t)


def T():
    N()
    TP()


def TP():
    t = l.obtenerToken()
    if (t != None):
        if seEspera(t.getSubTipo(), SubTipoToken.OPERADOR_MULTIPLICACION) or seEspera(t.getSubTipo(), SubTipoToken.OPERADOR_DIVISION) or seEspera(t.getSubTipo(), SubTipoToken.OPERADOR_MODULO):
            N()
            TP()
        else:
            l.regresarToken(t)


def N():
    t = l.obtenerToken()
    if (t != None):
        if seEspera(t.getSubTipo(), SubTipoToken.NEGACION):
            F()
        else:
            l.regresarToken(t)
            F()


def F():
    t = l.obtenerToken()
    if (not seEspera(t.getTipo(), TipoToken.IDENTIFICADOR)) and (
            not seEspera(t.getSubTipo(), SubTipoToken.NUMERO_ENTERO)) and (
            not seEspera(t.getSubTipo(), SubTipoToken.NUMERO_REAL)):
        print("Error, se espera identificador, o numero ",t.getnumLinea());
    else:
        print("Reconoci ", t)

PROGRAMA()

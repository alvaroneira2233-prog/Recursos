# tipos de datos

## char
CHAR(n):es una caena de longitud fija donde (n) es el numero de caracrteres que almacenara
<img width="761" height="159" alt="image" src="https://github.com/user-attachments/assets/49294021-5d1d-4f6f-8882-26a74ebbc17e" />
si se escribe menos letras en los caracteres quqedaran como espacios blancos y consumiran el almacenamieno de la base de datos 
asi que es ineficiente

## varchar
VARCHAR a diferencia de CHAR tiene cadenas de logitud variable osea que en vez de que se pierda espacio cunado se escribe menos 
de lo estipulado no consumira espacio en la base de datos inecesariamente 
<img width="735" height="245" alt="image" src="https://github.com/user-attachments/assets/0ff0ae51-6082-4a13-8008-62bece17fdb8" />
asi siendo mas facil guardar datos como nombres o direccciones sin consumir de mas 

## tetx
el tipo tetx nos sirve principalmente para guardar varios datos sin longitud fija como una descripccion 
<img width="746" height="216" alt="image" src="https://github.com/user-attachments/assets/95bb81c7-81a0-457b-9a69-53dfd09e5992" />

## analisisde caso pracctico
en caso de guardar un numero fijo de caracteres como lo son las matriculas de autos la mejor opcion es usar char 
ya que guardan la informacion de forma igual y no hay gastos de memoria para la base de datos

## gestion de almacenamiento
si utilizamos varchar y ponemos una longitud de caracteres muy grande pero escribimos pocos datos dentro de esta hbara un consume completamente inecesario para el servidor gastando no almacenamiento si no ram , para casos como estos es mejor no colocar una logitud
muy larga 















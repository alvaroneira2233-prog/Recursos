# proceso de instalacion 
---
## como instalarlo
primero descargamos la version que uno quiera (utilizare la 9.5.25) desde la paguina principal
(https://www.enterprisedb.com/download-postgresql-binaries)

<img width="586" height="210" alt="image" src="https://github.com/user-attachments/assets/cd22bd3e-b39d-42c0-8907-9a0cff780647"/>

## ya instalado
se descomprime el archivo, dejando estas carpetas

<img width="598" height="346" alt="image" src="https://github.com/user-attachments/assets/f1099320-1adc-411e-9f7e-bee50e91a93a" />

y abrimos la terminal

<img width="1059" height="554" alt="image" src="https://github.com/user-attachments/assets/4522a28e-1dea-481b-a4da-f840f34ff3e0" />

## iniciamos postgres
### Flujo completo para PostgreSQL "portable" en Windows

## 1. Crear el clúster de datos:

```powershell
.\bin\initdb.exe -D data -U postgres -W -E UTF8
```
<img width="985" height="508" alt="image" src="https://github.com/user-attachments/assets/1cb2bac8-aa7e-4bfa-88c8-44740adcd5ce" />

tambien le ponemos la contraseña

## 2. Iniciar el servidor:

```powershell
.\bin\pg_ctl.exe -D data -l logfile start
```
<img width="980" height="478" alt="image" src="https://github.com/user-attachments/assets/651974fb-75c8-459c-ae4e-8bfff8681a02" />
ahora si iniciamos el servidor

## 3. Verificar que está funcionando:

```powershell
.\bin\pg_isready.exe
```
<img width="981" height="469" alt="image" src="https://github.com/user-attachments/assets/218128c3-5a12-472b-814f-80680e77c9de" />
revisamos que funcione correctamente

##  4. Conectarse:

```powershell
.\bin\psql.exe -U postgres
```
o

```powershell
.\bin\psql.exe -h localhost -U postgres
```
<img width="983" height="469" alt="image" src="https://github.com/user-attachments/assets/e1673c82-ed16-48ce-bac8-189875338116" />

ns q paso

### Verifica la versión

También conviene revisar qué versión descargaste:

```powershell
.\bin\postgres.exe --version
```

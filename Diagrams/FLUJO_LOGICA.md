 ## estructura del diagarma
```mermaid
graph TD
    A([Inicio: llamada al método vender]) --> B{¿cantidad > 0 y<br/>cantidad <= stock?}
    
    B -- Sí --> C[Restar cantidad al stock]
    C --> D[Retornar True]
    D --> E([Fin])
    
    B -- No --> F[Retornar False]
    F --> E
    ```

---
## prompt
[prompt utilizado](https://github.com/alvaroneira2233-prog/Recursos/tree/main/Diagrams)
---

 ## estructura del diagarma
```mermaid
graph TD
    A[inicio: llemada al metodo vender] --> B
    {¿cantidad<=stock?}
    B -- si --> C[Restar cantidad al stock]
    C -->D[imprimir: venta realizada y saldo actual]
    D --> E[fin]
    B -- no --> F[imprimir: stock insuficientes]
    F --> E
```







```

---
## prompt
[prompt utilizado](https://github.com/alvaroneira2233-prog/Recursos/tree/main/Diagrams)
---

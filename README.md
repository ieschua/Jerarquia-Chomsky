# Jerarquia-Chomsky

Según Noam Chomosky, hay cuatro tipos de gramáticas: tipo 0, tipo 1, tipo 2 y tipo 3.

Difieren de la siguiente manera:	 

| Tipo de gramatica  | Gramatica aceptada             | Autómata                   |
| ------------------ |:------------------------------:| --------------------------:|
| Tipo 0             | Gramática sin restricciones    | Máquina de Turing          |
| Tipo 1             | Gramática sensible al contexto | Autómata delimitado lineal |
| Tipo 2             | Gramática libre de contexto    | Autómata de empuje         |
| Tipo 3             | Gramática regular              | Autómata de estado finito  |

###  Tipo 0 - Gramática sin restricciones
Las producciones no tienen restricciones. Son cualquier gramática de estructura de fase, incluidas todas las gramáticas formales.
Generan los lenguajes que son reconocidos por una máquina de Turing.
Las producciones pueden ser en forma de α → β donde α es una cadena de terminales y no terminales con al menos un no terminal y α no puede ser nulo. β es una cadena de terminales y no terminales.

###  Tipo 1 - Gramática sensible al contexto
Las producciones deben estar en la forma
α A β → α γ β
donde A ∈ N (no terminal)
y α, β, γ ∈ (T ∪ N) * (Cadenas de terminales y no terminales)
Las cadenas α y β pueden estar vacías, pero γ no deben estar vacías.
La regla S → ε está permitida si S no aparece en el lado derecho de ninguna regla. Los lenguajes generados por estas gramáticas son reconocidos por un autómata acotado lineal.

###  Tipo 2 - Idiomas libres de contexto
Una gramática libre de contexto (CFG) es aquella cuyas reglas de producción son de la forma: 
Las producciones deben tener la forma A → γ
donde A ∈ N (no terminal)
y γ ∈ (T ∪ N) * (Cadena de terminales y no terminales).

###  Tipo 3 - Idiomas regulares
Como hemos comentado, un lenguaje regular es aquel que puede representarse mediante una gramática regular, describirse mediante una expresión regular o aceptarse mediante una NFA o DFA. 

### APLICACIÓN DEL PROGRAMA
Para poder usar el programa, se deben de tomar en cuenta varios elementos, los cuales veremos en un ejemplo:
	S -> abS
	S -> a
Donde:
  * Funciones de producción: 2
  * Simbolo inicial: S
  * Funcion 0:
  ``` Lado izquierdo de la función: S ```
  ``` Lado derecho de la función: abS ```
  * Funcion 1:
  ``` Lado izquierdo de la función: S ```
  ``` Lado derecho de la función: a ```
### RESULTADO: TIPO 3

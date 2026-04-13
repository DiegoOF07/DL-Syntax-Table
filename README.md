# First, Follow y Tabla de Análisis Sintáctico Predictivo

Implementación en Python de los algoritmos **FIRST**, **FOLLOW** y construcción de la **tabla de análisis sintáctico** para gramáticas libres de contexto.

---

## Cómo ejecutar

1. Clonar el repositorio
2. Localizar la raíz del proyecto
3. Ejecutar el siguiente comando

```bash
python main.py
```

El programa procesará automáticamente todos los archivos `.txt` dentro de la carpeta `grammars/` y, para cada uno, mostrará:

1. La gramática ingresada (símbolo inicial, producciones, terminales y no-terminales)
2. Los conjuntos FIRST de cada no-terminal
3. Los conjuntos FOLLOW de cada no-terminal
4. La tabla de análisis sintáctico
5. Si la gramática es LL(1) y, en caso contrario, los conflictos encontrados

---

## Formato de las gramáticas

Los archivos `.txt` en `/grammars` siguen este formato:

- El **primer no-terminal** que aparezca se toma como símbolo inicial.
- Se usa `->` para separar cabeza de cuerpo.
- Las alternativas se separan con `|`.
- La producción vacía se escribe como `ε`.
- Las líneas que comienzan con `#` son comentarios.

---


## Gramáticas probadas

### Gramática 1: Expresiones Aritméticas (Proveniente del documento)

```
E  -> T E'
E' -> + T E' | ε
T  -> F T'
T' -> * F T' | ε
F  -> ( E ) | id
```

**¿Es LL(1)?**  Sí

Esta gramática está diseñada específicamente para eliminar la ambigüedad y la recursión izquierda de la gramática de expresiones aritméticas, haciéndola apta para análisis predictivo. Se incluye porque es el ejemplo del curso.

#### Syntax table
|NT / T| id     | +        | *        | (      | )    | $    |
| --- | ------ | -------- | -------- | ------ | ---- | ---- |
| E   | E→T E' |          |          | E→T E' |      |      |
| E'  |        | E'→+T E' |          |        | E'→ε | E'→ε |
| T   | T→F T' |          |          | T→F T' |      |      |
| T'  |        | T'→ε     | T'→*F T' |        | T'→ε | T'→ε |
| F   | F→id   |          |          | F→(E)  |      |      |

### Gramática 2: Sentencias if-else 

```
S -> i E t S S' | a
S' -> e S | ε
E -> b
```

> Donde `i`=`if`, `t`=`then`, `e`=`else`, `a`=sentencia simple, `b`=condición booleana.

**¿Es LL(1)?**  No

**Conflicto detectado:**
Producción 1 | Producción 2 
S' → e S | S' → ε      

**Justificación de elección:** El problema del *dangling else* es un ejemplo clásico de gramática ambigua en el diseño de lenguajes. El conflicto en `[S', e]` ilustra perfectamente por qué muchos lenguajes deben definir explícitamente que el `else` pertenece al `if` más cercano.

---

### Gramática 3: Expresiones Booleanas

```
B -> A B'
B' -> or A B' | ε
A -> C A'
A' -> and C A' | ε
C -> not C | ( B ) | true | false
```

**¿Es LL(1)?** Sí

**Justificación de elección:** Esta gramática representa operadores booleanos (`and`, `or`, `not`) con la precedencia estándar (`not` > `and` > `or`). Se eligió ya que al igual que la primer gramática ha sido manipulada para eliminar la recursividad por la izquierda y es relativamente compleja reflejando que el patrón de la primer gramática no es un caso aislado.

#### Syntax table
| NT \ T | (       | )    | and         | false   | not     | or         | true   | $    |
| ------ | ------- | ---- | ----------- | ------- | ------- | ---------- | ------ | ---- |
| A      | A→C A'  |      |             | A→C A'  | A→C A'  |            | A→C A' |      |
| A'     |         | A'→ε | A'→and C A' |         |         |   A'→ε     |        | A'→ε |
| B      | B→A B'  |      |             | B→A B'  | B→A B'  |            | B→A B' |      |
| B'     |         | B'→ε |             |         |         | B'→or A B' |        | B'→ε |
| C      | C→( B ) |      |             | C→false | C→not C |            | C→true |      |

---

### Video con la explicación de youtube
[![Video con la explicación](https://img.youtube.com/vi/oL19SUQ4nEg/0.jpg)](https://youtu.be/oL19SUQ4nEg)

# **Proyecto Final - Simple Compiler**

## Índice 

1. [Tecnologías](#Tecnologías)
2. [Instrucciones](#Instrucciones)
3. [Proyecto Final](#Proyecto-Final)
4. [Requisitos](#Requisitos)
    1. [Operaciones Permitidas](#Operaciones-Permitidas)
        1. Aritméticas
        2. Booleanas
        3. Operaciones de bloques
        4. Un sistema de tipos
    2. [Operaciones permitidas entre el sistema de tipos](#Operaciones-permitidas-entre-el-sistema-de-tipos)
    3. [Flujos de control existentes](#Flujos-de-control-existentes)
    4. [Código de tres direcciones](#Código-de-tres-direcciones)

## **Tecnologías**

- Python 3
- [PLY](https://github.com/dabeaz/ply)

Para la parte de análisis sintáctico se podrá utilizar PLY es una implementación 100% Python de las herramientas de análisis lex y yacc. 

## **Instrucciones**

```
$ python3 compiler.py <file.txt>
```

## **Proyecto Final**

Como proyecto final crearemos un pequeño compilador, para un lenguaje que cuenta con las siguientes funcionalidades:

## **Requisitos**

### **Operaciones Permitidas**

- **Aritméticas**
    
    - Suma +
    - Resta -
    - Multiplicación *
    - División /
    - Exponenciación ^
    - Comparación:
    - ==
    - != 
    - \>
    - <
    - \>=
    - <=

- **Booleanas**

    - and 
    - or

- **Operaciones de bloques**

    - ( )
    - { }

- **Un sistema de tipos**

    - Int
    - Float
    - String
    - Bolean

### **Operaciones permitidas entre el sistema de tipos**

|          | int                     | float                   | string             | boolean      |
| :------: | :---------------------: | :---------------------: | :----------------: | :----------: |
| int      | Aritméticas Comparación | Aritméticas Comparación | + ( Concatenación )| and or == != |
| float    | Aritméticas Comparación | Aritméticas Comparación | + ( Concatenación )| and or == != |
| string   |                         |                         | + ( Concatenación )| == !=        |
|boolean   |                         |                         |                    | and or == != |

### **Flujos de control existentes** 

Deberán seguir una estructura similar al lenguaje C, por simplicidad todo deberán llevar llaves

- If, Else, Elif
- While () {}
- For (;;) {}
- Para marcar el final de una sentencia se utilizara ";"
- Es permitido el declarar y asignar una variable en la misma linea

### **Código de tres direcciones**

|               | Resultado | Dirección 1                     | Operador      | Dirección 2    | Ejemplo                        |
| :-----------: | :-------: | :-----------------------------: | :-----------: | :------------: | :----------------------------: |
| If            | Null      | Variable con condición booleana | IFGOTO        | Etiqueta       | v1 IFGOTO L1                   |
| * / + - ^	    | Variable  | Constant/value                  | * / + - ^     | Constant/value | t1 = 3 * 3,  t3 = t1 / t2      |
| toInt toFloat | Variable  | Const/variable                  | toInt toFloat | Null           | t2 = toInt t1, t2 = toFloat t1 |


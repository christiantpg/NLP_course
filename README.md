# 📚 Trabajos Prácticos - Procesamiento del Lenguaje Natural

Este repositorio contiene el desarrollo de los trabajos prácticos realizados para la materia **Procesamiento del Lenguaje Natural** cursada en la **FIUBA** durante el año **2025**.

---

## 👋 Contenido

- [Trabajo Práctico 1: Análisis de similitud de términos en un corpus](#trabajo-práctico-1-análisis-de-similitud-de-términos-en-un-corpus)
- [Trabajo Práctico 2: Armado de embeddings](#trabajo-práctico-2-armado-de-embeddings)
- [Trabajo Práctico 3: Generador de secuencias de texto por caracteres](#trabajo-práctico-3-generador-de-secuencias-de-texto-por-caracteres)
- [Trabajo Práctico 4: Bot conversacional](#trabajo-práctico-4-bot-conversacional)

---

## 🛠️ Herramientas utilizadas

- Python 3.12
- Bibliotecas principales: Pandas, Numpy, TensorFlow, Keras, FastText

---

## 📚 Trabajos Prácticos

### Trabajo Práctico 1: Análisis de similitud de términos en un corpus

El trabajo consistió en analizar diferentes documentos presentes en un corpus y encontrar similitudes entre ellos.

Se realizó un estudio de los términos presentes en cada documento para clasificarlos y agruparlos. Se utilizó un vectorizador **TF-IDF** y se compararon modelos de clasificación como **Naive Bayes Multinomial** y **Complement Naive Bayes**. Además, se utilizó **Optuna** para optimizar los hiperparámetros de los modelos.

Posteriormente, se eligieron términos al azar y se entrenó un modelo para encontrar los términos más relacionados.

[🔗 Link al notebook](desafio_1.ipynb)

---

### Trabajo Práctico 2: Armado de embeddings

A partir de un dataset del lore de un juego de cartas, se crearon embeddings personalizados para representar las palabras.

El objetivo del trabajo fue entender cómo los embeddings capturan más información semántica sobre las palabras que una representación basada únicamente en enteros.

Se realizó una representación gráfica de los vectores creados, observando que los embeddings no solo representaban numéricamente las palabras, sino que además preservaban las relaciones semánticas entre ellas.

[🔗 Link al notebook](desafio_2.ipynb)

---

### Trabajo Práctico 3: Generador de secuencias de texto por caracteres

Este trabajo consistió en generar nuevas secuencias de caracteres a partir de un corpus.

Se utilizó un dataset de letras del artista **Charly García**, con el objetivo de generar nuevos versos siguiendo el estilo del músico.

Aunque el modelo no alcanzó una generación totalmente coherente, logró producir palabras comunes en las letras del artista, mostrando un avance significativo. Se considera que con una mejor limpieza del corpus se podrían obtener resultados aún más satisfactorios.

El modelo utilizado fue una red **GRU** con capas de **Embedding** y **Dropout**. Como salida se empleó una capa **Dense** con activación **softmax**, lo que permitió ajustar la "temperatura" del modelo para controlar la creatividad en la generación.

[🔗 Link al notebook](desafio_3.ipynb)

---

### Trabajo Práctico 4: Bot conversacional

A partir de un corpus de mensajes en inglés entre usuarios y agentes, se desarrolló un **bot conversacional** capaz de responder como un agente.

Para ello, además de aplicar procesos de tokenización y padding, se utilizaron embeddings preentrenados (**FastText**).  
Se implementó una arquitectura **encoder-decoder** utilizando dos capas **LSTM**.

Se puso en práctica la elección de cada uno de los parámetros de configuración de cada una de las capas del modelo, así como las dimensiones de las entradas y las salidas. En el notebook podrán encontrar gráficos que ilustran estas configuraciones.

[🔗 Link al notebook](desafio_4.ipynb)

---

## 👨‍💻 Autor

- Christian Gabriel Pisani Testa
- christian.tpg@gmail.com
- [LinkedIn](https://www.linkedin.com/in/christianpisani/)

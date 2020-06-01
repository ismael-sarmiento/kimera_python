# ¿Qué es la serialización o marshalling?

* [Reference Link](https://codingornot.com/que-es-la-serializacion-o-marshalling)

La serialización es un proceso mediante el cual podemos convertir objetos de un programa en ejecución en flujos de bytes capaces de ser 
almacenados en dispositivos, bases de datos o de ser enviados a través de la red y, posteriormente, ser capaces de reconstruirlos en los equipos 
donde sea necesario. Al hablar de “objetos”, no me refiero únicamente al significado que estos tienen en la POO; un objeto es cualquier estructura 
de datos, función o método que esté en memoria.

Uno de los principales objetivos de la serialización es permitir crear flujos de bytes independientes de la arquitectura de los equipos en los 
que se utilicen, inclusive, que los objetos puedan ser reconstruidos en otros programas sin importar que el lenguaje con el que son escritos sea 
diferente al que se usó para crear el objeto originalmente.

Marshalling puede usarse como sinónimo de serialización, sin embargo, debes de tener cuidado porque en lenguajes de programación como Java, 
marshalling se refiere a la acción de almacenar el estado de un objeto junto con su código, mientras que serializar es solamente crear copias de 
objetos como flujos de bytes. El procedimiento inverso de la serialización es la deserialización o unmarshalling.

## Importancia de la serialización

La importancia que tiene este procedimiento no se limita al envío de bytes por la red. Son varias las razones por las que muchos lenguajes de 
programación como C, C++, Java, C#, Python y Perl (entre otros) han incluido paquetes, módulos o API enfocadas en serializar datos. En seguida 
señalo algunas de esas razones:

* Permite hacer llamados a procedimientos remotos (RPC).
* Sirve para identificar cambios de datos en ejecución.
* Podemos almacenar objetos en dispositivos de almacenamiento como discos duros.
* Si un programa en ejecución termina inesperadamente o detecta algún problema, puede cargar un respaldo completo o parcial.
* Permite intercambiar objetos entre programas independientes.

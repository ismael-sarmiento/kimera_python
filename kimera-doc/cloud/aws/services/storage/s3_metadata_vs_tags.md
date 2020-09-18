# S3 - Metadata vs Tags

* [Reference Link](https://stackoverflow.com/questions/42126348/difference-between-object-tags-and-object-metadata/42146207)
* [Metadatos del sistema almacenados en un bucket de S3](https://docs.aws.amazon.com/es_es/AmazonS3/latest/dev/UsingMetadata.html#object-metadata) 

Tanto los metadatos como las etiquetas son esencialmente "metadatos", pero existen diferencias importantes en cómo se pueden (o no) utilizar para
modificar el comportamiento del servicio y cómo se puede (o no) acceder a sus valores.

Un objeto en S3, incluidos sus metadatos, es, estrictamente hablando, inmutable. La consola le brinda la capacidad de "editar" metadatos, 
pero esa no es una descripción precisa de lo que está sucediendo. Cuando edita los metadatos de un objeto, en realidad está sobrescribiendo el 
objeto con una copia de sí mismo, con sus metadatos modificados. Si el depósito tiene una versión, ahora tiene dos copias del objeto con dos 
fechas diferentes y metadatos modificados.

Las etiquetas son un "subrecurso", en cierto sentido, "al lado" de un objeto, se administran por separado y se pueden modificar sin modificar el 
objeto en sí.

Puede controlar, por separado a través de política, si un usuario de IAM puede leer o escribir objetos + metadatos o etiquetas. Los objetos y 
los metadatos se manejan juntos en permisos (si puede hacer uno, siempre puede hacerlo con el otro) pero las etiquetas son permisos separados.

When you GET an object, the actual metadata is returned in the HTTP response headers. This means a user downloading an object can see the metadata
if they know how to inspect the HTTP headers.

Por el contrario, las etiquetas no se devuelven en los encabezados en respuesta a una solicitud GET; en su lugar, solo se devuelve el encabezado 
`x-amz-tagging-count:`, que informa el número de etiquetas en el objeto si no es cero. Sin embargo, tenga en cuenta que, si bien las etiquetas 
son más apropiadas para almacenar datos patentados, no lo son para almacenar datos confidenciales no cifrados.

El total de todas las claves y valores de metadatos para cada objeto está limitado a 2 KB. Tenga en cuenta que el límite se expresa en bytes, 
por lo que los caracteres multibyte consumen más de un byte por carácter hacia el límite. No hay límite en la cantidad de claves de metadatos, 
solo el límite total de 2 KB para los metadatos del usuario. Solo los caracteres US-ASCII son totalmente compatibles con las claves y valores de 
metadatos de objetos, y los metadatos deben estar compuestos por caracteres que sean válidos como encabezados HTTP, ya que así es como se envían 
los metadatos de objetos.

Los límites de las etiquetas son diferentes. Cada objeto puede tener hasta 10 etiquetas, cada clave de etiqueta está limitada a 128 caracteres 
(no bytes) y cada valor de etiqueta está limitado a 256 caracteres (no bytes), aunque los límites son menores, como se indicó anteriormente, 
cuando las etiquetas se montan junto con la solicitud PUT. A diferencia de los metadatos, las etiquetas admiten UTF-8.

Las claves y valores de metadatos se cuentan como bytes facturables que contribuyen al tamaño facturado del almacenamiento de objetos. 
Las etiquetas se facturan por separado con un foro diferente.

No se pueden utilizar etiquetas ni metadatos para "escanear" objetos. No es posible solicitar al servicio S3 una lista de objetos con etiquetas 
específicas o con metadatos específicos.

## Las políticas de IAM sobre buckets / users / roles pueden usar valores de tags (etiquetas) con fines de control de acceso, pero no pueden usar valores de metadatos.

Hay claves de condición de política de IAM que permiten el control de acceso a objetos basados en etiquetas. No existen funciones de control de 
acceso similares basadas en metadatos.

* [Reference Link](https://docs.aws.amazon.com/es_es/AmazonS3/latest/dev/object-tagging.html)

## Las políticas del ciclo de vida del bucket pueden usar los valores de los tags (etiquetas), pero no los de los metadatos.

Las políticas del ciclo de vida se pueden utilizar para modificar la clase de almacenamiento de un objeto (a estándar / acceso poco frecuente o 
glaciar) o purgar objetos o versiones después de un intervalo de tiempo configurable. Antes de la introducción de las etiquetas de objeto, estas
reglas se aplicaban a todo el depósito o a un determinado prefijo, como imágenes /. Ahora, las etiquetas permiten aplicar políticas de ciclo de 
vida basadas en etiquetas de objeto, por lo que (por ejemplo) los datos transitorios se pueden mezclar con datos permanentes mientras se aplican 
políticas de ciclo de vida de manera diferente sin la necesidad de almacenar los objetos en diferentes jerarquías de claves para la coincidencia 
de prefijos.




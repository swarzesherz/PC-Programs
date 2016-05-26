.. es_how_to_generate_xml-markup:

===================
Cómo usar el Markup
===================

Introducción
============

Este manual tiene como objetivo presentar el uso del programa de marcación `Markup <markup.html>`_ 


.. _sugestao-id:

Recomendaciones para asignar el atributo "ID"
=============================================

El atributo "ID" se usa para identificar algunos elementos como figuras, tablas, afiliaciones, etc. Este atributo permite establecer referencias cruzadas entre la mención del elemento en el texto y el elemento en sí. 
Para determinar el "ID" de un elemento, combine el prefijo del tipo de elemento y un número entero como se muestra a continuación:

+------------------------+---------------------------+---------+---------------------+
| Elemento XML           | Descripción               | Prefijo | Ejemplo             |
+========================+===========================+=========+=====================+
| aff                    | Afiliación                | aff     | aff1, aff2, ...     |
+------------------------+---------------------------+---------+---------------------+
| app                    | Apéndice                  | app     | app1, app2, ...     |
+------------------------+---------------------------+---------+---------------------+
| author-notes/fn |      | Notas de pie del artículo | fn      | fn1, fn2, ...       | 
| fn-group/fn            |                           |         |                     |
+------------------------+---------------------------+---------+---------------------+
| boxed-text             | Caja de texto             | bx      | bx1, bx2, ...       |
+------------------------+---------------------------+---------+---------------------+
| corresp                | Correspondencia           | c       | c1, c2, ...         |
+------------------------+---------------------------+---------+---------------------+
| def-list               | Lista de Definiciones     | d       | d1, d2, ...         |
+------------------------+---------------------------+---------+---------------------+
| disp-formula           | Ecuaciones                | e       | e1, e2, ...         |
+------------------------+---------------------------+---------+---------------------+
| fig                    | Figuras                   | f       | f1, f2, ...         |
+------------------------+---------------------------+---------+---------------------+
| glossary               | Glosario                  | gl      | gl1, gl2, ...       |
+------------------------+---------------------------+---------+---------------------+
| media                  | Media                     | m       | m1, m2, ...         |
+------------------------+---------------------------+---------+---------------------+
| ref                    | Referencia bibliográfica  | B       | B1, B2, ...         |
+------------------------+---------------------------+---------+---------------------+
| sec                    | Secciones                 | sec     | sec1, sec2, ...     |
+------------------------+---------------------------+---------+---------------------+
| sub-article            | sub-artículo              | S       | S1, S2, ...         |
+------------------------+---------------------------+---------+---------------------+
| supplementary-material | Suplemento                | suppl   | suppl1, suppl2, ... |
+------------------------+---------------------------+---------+---------------------+
| table-wrap-foot/fn     | Notas de pie de tabla     | TFN     | TFN1, TFN2, ...     |
+------------------------+---------------------------+---------+---------------------+
| table-wrap             | Tabla                     | t       | t1, t2, ...         |
+------------------------+---------------------------+---------+---------------------+



.. _dados-basicos:

Datos Básicos
=============

Estando el archivo del documento formateado de acuerdo con las indicaciones del manual `Preparación de Archivos para el Programa Markup <es_how_to_generate_xml-prepara.html>`_ , abra el documento en el programa `Markup <markup.html>`_ y seleccione el elemento [doc]:

.. image:: img/doc-mkp-formulario.jpg
   :height: 400px
   :align: center


Al hacer clic en [doc] el programa abrirá un formulario para ser completado con los datos básicos del artículo:

Seleccione la revista en el campo "collection/journal", el programa llenará algunos datos automáticamente como ISSNs, título abreviado, acrónimo, entre otros. Los demás datos deberán llenarse manualmente de acuerdo con las siguientes indicaciones:


+-------------------+-----------------------------------------------------------------------------------------------+
| Campo             | Descripción                                                                                   |
+===================+===============================================================================================+
| license           | Si no se inserta automáticamente, llene con la URL de la licencia creative commons            |
|                   | adoptada por la revista. Consulte las licencias en:                                           |
|                   | http://docs.scielo.org/projects/scielo-publishing-schema/                                     |
+-------------------+-----------------------------------------------------------------------------------------------+
| volid             | Inserte volumen, si lo hay. Para Ahead of Print, no incluya volumen                           |
+-------------------+-----------------------------------------------------------------------------------------------+
| supplvol          | Cuando se trate de un suplemento de volumen incluya su parte o número correspondiente.        |
|                   | **Ejemplo: vol.12 supl.A**, llene con **A**, este campo                                       |
+-------------------+-----------------------------------------------------------------------------------------------+
| issueno           | Ingrese el número del fascículo. Cuando se trate de un artículo publicado en ahead of         |
|                   | print, inserte ahead en este campo                                                            |
+-------------------+-----------------------------------------------------------------------------------------------+
| supplno           | En caso de que sea un suplemento de fascículo incluya su parte o número                       |
|                   | correspondiente. **Ejemplo: n.37, supl.A**, llene con **A** en este campo                     |
+-------------------+-----------------------------------------------------------------------------------------------+
| isidpart          | Úselo en casos de press release, incluya la sigla pr                                          |
+-------------------+-----------------------------------------------------------------------------------------------+
| dateiso           | Fecha de publicación formada por año, mes y día **(YYYYMMDD)**. Llene siempre                 |
|                   | con el último mes de la periodicidad. Por ejemplo, si la revista es bimensual                 |
|                   | escriba **20140600**. Use **00** para mes y día cuando no se cuente con esta                  |
|                   | información. **Ejemplo: 20140000**.                                                           |
+-------------------+-----------------------------------------------------------------------------------------------+
| month/season      | Ingrese el mes o mes inicial/mes final, en inglés (tres letras) y punto,                      |
|                   | excepto para May, June y July. **Ej.: May/June, July/Aug.**                                   |
+-------------------+-----------------------------------------------------------------------------------------------+
| fpage             | Primera página del documento. Para artículo en Ahead of Print, incluya 00                     |
+-------------------+-----------------------------------------------------------------------------------------------+
| @seq              | Para artículos que inician en la misma página de un artículo anterior, incluya la             |
|                   | secuencia con letra                                                                           |
+-------------------+-----------------------------------------------------------------------------------------------+
| lpage             | Ingrese la última página del documento.                                                       |
+-------------------+-----------------------------------------------------------------------------------------------+
| elocatid          | Incluya la identificación electrónica del documento. En este caso no llenar fpage y lpage     |
+-------------------+-----------------------------------------------------------------------------------------------+
| order (in TOC)    | Incluya el orden del artículo en la tabla de contenido del fascículo. Debe tener, como        |
|                   | mínimo dos dígitos. Por ejemplo, si el artículo fuera el primero de la tabla de contenido,    |
|                   | llene este campo con **01** y así en adelante.                                                |
+-------------------+-----------------------------------------------------------------------------------------------+
| pagcount*         | Inserte las páginas totales del artículo. Para Ahead of Print, escriba el valor 1             |
+-------------------+-----------------------------------------------------------------------------------------------+
| doctopic*         | Indique el tipo de documento que se va a marcar. Por ejemplo: artículo original, reseña,      | 
|                   | carta, comentario etc. En el caso de Ahead Of Print, incluya siempre el tipo artículo         |
|                   | original, excepto para errata                                                                 |
+-------------------+-----------------------------------------------------------------------------------------------+
| language*         | Seleccione el idioma principal del texto a ser marcado                                        |
+-------------------+-----------------------------------------------------------------------------------------------+
| version*          | Identifique la versión de la DTD usada en el proceso de marcación (La versión actual es 4.0)  |
+-------------------+-----------------------------------------------------------------------------------------------+
| artdate (rolling) | Es obligatorio escribir la fecha **YYYYMMDD** cuando se trate de un artículo rolling pass.    |
|                   | Rolling pass es un modelo publicación dónde la revista publica sus artículos en un volumen    |
|                   | único conforme estos quedan listos                                                            |
+-------------------+-----------------------------------------------------------------------------------------------+
| ahpdate           | Indicar la fecha de publicación de un artículo publicado en ahead of print                    |
+-------------------+-----------------------------------------------------------------------------------------------+


.. note:: Los campos que tienen un asterisco al lado, son obligatorios.


.. _front:

Front
=====

Una vez que se completó el llenado del formulario, al hacer clic en [Ok] se abrirá una ventana preguntando si el documento tiene el formato adecuado para efectuar la marcación automática:

.. image:: img/doc-mkp-mkp-automatic.jpg
   :height: 450px
   :align: center


Al hacer clic en [Sí], el programa realizará la marcación automática de los elementos básicos del documento.

.. image:: img/doc-mkp-mkp--auto.jpg
   :height: 400px
   :width: 300px
   :align: center


.. note:: Cuando el archivo no tenga el formato recomendado en "Preparación de Archivos para el Programa Markup", el programa 
          no identificará correctamente los elementos.



Después de la marcación automática es necesario completar la marcación de los elementos básicos. 


.. _titulo:

Doctitle
--------

Confiera el idioma inserido en [doctitle] para títulos traducidos y, si necesario, corrija.
Para corregir, seleccione el elemento "incorrecta" y haga un clic en el  "lápiz" para editar los atributos:


.. image:: img/doc-mkp-language-doctitle.jpg
   :height: 400px
   :align: center

Haga el mismo para los demás títulos traducidos.


.. _autores:

Autores
-------

Algunos autores presentan más que 1 label al lado del nombre, sin embargo el programa no hace la marcación automática de más que 1 label. De esa forma, seleccione el label del autor y marque con el elemento [xref].


.. image:: img/doc-mkp-xref-label.jpg
   :height: 300px
   :align: center

Por si tratar de referencia cruzada (xref) de afiliación, el tipo de xref (ref-type) seleccionado fue el "affiliation" y el rid (relacionado al ID) "aff3" para relacionar el label 3 a la afiliación correspondiente.

El programa Markup no hace marcación automática de función de autor cómo, por ejemplo, el cargo ejercido. Para eso, es necesario seleccionar el dato que consta al lado del nombre del autor, ir para el nivel inferior del elemento [author] e identificar ese dato con el elemento [role].

.. image:: img/doc-mkp-role-author.jpg
   :height: 230px
   :align: center


.. image:: img/doc-mkp-mkp-role-author.jpg
   :height: 230px
   :align: center


.. note:: el programa no identifica automáticamente símbolos o letras como label, la cual debe ser marcada manualmente, observándose 
          el tipo de referencia cruzada a ser incluida.


.. raw:: html

   <iframe width="640" height="360" src="https://www.youtube.com/embed/R8YYjXZSk1c?list=PLQZT93bz3H79NTc-aUFMU_UZgo4Vl2iUH" frameborder="0" allowfullscreen></iframe>


.. _sigblock:

Sig-block
=========

Generalmente archivos Editoriales, Presentaciones etc. poseen al final del texto la asignatura del autor o editor.
Para identificar la asignatura del autor, sea en imagen, sea en texto, es necesario seleccionar la asignatura e identificar con el elemento [sigblock]:

.. image:: img/mkp-sigblock-select.jpg
   :height: 200px
   :align: center

Seleccione apenas la asignatura e identifique con el elemento [sig]:

.. image:: img/mkp-sigblock-sig.jpg
   :height: 180px
   :align: center

Sigue el resultado de la identificación de asignatura del autor/editor:

.. image:: img/mkp-result-sigblock.jpg
   :height: 150px
   :align: center

.. note:: Algunas asignaturas presentan al lado del nombre del autor su cargo o función. Para la identificación de [sig], no considerar la función.


.. _onbehalf:

On Behalf
=========

El elemento [on-behalf] es utilizado cuando un autor ejerce papel de representante de un grupo o institución. 
Para identificar ese dato, verifique se la información del representante del grupo está en la misma línea del autor anterior. Ejemplo:


    Fernando Augusto Proietti :sup:`2`  Interdisciplinary HTLV Research Group


El programa identificará el autor "Fernando Augusto Proietti" de la siguiente manera:

.. image:: img/mkp-on-behalf.jpg
   :height: 150px
   :align: center


Seleccione el nombre del grupo o institución e identifique con el elemento: [onbehalf]:

.. image:: img/mkp-tag-onbehalf.jpg
   :height: 150px
   :align: center


Contrib-ID
==========

Autores que presentan registro en el ORCID o en el Lattes deben inserir el link de registro al lado del nombre, después el label del autor:

.. image:: img/mkp-contrib-id.jpg
   :height: 230px
   :align: center

Al hacer la marcación de [doc] el programa identificará automáticamente todos los datos iniciales del documento, inclusive marcará en [author] el link de registro.
Aún que el programa incluya el link en el elemento [author], será necesario completar la marcación de ese dado.

Para eso, entre en el nivel de [autor], seleccione el link del autor  y haga un clic en [author-id].
En la ventana abierta por el programa, seleccione el tipo de registro del autor: si lattes o ORCID  y haga un clic en [Continuar]

.. image:: img/mkp-marcando-id-contrib.jpg
   :height: 230px
   :align: center



.. _afiliación:

Afiliaciones
------------

El programa Markup hace la identificación solo del grupo de datos de cada afiliación con el elemento [normaff], o sea, la marcación detallada de las afiliaciones no es hecha automáticamente.
Complete la marcación de las afiliaciones identificando: institución mayor [orgname], división 1 [orgdiv1], división 2 [orgdiv2], ciudad [city], estado [state] (eses 4 últimos, si presentes) y el país [country].

Para hacer la identificación de los elementos arriba, va al nivel inferior del elemento [normaff] y haga la marcación detallada de cada afiliación.


.. image:: img/doc-mkp-detalhamento-aff.jpg
   :height: 350px
   :align: center


En la sequencia, será necesario verificar se la institución marcada y su país correspondiente, posee forma normalizada por SciELO. Para eso, seleccione el elemento [normaff]  y haga un clic en el "lápiz" para editar los atributos. El programa abrirá una ventana para la normalización de los elementos indicados en los campos en blanco.


.. image:: img/doc-mkp-normalizacao-aff.jpg
   :height: 350px
   :align: center



En el campo "icountry" seleccione el país de la institución mayor (orgname), en seguida haga un clíc en "find" para encontrar la institución normalizada. Al hacer ese procedimiento, el programa Markup consultará nuestra base de datos de instituciones normalizadas y verificará si la institución seleccionada consta en la lista.


.. image:: img/doc-mkp-normalizadas.jpg
   :height: 350px
   :align: center



.. image:: img/doc-mkp-aff.jpg
   :height: 150px
   :align: center



.. note:: Haga la búsqueda por el idioma de origen de la institución, excepto para lenguas no latinas, cuando la consulta deberá ser hecha en inglés. Caso la institución no exista en la lista del Markup, seleccione el elemento "No match found"  y haga un clic en [OK].


.. _resumen:

Resúmenes
=========

Los resúmenes deben ser identificados manualmente. Para marcación de resúmenes simples (sin secciones) e para los resúmenes estructurados (con secciones) utilizar el elemento [xmlabstr]. En la marcación, seleccione el título del resumen y el texto y, en seguida, marque con el elemento [xmlabstr].

Resumen sin Sección:
--------------------

**seleccionando:** 

.. image:: img/doc-mkp-select-abstract-s.jpg
   :height: 350px
   :align: center


Cuando cliquear en [xmlabstr] el programa abrirá una ventana donde si debe seleccionar el idioma del resumen marcado:


**marcación:** 

.. image:: img/doc-mkp-idioma-resumo.jpg
   :height: 350px
   :width: 450px
   :align: center


**Resultado**

.. image:: img/doc-mkp-mkp-abstract.jpg
   :align: center


Ya en resúmenes estructurados, el programa también marcará cada sección del resumen y sus respectivos párrafos.


Resumen con Sección:
--------------------

Siga los mismos pasos descriptos para resumen sin sección:


**seleccionando:** 

.. image:: img/doc-mkp-select-abstract.jpg
   :align: center


**marcación:**
		  
.. image:: img/doc-mkp-idioma-abstract.jpg
   :height: 400px
   :align: center


**Resultado**

.. image:: img/doc-mkp-mkp-resumo.jpg
   :align: center


.. raw:: html

   <iframe width="640" height="360" src="https://www.youtube.com/embed/FVTjDOIGV0Y?list=PLQZT93bz3H79NTc-aUFMU_UZgo4Vl2iUH" frameborder="0" allowfullscreen></iframe>


.. _palabra-clave:

Keywords
========

El programa Markup presenta dos íconos para identificación de palabras-clave, [* kwdgrp] e [kwdgrp].
El ícono [*kwdgrp], con asterisco, es utilizado para marcación automática de cada palabra-clave y también del título. Para eso, seleccione toda la información, incluso el título, e identifique los datos con el elemento [*kwdgrp].


Marcación Automática:
---------------------

**seleccionando:**
 
.. image:: img/doc-mkp-select-kwd.jpg
   :height: 300px
   :align: center


En la ventana abierta por el programa, seleccione el idioma de las palabras-clave marcadas:


**marcación:** 

.. image:: img/doc-mkp-mkp-kwd.jpg
   :height: 300px
   :align: center


.. image:: img/doc-mkp-kwd-grp.jpg
   :height: 100px
   :align: center




Marcación Manual:
-----------------

Caso la marcación automática no ocurra conforme el esperado, si puede marcar el grupo de palabras-clave manualmente. Seleccione el grupo de palabras-clave y marque con el elemento [kwdgrp].


**marcación:**

.. image:: img/doc-mkp-selection-kwd-s.jpg
   :height: 350px
   :align: center



En seguida, haga la marcación de ítem por ítem. Por lo tanto, seleccione el título de las palabras-clave e identifique con el elemento [sectitle]:

.. image:: img/doc-mkp-sec-kwd.jpg
   :height: 300px
   :align: center


En la secuencia, seleccione palabra por palabra y marque con el elemento [kwd]:

.. image:: img/doc-mkp-kwd-kwd.jpg
   :height: 300px
   :align: center



.. raw:: html

   <iframe width="640" height="360" src="https://www.youtube.com/embed/6sNTlHF8WdU?list=PLQZT93bz3H79NTc-aUFMU_UZgo4Vl2iUH" frameborder="0" allowfullscreen></iframe>


.. _historico:

History
=======

El elemento [hist] es utilizado para marcar el histórico del documento. Seleccione todo el dato de histórico y marque con el elemento [hist]:


.. image:: img/doc-mkp-hist-select.jpg
   :height: 250px
   :align: center



Seleccione la fecha de recibido y marque con el elemento [received]. Confiera la fecha ISO indicada en el campo dateiso y corrija, se necesario. La estructura de la fecha ISO esperada es:
AÑO MES DÍA. 

.. image:: img/doc-mkp-received.jpg
   :height: 350px
   :align: center


Caso haya la fecha de revisado, selecciónela y marque con el elemento [revised]. Haga el mismo para la fecha de acepto; seleccionando el elemento [accepted]. Confiera la fecha ISO indicada en el campo dateiso y corrija, se necesario.

.. image:: img/doc-mkp-accepted.jpg
   :height: 350px
   :align: center


.. raw:: html

   <iframe width="640" height="360" src="https://www.youtube.com/embed/w4Bw7dXpS0E?list=PLQZT93bz3H79NTc-aUFMU_UZgo4Vl2iUH" frameborder="0" allowfullscreen></iframe>
   


.. _correspondencia:

Correspondencia
===============

Con el elemento [corresp] es posible marcar los datos de correspondencia del autor. Ese elemento posee un subnivel para identificación del e-mail del autor. Seleccione toda la información de correspondencia y marque con el elemento [corresp]. Será presentada una ventana para marcación del ID de correspondencia que, en ese caso, debe ser "c" + el número de orden de la correspondencia.

.. image:: img/doc-mkp-corresp-select.jpg
   :height: 300px
   :align: center


Seleccione el e-mail del autor correspondiente y marque con el elemento [email]. Suba un nivel para marcar el próximo elemento.

.. image:: img/doc-mkp-email-corresp.jpg
   :height: 300px
   :align: center

.. raw:: html

   <iframe width="560" height="315" src="https://www.youtube.com/embed/fuzSrOMlSvo?list=PLQZT93bz3H79NTc-aUFMU_UZgo4Vl2iUH" frameborder="0" allowfullscreen></iframe>

.. _ensayo-clinico:

Ensayo Clínico
==============

Archivos que presentan información de ensayo clínico con número de registro, deben ser marcados con el elemento [cltrial]:

.. image:: img/doc-mkp-tag-cltrial.jpg
   :height: 150px
   :align: center


En la ventana abierta por el programa, llene el campo de URL de la base de datos donde el Ensayo fue indexado y el campo "ctdbid" seleccionando la base correspondiente:

.. image:: img/doc-mkp-clinicaltr.jpg
   :height: 300px
   :align: center

Para encontrar la URL del ensayo clínico haga una búsqueda en la internet por el número de registro para llenar el atributo conforme ejemplo que sigue.

.. image:: img/doc-mkp-ensaio.jpg
   :height: 80px
   :align: center

.. note:: Comúnmente la información de Ensayo clínico está posicionada bajo los resúmenes o palabras-clave.


.. raw:: html

   <iframe width="560" height="315" src="https://www.youtube.com/embed/0bln_fugnAA?list=PLQZT93bz3H79NTc-aUFMU_UZgo4Vl2iUH" frameborder="0" allowfullscreen></iframe>


.. _referencias:

Referencias
===========

As referencias bibliográficas son marcadas elemento por elemento y su formato original es mantenido para presentación en el sitio del SciELO.

El programa marcará todas las referencias seleccionadas con el elemento [ref] del tipo [book]. El cambio del tipo de referencia será manual o automática, dependiendo del tipo de elemento marcado, conforme será observado más adelante.


.. image:: img/doc-mkp-select-refs-mkp.jpg
   :height: 400px
   :align: center



.. image:: img/doc-mkp-mkp-refs.jpg
   :height: 400px
   :align: center

.. raw:: html

   <iframe width="560" height="315" src="https://www.youtube.com/embed/MoTVIJk21UM?list=PLQZT93bz3H79NTc-aUFMU_UZgo4Vl2iUH" frameborder="0" allowfullscreen></iframe> 


.. _tipos-de-referencias:

Tipos de Referencias
--------------------

A partir de la marcación hecha, algunos tipos de referencia serán alterados automáticamente sin intervención manual (ex.: tesis, conferencia, informes, patente y artículo de revista); ya para los demás casos, será necesario el cambio manual.
Para alterar el tipo de referencia haga un clíc en el elemento [ref], en seguida, en el lápiz "Editar Atributos" y en "reftype" para seleccionar el tipo correcto.

.. image:: img/doc-mkp-edit-ref-type.jpg
   :height: 400px
   :align: center


.. image:: img/doc-mkp-ref-editado-legal-doc.jpg
   :height: 150px
   :width: 400px
   :align: center


Recomiéndese la edición de "reftype" solamente **después** de marcar todos los elementos de la [ref], pues dependiendo de los elementos marcados el "reftype" será cambiado automáticamente por el Markup. 

.. note:: Una referencia debe tener su tipología siempre basada en el su contenido y nunca en su suporte. Por ejemplo, una ley representa un documento legal, sin embargo el tipo de referencia es "legal-doc", mismo que esté publicado en un jornal o sitio. Una referencia de artículo de una revista científica, mismo que publicado en un sitio posee el tipo "journal". 
          Es importante entender estos aspectos en las referencias para poder interpretar su tipología e sus elementos. Ni toda referencia que posee un enlace es una "webpage", ni toda la referencia que posee un volumen es un "journal", libros también pueden tener volúmenes.


Adelante los tipos de referencia suportados por SciELO y la marcación de cada [ref].


.. _tese:

Thesis
^^^^^^

Utilizada para referenciar monografías, tesis para obtención de un grado académico, tales como libre-docencia, doctorado, maestría etc. La seleción del elemento [thesgrp] determinará el cambio del tipo de [book] para [thesis]. Ex:


   *PINHEIRO, Fernanda Domingos. A defesa da liberdade: libertos e livres de cor nos tribunais do Antigo Regime portugues (Mariana e Lisboa, 1720-1819). Tese de doutorado, Departamento de História, Instituto de Filosofia e Ciencias Humanas, Universidade Estadual de Campinas, 2013*

.. image:: img/doc-mkp-ref-thesis.jpg
   :height: 200px
   :align: center



.. raw:: html

   <iframe width="560" height="315" src="https://www.youtube.com/embed/h1ytjcXZv5U?list=PLQZT93bz3H79NTc-aUFMU_UZgo4Vl2iUH" frameborder="0" allowfullscreen></iframe>


.. _conferencia:

Confproc
^^^^^^^^
Utilizada para referenciar documentos relacionados a eventos: atas, anales, convenciones, conferencias entre otros. Al marcar el elemento [confgrp] el programa cambiará el tipo de referencia para [confproc]. Ex.:


   *FABRE, C. Interpretation of nominal compounds: combining domain-independent and domain-specific information. In: INTERNATIONAL CONFERENCE ON COMPUTATIONAL LINGUISTICS (COLING), 16, 1996, Stroudsburg. Proceedings... Stroudsburg: Association of Computational Linguistics, 1996. v.1, p.364-369.*


.. image:: img/doc-mkp-ref-confproc.jpg
   :height: 250px
   :align: center


.. raw:: html

   <iframe width="560" height="315" src="https://www.youtube.com/embed/k0OWNjboFWE?list=PLQZT93bz3H79NTc-aUFMU_UZgo4Vl2iUH" frameborder="0" allowfullscreen></iframe>



.. _relatorio:

Report
^^^^^^

Utilizada para referenciar informes técnicos, normalmente de autoría institucional. Al marcar el elemento [reportid] el programa cambiará el tipo de referencia para [report]. Ex.:


   *AMES, A.; MACHADO, F.; RENNÓ, L. R. SAMUELS, D.; SMITH, A.E.; ZUCCO, C. The Brazilian Electoral Panel Studies (BEPS): Brazilian Public Opinion in the 2010 Presidential Elections. Technical Note No. IDB-TN-508, Inter-American Debelopment Bank, Department of Research and Chief Economist, 2013.*


.. image:: img/doc-mkp-ref-report.jpg
   :height: 250px
   :align: center

.. note:: En los casos en que no haya número de informe, el cambio del tipo de referencia deberá ser hecha manualmente.


.. _patente:

Patent
^^^^^^

Utilizada para referenciar patentes; la patente representa un título de propiedad que confiere a su titular el derecho de impedir terceros exploraren su creación. Ej.:


   *SCHILLING, C.; DOS SANTOS, J. Method and Device for Linking at Least Two Adjoinig Work Pieces by Friction Welding, U.S. Patent WO/2001/036144, 2005.*

.. image:: img/doc-mkp-patent.jpg
   :align: center


.. raw:: html

   <iframe width="560" height="315" src="https://www.youtube.com/embed/4BffTcmIkF8?list=PLQZT93bz3H79NTc-aUFMU_UZgo4Vl2iUH" frameborder="0" allowfullscreen></iframe>


.. _libro:

Book
^^^^

Utilizada para referenciar libros o parte de ellos (capítulos, tomos, series etc), manuales, guías, catálogos, enciclopedias, diccionarios entre otros.
Ex.: 

   *LORD, A. B. The singer of tales. 4th. Cambridge: Harvard University Press, 1981.*


.. image:: img/doc-mkp-ref-book.jpg
   :height: 180px
   :align: center


.. raw:: html

   <iframe width="560" height="315" src="https://www.youtube.com/embed/geq2_UgMYa0?list=PLQZT93bz3H79NTc-aUFMU_UZgo4Vl2iUH" frameborder="0" allowfullscreen></iframe>



.. _libro-inpress:

Book en press
^^^^^^^^^^^^^

Libros finalizados, pero aún no publicados presentan la información "no prelo", "forthcomming" o ""in press"" normalmente al final de la referencia. En ese caso, la marcación será hecha conforme sigue:


   *CIRENO, F.; LUBAMBO, C. Estratégia eleitoral e eleiciones para Câmara dos Deputados no Brasil en 2006, no prelo.*

.. image:: img/doc-mkp-ref-book-no-prelo.jpg
   :height: 180px
   :align: center

.. raw:: html

   <iframe width="560" height="315" src="https://www.youtube.com/embed/P2fiGsmitqM?list=PLQZT93bz3H79NTc-aUFMU_UZgo4Vl2iUH" frameborder="0" allowfullscreen></iframe>


.. _capitulo-de-libro:

Book Chapter
^^^^^^^^^^^^

División de un libro (título del capítulo e sus respectivos autores, si haya, seguido del título del libro y sus autores) numerado o no


   *Lastres, H.M.M.; Ferraz, J.C. Economia da información, do conhecimento e do aprendizado. In: Lastres, H.M.M.; Albagli, S. (Org.). Informaciónn e globalización na era do conhecimento. Rio de Janeiro: Campus, 1999. p.27-57.*

.. image:: img/doc-mkp-ref-chapter-book.jpg
   :height: 300px
   :align: center


.. _revista:

journal
^^^^^^^

Utilizada para referenciar publicaciones seriadas científicas, como revistas, boletins y jornales, editadas en unidades sucesivas, con designación numéricas e/o cronológicas y destinada a ser continuada indefinidamente. Al marcar [arttile-title] el programa cambiará el tipo de referencia para [journal]. Ex.:


   *Cardinalli, I. (2011). A saúde e a doença mental segundo a fenombrenologia existencial. Revista da Associación Brasileira de Daseinsanalyse, São Paulo, 16, 98-114.*

.. image:: img/doc-mkp-ref-journal.jpg
   :height: 200px
   :align: center


.. raw:: html

   <iframe width="560" height="315" src="https://www.youtube.com/embed/2gD6Ej1v0h4?list=PLQZT93bz3H79NTc-aUFMU_UZgo4Vl2iUH" frameborder="0" allowfullscreen></iframe>



En las referencias que siguen, su tipo deberá ser cambiado manualmente de [book] para el tipo correspondiente.


.. _ley:

legal-doc
^^^^^^^^^

Utilizada para referenciar documentos jurídicos, incluyen datos acerca de legislación y  jurisprudencia. Ej.:


   *Brasil. Portaria en el 1169/GM en 15 de junho de 2004. Institui a Política Nacional de Atención Cardiovascular de Alta Complexidade, e dá outras providencias. Diário Oficial 2004; seción 1, n.115, p.57.*

.. image:: img/doc-mkp-ref-legal-doc1.jpg
   :height: 180px
   :align: center


.. _jornal:

Newspaper
^^^^^^^^^

Utilizada para referenciar publicaciones seriadas sin cuño científico, como magazines e jornales. Ex.:


   *TAVARES de ALMEIDA, M. H. "Mais do que meros rótulos". Artigo publicado no Jornal Folha de S. Paulo, en el día 25/02/2006, na coluna Opinião, p. A. 3.*

.. image:: img/doc-mkp-newspaper.jpg
   :align: center


.. _base-de-dados:

Database
^^^^^^^^ 

Utilizada para referenciar bases y bancos de datos. Ex.:


	*IPEADATA. Disponivel em: http://www.ipeadata.gov.br.  Acesso em: 12 fev. 2010.*

.. image:: img/doc-mkp-ref-database.jpg
   :height: 100px
   :align: center


.. raw:: html

   <iframe width="560" height="315" src="https://www.youtube.com/embed/yXr97tNjDXA?list=PLQZT93bz3H79NTc-aUFMU_UZgo4Vl2iUH" frameborder="0" allowfullscreen></iframe>

.. _software:

Software
^^^^^^^^

Utilizada para referenciar un software, un programa de computador. Ex.:


	*Nelson KN. Comprehensive body composition software [computer program on disk]. Release 1.0 for DOS. Champaign (IL): Human Kinetics, c1997. 1 computer disk: color, 3 1/2 in.*

.. image:: img/doc-mkp-ref-software.jpg
   :height: 200px
   :align: center

.. raw:: html

   <iframe width="560" height="315" src="https://www.youtube.com/embed/KMaiNAJ__U4?list=PLQZT93bz3H79NTc-aUFMU_UZgo4Vl2iUH" frameborder="0" allowfullscreen></iframe>


.. _web:

Webpage
^^^^^^^

Utilizada para referenciar, páginas web o información contenidas en blogs, twiter, facebook, listas de discusión entre otros. 

**Ejemplo 1**

   *UOL JOGOS. Fórum de jogos online: Por que os portugas falam que o sotaque portugues do Brasil é açucarado???, 2011. Disponivel en <http://forum.jogos.uol.com.br/_t_1293567>. Acessado em 06 de fevereiro de 2014.*

.. image:: img/doc-mkp-ref-web-uol.jpg
   :align: center


**Ejemplo 2**

   *BANCO CENTRAL DO BRASIL. Disponivel em: www.bcb.gov.br.*

.. image:: img/doc-mkp-ref-web-bb.jpg
   :align: center


.. raw:: html

   <iframe width="560" height="315" src="https://www.youtube.com/embed/EwufVmJ4R74?list=PLQZT93bz3H79NTc-aUFMU_UZgo4Vl2iUH" frameborder="0" allowfullscreen></iframe>


.. _otro:

Other
^^^^^

Utilizada para referenciar tipos no previstos por SciELO. Ej.:


   *INAC. Grupo Nacional de Canto e Dança da República Popular de Moçambique. Maputo, [s.d.].*

.. image:: img/doc-mkp-ref-other.jpg
   :align: center


.. raw:: html

   <iframe width="560" height="315" src="https://www.youtube.com/embed/ulL9TlVNcJE?list=PLQZT93bz3H79NTc-aUFMU_UZgo4Vl2iUH" frameborder="0" allowfullscreen></iframe>


.. _previous:

"Previous" en referencias
=========================

Hay normas que permiten que las obras que referencian la misma autoría repetidamente, sean sustituidas por un guion equivalente a seis espacios. Ex.:


*______. Another one bites the dust: Merck cans hep C fighter Victrelis as new meds take flight [Internet]. Washington: FiercePharma; 2015.*

Al hacer la marcación de [refs] el programa duplicará la referencia con previous de la siguiente forma:

[ref id="r16" reftype="book"] [text-ref]______. Another one bites the dust: Merck cans hep C fighter Victrelis as new meds take flight &#91;Internet&#93;. Washington: FiercePharma; 2015[/text-ref]. * ______. Another one bites the dust: Merck cans hep C fighter Victrelis as new meds take flight &#91;Internet&#93;. Washington: FiercePharma; 2015*[/ref]

.. note:: en referencias que presentan el elemento [text-ref], el dato a ser marcado deberá ser el que consta después del [/text-ref]. Nunca hacer la marcación de la referencia que consta en [text-ref][/text-ref].

Para identificación de referencias con ese tipo de dato, seleccione los guiones e identifique con el elemento [*authors] con asterisco. El programa recuperará el nombre del autor previamente marcado e hará la identificación automática del grupo de autores, identificando el apellido y el primero nombre.



.. _automata:

Marcación Automática
--------------------

El programa Markup dispone de una funcionalidad que optimiza el proceso de marcación de las referencias bibliográficas que siguen la norma Vancouver. Caso haya adaptaciones en la norma, el programa no hará la marcación correctamente.


**Seleccione todas as referencias**

.. image:: img/doc-mkp-automata-select.jpg
   :align: center


**Clique en el ícono "Markup: Marcación Automática 2"**

.. image:: img/doc-mkp-automata.jpg
   :align: center


Vea que todas las referencias fueran marcadas automáticamente y de forma detallada.

.. image:: img/doc-mkp-ref-mkup-automata.jpg
   :align: center


A pesar del programa hacer la marcación automática de las referencias, será necesario analizar atentamente referencia por referencia afín de verificar si algún dato no fue o fue marcado incorrectamente.
Si hubiera algún error a ser corregido, entre en el nivel de [ref] en "Barras de Herramientas Personalizadas" e haga las correcciones e/o incluya las marcaciones faltantes.

.. note:: el uso de la marcación automática en referencias solo es posible caso as referencias bibliográficas estén de acuerdo con la norma Vancouver, siguiéndola literalmente. 
          Para las demás normas tal funcionalidad no está disponible.



.. _ref-numerica:

Referencia numérica
-------------------
Algunas revistas presentan referencias bibliográficas numeradas, las cuales son referenciadas así en el cuerpo del texto. El número correspondiente a la referencia tambiém debe ser marcado.
Después de la marcación del grupo de referencias, baje un nivel en [ref], seleccione el número de la referencia y marque con el elemento [label]:

.. image:: img/label-ref-num.jpg
   :height: 300px
   :align: center

.. note:: el programa Markup no hace la identificación automática de ese dato.


.. _nota-de-pie:

Notas de Pie
============

As notas de pie pueden aparecer antes del cuerpo del texto o después. No hay una posición fija dentro del archivo .doc. Mientras tanto, es necesario evaluar la nota indicada, pues dependiendo del tipo de nota inserida en fn-type, el programa genera el archivo .xml con información de notas de autores en ``<front>`` o en ``<back>``. Para más información acerca de los tipos de nota consulte la documentación de SPS en <http://docs.scielo.org/projects/scielo-publishing-schema/es_BR/1.2-branch/tagset.html#notas-de-autor> y<http://docs.scielo.org/projects/scielo-publishing-schema/es_BR/1.2-branch/tagset.html#notas-gerais>.

Seleccione la nota y marque con el elemento [fngrp].

.. image:: img/doc-mkp-select-fn-contri.jpg
   :height: 350px
   :align: center


Caso la nota presente un título o un símbolo, seleccione la información y marque con el elemento [label]:

.. image:: img/doc-mkp-fn-label-con.jpg
   :height: 200px
   :align: center


Tipos de notas
--------------

Soporte sin Información de Financiamiento
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Para notas de pie que presentan soporte de entidades, institución o persona física sin dado de financiamiento y número de contracto, seleccione la nota del tipo "Pesquisa en la cual el artículo es basado fue apoyado por alguna entidad":


.. image:: img/doc-mkp-fn-supp.jpg
   :height: 250px
   :align: center


.. raw:: html

   <iframe width="560" height="315" src="https://www.youtube.com/embed/a_b9uzylEUU?list=PLQZT93bz3H79NTc-aUFMU_UZgo4Vl2iUH" frameborder="0" allowfullscreen></iframe>


Soporte con datos de Financiamiento
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Para notas de pie que presentan datos de financiamiento con número de contracto, seleccione nota del tipo "Declaración o negación de recibimiento de financiamiento en apoyo a la pesquisa cuyo el artículo es basado". En ese caso, será preciso marcar los datos de financiamiento con el elemento [funding]:

.. image:: img/doc-mkp-select-fn-fdiscl.jpg
   :height: 300px
   :align: center


El próximo paso será seleccionar el primero grupo de institución financiadora + el número de contracto y marcar con el elemento [award].

.. image:: img/doc-mkp-award-select.jpg
   :height: 200px
   :align: center


En seguida, seleccione la institución financiadora y marque con el elemento [fundsrc]:

.. image:: img/doc-mkp-fund-source-fn.jpg
   :height: 200px
   :align: center


Seleccione cada número de contracto y marque con el elemento [contract]:

.. image:: img/doc-mkp-contract-fn.jpg
   :height: 300px
   :align: center


Caso la nota de pie presente más que una institución financiadora y número de contracto, haga la marcación conforme el ejemplo:

.. image:: img/doc-mkp-mkp-fn-fund-2.jpg
   :height: 300px
   :align: center
   

.. raw:: html

   <iframe width="560" height="315" src="https://www.youtube.com/embed/FVTnNPGqWiU?list=PLQZT93bz3H79NTc-aUFMU_UZgo4Vl2iUH" frameborder="0" allowfullscreen></iframe>


.. _fn-automatico:

Notas de Pie - Identificación Automática
========================================

Para notas de pie que están posicionadas al fin de cada página en el documento, con formateo de notas de pie del Word, es posible hacer la marcación automática del número referenciado en el documento y su nota respectiva.

Las llamadas de nota de pie en el cuerpo del texto deberán estar con un formateo simple: en formato numérico y sobrescrito.
Ya las notas, deberán estar en formato de nota de pie del Word con un espacio antes de la nota.

.. image:: img/mkp-espaco-fn.jpg
   :height: 300px
   :align: center

Estando formateado correctamente, haga un clic con el mouse en cualquier párrafo y, en seguida, clique en [* fn].

.. image:: img/mkp-botao-fn.jpg
   :height: 300px
   :align: center

Al cliquear en [*fn] el programa hará la marcación automática de [xref] en el cuerpo del texto y también de la nota al pie de la página.

.. image:: img/mkp-nota-automatico.jpg
   :height: 300px
   :align: center



.. _apendice:

Apéndices
=========

La marcación de apéndices, anexos y materiales suplementares debe ser hecha por el elemento [appgrp]:

.. image:: img/doc-mkp-element-app.jpg
   :height: 100px
   :align: center

Seleccione todo el grupo de apéndice, incluso el título, si haya,  y haga un clic en [appgrp]:


.. image:: img/doc-mkp-app.jpg
   :height: 300px
   :align: center


Seleccione apéndice por apéndice y marque con el elemento [app]

.. image:: img/doc-mkp-id-app.jpg
   :height: 300px
   :align: center

.. note:: el id debe ser siempre único en el documento.

Caso el apéndice sea una figura, tabla, cuadro etc, seleccione el título de apéndice y marque con el elemento [sectitle]. Utilicé los íconos fluctuantes (tabwrap, figgrp, * list, etc) del programa Markup para identificación del objeto que será marcado.

**íconos fluctuantes**

.. image:: img/doc-mkp-tags-flutuantes.jpg
   :height: 100px
   :align: center

Ejemplo, seleccione la figura con su respectivo label e caption y marque con el elemento [figgrp]

.. image:: img/doc-mkp-app-fig1.jpg
   :height: 300px
   :align: center


.. image:: img/doc-mkp-app-fig2.jpg
   :height: 350px
   :width: 350px
   :align: center

.. note:: Asegúrese que el ID de la figura de apéndice es único en el documento.


.. raw:: html

   <iframe width="560" height="315" src="https://www.youtube.com/embed/ZqjFc0Hg4P8?list=PLQZT93bz3H79NTc-aUFMU_UZgo4Vl2iUH" frameborder="0" allowfullscreen></iframe>


Para apéndices que presentan párrafos, seleccione el título del apéndice y marque con el elemento [sectitle]

.. image:: img/doc-mkp-sectitle-app-paragrafo1.jpg
   :height: 300px
   :align: center


Seleccione el párrafo y marque con el elemento [p]

.. image:: img/doc-mkp-sectitle-app-paragrafo2.jpg
   :height: 300px
   :align: center


.. raw:: html

   <iframe width="560" height="315" src="https://www.youtube.com/embed/_BM7cKHcWoA?list=PLQZT93bz3H79NTc-aUFMU_UZgo4Vl2iUH" frameborder="0" allowfullscreen></iframe>


.. _agradecimientos:

Agradecimientos
===============

La sección de agradecimiento, generalmente, encontrase entre el final del cuerpo del texto e las referencias bibliográficas. Para marcación automática de los elementos de agradecimiento seleccione todo el texto, incluso su título, y marque con el elemento [ack]. 


**seleccionando [ack]**

.. image:: img/doc-mkp-ack-nofunding.jpg
   :height: 200px
   :align: center

**Resultado esperado**

.. image:: img/doc-mkp-ack-fim.jpg
   :height: 150px
   :align: center



.. raw:: html

   <iframe width="560" height="315" src="https://www.youtube.com/embed/sxZlGq4vwhk?list=PLQZT93bz3H79NTc-aUFMU_UZgo4Vl2iUH" frameborder="0" allowfullscreen></iframe>


Comúnmente los agradecimientos presentan datos de financiamiento, con número de contracto y institución financiadora. Cuando presentes, marque los datos con el elemento [funding].

.. image:: img/doc-mkp-nivel-inf-ack.jpg
   :height: 200px
   :align: center

Seleccione el primero conjunto de institución y número de contravto y marque con el elemento [award]:

.. image:: img/doc-mkp-select-1-award-ack.jpg
   :height: 200px
   :align: center

Seleccione la institución financiadora y marque con el elemento [fundsrc]:

.. image:: img/doc-mkp-fundsrc1.jpg
   :height: 200px
   :align: center

.. note:: Caso haya más que una institución financiadora para el mismo número de contracto, seleccione cada institución en un [fundsrc]


Marque el número de contracto con el elemento [contract]:

.. image:: img/doc-mkp-ack-contract1.jpg
   :height: 200px
   :align: center

Cuando hubiera más de una institución financiadora y número de contrato, marcar conforme sigue:

.. image:: img/doc-mkp-ack-finaliz.jpg
   :height: 230px
   :align: center


.. raw:: html

   <iframe width="560" height="315" src="https://www.youtube.com/embed/P-uM3_bpS1Q?list=PLQZT93bz3H79NTc-aUFMU_UZgo4Vl2iUH" frameborder="0" allowfullscreen></iframe>


.. _glosario:

Glosario
========

Glosarios son incluidos en los documentos después de las referencias bibliográficas, en apéndices o cajas de texto. Para marcarlo, seleccione todos los ítems que la compone y marque con el elemento [glossary]. Seleccione todos los ítems nuevamente y marque con el elemento :ref:`lista-definición`. Sigue ejemplo de marcación de glosario presente después de las referencias bibliográficas:

.. image:: img/doc-mkp-glossary-.jpg
   :height: 200px
   :align: center

Seleccione todos los datos de glosario y marque con el elemento :ref:`lista-definicao`:

.. image:: img/doc-mkp-select-gdef.jpg
   :height: 200px
   :align: center

El resultado de la marcación será:

.. image:: img/doc-mkp-glossary.jpg
   :height: 200px
   :align: center



.. _xmlbody:

xmlbody
=======


Con el cuerpo del texto formateado de acuerdo con las instrucciones de `Preparación de archivos <es_how_to_generate_xml-prepara.html#formatacao-do-archivo>`_ y después de haber realizado la marcación de referencias bibliográficas, es posible iniciar con la marcación de [xmlbody].

Seleccione todo el cuerpo del texto y de clic en el botón [xmlbody], verificar las secciones, subsecciones, citas, etc. presentadas en la ventana que abre el programa, y si es necesario corrija y de clic en "Aplicar".

.. image:: img/doc-mkp-select-xmlbody.jpg
   :height: 300px
   :align: center


.. image:: img/doc-mkp-xmlbody-select.jpg
   :height: 350px
   :width: 350px
   :align: center

.. note:: En caso que alguna información sea incorrecta, seleccione el ítem a ser corregido en la ventana, seleccione la opción correcta en el menú desplegable al lado del botón "Corregir", de clic en "Corregir". Verifique nuevamente  y de clic en "Aplicar".


Al dar clic en "Aplicar" el programa preguntará si las referencias en el cuerpo del texto se ajustan al patrón de citación autor-fecha. Si el documento presenta este patrón, de clic en [Sí], en caso contrario de clic en [No].


.. image:: img/doc-mkp-refs-padrao.jpg
   :height: 300px
   :align: center

**Patrón autor-fecha**

.. image:: img/doc-mkp-ref-author.jpg
   :height: 200px
   :align: center

**Patrón numérico**

.. image:: img/doc-mkp-ref-num.jpg
   :height: 250px
   :align: center


Es a partir del documento formateado de acuerdo con las instrucciones de `Preaparación de archivos <es_how_to_generate_xml-prepara.html#formatacao-do-archivo>`_ que el programa marca automáticamente secciones, subsecciones, párrafos, referencias de autores en el cuerpo del texto, llamadas a figuras y tablas, ecuaciones en línea etc.

.. image:: img/doc-mkp-complete.jpg
   :height: 300px
   :width: 200px
   :align: center

Verifique si los datos fueron marcados correctamente y complete la marcación de los elementos que no fueron identificados en el documento.


.. raw:: html

   <iframe width="560" height="315" src="https://www.youtube.com/embed/rsz78JNpz44?list=PLQZT93bz3H79NTc-aUFMU_UZgo4Vl2iUH" frameborder="0" allowfullscreen></iframe>


.. _sección:

Secciones y subsecciones
------------------------

Después de la marcación automática de [xmlbody], cerciórese que los tipos de secciones fueron asignados correctamente.

.. image:: img/doc-mkp-section-combinada.jpg
   :align: center

En algunos casos, la marcación automática no identifica la sección correctamente. En esos casos, seleccione la sección, de clic en el lápiz "Editar Atributos" e indique el tipo correcto de sección.

.. image:: img/doc-mkp-sec-compost.jpg
   :height: 250px
   :align: center


**Resultado**

.. image:: img/doc-mkp-section-combinada.jpg
   :height: 200px
   :align: center

.. note:: En el menú desplegable las secciones combinadas inician con un asterisco.



.. raw:: html

   <iframe width="560" height="315" src="https://www.youtube.com/embed/P7fu28h7Cws" frameborder="0" allowfullscreen></iframe>


.. _xref:

Referencia cruzada de referencias bibliográficas
------------------------------------------------

Las referencias con el patrón autor-fecha serán identificados automáticamente en el cuerpo del texto sólo si el apellido del autor y la fecha están marcados en las *referencias bibliográficas*, y sólo si el apellido del autor está presente en el cuerpo del texto igual al que fue marcado en [refs].
En algunos casos que el programa Markup no realizará la marcación automática de [xref] en el documento. Ej.:

**Citas de autor**


*Apellido del autor + "in press" o derivados:*

.. image:: img/doc-mkp-xref-noprelo.jpg
   :height: 200px
   :align: center


*Autor corporativo:*

.. image:: img/doc-mkp-ref-cauthor.jpg
  :height: 150px
  :align: center

Para identificar el [xref] de las citas que no fueron marcadas automáticamente, primero identifique el ID de la *referencia bibliográfica* no identificada, enseguida seleccione la cita deseada y márquela con el elemento [xref].

.. image:: img/doc-mkp-xref-manual.jpg
   :height: 300px
   :align: center


Llene sólo los campos "ref-type" y "rid". En "ref-type", seleccione el tipo de referencia cruzada que corresponda, en este caso "Referencia bibliográfica", enseguida indique el ID correspondiente a la referencia bibliográfica citada. Verifique y de clic en [Continuar].

.. image:: img/doc-mkp-xref-manual-refs.jpg
   :height: 180px
   :align: center

.. note:: No inserte hipervínculos en el dato a ser marcado.


**Llamadas de cuadros, ecuaciones y cajas de texto:**

La marcación de las referencias cruzadas en cuadros, ecuaciones y cajas de texto sigue las mismas etapas descritas en las referencias bibliográficas.


**Cuadro:**

Seleccione [ref-type] de tipo "Figura" e indique la secuencia del ID en el documento para este elemento.

.. image:: img/doc-mkp-chart.jpg
   :height: 100px
   :align: center


   *Resultado*

.. image:: img/doc-mkp-xref-chart.jpg
   :align: center


**Ecuaciones:**

Seleccione [ref-type] de tipo "Fórmula" e indique la secuencia del ID en el documento para este elemento.


.. image:: img/doc-mkp-eq-man.jpg
   :align: center


   *Resultado*

.. image:: img/doc-mkp-xref-equation.jpg
   :height: 80px
   :align: center


**Caja de texto:**

Seleccione [ref-type] de tipo "Caja de texto o barra lateral" e indique la secuencia del ID en el documento para este elemento.

.. image:: img/doc-mkp-box-man.jpg
   :height: 280px
   :align: center


   *Resultado*

.. image:: img/doc-mkp-xref-boxed.jpg
   :align: center



.. raw:: html

   <iframe width="560" height="315" src="https://www.youtube.com/embed/mGncaEawiKA?list=PLQZT93bz3H79NTc-aUFMU_UZgo4Vl2iUH" frameborder="0" allowfullscreen></iframe>


.. _paragrafo:

Párrafos
--------

Los párrafos son marcados automáticamente en el cuerpo del texto al hacer la identificación de [xmlbody]. En caso que el programa no haya marcado un párrafo o que la marcación automática haya identificado un párrafo con el elemento incorrecto, es posible realizar la marcación manual de ese dato. Para ello, seleccione el párrafo deseado, verifique si el párrafo pertenece a alguna sección o subsección y ubique el elemento [p] dentro los niveles de [sec] o [subsec].


.. image:: img/doc-mkp-subsec-p.jpg
   :height: 250px
   :align: center


*Resultado*

.. image:: img/doc-mkp-element-p.jpg
   :height: 100px
   :align: center



.. raw:: html

   <iframe width="560" height="315" src="https://www.youtube.com/embed/wjQ-YiMD6oc?list=PLQZT93bz3H79NTc-aUFMU_UZgo4Vl2iUH" frameborder="0" allowfullscreen></iframe>



.. _figura:

Figuras
-------

Al hacer la marcación de [xmlbody] el programa identifica automáticamente las imágenes con el elemento "graphic". 

Para marcar el grupo de datos de la figura, seleccione la imagen, su leyenda (label y caption) y la fuente si existe, marque la selección con el elemento [figgrp].

.. image:: img/doc-mkp-select-fig.jpg
   :height: 400px
   :align: center

* Llene el "id" de la figura en la ventana que abre el programa.

.. image:: img/doc-mkp-id-fig.jpg
   :height: 200px
   :align: center

Cerciórese que el ID de la figura es único en el documento.


.. image:: img/doc-mkp-fig-incomp.jpg
   :height: 400px
   :align: center

.. note:: La marcación completa de la figura es de extrema importancia. Si la figura no fuera marcada con el elemento [figgrp] y sus respectivos datos, el programa no generará el elemento [fig] correspondiente en el documento.


* Después de la marcación de [figgrp], en caso que la imagen presente información de fuente, seleccione el dato y márquelo con el elemento [attrib]:

.. image:: img/doc-mkp-attrib-fig.jpg
   :height: 400px
   :align: center



.. raw:: html

   <iframe width="560" height="315" src="https://www.youtube.com/embed/qbE3tLoYr3c?list=PLQZT93bz3H79NTc-aUFMU_UZgo4Vl2iUH" frameborder="0" allowfullscreen></iframe>



.. note:: La marcación de label y caption será automática si el formato conforme con las instrucciones dadas en `Preparación de archivos <es_how_to_generate_xml-prepara.html#formatacao-do-archivo>`_, con label y caption debajo de la imagen en el archivo .doc. La información de fuente debe estar arriba de la imagen.


.. _tabla:

Tablas
------

Las tablas pueden ser presentadas como imagen o texto. Las tablas presentadas como imagen deben contener label, caption y notas en texto (sólo si existen), para que todos los elementos sean marcados.
Las tablas deben estar, de preferencia en formato texto, utilizando figuras para tablas complejas (con celdas combinadas, símbolos, fórmulas, imágenes etc).


Tablas en imagen
^^^^^^^^^^^^^^^^

Al realizar la marcación de [xmlbody] el programa identifica automáticamente el "graphic" de la tabla. Seleccione todos los datos de la tabla (imagen, label, caption y notas al pie si existen) y márquelos con el elemento [tabwrap].

Del mismo modo que en las figuras, el ID del elemento deberá ser el indicado para tablas (t1, t2, t3 ...). Cerciórese que el ID de tabla es único en el documento.

.. image:: img/doc-mkp-select-tableimg.jpg
   :height: 450px
   :width: 300px
   :align: center

* Llene el "ID" de la tabla en la ventana que abre el programa.

.. image:: img/doc-mkp-id-figimg.jpg
   :align: center

Cerciórese que el ID de la tabla es único en el documento.

.. image:: img/doc-mkp-tabimg.jpg
   :height: 450px
   :width: 300px
   :align: center

.. note:: El programa realiza la marcación automática de label, caption y notas al pie de tabla.


Tablas en Texto
^^^^^^^^^^^^^^^

El programa también codifica tablas en texto. Para ello, seleccione toda la información de tabla (label, caption, cuerpo de la tabla y notas al pie si existen) y márquela con el elemento [tabwrap].

.. image:: img/doc-mkp-select-tab-text.jpg
   :height: 350px
   :align: center


.. note:: El encabezado de las columnas de la tabla debe estar en negritas. El formateo es esencial para que el programa pueda identificar de forma correcta el [thead] y los elementos que lo componen.

* Llene el "ID" de la tabla en la ventana que abre el programa.

.. image:: img/doc-mkp-id-tabtext.jpg
   :height: 200px
   :align: center

Cerciórese que el ID de la tabla es único en el documento.


.. image:: img/doc-mkp-tabcomplete.jpg
   :height: 400px
   :width: 280px
   :align: center


.. note:: Las tablas irregulares, con celdas combinadas o de gran tamaño posiblemente presenten problemas de marcación. En ese caso algunos elementos deberán ser identificados manualmente por medio del programa Markup o en el XML cuando se haya generado.


.. _ecuación:

Ecuaciones
----------

Hay dos tipos de ecuaciones soportadas por el programa: las ecuaciones en línea (en medio de un párrafo) y las ecuaciones en párrafo.

**Ecuación en línea**

Las ecuaciones en línea deben ser insertadas en el párrafo como imagen. La marcación es hecha automáticamente por el programa al hacer la identificación de [xmlbody].

.. image:: img/doc-mkp-eqline.jpg
   :height: 200px
   :align: center

Si el programa no hiciera la marcación automática de la ecuación en línea, es posible hacer la marcación manualmente. Para ello seleccione la ecuación en línea y márquela en el elemento [graphic].

.. image:: img/doc-mkp=eqline-man.jpg
   :height: 250px
   :align: center

En el campo "href" se agrega el nombre del archivo:

.. image:: img/doc-mkp-eq-line-href.jpg
   :height: 200px
   :align: center

El resultado será:

.. image:: img/doc-mkp-eqline.jpg
   :height: 200px
   :align: center

**Ecuaciones**

Las ecuaciones presentadas como párrafos deben ser identificadas con el elemento [equation]

.. image:: img/doc-mkp-eq1.jpg
   :height: 200px
   :align: center

Llene el "ID" de la ecuación en la ventana que abre el programa. Cerciórese que el id de la ecuación es único en el documento.

.. image:: img/doc-mkp-eq2.jpg
   :height: 200px
   :align: center

Al realizar la marcación de la ecuación, el programa identifica el elemento [equation]. En caso que exista información del número de la ecuación, márquela con el elemento [label].

.. image:: img/doc-mkp-eq3.jpg
   :height: 200px
   :align: center

.. _Caja-de-texto:

Cajas de texto
--------------

Las cajas de texto pueden presentar figuras, ecuaciones, listas, glosarios o un texto. Para marcar este elemento, seleccione toda la información de la caja de texto incluyendo el label y caption, y márquela con [*boxedtxt]:

.. image:: img/doc-mkp-boxselect.jpg
   :height: 300px
   :align: center

Llene el campo de ID de la caja de texto en la ventana que abre el programa, después de la selección de [*boxedtxt]. Cerciórese que el ID de boxed-text es único en el documento.

.. image:: img/doc-mkp-id-bxt.jpg
   :height: 200px
   :align: center

Utilizando [*boxedtxt] el programa realiza la marcación automática del título de la caja de texto y también de los párrafos:

.. image:: img/doc-mkp-resultboxed.jpg
   :height: 400px
   :align: center

Cuando la caja de texto presente una figura, tabla, lista etc, también es posible utilizar el elemento [*boxedtxt] y después marcar estos elementos utilizando las etiquetas flotantes del programa.

.. raw:: html

   <iframe width="560" height="315" src="https://www.youtube.com/embed/M52p5PXceL8?list=PLQZT93bz3H79NTc-aUFMU_UZgo4Vl2iUH" frameborder="0" allowfullscreen></iframe>


.. _verso:

Marcación de versos
-------------------

Para identificar versos o poemas en el cuerpo del texto, seleccione toda la información, incluyendo el título y autoría si existe, y márquela con el elemento [versegrp]: 

.. image:: img/doc-mkp-selectverse.jpg
   :height: 150px
   :align: center

El programa identificará cada línea como [verseline]. En caso que el poema presente título, elimine la marcación de [verseline], seleccione el título y márquelo con el elemento [label]. La autoría del poema debe ser marcada con el elemento [attrib].

.. image:: img/doc-mkp-versee.jpg
   :height: 150px
   :align: center


.. image:: img/doc-mkp-versline-attr.jpg
   :height: 180px
   :align: center


.. raw:: html

   <iframe width="560" height="315" src="https://www.youtube.com/embed/2ZmX8mrFjvU?list=PLQZT93bz3H79NTc-aUFMU_UZgo4Vl2iUH" frameborder="0" allowfullscreen></iframe>


.. _citación:

Citas textuales
---------------

Las citas son marcadas automáticamente en el cuerpo del texto, al realizar la marcación de [xmlbody], siempre que estén con el formateo adecuado.

.. image:: img/mkp-doc-quoteok.jpg
   :height: 200px
   :align: center

Cuando el programa no realice la marcación automática, seleccione la cita deseada y márquela con el elemento [quote]:

.. image:: img/doc-mkp-quotee.jpg
   :height: 300px
   :align: center

El resultado debe ser:

.. image:: img/mkp-doc-quoteok.jpg
   :height: 200px
   :align: center


.. raw:: html

   <iframe width="560" height="315" src="https://www.youtube.com/embed/6oRIqNW4S6M?list=PLQZT93bz3H79NTc-aUFMU_UZgo4Vl2iUH" frameborder="0" allowfullscreen></iframe>



.. _lista:

Listas
------

Para identificar listas seleccione todos los ítems y márquelos con el elemento [*list]. Seleccione el tipo de lista en la ventana que abre el programa:

.. image:: img/doc-mkp-list-type.jpg
   :height: 400px
   :width: 380px
   :align: center

Verifique los posibles tipos de lista en :ref:`elemento-list` y seleccione el más adecuado:

.. image:: img/doc-mkp-list.jpg
   :height: 250px
   :align: center




.. raw:: html

   <iframe width="560" height="315" src="https://www.youtube.com/embed/6697hJl4H7M?list=PLQZT93bz3H79NTc-aUFMU_UZgo4Vl2iUH" frameborder="0" allowfullscreen></iframe>


.. note:: El programa Markup no realiza la marcación de sublistas. Para saber como marcar sublistas, consulte la documentación "Markup_90_O_que_ha_novo.pdf" sección "Processos Manuais".


.. _elemento-list:

El atributo ``@list-type`` especifica el prefijo a ser utilizado en el marcador de la lista. Los valores posibles son:

+----------------+----------------------------------------------------------------------+
| Valor          | Descripción                                                          |
+================+======================================================================+
| order          | Lista ordenada, cuyo prefijo utilizado es un número o letra          |
|                | dependiendo del estilo.                                              |
+----------------+----------------------------------------------------------------------+
| bullet         | Lista desordenada, cuyo prefijo utilizado es un punto, barra u       |
|                | otro símbolo.                                                        |
+----------------+----------------------------------------------------------------------+
| alpha-lower    | Lista ordenada, cuyo prefijo es un carácter alfabético en minúscula. |
+----------------+----------------------------------------------------------------------+
| alpha-upper    | Lista ordenada, cuyo prefijo es un carácter alfabético en mayúscula. |
+----------------+----------------------------------------------------------------------+
| roman-lower    | Lista ordenada, cuyo prefijo es un número romano en minúscula.       |
+----------------+----------------------------------------------------------------------+
| roman-upper    | Lista ordenada, cuyo prefijo es un número romano en mayúscula.       |
+----------------+----------------------------------------------------------------------+
| simple         | Lista simple, sin prefijo en los ítems.                              |
+----------------+----------------------------------------------------------------------+


.. _lista-definición:

Listas de definiciones
----------------------

Para marcar listas de definiciones seleccione todos los datos, incluyendo el título si existe, y márquelos con el elemento [*deflist]

.. image:: img/doc-mkp-deflistselect.jpg
   :height: 300px
   :align: center

En la ventana que abre el programa, llene el campo de "id" de la lista. Cerciórese que el id es único en el documento.

.. image:: img/doc-mkp-def-selec.jpg
   :height: 200px
   :align: center


Confirme la identificación del título de la lista de definiciones y enseguida la marcación del mismo:

.. image:: img/doc-mkp-question-def.jpg
   :height: 150px
   :align: center


.. image:: img/doc-mkp-def-sectitle.jpg
   :height: 150px
   :align: center


Al finalizar, verifique si la marcación automática de cada término de la lista de definiciones está conforme al siguiente ejemplo.

.. image:: img/doc-mkp-deflist.jpg
   :height: 300px
   :align: center

.. note:: El programa realiza la marcación automática de cada ítem de la lista de definiciones sólo sí la lista está con el formato requerido por SciELO: el término en negritas, guión como separador y la definición del término sin formato.

Cuando el programa no realice la marcación automática de la lista de definiciones, es posible identificar los elementos manualmente.

* Seleccione toda la lista de definiciones y márquelas con el elemento [deflist], sin asterisco:

.. image:: img/doc-mkp-mandef1.jpg
   :height: 300px
   :align: center


* Marque el título con el elemento [sectitle] (solo si existe la información de título):

.. image:: img/doc-mkp-defsect.jpg
   :height: 250px
   :align: center

* Seleccione el término y la definición y márquelos con el elemento [defitem]:

.. image:: img/doc-mkp-defitem.jpg
   :height: 250px
   :align: center

* Seleccione solo el término y márquelo con el elemento [term]:

.. image:: img/doc-mkp-term.jpg
   :height: 80px
   :align: center

* El próximo paso será seleccionar la definición y marcarla con el elemento [def]:

.. image:: img/mkp-doc-def.jpg
   :height: 200px
   :align: center


Haga lo mismo con los demás términos y definiciones.


.. _material-suplementar:

Material suplementario
----------------------

La marcación de materiales suplementarios debe ser hecha con el elemento [supplmat]. El material suplementario puede estar en línea, como un párrafo "suelto" en el documento o como apéndice.


.. _suplemento-en-párrafo:

Material suplementario en [xmlbody]
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Seleccione todo contenido del material suplementario, incluyendo label y caption si existe, y márquelo con el elemento [supplmat]:

.. image:: img/doc-mkp-suppl-f.jpg
   :height: 300px
   :align: center


En la ventana que abre el programa, llene el campo de "id", el cual deberá ser único en el documento, y el campo "href" con el nombre del archivo .doc:


.. image:: img/doc-mkp-supplfig.jpg
   :height: 200px
   :align: center

Después realice la marcación de label del material suplementario. Seleccione todos los datos de la figura y márquelos con el elemento [figgrp]. La marcación deberá quedar conforme al siguiente ejemplo:

.. image:: img/doc-mkp-suppl2.jpg
   :height: 300px
   :align: center


.. _suplemento-en-línea:

Material suplementario en línea
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Seleccione la información del material suplementario y márquela con el elemento [supplmat]:

.. image:: img/doc-mkp-selectms.jpg
   :height: 180px
   :align: center

En la ventana que abre el programa, llene el campo de "id", el cual deberá ser único en el documento, y el campo "href" con el nombre del PDF del material suplementario exactamente como esta en la carpeta "src".

.. image:: img/doc-mkp-camposms.jpg
   :height: 200px
   :align: center


La marcación deberá ser:

.. image:: img/doc-nkp-supple.jpg
   :align: center

.. note:: Antes de iniciar la marcación de material suplementario cerciórese que el PDF del material suplementario se encuentra en la carpeta "src" como esta descrito en `Estructura de carpetas <es_how_to_generate_xml-prepara.html#estrutura-de-pastas>`_.


.. _suplemento-en-apéndice:

Material suplementario como apéndice
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Primero se debe marcar el material suplementario con el elemento [appgrp] y enseguida el elemento [app].

.. image:: img/doc-mkp-suppl-appo.jpg
  :height: 400px
  :width: 350px
  :align: center

Seleccione nuevamente todo el contenido del material suplementario y márquelo con el elemento [app]. Enseguida, marque el label del material con el elemento [sectitle]:

.. image:: img/doc-mkp-suppl-app.jpg
   :height: 400px
   :width: 350px
   :align: center


Seleccione el material suplementario y márquelo con el elemento [supplmat]:

.. image:: img/doc-mkp-app-suuol.jpg
   :height: 400px
   :width: 350px
   :align: center
   

Después de la marcación de [supplmat] marque el objeto del material con las etiquetas flotantes:

.. image:: img/doc-mkp-suppl4.jpg
   :height: 400px
   :width: 350px
   :align: center


.. _sub-article:

Subdocumentos
=============

Traducciones
------------

Los documentos traducidos presentan un formato específico:

1. El documento del idioma principal debe seguir el formato indicado en `Preparación de archivos <es_how_to_generate_xml-prepara.html#formatacao-do-archivo>`_
2. Después de la última información en el documento principal y dentro del mismo .doc o .docx, agregue la traducción del documento.

La traducción del documento debe ser simplificada:

1. Agregar sólo la información que presente traducción, por ejemplo:
    a. Sección - si existe su traducción
    b. Autores y afiliaciones - Sólo si existe afiliación traducida
    c. Resúmenes – si existe su traducción
    d. Palabras clave - si existe su traducción
    e. Correspondencia - si existe su traducción
    f. Notas de autor o del archivo - si existe su traducción
    g. Cuerpo del texto.
    
2. El título es obligatorio;
3. No agregar nuevamente referencias bibliográficas;
4. Mantener las citaciones bibliográficas en el cuerpo del texto de acuerdo con el PDF.

Vea el siguiente ejemplo:

.. image:: img/mkp-doc-formatado.jpg
   :height: 400px
   :width: 200px


Marcando documentos con traducciones
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Con el documento formateado, marque el documento con el elemento [doc] y complete la información.
La marcación del documento con el idioma principal no cambia, siga las instrucciones anteriores para la marcación de los elementos.

.. image:: img/mkp-subdoc-fechadoc.jpg
   :align: center


.. note:: Es fundamental que el último elemento del documento completo sea el elemento [/doc]. 


Una vez finalizada la marcación del documento con el idioma principal seleccione toda la traducción y márquela con el elemento [subdoc].
En la ventana que abre el programa, llene los siguientes campos: 

* id       - Identificador único del documento: S + nº secuencial
* subarttp - Seleccionar el tipo de artículo: "translation"
* language - Idioma de la traducción del documento

.. image:: img/mkp-subdoc-inicio.jpg
   :height: 300px
   :width: 600px
   :align: center

Realice la marcación de la traducción del documento, con los elementos en nivel de [subdoc]:


.. image:: img/mkp-subdoc-nivel.jpg
   :height: 350px
   :width: 500px
   :align: center


.. note::  El programa Markup no realiza la marcación automática del documento traducido.


Afiliación traducida
^^^^^^^^^^^^^^^^^^^^

La marcación de una afiliación traducida es diferente de a la marcación del documento en el idioma principal.
Las afiliaciones traducidas no deben presentar datos detallados. 
Seleccione la afiliación traducida y márquela con el elemento [afftrans] del nivel [subdoc]:

.. image:: img/mkp-afftrans.jpg
   :height: 300px
   :align: center

Después haber marcado de los datos iniciales de la traducción, continué con la marcación del cuerpo del texto.


.. attention:: El ID de los autores y afiliaciones deben ser únicos. Por lo tanto, no debe poner el mismo ID del idioma principal.


Marcando 'body' de la traducción
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

La marcación del cuerpo del texto sigue la mismas instrucciones anteriores. Seleccione todo el cuerpo del texto y márquelo con el elemento [xmlbody] del nivel [subdoc]. 

El programa realizara la marcación automática de las referencias cruzadas en el cuerpo del texto agregando el 'rid" correspondiente al 'id' de las referencias bibliográficas marcadas en el documento principal.

.. image:: img/mkp-body-trans.jpg
   :height: 300px
   :align: center


Mantenga los RIDs agregados automáticamente.
Figuras, tablas, ecuaciones, apéndices etc deben presentar un ID diferente a los del documento principal.
Para ello, dé continuidad a los IDs, por ejemplo:


**El documento principal presenta 2 figuras:**

.. image:: img/mkp-fig-id-ingles.jpg
   :height: 350px
   :align: center

.. note:: El ID de la última figura es 'f2'.


**En el artículo traducido también hay 2 figuras:**

.. image:: img/mkp-fig-id-traducao.jpg
   :height: 350px
   :align: center

Observe como la secuencia es continua en los IDs de las figuras.
Considere esta regla para: autores y sus respectivas afiliaciones, figuras, tablas, cajas de texto, ecuaciones, apéndices etc.


.. note:: Cuando exista más de una traducción en el artículo, marque cada una con el elemento [subdoc].


.. _carta-respuesta:

Carta y respuesta
-----------------

La carta y su respuesta también deben estar en un único archivo .doc o .docx.

1. La carta debe seguir el formato indicado en `Preparación de archivos <es_how_to_generate_xml-prepara.html#formatacao-do-archivo>`_
2. Después de la última información de la carta y dentro del mismo .doc o .docx, agregue la respuesta del documento.

La respuesta debe estar en el mismo documento que la carta. A continuación se muestran cuales son los datos que deben estar presentes en la respuesta:

1. Agregar sección
2. Autores y afiliaciones si existen
3. Correspondencia si existe
4. Notas de autor o del archivo si existen
5. El título es obligatorio
6. Referencias bibliográficas, si están presentes en la respuesta

Observe el siguiente ejemplo:

[imagen]


Marcando carta y respuesta
^^^^^^^^^^^^^^^^^^^^^^^^^^

Con el archivo formateado, marque el documento con el elemento [doc] y complete la información. Obs.: En [doctopic] seleccione el tipo "carta". 
La marcación de la carta no cambia, siga las instrucciones anteriores para la marcación de los elementos.

.. image:: img/mkp-formulario-carta.jpg
   :height: 450px
   :align: center

.. note:: Es fundamental que el último elemento del documento completo sea el elemento [/doc].


Una vez finalizada la marcación de la carta, seleccione toda el contenido de la respuesta y márquelo con el elemento [subdoc].
En la ventana que abre el programa, llene los siguientes campos: 

* id       - Identificador único del documento: S + nº secuencial
* subarttp - Seleccionar el tipo de artículo: "reply"
* language - Idioma de la respuesta a la carta.

.. image:: img/mkp-resposta-form.jpg
   :align: center

.. note::  El programa Markup no realiza la marcación automática de la respuesta.

Realice la marcación de la respuesta del documento, con los elementos en nivel de [subdoc]:

.. image:: img/mkp-dados-basicos-resposta.jpg
   :align: center


.. note:: Los datos como: afiliaciones y autores, objetos en el cuerpo del texto y referencias bibliográficas deben presentar IDs secuenciales, siguiendo el orden de la carta. Ejemplo, si la última afiliación de la carta fue "aff3", en el documento de la respuesta la primer afiliación será "aff4" etc.


.. _errata:

Errata
======

Para marcar una errata, primero verifique que el archivo éste formateado correctamente de acuerdo a las siguientes instrucciones:

* 1ª línea: DOI
* 2ª línea: Sección "Errata" o "Erratum"
* 3ª línea: Título "Errata" o "Erratum" (de acuerdo al PDF)
* Saltar 2 líneas
* Cuerpo del texto

.. image:: img/mkp-exemplo-errata.jpg
   :height: 300px
   :align: center


Marcando la errata
------------------

Abra la errata en el programa Markup y márquela con el elemento [doc].
Al abrir el formulario, seleccione el título de la revista y verifique los metadatos que son llenados de forma automática.
Complete los demás campos, y en el campo [doctopic] seleccione "errata" y de clic en [OK]
El programa marcará automáticamente los elementos básicos de la errata como: sección, número DOI y título:

.. image:: img/mkp-formulario-errata.jpg
   :height: 350px
   :align: center

Para finalizar la marcación de la errata, verifique que todos los elementos fueron identificados correctamente y continué con la marcación.
Seleccione el cuerpo del texto y márquelo con el elemento [xmlbody]:

.. image:: img/mkp-xmlbody-errata.jpg
   :height: 350px
   :align: center


Ponga el cursor del mouse antes del elemento [toctitle],  y de un clic en [related].
En la ventana que abre el programa, llene los campos: [reltp] (tipo de relación) con el valor "corrected-article" y [pid-doi] (número PID o DOI relacionado) con el número DOI del artículo que será corregido y de clic en [Continuar]:
 
.. image:: img/mkp-related-campos.jpg
   :height: 200px
   :align: center

El programa inserta el elemento [related], el cual enlazará al artículo que presenta el error:

.. image:: img/mkp-resultado-related.jpg
   :height: 300px
   :align: center


.. note:: La versión más reciente del programa Markup acepta los tipos: DOI, PID, SciELO-PID y SciELO-AID.


.. _ahead:

Ahead Of Print
==============

El archivo "Ahead Of Print" (AOP) debe estar formateado de acuerdo a las instrucciones de `Preparación de archivos <es_how_to_generate_xml-prepara.html#formatacao-do-archivo>`_. Como los archivos en AOP no presentan sección, volumen, número y paginación, después del número de DOI de debe dejar una línea en blanco, y enseguida agregar el título del documento:

.. image:: img/mkp-exemplo-ahead.jpg
   :height: 300px
   :align: center

En el formulario para Ahead Of Print, se debe poner el valor "00" en los campos: [fpage], [lpage], [volumen] e [issue].

En [dateiso] ponga la fecha de publicación completa: Año+Mes+Día, y en el campo [season] ponga el mes de publicación.
El total de páginas [pagcount*], para archivos AOP siempre debe ser "1":

.. image:: img/aop-vol-pag-counts.jpg
   :height: 300px
   :align: center


En el campo [doctopic] seleccione el valor "artículo original".

En el campo [order] se deben poner 5 dígitos que obedezcan a la siguiente regla de SciELO:

Para construir el ID para AOP se utilizará una parte de la numeración del fascículo y otra del orden del documento.

*1 - Copie los tres primeros dígitos del fascículo*

Ejemplo el fascículo de la bjmbr número 7 del 2015 = fascículo 0715 **usar: 071**

*2- Agregue los dos últimos dígitos que representarán la cantidad de artículos en el fascículo.*


+------------------------------------------------------------+
|     Ejemplo el fascículo bjmbr 0715 tiene 5 artículos:     |
+=========================================+==================+
| 1414-431X-bjmbr-1414-431X20154135.xml   |  -> **usar: 01** |
+-----------------------------------------+------------------+
| 1414-431X-bjmbr-1414-431X20154316.xml   |  -> **usar: 02** |
+-----------------------------------------+------------------+
| 1414-431X-bjmbr-1414-431X20154355.xml   |  -> **usar: 03** |
+-----------------------------------------+------------------+
| 1414-431X-bjmbr-1414-431X20154363.xml   |  -> **usar: 04** |
+-----------------------------------------+------------------+
| 1414-431X-bjmbr-1414-431X20154438.xml   |  -> **usar: 05** |
+-----------------------------------------+------------------+


El campo order deberá presentar el valor de la siguiente forma:

**3 primeros dígitos del fascículo + 2 dígitos de la cantidad del fascículo**

Archivo 1:

.. image:: img/mkp-other-aop1.jpg
   :align: center

Archivo 2:

.. image:: img/mkp-other-aop2.jpg
   :align: center

etc.


En el campo [ahpdate] ponga la misma fecha que en [dateiso]. Después de llenar todos los datos, de clic en [Ok].

.. image:: img/doc-preench-aop.jpg
   :height: 300px
   :align: center


.. note:: Al generar el archivo .xml el programa agregara automáticamente el elemento <subject> con el valor "Articles", de acuerdo a las recomendaciones del SciELO PS.


.. _rolling-pass:

Publicación continua (Rolling Pass)    
===================================
El archivo de Rolling Pass debe estar formateado de acuerdo a las instrucciones de `Preparación de archivos <es_how_to_generate_xml-prepara.html#formatacao-do-archivo>`_. 

Antes de llenar el formulario de Rolling Pass, se debe saber el formato de publicación adoptado por la revista, el cual puede ser:

**Volumen y número**

.. image:: img/mkp-rp-vol-num.jpg
    :height: 50px


**Volumen**

.. image:: img/mkp-rp-vol.jpg
   :height: 50px


**Número**

.. image:: img/mkp-rp-num.jpg
   :height: 50px


El campo [order] es compuesto por un orden que determinará la sección de los archivos y también el orden de publicación. Por lo tanto, primero defina una centena para cada sección, por ejemplo:

* Editorials: 0100
* Original Articles: 0200
* Review Article: 0300
* Letter to the Author: 0400
   …

Los artículos deberán presentar un ID único dentro de su sección. Por lo que es recomendable crear una plantilla que muestre el ID utilizando, ejemplo:

**Original Articles**

* 1234-5678-rctb-v10-0239.xml 0100
* 1234-5678-rctb-v10-0328.xml 0101
* **1234-5678-rctb-v10-0356.xml 0102**
* ...

El identificador electrónico del documento debe ser agregado en el campo [elocatid].

.. image:: img/rp-formulario.jpg
   :height: 300px
   :align: center


.. note:: Los archivos Rolling Pass presentan elocation. Por ello no se debe llenar datos correspondientes a [fpage] y [lpage].


.. _resena:

Reseñas
=======

Las reseñas generalmente presentan un dato más que los documentos comunes: la referencia bibliográfica del libro reseñado.
El formato del documento debe seguir instrucciones disponibles en `Preparación de archivos <es_how_to_generate_xml-prepara.html#formatacao-do-archivo>`_ , incluyendo la referencia bibliográfica del documento reseñado antes del cuerpo del texto. 

Ejemplo:

.. image:: img/mkp-format-resenha.jpg
   :align: center
   :height: 500px


Marcando Reseñas
----------------

Con el documento previamente formateado, realice la marcación de documento con el elemento [doc] y complete los datos. En el campo [doctopic] seleccione "reseña (book review)". La marcación de los datos iniciales es similar a las instrucciones anteriores, excepto por la marcación de la referencia del libro reseñado.

Para marcar la referencia del libro, seleccione la referencia completa y márquela con el elemento [product]. En la ventana que abre el programa, seleccione el tipo de referencia bibliográfica en [prodtype]:

.. image:: img/mkp-product.jpg
   :align: center

Después realice la marcación de la referencia usando los elementos presentados del nivel [prodtype]:

.. image:: img/mkp-product-reference.jpg
   :align: center

Termine la marcación del archivo y genere el XML.


.. note:: El programa no muestra todos los elementos para la marcación de referencias bibliográficas en el elemento [product]. Marque solo los datos de la referencia con los elementos disponibles en el nivel [prodtype].


.. _formato-corto:

Artículos en formato corto
==========================

La marcación en formato corto es utilizada sólo en los casos de inclusión de números retrospectivos en la colección de la revista.
El documento en formato corto tendrá los datos básicos del documento (título del artículo, autores, afiliaciones, sección, resumen, palabras clave y las referencias completas).
El cuerpo del texto de un documento en formato corto debe ser eliminado, sustituyendo el texto por los párrafos:

   *Texto completo disponible sólo en PDF.*

   *Full text available only in PDF format.*

.. image:: img/mkp-format-abrev-estrutura.jpg
   :align: center
   :height: 200px


Marcando formato corto
----------------------

Con el documento previamente formateado, realice la marcación del documento con el elemento [doc] y complete los datos iniciales de acuerdo con los datos del documento. 

En la marcación de archivos en el formato corto no es necesario seguir orden para la marcación de referencias bibliográficas y [xmlbody].
Realice la marcación de referencias bibliográficas de acuerdo con las instrucciones de :ref:`_referencias`:

.. image:: img/mkp-abrev-refs.jpg
   :align: center

La marcación de los párrafos se debe hacer con el elemento [xmlbody], seleccionando los párrafos y dando clic en [xmlbody]:

.. image:: img/mkp-xmlbody-abrev.jpg
   :align: center


.. note:: La única información que no será marcada en los documentos en 'Formato corto' será el cuerpo del texto, el cual estará disponible en el PDF.


.. _press-release:

Press Release
=============

Por ser un texto de divulgación que utiliza para dar más visibilidad a un fascículo o artículo publicado en una revista, el press realise no sigue la misma estructura de un artículo científico. Por lo tanto, no posee sección, número de DOI, y no es obligatorio incluir la afiliación del autor.
Una vez aprobados los 'Press Releases' podrán ser formateados para una marcación más optimizada.

* 1ª línea del documento: Correspondiente al número de DOI, debe quedar en blanco.
* 2ª línea del documento: Correspondiente a la sección del documento, debe quedar en blanco.
* 3ª línea del documento: Agregue el título del Press Release.
* 4ª línea del documento: Saltar.
* 5ª línea del documento: Agregue el nombre del autor del Press Release.
* 6ª línea del documento: Saltar.
* 7ª línea del documento: Agregar la afiliación, si no existe dejar la línea en blanco.
* 8ª línea del documento: Saltar.
* Agregue el texto del documento Press Release, incluyendo la firma del autor si existe.


Marcar el Press Release
-----------------------

Con el documento previamente formateado, realice la marcación del documento con el elemento [doc] y considere los siguientes valores:

* En los campos 'volid' y 'issue' ponga los datos correspondientes al fascículo con el que esta relacionado el Press Release y en 'isidpart' ponga el valor 'pr' que identifica al documento como un Press Release.
* En el campo de [doctopic] seleccione el tipo "press release".
* Cuando el Press Release esté relacionado con un fascículo, ponga el valor "00001" en el campo [order] para que el Press Release sea posicionado correctamente en la tabla de contenido de la revista.
* Cuando el Press Release sea de un artículo, ponga sólo el valor "01".

.. image:: img/mkp-form-press-release.jpg
   :align: center


Al dar clic en [OK] el programa marcará automáticamente todos los datos iniciales, omitiendo el número de DOI y los demás datos no presentes en el Press Release.

Complete los demás datos del Press Relase como: [xref] de autores, normalización de afiliaciones (si existen), cuerpo del texto con el elemento [xmlbody] y la marcación de la firma del autor con el elemento [sigblock].

.. image:: img/mkp-press-release.jpg
   :align: center


En caso que el Press Release esté relacionado a un artículo específico, será necesario relacionarlo al artículo divulgado.
Ponga el cursor del mouse después del elemento [doc]  y de clic en el elemento [related]. Después llene los campos 'reltp' (tipo de relación) y 'pid-doi'.
En el campo 'reltp' seleccione 'press-release' y en 'pid-doi' ponga el número de DOI del artículo relacionado.

.. image:: img/mkp-related-press-release.jpg
   :align: center


.. note:: La marcación del el elemento [related] sólo se realizará en Press Releases relacionados a un "artículo".


.. _procesos-manuales:

Procesos Manuales
=================

El programa de marcación atiende más 80% de las reglas establecidas en el SciELO Publishing Schema. 
Hay algunos datos que deben ser marcados manualmente, sea en el propio programa Markup, sea directamente en el archivo xml generado por el programa.


Afiliación con más de una institución
-------------------------------------

El programa Markup no realiza marcación de afiliaciones con más que una institución. En ese caso, el dato será incluido directamente en el archivo .xml.
Abra el archivo .xml en un editor de XML y incluya el elemento <aff> con un ID diferente del que ya consta en el documento:

.. image:: img/mkp-aff-xml-id.jpg
   :align: center

.. note:: la afiliación incluida manualmente no debe presentar <label> y <institution content-type="original">, ya que sus datos para presentación en el sitio ya están disponibles en la afiliación marcada en el programa.


Verifique la segunda institución de la afiliación original y copie para la afiliación nueva haciendo la marcación del dato con el elemento <institution content-type="orgname"> y <institution content-type="normalized">:

.. image:: img/mkp-aff-id-xml-norm.jpg
   :align: center

Caso esa institución tenga divisiones, haga la marcación del dato conforme las demás ya hechas en el documento.
En seguida, marque su país correspondiente con el elemento <country country="xx">:

.. image:: img/mkp-xml-aff-complete.jpg
   :align: center

El próximo paso será relacionar esa afiliación <aff id="affx"> con el autor correspondiente.
Considerando que el autor no presenta más que un label, insiera el elemento <xref> cerrado:

.. image:: img/mkp-xref-fechada.jpg
   :align: center

Salve el documento .xml y valide el archivo.


.. _media:

Tipo de Media
-------------

El programa Markup hace también la identificación de medias como: 

* Vídeos
* audios
* Peliculas
* Animaciones

Desde que sus archivos estén disponibles en la carpeta "src" con el mismo nombre del archivo .doc, acrecentado de guion y el ID de la media. Ejemplo:

      *Artículo12-m1.wmv*

La marcación de la media en el cuerpo del texto debe ser hecha a través del elemento [media]. En la ventana abierta por el programa, llene los campos "id" y "href".
En el campo "id" insiera el prefijo "m" + el número de orden de la media. Ejemplo: m1.

Ya en "href" insiera el nombre de la media con la extensión: "Artículo12-m1.wmv".

.. image:: img/mkp-tpmedia.jpg
   :align: center

Hecho eso, genere en archivo .xml.

Con el archivo .xml generado verifique se hay errores y corrija, se necesario, los atributos que cualifican el tipo de media.
El Programa presenta los atributos:

* mime-subtype - especifica el tipo de media como "video" o "application".
* mimetype     - especifica el formato de la media.

Es posible que el programa insiera valores incorrectos en los atributos mencionados arriba. Ejemplo:

.. image:: img/mkp-mime-subtype.jpg
   :align: center

Para corregir, excluya el valor "x-ms-wmv" y insiera apenas "wmv" que es el formato del video. Caso el atributo @mimetype presente valor diferente de "application" o "video", corrija el dato.


.. _sublista:

Identificación de sublistas
---------------------------

El programa Markup no hace la identificación de sublistas, mientras tanto es necesario utilizar un editor de XML para ajustar los ítems de sublista.
Hay dos métodos para la marcación manual de sublistas:

Método 1:
^^^^^^^^^

Aun en el programa Markup, seleccione toda la lista y marque con el elemento [*list] y genere el archivo .xml.
Con el archivo .xml generado, encuentre la lista y haga la siguiente alteración:

Primeramente, encuentre los ítems de sublista:

.. image:: img/mkp-itensublist.jpg
   :align: center

Adicione el elemento <list> arriba del primero ítem <list-item> de la sublista:

.. image:: img/mkp-sub-lista.jpg
   :align: center

Recorte el elemento </list-item> que consta arriba del elemento <list> de la sublista:

.. image:: img/mkp-recort-listitem.jpg
   :align: center

Pegue el elemento </list-item> recortado luego después del elemento </list> de la sublista:

.. image:: img/mkp-cola-list-item.jpg
   :align: center


Caso la sublista presente un marcador diferente del inserido en la lista, es posible adicionar el atributo @list-type na tag <list> de la sublista y inserir algún de los valores que sigue:

* order
* bullet
* alpha-lower
* alpha-upper
* roman-lower
* roman-upper
* simple


Método 2:
^^^^^^^^^

Caso la lista y sublista no tengan sido marcadas en el programa Markup, es posible que al generar el archivo .xml la lista tenga sido identificada como párrafos.
Por lo tanto, será necesario hacer la identificación manual de la lista y de la sublista.

Primeramente, borre todos los párrafos de la lista y sublista y marque todos los ítems con el elemento <list> acrecentando el atributo @list-type= con el valor correspondiente al marcador de la lista:

.. image:: img/mkp-manual-list.jpg
   :align: center

Insiera el elemento <list-item> y <p> para cada ítem de la lista:

.. image:: img/mkp-list-sem-sublist.jpg
   :align: center

Marque los ítems de la sublista:

.. image:: img/mkp-itensublist.jpg
   :align: center

Adicione un elemento <list> antes del primero elemento <list-item> de la sublista:

.. image:: img/mkp-sub-lista.jpg
   :align: center


Recorte el elemento </list-item> que consta antes del elemento <list> de la sublista:

.. image:: img/mkp-recort-listitem.jpg
   :align: center


Ahora, pegue el elemento </list-item> recortado luego después de </list> de la sublista:

.. image:: img/mkp-cola-list-item.jpg
   :align: center



.. _leyenda-traducida:

Leyendas Traducidas
-------------------

El Programa Markup no hace la marcación de figuras o tablas con leyendas traducidas. Para hacer la marcación es necesario utilizar un editor de XML. Verifique la marcación de leyendas de tablas y de figuras que sigue:

**Tablas**

Abra el archivo .xml en un editor de su preferencia y localice la tabla que presenta la leyenda traducida.

Insiera el elemento <table-wrap-group> envolviendo toda la tabla, desde <table-wrap>:

.. image:: img/mkp-tab-wrap-g-legend.jpg
   :align: center

Borre el @id="xx" de <table-wrap> y insiera el atributo de idioma @xml:lang="xx" con la sigla correspondiente al idioma principal de la tabla. En seguida, insiera un @id único para el <table-wrap-group>:

.. image:: img/mkp-tab-legend-ids.jpg
   :align: center


Insiera un novo elemento <table-wrap> con <label>, <caption> y <title> luego después de <table-wrap-group> con el atributo de idioma @xml:lang="xx" correspondiente al idioma de la traducción. E insiera la leyenda traducida en <title>:

.. image:: img/mkp-legenda-trans-tab.jpg
   :align: center


.. note:: Para tablas codificadas el proceso es lo mismo.


**Figuras**

Abra el archivo .xml en un editor de su preferencia y localice la figura que presenta la leyenda traducida.

Insiera el elemento <fig-group> envolviendo toda la figura, desde <fig>:

.. image:: img/mkp-fig-legend.jpg
   :align: center

Borre el @id="xx" de <fig> e insiera el atributo de idioma @xml:lang="xx" con la sigla correspondiente al idioma principal de la figura. En seguida, insiera un @id único para el <fig-group>:

.. image:: img/mkp-fig-group-trans.jpg
   :align: center


Insiera un nuevo elemento <fig> con <label>, <caption> y <title> logo abaixo de <fig-group> con el atributo de idioma @xml:lang="xx" correspondiente al idioma de la traducción. E insiera la leyenda traducida en <title>:

.. image:: img/mkp-fig-legend-traduzida.jpg
   :align: center


.. _author-sem-label:

Autores sin label
-----------------

Algunos autores no presentan label en autor y en afiliación. Para marcar el dato, haga la marcación tradicional del autor en el programa Markup e insiera en afiliación el ID de cada autor.
Después de generar el archivo .xml del documento, ábralo en un editor de XML e insiera la <xref> cerrada de cada autor.

.. image:: img/mkp-author-sem-label.jpg
   :align: center

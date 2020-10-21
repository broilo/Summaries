# Big Data

## O que é?

> Definição: "Big Data é uma nova geração de tecnologias e arquiteturas, desenhadas de maneira econômica para extrar *valor* de grandes *volumes* de dados, provenientes de uma *variedade* de fontes, permitindo alta *velocidade* na captura, exploração e análise dos dados" (IDC, 2011).

* Volume: data at scale
* Variedade: data in many forms
* Velocidade: data in motion
* Veracidade: data uncertainty
* Valor: só tem sentido em falar em Big Data se isso vai agregar algum valor, seja financeiro ou seja numa pesquisa.
    - Só armazenar os dados, não faz muito sentido.
        * É preciso extrair informação, valor.

**Exemplo:**  O Large Hadron Collider (LHC) produz aproxidamente 1 petabyte de dados por segundo (informação referente ao ano de 2013). Mas apenas 1% dos dados são processados, gerando 25 petabytes por ano.

> Ou seja: é impossível lidar com todo o conjunto de dados gerado!

* O volume de dados cresce muito, seja lá qual for a fonte.
* Esse volume cresceu de mais, e ficou difícil simplesmente usar as ferramentas que eram usadas antes.

## Como começar a pensar em Big Data?

* Aumento no volume de dados
    - Limitação dos bancos relacionais
        * Oportunidade de realizar computação paralela usando hardware de baixo custo.

> Trabalhar com um grande número de dados, processando de forma paralela com máquinas de baixo custo.

## Qual o formato que chegam os dados?

> Esses dados chegam de qualquer maneira e forma!

### Dados estruturados

> Exemplo: tabelas de um banco de dedos relacional, banco de dados semântico.

* Possui esquema fixo
* Formato bem definido
* Conhecimento prévio da estrutura de dados
* Simplicidade para relacionar informações
* Dificuldade para alterar o modelo -> isso é uma desvantagem!

**SQL**

* Pros:
    - Bancos de dados relacionais são bons para dados estruturados e transacionais
    - Possuem baixo tempo de resposta e são capazes de realizar consultas compelxas.

* Contras: 
    - Pode ser difícil de escalar.
    - Esquema fixo pode dificultar a organização e evolução dos dados.

* Ex: Oracle, MySQL, PostgreSQL, SQL Server.

### Dados não estruturados

> Exemplo: documentos, informações de streaming, chave/valor.

* Sem tipo predefinido -> o dado vai sendo modelado com o tempo.
* Não possui estrutura regular
* Pouco ou nenhum controle sobre a forma
* Manipulação mais simplificada
* Facilidade de alteração do modelo

**NoSQL**

* Pros:
    - Bom para dados não relacionais.
    - Arquitetura sem esquema permite mudanças freqüentes.
    - Escalabilidade mais fácil
    - Roda bem em ambientes distribuídos.

* Contras:
    - Ferramentas ainda em fase de amadurecimento.
    - Incompatibilidade com SQL.

* Ex: MongoDB, Elastic Search, HBase, CouchBase.

## Big Data evoluiu com o aumento do volume de dados, mas como isso aconteceu?

* Escalamento vertical
    * Antes, se tentava escalar a máquina -> Montar uma máquina mais poderosa.
    * Só que isso começou a ser inviável e caroo.

* Escalamento horizontal
    * Ao invés de usar máquinas cada vez mais poderoas -> usar então máquinas mais simples, porém em quantidade (cluster para processar os dados em paralelo).
    * É aqui que mora o grande universo de Big Data!

> Obs: Big Data é uma tecnologia que permite processar um grande volume de dados. E esses dados *não cabem na memória do teu pc*. Ou seja, se tu tens um conjunto de dados que cabe na memória do teu PC, então tu não precisa usar Big Data para processar estes dados.

## Qual o papel de um Cientista de Dados em Big Data?

> Tem como principal função validar hipóteses e extrair insights a partir dos dados.

* Atribuições:
    * Data mining
    * Sistemas de recomendação
    * Machine Learning
    * Inteligência Artificial
    * Modelagem Estatística
    * Metodologia de testes

* Skills:
    * Matemática
    * Estatísitca
    * Visualização de dados
    * Machine Learning
    * Programação

## Qual o papel de um Engenheiro de Dados em Big Data?

> Garantir o fluxo contínuo entre as fontes de dados e os sistemas de armazenamento e processamento. São responsáveis por definir a arquitetura dos dados.

* Atribuições:
    * Transformação de dados
    * Processamento paralelo
    * Integração de sistemas heterogêneos
    * Construir aplocações escaláveis
    * Análise de performance

* Skills:
    * Programação
    * Design de banco de dados e otimização

# Spark

> Tecnologia criada para aumentar ainda mais a performance de processamento de grande volumes de dados em paralelo.

* Spark roda em cima do Hadoop
    * Isso faz com que o Spark leia arquivos que estão no HDFS.
* Tem uma API unificada e bem vasta.

```
>>> data=[("Newton", 1643), ("Einstein", 1879), ("Gauss", 1777)]
>>> df=spark.createDataFrame(data, ["name", "birth"])
>>> df.printSchema()
root
 |-- name: string (nullable = true)
 |-- birth: long (nullable = true)

>>> df.show()
+--------+-----+                                                                
|    name|birth|
+--------+-----+
|  Newton| 1643|
|Einstein| 1879|
|   Gauss| 1777|
+--------+-----+

>>> PATH="/home/broilo/Downloads/titanic/train.csv"
>>> df=spark.read.format("com.databricks.spark.csv") \
...    .option("header", "true") \
...    .option("inferSchema", "true")
>>> df.load(PATH)
DataFrame[PassengerId: int, Survived: int, Pclass: int, Name: string, Sex: string, Age: double, SibSp: int, Parch: int, Ticket: string, Fare: double, Cabin: string, Embarked: string]
>>> df.show()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'DataFrameReader' object has no attribute 'show'
>>> df=spark.read.format("com.databricks.spark.csv") \
... .option("header", "true") \
... .option("inferSchema", "true") \
... .load(PATH)
>>> df.show()
+-----------+--------+------+--------------------+------+----+-----+-----+----------------+-------+-----+--------+
|PassengerId|Survived|Pclass|                Name|   Sex| Age|SibSp|Parch|          Ticket|   Fare|Cabin|Embarked|
+-----------+--------+------+--------------------+------+----+-----+-----+----------------+-------+-----+--------+
|          1|       0|     3|Braund, Mr. Owen ...|  male|22.0|    1|    0|       A/5 21171|   7.25| null|       S|
|          2|       1|     1|Cumings, Mrs. Joh...|female|38.0|    1|    0|        PC 17599|71.2833|  C85|       C|
|          3|       1|     3|Heikkinen, Miss. ...|female|26.0|    0|    0|STON/O2. 3101282|  7.925| null|       S|
|          4|       1|     1|Futrelle, Mrs. Ja...|female|35.0|    1|    0|          113803|   53.1| C123|       S|
|          5|       0|     3|Allen, Mr. Willia...|  male|35.0|    0|    0|          373450|   8.05| null|       S|
|          6|       0|     3|    Moran, Mr. James|  male|null|    0|    0|          330877| 8.4583| null|       Q|
|          7|       0|     1|McCarthy, Mr. Tim...|  male|54.0|    0|    0|           17463|51.8625|  E46|       S|
|          8|       0|     3|Palsson, Master. ...|  male| 2.0|    3|    1|          349909| 21.075| null|       S|
|          9|       1|     3|Johnson, Mrs. Osc...|female|27.0|    0|    2|          347742|11.1333| null|       S|
|         10|       1|     2|Nasser, Mrs. Nich...|female|14.0|    1|    0|          237736|30.0708| null|       C|
|         11|       1|     3|Sandstrom, Miss. ...|female| 4.0|    1|    1|         PP 9549|   16.7|   G6|       S|
|         12|       1|     1|Bonnell, Miss. El...|female|58.0|    0|    0|          113783|  26.55| C103|       S|
|         13|       0|     3|Saundercock, Mr. ...|  male|20.0|    0|    0|       A/5. 2151|   8.05| null|       S|
|         14|       0|     3|Andersson, Mr. An...|  male|39.0|    1|    5|          347082| 31.275| null|       S|
|         15|       0|     3|Vestrom, Miss. Hu...|female|14.0|    0|    0|          350406| 7.8542| null|       S|
|         16|       1|     2|Hewlett, Mrs. (Ma...|female|55.0|    0|    0|          248706|   16.0| null|       S|
|         17|       0|     3|Rice, Master. Eugene|  male| 2.0|    4|    1|          382652| 29.125| null|       Q|
|         18|       1|     2|Williams, Mr. Cha...|  male|null|    0|    0|          244373|   13.0| null|       S|
|         19|       0|     3|Vander Planke, Mr...|female|31.0|    1|    0|          345763|   18.0| null|       S|
|         20|       1|     3|Masselmani, Mrs. ...|female|null|    0|    0|            2649|  7.225| null|       C|
+-----------+--------+------+--------------------+------+----+-----+-----+----------------+-------+-----+--------+
only showing top 20 rows

>>>
```

## Refências

1. [Curso de Big Data](https://www.youtube.com/watch?v=1SNoNTaWFIo)

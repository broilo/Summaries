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

## Exemplo:

```
$SPARK_HOME/bin/pyspark

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
...    .option("inferSchema", "true") \
...    .load(PATH)
>>> df.printSchema()
root
 |-- PassengerId: integer (nullable = true)
 |-- Survived: integer (nullable = true)
 |-- Pclass: integer (nullable = true)
 |-- Name: string (nullable = true)
 |-- Sex: string (nullable = true)
 |-- Age: double (nullable = true)
 |-- SibSp: integer (nullable = true)
 |-- Parch: integer (nullable = true)
 |-- Ticket: string (nullable = true)
 |-- Fare: double (nullable = true)
 |-- Cabin: string (nullable = true)
 |-- Embarked: string (nullable = true)

>>> df.count()
891
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

>>> df.select("Name", "Survived").show()
+--------------------+--------+
|                Name|Survived|
+--------------------+--------+
|Braund, Mr. Owen ...|       0|
|Cumings, Mrs. Joh...|       1|
|Heikkinen, Miss. ...|       1|
|Futrelle, Mrs. Ja...|       1|
|Allen, Mr. Willia...|       0|
|    Moran, Mr. James|       0|
|McCarthy, Mr. Tim...|       0|
|Palsson, Master. ...|       0|
|Johnson, Mrs. Osc...|       1|
|Nasser, Mrs. Nich...|       1|
|Sandstrom, Miss. ...|       1|
|Bonnell, Miss. El...|       1|
|Saundercock, Mr. ...|       0|
|Andersson, Mr. An...|       0|
|Vestrom, Miss. Hu...|       0|
|Hewlett, Mrs. (Ma...|       1|
|Rice, Master. Eugene|       0|
|Williams, Mr. Cha...|       1|
|Vander Planke, Mr...|       0|
|Masselmani, Mrs. ...|       1|
+--------------------+--------+
only showing top 20 rows

>>> df.select("Name", "Survived").show(truncate=False)
+-------------------------------------------------------+--------+
|Name                                                   |Survived|
+-------------------------------------------------------+--------+
|Braund, Mr. Owen Harris                                |0       |
|Cumings, Mrs. John Bradley (Florence Briggs Thayer)    |1       |
|Heikkinen, Miss. Laina                                 |1       |
|Futrelle, Mrs. Jacques Heath (Lily May Peel)           |1       |
|Allen, Mr. William Henry                               |0       |
|Moran, Mr. James                                       |0       |
|McCarthy, Mr. Timothy J                                |0       |
|Palsson, Master. Gosta Leonard                         |0       |
|Johnson, Mrs. Oscar W (Elisabeth Vilhelmina Berg)      |1       |
|Nasser, Mrs. Nicholas (Adele Achem)                    |1       |
|Sandstrom, Miss. Marguerite Rut                        |1       |
|Bonnell, Miss. Elizabeth                               |1       |
|Saundercock, Mr. William Henry                         |0       |
|Andersson, Mr. Anders Johan                            |0       |
|Vestrom, Miss. Hulda Amanda Adolfina                   |0       |
|Hewlett, Mrs. (Mary D Kingcome)                        |1       |
|Rice, Master. Eugene                                   |0       |
|Williams, Mr. Charles Eugene                           |1       |
|Vander Planke, Mrs. Julius (Emelia Maria Vandemoortele)|0       |
|Masselmani, Mrs. Fatima                                |1       |
+-------------------------------------------------------+--------+
only showing top 20 rows

>>> df.select("Name", "Survived").show(2, False)
+---------------------------------------------------+--------+
|Name                                               |Survived|
+---------------------------------------------------+--------+
|Braund, Mr. Owen Harris                            |0       |
|Cumings, Mrs. John Bradley (Florence Briggs Thayer)|1       |
+---------------------------------------------------+--------+
only showing top 2 rows

>>> df.select("Name", "Survived").show(2)
+--------------------+--------+
|                Name|Survived|
+--------------------+--------+
|Braund, Mr. Owen ...|       0|
|Cumings, Mrs. Joh...|       1|
+--------------------+--------+
only showing top 2 rows

>>> df.filter(df["Embarked"]=="S").count()
644

>>> df.select(df["Embarked"]).distinct().show()
+--------+                                                                      
|Embarked|
+--------+
|       Q|
|    null|
|       C|
|       S|
+--------+

>>> df.select(df["Embarked"]).distinct().show(truncate=False)
+--------+
|Embarked|
+--------+
|Q       |
|null    |
|C       |
|S       |
+--------+

>>> df.select(df["Age"]).distinct().show(truncate=False)
+----+
|Age |
+----+
|8.0 |
|70.0|
|7.0 |
|20.5|
|49.0|
|29.0|
|40.5|
|64.0|
|47.0|
|42.0|
|24.5|
|44.0|
|35.0|
|null|
|62.0|
|18.0|
|80.0|
|34.5|
|39.0|
|1.0 |
+----+
only showing top 20 rows

>>> df.select(df["Age"]).distinct().show(100, truncate=False)
+----+
|Age |
+----+
|8.0 |
|70.0|
|7.0 |
|20.5|
|49.0|
|29.0|
|40.5|
|64.0|
|47.0|
|42.0|
|24.5|
|44.0|
|35.0|
|null|
|62.0|
|18.0|
|80.0|
|34.5|
|39.0|
|1.0 |
|45.5|
|34.0|
|37.0|
|25.0|
|36.0|
|0.92|
|41.0|
|0.42|
|4.0 |
|30.5|
|23.0|
|56.0|
|50.0|
|14.5|
|45.0|
|0.75|
|71.0|
|32.5|
|31.0|
|11.0|
|58.0|
|23.5|
|21.0|
|51.0|
|14.0|
|0.67|
|63.0|
|48.0|
|22.0|
|60.0|
|74.0|
|66.0|
|36.5|
|19.0|
|3.0 |
|53.0|
|61.0|
|59.0|
|46.0|
|28.0|
|28.5|
|2.0 |
|57.0|
|17.0|
|38.0|
|27.0|
|10.0|
|40.0|
|30.0|
|13.0|
|33.0|
|6.0 |
|20.0|
|52.0|
|32.0|
|15.0|
|5.0 |
|24.0|
|55.0|
|70.5|
|55.5|
|26.0|
|0.83|
|9.0 |
|65.0|
|16.0|
|12.0|
|54.0|
|43.0|
+----+

>>> df.groupBy("Age").count().show(truncate=False)
+----+-----+
|Age |count|
+----+-----+
|8.0 |4    |
|70.0|2    |
|7.0 |3    |
|20.5|1    |
|49.0|6    |
|29.0|20   |
|40.5|2    |
|64.0|2    |
|47.0|9    |
|42.0|13   |
|24.5|1    |
|44.0|9    |
|35.0|18   |
|null|177  |
|62.0|4    |
|18.0|26   |
|80.0|1    |
|34.5|1    |
|39.0|14   |
|1.0 |7    |
+----+-----+
only showing top 20 rows

>>> df.groupBy("Age").count().show(100, truncate=False)
+----+-----+
|Age |count|
+----+-----+
|8.0 |4    |
|70.0|2    |
|7.0 |3    |
|20.5|1    |
|49.0|6    |
|29.0|20   |
|40.5|2    |
|64.0|2    |
|47.0|9    |
|42.0|13   |
|24.5|1    |
|44.0|9    |
|35.0|18   |
|null|177  |
|62.0|4    |
|18.0|26   |
|80.0|1    |
|34.5|1    |
|39.0|14   |
|1.0 |7    |
|45.5|2    |
|34.0|15   |
|37.0|6    |
|25.0|23   |
|36.0|22   |
|0.92|1    |
|41.0|6    |
|0.42|1    |
|4.0 |10   |
|30.5|2    |
|23.0|15   |
|56.0|4    |
|50.0|10   |
|14.5|1    |
|45.0|12   |
|0.75|2    |
|71.0|2    |
|32.5|2    |
|31.0|17   |
|11.0|4    |
|58.0|5    |
|23.5|1    |
|21.0|24   |
|51.0|7    |
|14.0|6    |
|0.67|1    |
|63.0|2    |
|48.0|9    |
|22.0|27   |
|60.0|4    |
|74.0|1    |
|66.0|1    |
|36.5|1    |
|19.0|25   |
|3.0 |6    |
|53.0|1    |
|61.0|3    |
|59.0|2    |
|46.0|3    |
|28.0|25   |
|28.5|2    |
|2.0 |10   |
|57.0|2    |
|17.0|13   |
|38.0|11   |
|27.0|18   |
|10.0|2    |
|40.0|13   |
|30.0|25   |
|13.0|2    |
|33.0|15   |
|6.0 |3    |
|20.0|15   |
|52.0|6    |
|32.0|18   |
|15.0|5    |
|5.0 |4    |
|24.0|30   |
|55.0|2    |
|70.5|1    |
|55.5|1    |
|0.83|2    |
|26.0|18   |
|9.0 |8    |
|65.0|3    |
|16.0|17   |
|12.0|1    |
|54.0|8    |
|43.0|5    |
+----+-----+

>>> df.groupBy("Age").count().orderBy("count").show(truncate=False)
+----+-----+                                                                    
|Age |count|
+----+-----+
|55.5|1    |
|66.0|1    |
|53.0|1    |
|70.5|1    |
|0.67|1    |
|0.92|1    |
|74.0|1    |
|0.42|1    |
|23.5|1    |
|36.5|1    |
|20.5|1    |
|14.5|1    |
|24.5|1    |
|80.0|1    |
|34.5|1    |
|12.0|1    |
|40.5|2    |
|0.75|2    |
|71.0|2    |
|64.0|2    |
+----+-----+
only showing top 20 rows

>> df.groupBy("Age").count().orderBy("count", ascending=False).show(truncate=False)
+----+-----+                                                                    
|Age |count|
+----+-----+
|null|177  |
|24.0|30   |
|22.0|27   |
|18.0|26   |
|19.0|25   |
|28.0|25   |
|30.0|25   |
|21.0|24   |
|25.0|23   |
|36.0|22   |
|29.0|20   |
|26.0|18   |
|27.0|18   |
|35.0|18   |
|32.0|18   |
|31.0|17   |
|16.0|17   |
|34.0|15   |
|23.0|15   |
|33.0|15   |
+----+-----+
only showing top 20 rows

>>> df.groupBy("Age").sum("Fare").show()
+----+------------------+
| Age|         sum(Fare)|
+----+------------------+
| 8.0|             113.2|
|70.0|              81.5|
| 7.0|           95.0625|
|20.5|              7.25|
|49.0|          359.5751|
|29.0|          541.8165|
|40.5|             22.25|
|64.0|             289.0|
|47.0|248.41250000000002|
|42.0|          482.6334|
|24.5|              8.05|
|44.0|267.82500000000005|
|35.0|1607.6249999999998|
|null| 3922.066300000001|
|62.0|             143.6|
|18.0| 989.6499999999999|
|80.0|              30.0|
|34.5|            6.4375|
|39.0| 513.2665999999999|
| 1.0|210.04169999999996|
+----+------------------+
only showing top 20 rows

>>> df.describe("Fare").show()
+-------+-----------------+
|summary|             Fare|
+-------+-----------------+
|  count|              891|
|   mean| 32.2042079685746|
| stddev|49.69342859718089|
|    min|              0.0|
|    max|         512.3292|
+-------+-----------------+

>>> df.groupBy("Age").agg(F.sum(df.Fare), F.max(df.Fare), F.count(df.Fare), F.avg(df.Fare)).show()
+----+------------------+---------+-----------+------------------+
| Age|         sum(Fare)|max(Fare)|count(Fare)|         avg(Fare)|
+----+------------------+---------+-----------+------------------+
| 8.0|             113.2|    36.75|          4|              28.3|
|70.0|              81.5|     71.0|          2|             40.75|
| 7.0|           95.0625|  39.6875|          3|           31.6875|
|20.5|              7.25|     7.25|          1|              7.25|
|49.0|          359.5751| 110.8833|          6|59.929183333333334|
|29.0|          541.8165| 211.3375|         20|27.090825000000002|
|40.5|             22.25|     14.5|          2|            11.125|
|64.0|             289.0|    263.0|          2|             144.5|
|47.0|248.41250000000002|  52.5542|          9| 27.60138888888889|
|42.0|          482.6334|  227.525|         13|37.125646153846155|
|24.5|              8.05|     8.05|          1|              8.05|
|44.0|267.82500000000005|     90.0|          9| 29.75833333333334|
|35.0|1607.6249999999998| 512.3292|         18| 89.31249999999999|
|null| 3922.066300000001|  227.525|        177|22.158566666666673|
|62.0|             143.6|     80.0|          4|              35.9|
|18.0| 989.6499999999999|  262.375|         26| 38.06346153846153|
|80.0|              30.0|     30.0|          1|              30.0|
|34.5|            6.4375|   6.4375|          1|            6.4375|
|39.0| 513.2665999999999| 110.8833|         14|36.661899999999996|
| 1.0|210.04169999999996|     46.9|          7|30.005957142857138|
+----+------------------+---------+-----------+------------------+
only showing top 20 rows

>>> df.groupBy("Age").agg(F.sum("Fare"), F.max("Fare"), F.count("Fare"), F.avg("Fare")).show()
+----+------------------+---------+-----------+------------------+
| Age|         sum(Fare)|max(Fare)|count(Fare)|         avg(Fare)|
+----+------------------+---------+-----------+------------------+
| 8.0|             113.2|    36.75|          4|              28.3|
|70.0|              81.5|     71.0|          2|             40.75|
| 7.0|           95.0625|  39.6875|          3|           31.6875|
|20.5|              7.25|     7.25|          1|              7.25|
|49.0|          359.5751| 110.8833|          6|59.929183333333334|
|29.0|          541.8165| 211.3375|         20|27.090825000000002|
|40.5|             22.25|     14.5|          2|            11.125|
|64.0|             289.0|    263.0|          2|             144.5|
|47.0|248.41250000000002|  52.5542|          9| 27.60138888888889|
|42.0|          482.6334|  227.525|         13|37.125646153846155|
|24.5|              8.05|     8.05|          1|              8.05|
|44.0|267.82500000000005|     90.0|          9| 29.75833333333334|
|35.0|1607.6249999999998| 512.3292|         18| 89.31249999999999|
|null| 3922.066300000001|  227.525|        177|22.158566666666673|
|62.0|             143.6|     80.0|          4|              35.9|
|18.0| 989.6499999999999|  262.375|         26| 38.06346153846153|
|80.0|              30.0|     30.0|          1|              30.0|
|34.5|            6.4375|   6.4375|          1|            6.4375|
|39.0| 513.2665999999999| 110.8833|         14|36.661899999999996|
| 1.0|210.04169999999996|     46.9|          7|30.005957142857138|
+----+------------------+---------+-----------+------------------+
only showing top 20 rows

>>> df.groupBy("Age").agg(F.sum("Fare"), F.max("Fare"), F.count("Fare"), F.avg("Fare")).show(100, truncate=False)
+----+------------------+---------+-----------+------------------+
|Age |sum(Fare)         |max(Fare)|count(Fare)|avg(Fare)         |
+----+------------------+---------+-----------+------------------+
|8.0 |113.2             |36.75    |4          |28.3              |
|70.0|81.5              |71.0     |2          |40.75             |
|7.0 |95.0625           |39.6875  |3          |31.6875           |
|20.5|7.25              |7.25     |1          |7.25              |
|49.0|359.5751          |110.8833 |6          |59.929183333333334|
|29.0|541.8165          |211.3375 |20         |27.090825000000002|
|40.5|22.25             |14.5     |2          |11.125            |
|64.0|289.0             |263.0    |2          |144.5             |
|47.0|248.41250000000002|52.5542  |9          |27.60138888888889 |
|42.0|482.6334          |227.525  |13         |37.125646153846155|
|24.5|8.05              |8.05     |1          |8.05              |
|44.0|267.82500000000005|90.0     |9          |29.75833333333334 |
|35.0|1607.6249999999998|512.3292 |18         |89.31249999999999 |
|null|3922.066300000001 |227.525  |177        |22.158566666666673|
|62.0|143.6             |80.0     |4          |35.9              |
|18.0|989.6499999999999 |262.375  |26         |38.06346153846153 |
|80.0|30.0              |30.0     |1          |30.0              |
|34.5|6.4375            |6.4375   |1          |6.4375            |
|39.0|513.2665999999999 |110.8833 |14         |36.661899999999996|
|1.0 |210.04169999999996|46.9     |7          |30.005957142857138|
|45.5|35.725            |28.5     |2          |17.8625           |
|34.0|249.54580000000004|32.5     |15         |16.63638666666667 |
|37.0|178.8667          |53.1     |6          |29.811116666666667|
|25.0|561.5626          |151.55   |23         |24.415765217391304|
|36.0|1319.2291         |512.3292 |22         |59.96495909090909 |
|0.92|151.55            |151.55   |1          |151.55            |
|41.0|235.13330000000002|134.5    |6          |39.18888333333334 |
|0.42|8.5167            |8.5167   |1          |8.5167            |
|4.0 |295.4333          |81.8583  |10         |29.543329999999997|
|30.5|15.8              |8.05     |2          |7.9               |
|23.0|569.9207999999999 |263.0    |15         |37.994719999999994|
|56.0|175.9041          |83.1583  |4          |43.976025         |
|50.0|640.2583          |247.5208 |10         |64.02583          |
|14.5|14.4542           |14.4542  |1          |14.4542           |
|45.0|441.82090000000005|164.8667 |12         |36.81840833333334 |
|0.75|38.5166           |19.2583  |2          |19.2583           |
|71.0|84.1584           |49.5042  |2          |42.0792           |
|32.5|43.0708           |30.0708  |2          |21.5354           |
|31.0|629.1542          |164.8667 |17         |37.00907058823529 |
|11.0|216.9625          |120.0    |4          |54.240625         |
|58.0|469.5083000000001 |153.4625 |5          |93.90166000000002 |
|23.5|7.2292            |7.2292   |1          |7.2292            |
|21.0|757.5749          |262.375  |24         |31.56562083333333 |
|51.0|201.26670000000001|77.9583  |7          |28.752385714285715|
|14.0|255.7542          |120.0    |6          |42.6257           |
|0.67|14.5              |14.5     |1          |14.5              |
|63.0|87.5458           |77.9583  |2          |43.7729           |
|48.0|341.0376          |76.7292  |9          |37.89306666666667 |
|22.0|688.6291          |151.55   |27         |25.50478148148148 |
|60.0|220.0             |79.2     |4          |55.0              |
|74.0|7.775             |7.775    |1          |7.775             |
|66.0|10.5              |10.5     |1          |10.5              |
|36.5|26.0              |26.0     |1          |26.0              |
|19.0|696.7374000000001 |263.0    |25         |27.869496000000005|
|3.0 |154.6917          |41.5792  |6          |25.78195          |
|53.0|51.4792           |51.4792  |1          |51.4792           |
|61.0|72.0583           |33.5     |3          |24.019433333333335|
|59.0|20.75             |13.5     |2          |10.375            |
|46.0|166.375           |79.2     |3          |55.458333333333336|
|28.0|525.5039999999999 |82.1708  |25         |21.020159999999997|
|28.5|23.3292           |16.1     |2          |11.6646           |
|2.0 |375.3625          |151.55   |10         |37.53625          |
|57.0|22.85             |12.35    |2          |11.425            |
|17.0|369.0625          |110.8833 |13         |28.389423076923077|
|38.0|690.2666          |227.525  |11         |62.751509090909096|
|27.0|546.5041000000001 |211.5    |18         |30.361338888888895|
|10.0|52.05             |27.9     |2          |26.025            |
|40.0|482.42910000000006|153.4625 |13         |37.10993076923077 |
|30.0|638.5417          |106.425  |25         |25.541668         |
|13.0|26.7292           |19.5     |2          |13.3646           |
|33.0|387.3833000000001 |90.0     |15         |25.82555333333334 |
|6.0 |76.75             |33.0     |3          |25.583333333333332|
|20.0|129.3626          |15.7417  |15         |8.624173333333333 |
|52.0|308.4167          |93.5     |6          |51.40278333333333 |
|32.0|437.8208000000001 |76.2917  |18         |24.323377777777782|
|15.0|248.27509999999998|211.3375 |5          |49.65501999999999 |
|5.0 |90.8708           |31.3875  |4          |22.7177           |
|24.0|1291.0707         |263.0    |30         |43.03569          |
|55.0|46.5              |30.5     |2          |23.25             |
|70.5|7.75              |7.75     |1          |7.75              |
|55.5|8.05              |8.05     |1          |8.05              |
|0.83|47.75             |29.0     |2          |23.875            |
|26.0|343.5625          |78.85    |18         |19.086805555555557|
|9.0 |223.50830000000002|46.9     |8          |27.938537500000002|
|65.0|96.27919999999999 |61.9792  |3          |32.093066666666665|
|16.0|437.66669999999993|86.5     |17         |25.745099999999997|
|12.0|11.2417           |11.2417  |1          |11.2417           |
|54.0|355.81669999999997|78.2667  |8          |44.477087499999996|
|43.0|298.9875          |211.3375 |5          |59.7975           |
+----+------------------+---------+-----------+------------------+

>>> df.groupBy("Age").agg(F.sum("Fare"), F.max("Fare"), F.count("Fare"), F.avg("Fare")) \
...  .orderBy("sum(Fare)", descending=False) \
...  .show(100, truncate=False)
+----+------------------+---------+-----------+------------------+              
|Age |sum(Fare)         |max(Fare)|count(Fare)|avg(Fare)         |
+----+------------------+---------+-----------+------------------+
|34.5|6.4375            |6.4375   |1          |6.4375            |
|23.5|7.2292            |7.2292   |1          |7.2292            |
|20.5|7.25              |7.25     |1          |7.25              |
|70.5|7.75              |7.75     |1          |7.75              |
|74.0|7.775             |7.775    |1          |7.775             |
|55.5|8.05              |8.05     |1          |8.05              |
|24.5|8.05              |8.05     |1          |8.05              |
|0.42|8.5167            |8.5167   |1          |8.5167            |
|66.0|10.5              |10.5     |1          |10.5              |
|12.0|11.2417           |11.2417  |1          |11.2417           |
|14.5|14.4542           |14.4542  |1          |14.4542           |
|0.67|14.5              |14.5     |1          |14.5              |
|30.5|15.8              |8.05     |2          |7.9               |
|59.0|20.75             |13.5     |2          |10.375            |
|40.5|22.25             |14.5     |2          |11.125            |
|57.0|22.85             |12.35    |2          |11.425            |
|28.5|23.3292           |16.1     |2          |11.6646           |
|36.5|26.0              |26.0     |1          |26.0              |
|13.0|26.7292           |19.5     |2          |13.3646           |
|80.0|30.0              |30.0     |1          |30.0              |
|45.5|35.725            |28.5     |2          |17.8625           |
|0.75|38.5166           |19.2583  |2          |19.2583           |
|32.5|43.0708           |30.0708  |2          |21.5354           |
|55.0|46.5              |30.5     |2          |23.25             |
|0.83|47.75             |29.0     |2          |23.875            |
|53.0|51.4792           |51.4792  |1          |51.4792           |
|10.0|52.05             |27.9     |2          |26.025            |
|61.0|72.0583           |33.5     |3          |24.019433333333335|
|6.0 |76.75             |33.0     |3          |25.583333333333332|
|70.0|81.5              |71.0     |2          |40.75             |
|71.0|84.1584           |49.5042  |2          |42.0792           |
|63.0|87.5458           |77.9583  |2          |43.7729           |
|5.0 |90.8708           |31.3875  |4          |22.7177           |
|7.0 |95.0625           |39.6875  |3          |31.6875           |
|65.0|96.27919999999999 |61.9792  |3          |32.093066666666665|
|8.0 |113.2             |36.75    |4          |28.3              |
|20.0|129.3626          |15.7417  |15         |8.624173333333333 |
|62.0|143.6             |80.0     |4          |35.9              |
|0.92|151.55            |151.55   |1          |151.55            |
|3.0 |154.6917          |41.5792  |6          |25.78195          |
|46.0|166.375           |79.2     |3          |55.458333333333336|
|56.0|175.9041          |83.1583  |4          |43.976025         |
|37.0|178.8667          |53.1     |6          |29.811116666666667|
|51.0|201.26670000000001|77.9583  |7          |28.752385714285715|
|1.0 |210.04169999999996|46.9     |7          |30.005957142857138|
|11.0|216.9625          |120.0    |4          |54.240625         |
|60.0|220.0             |79.2     |4          |55.0              |
|9.0 |223.50830000000002|46.9     |8          |27.938537500000002|
|41.0|235.13330000000002|134.5    |6          |39.18888333333334 |
|15.0|248.27509999999998|211.3375 |5          |49.65501999999999 |
|47.0|248.41250000000002|52.5542  |9          |27.60138888888889 |
|34.0|249.54580000000004|32.5     |15         |16.63638666666667 |
|14.0|255.7542          |120.0    |6          |42.6257           |
|44.0|267.82500000000005|90.0     |9          |29.75833333333334 |
|64.0|289.0             |263.0    |2          |144.5             |
|4.0 |295.4333          |81.8583  |10         |29.543329999999997|
|43.0|298.9875          |211.3375 |5          |59.7975           |
|52.0|308.4167          |93.5     |6          |51.40278333333333 |
|48.0|341.0376          |76.7292  |9          |37.89306666666667 |
|26.0|343.5625          |78.85    |18         |19.086805555555557|
|54.0|355.81669999999997|78.2667  |8          |44.477087499999996|
|49.0|359.5751          |110.8833 |6          |59.929183333333334|
|17.0|369.0625          |110.8833 |13         |28.389423076923077|
|2.0 |375.3625          |151.55   |10         |37.53625          |
|33.0|387.3833000000001 |90.0     |15         |25.82555333333334 |
|16.0|437.66669999999993|86.5     |17         |25.745099999999997|
|32.0|437.8208000000001 |76.2917  |18         |24.323377777777782|
|45.0|441.82090000000005|164.8667 |12         |36.81840833333334 |
|58.0|469.5083000000001 |153.4625 |5          |93.90166000000002 |
|40.0|482.42910000000006|153.4625 |13         |37.10993076923077 |
|42.0|482.6334          |227.525  |13         |37.125646153846155|
|39.0|513.2665999999999 |110.8833 |14         |36.661899999999996|
|28.0|525.5039999999999 |82.1708  |25         |21.020159999999997|
|29.0|541.8165          |211.3375 |20         |27.090825000000002|
|27.0|546.5041000000001 |211.5    |18         |30.361338888888895|
|25.0|561.5626          |151.55   |23         |24.415765217391304|
|23.0|569.9207999999999 |263.0    |15         |37.994719999999994|
|31.0|629.1542          |164.8667 |17         |37.00907058823529 |
|30.0|638.5417          |106.425  |25         |25.541668         |
|50.0|640.2583          |247.5208 |10         |64.02583          |
|22.0|688.6291          |151.55   |27         |25.50478148148148 |
|38.0|690.2666          |227.525  |11         |62.751509090909096|
|19.0|696.7374000000001 |263.0    |25         |27.869496000000005|
|21.0|757.5749          |262.375  |24         |31.56562083333333 |
|18.0|989.6499999999999 |262.375  |26         |38.06346153846153 |
|24.0|1291.0707         |263.0    |30         |43.03569          |
|36.0|1319.2291         |512.3292 |22         |59.96495909090909 |
|35.0|1607.6249999999998|512.3292 |18         |89.31249999999999 |
|null|3922.066300000001 |227.525  |177        |22.158566666666673|
+----+------------------+---------+-----------+------------------+

``` 

## Como submeter um pyspark script?

```
$SPARK_HOME/bin/spark-submit --master local[2] script-example.py
```
* Roda localmente na minha máquina
* Utilizando somente 2 núcleos de processamento
* Roda o script-example.py

## Como rodar o Spark no Jupyter?

```
$ export PYSPARK_DRIVER_PYTHON=jupyter
$ export PYSPARK_DRIVER_PYTHON_OPTS="notebook"
$ $SPARK_HOME/bin/pyspark
```

# Como Big Data funciona na prática?

 * Aplicações
    * Kafka: Sistema de armazenamento de dados distribuídos. É uma ferramenta que recebe os dados e os armazena por algum tempo.
        * Streaming: Aplicações que vão executar alguma coisa assim que o dado chega. E.g., um sistema de detecção de fraude.
            * Aplicações que em geral tenham um requisito de tempo e que precisa ser feito algo de imediato.
        * Batch: Aplicações que podem esperar os dados se acumularem para processá-los. Alicações que processam os dados que já estão armazenados em algum lugar (Hadoop-HDFS).
            ETL: Ferramentas que vão ler os dados, eventualmente vão fazer alguma agregação ou sumarização, e que vão jogar estes dados em algum banco de dados relacional. São jobs que lêem os dados, fazem alguma análise e disponibilizam em alguma ferramente que podem fazer uma consulta SQL, Tableau...
            * Machine Learning: Extrair algum tipo de inteligência dos dados. Processar os dados de forma que tenham alguma informação útil para o meu negócio.
                * Resultado do processo de ML atualiza um Cache, e este Cashe fica disponível para as aplicações online.
## Referências

1. [Curso de Big Data](https://www.youtube.com/watch?v=1SNoNTaWFIo)
1. [Pyspark.sql Documentation](https://spark.apache.org/docs/latest/api/python/pyspark.sql.html)

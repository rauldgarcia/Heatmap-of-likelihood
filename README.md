**Ajuste de distribuciones de probabilidad a datos de train y la distribución predictiva (test) para distribución gaussiana unidimensional.**

1. Defina n>10 puntos aleatorios extraídos de una distribución gaussiana (μ0, σ0).

   μ0=5, σ0=1.5

2. Grafique 3 figuras donde muestre los puntos, los valores de likelihood para 3 gaussianas.

   μ1=3, σ1=1

μ2=6, σ2=1.6

μ3=5.1, σ3=1.4

3. Genera el mapa térmico de las probabilidades  μ ∈ [2.5, 6.5] y σ ∈ [0, 2] y colocar una cruz en el máximo ML.

   Dividir el intervalo μ en 10 intervalos

Dividir el intervalo σ en 10 intervalos

4. Calcule con ML, μ, σ y vea que tanto coincide con su mapa termico.

Para obtener los puntos aleatorios se utiliza la función random.gauss de la librería random de python, a la cual se le ingresa como valores de entrada μ0=5, σ0=1.5 y nos da como dato de salida puntos correspondientes a la gaussiana de manera aleatoria. 

La ecuación utilizadas para calcular el likelihood es:

![](Aspose.Words.59bd68a6-9569-4f50-8413-dc21f1b4f0b6.001.png)

Mientras que la ecuación para calcular el  μ, σ a partir de los datos obtenidos es:

![](Aspose.Words.59bd68a6-9569-4f50-8413-dc21f1b4f0b6.002.png)


A la hora de correr el código se pudo notar que que al generar los datos de la gaussiana de manera aleatoria en las diferentes corridas en que se ejecuta el código los valores de likelihood van cambiando en cada una de las tres gaussianas establecidas, haciendo que incluso en algunas corridas la gaussiana de μ2=6, σ2=1.6 sea la que tenga un mayor likelihood, cuando lo común es que la gaussiana de  μ3=5.1, σ3=1.4 sea la que tiene el mayor likelihood, esto debido a que es la tiene valor de μ y σ mas cercano a los valores con los que se generaron los datos aleatorios.

Como se puede ver en el siguiente grafico, este fue uno de los pocos casos en los que era posible que los valores aleatorios fueran mas inclinados hacia la derecha, haciendo que el likelihood de la gaussiana roja sea la de mayo valor:

![](Aspose.Words.59bd68a6-9569-4f50-8413-dc21f1b4f0b6.003.png)

En las graficas siguientes, se puede observar que el likelihood mas alto es el de la gaussiana verde, que es lo que se espera que suceda de manera mas común de acuerdo a los datos de μ y σ establecidos al inicio. 

![](Aspose.Words.59bd68a6-9569-4f50-8413-dc21f1b4f0b6.004.png)

![](Aspose.Words.59bd68a6-9569-4f50-8413-dc21f1b4f0b6.005.png)

En el siguiente grafico se puede observar como al aumentar el numero de valores aleatorios generados a cien, el mapa térmico se disminuye en su área haciendo que solo una parte especifica sea la que tiene mayor probabilidad comparada con los gráficos anteriores donde el área era de mayor tamaño.

![](Aspose.Words.59bd68a6-9569-4f50-8413-dc21f1b4f0b6.006.png)

Finalmente se puede concluir que a pesar de generar datos de manera aleatoria, al estar generados de acuerdo a una distribución gaussiana especifica estos tenderán a estar en un rango especifico, aunque en una que otra corrida pueda ser que los datos lleguen a estar tendidos mas hacia un lado u otro, ademas de que mientras mas datos se vayan generando el mapa térmico ira teniendo un área menor donde los likelihoods tendrán mayor valor. 

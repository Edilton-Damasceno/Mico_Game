[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-718a45dd9cf7e7f842a935f5ebbe5719a5e09af4491e668f4dbf3b35d5cca122.svg)](https://classroom.github.com/online_ide?assignment_repo_id=10832375&assignment_repo_type=AssignmentRepo)
# Lab 02 - Implementando um TAD Vetor

Nesse Laboratório voce deve tentar implementar um **Tipo Abstrato de Dados** (**TAD**) *vetor*, utilizando o conceito de *Classe* da linguagem *Python*.

Um vetor deve ser caracterizado por ser um agregado de objetos do mesmo tipo. Para facilitar vamos considerar nessa implementação um vetor de numeros inteiros. 

Seu **TAD** *vetor* deve suportar as seguintes operações básicas:

1. **Construtor**: Recebe como parametro o tamanho máximo do vetor *n* e promove a sua alocação na memória. Para todas as demais operações esse tamanho máximo deve ser verificado. Apesar da alocação de memória, o vetor estará vazio nesse momento;
2. **Imprimir**: Gera uma saida formatada com todos os elementos do vetor;
3. **Tamanho**: Operação que retorna o numero de elementos atualmente armazenado no vetor;
4. **getElemento**: Retorna o elemento de posição *i* dentro do vetor;
4. **setElemento**: Modifica o elemento de posição *i* dentro do vetor, atribuindo a este um novo valor *k*;
4. **Minimo**: Retorna a menor valor armazenado no vetor e sua posição;
5. **Maximo**: Retorna o maior valor armazenado no vetor e sua posição;
6. **Inserir**: Adiciona um novo elemento ao vetor. Por convenção, o novo elemento deve ser adicionado como ultimo elemento do vetor. A operação deve sinalizar se foi realizada com sucesso ou não;
7. **Inverter**: Troca a ordem dos elementos do vetor;
8. **Buscar**: Procura entre os elementos armazenados no vetor, a primeira ocorrencia de um valor, denominado chave de busca, retornando, caso exista, a sua localização. A operação deve sinalizar se foi realizada com sucesso ou não; 
9. **Ocorrências**: Dada uma chave de busca, essa operação retorna o numero de ocorrências dessa chave no vetor;
10. **Remover**: Elimina do vetor a primeira ocorrencia do objeto com valor igual ao da chave. A operação deve sinalizar se foi realizada com sucesso ou não;  
11. **GerarEstatisticas**: calcula média e o desvio padrão dos elementos armazenados no vetor.
12. **E_Identico**: Essa operação compara dois vetores (o próprio e outro passado como parametro) e retorna um valor booleano sinalizando se os dois vetores são ou não identicos;

O **TAD**/*Classe* *vetor* deve ser codificado como um módulo em *Python*. Para testar seu **TAD** voce deve criar um programa de teste que avalie as operações que voce implementou. 

## Considerações:

O código base fornecido utiliza o objeto *array* do Python para a alocação do espaço de memória do vetor:

>     import array
>
>     class cVetor:
>   
>     def __init__(self, n):
>     
>        self.vet = [0] * n;

No entanto, sua classe *cVetor* deve gerenciar as informações do seu vetor sem utilizar métodos ou propriedade da class *array* da linguagem *Python*. 

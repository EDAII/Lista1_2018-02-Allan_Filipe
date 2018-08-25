## Lista 1 - Busca
### Sistema Buscador de Registros em ".csv"

##### Alunos

| Matrícula | Nome | GitHub |
|--|--|--|
| 15/0029624 | Allan Jefrey Pereira Nobre | @AllanNobre |
| 15/0059213 | Filipe Coelho Hilário Barcelos | @FilipeKN4 |

##### Para executar
```sh
$ python3 Lista1.py
```

##### Descrição
A aplicação consiste na leitura de um arquivo de registros ".csv", no qual deve seguir alguns padrões de tratamento de dados antes de ser utilizado como entrada nesse software. As regras de formatação do arquivo de registro são:

- Deve ser um arquivo ".csv";
- A primeira linha do seu arquivo ".csv" deve conter os títulos de descrição das colunas;
- A primeira coluna do seu arquivo ".csv" deve conter a informação que será o parâmetro de busca;
- Os valores da primeira coluna do ".csv" e o parâmetro de busca devem, ambos, ser valores numéricos;
- Os valores da primeira coluna do ".csv" não devem se repetir, ou seja, tem de ser uma Chave Primária;
- Recomenda-se que o arquivo ".csv" nã0 possua valores de céculas vazias;

Após a leitura do ".csv", pode-se inserir valores para que sejam buscados nos registros. Os resultados possíveis são:

- O Valor ter sido encontrado pelos dois algoritmos de busca implementados, retornando os dados do registro e o tempo de execução de cada busca, levando em conta a ordenação caso tenha sido necessária;
- O Valor não ter sido encontrado nos registros, retornando uma mensagem explicativa e o tempo de execução de cada busca, levando em conta a ordenação caso tenha sido necessária;

Vale lembrar que a cada nova busca, quando a ordenação é necessária, para fins didáticos, os dados são ordenados em uma variável de cópia temporária para a busca binária, de modo a manter os registros originais na mesma ordem. Essa abordagem foi tomada para que o tempo de execução fique claro quando se necessita ou não de uma ordenação para a busca.

Essa aplicação permite que os tempos de execução sejam avaliados para diversos casos, por exemplo, onde precisa-se ou não ordenar os registros antes da busca e até qual quantidade de registros as buscas começam a ter uma diferença de tempo significativa. A comparação perante a quantidade de dados na busca é possível graças a flexibilidade da aplicação na leitura dos arquivos ".csv" que podem conter uma quantidade enorme de registros.

##### Busca
Foram implementadas a Busca Sequencial com utilização de sentinela e a Busca Binária.

##### Ordenação
A ordenação foi utilizada somente para que a busca binária fosse possível, como não foi foco dessa Lista, foi utilizada a ordenação oferecida pela linguagem que usa o algoritmo Timsort (Algoritmo híbrido derivado do MergeSort e do Insertion Sort).

##### Observações
Seguem dois ".csv" de exemplo de entrada para a aplicação, um com mais registros e outro menor.

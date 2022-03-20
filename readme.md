# LAVIBSND Python
*Código desenvolvido e atualizado por Eduardo Salmoria Fantin. Para dúvidas, contatar por email(eduardosalmoria@gmail.com) ou via [linkedin](https://www.linkedin.com/in/eduardo-salmoria-fantin-210305182/?originalSubdomain=br)* 


O código em python do LavibsND é utilizado para a leitura de um arquivo .rst do Ansys e a conversão dele em um arquivo .eig, formato utilizado pela interface em Java e Fotran.

O código utiliza a biblioteca PyAnsys para a conversão do arquivo.

Python é uma linguagem interpretada e para a execução de um arquivo em Python é necessário que o usuário possua um interpretador instalado.

Como nem sempre o usuário possuirá um intepretador desse tipo em seu computador, um processo de freeze no código foi realizado, ou seja, o arquivo .py e todo o interpretador de python foram convertidos em um conjunto de arquivos gerenciado por um .exe. A biblioteca utilizada para tal foi a py2exe.
import sistema
import arquivo

arq = 'listagemDePessoas'

if not arquivo.arquivoExiste(arq):
    arquivo.criarArquivo('listagemDePessoas')

sistema.menu()

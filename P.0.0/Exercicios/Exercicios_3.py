# Exercício 3: Classe Livro
# Crie uma classe chamada Livro que possua os seguintes atributos:
# titulo
# autor
# num_paginas
# pagina_atual
# A classe também deve ter os seguintes métodos:
# avancar_pagina(): aumenta a pagina_atual em 1. Se já estiver na última página, deve permanecer na mesma.
# voltar_pagina(): diminui a pagina_atual em 1. Se já estiver na primeira página, deve permanecer na mesma.

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-Exercicio - 3=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

class livro:

    def __init__(self,titulo,autor,num_paginas,pagina_atual):

        self.titulo = titulo
        self.autor = autor
        self.paginas = num_paginas
        self.pagina_atual = pagina_atual

    def avancar_pagina(self):

        if self.pagina_atual < self.num_paginas:
            self.pagina_atual += 1

    def voltar_pagina(self):
        
        if self.pagina_atual > 0:
            self.pagina_atual -= 1

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

livro1 = livro("Harry Potter Prisioneiro de Azkaban","JK",448,112)
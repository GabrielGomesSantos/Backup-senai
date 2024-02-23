<?php
// Caminho para a pasta onde você deseja criar o banco de dados
$caminhoPastaDatabase = __DIR__;

// Nome do arquivo do banco de dados SQLite
$nomeDoArquivoBanco = $caminhoPastaDatabase . DIRECTORY_SEPARATOR . 'sqlite.db';

// Conecta ao banco de dados SQLite (ou cria se não existir)
$conexao = new SQLite3($nomeDoArquivoBanco);

// Verifica se houve erro na conexão
if (!$conexao) {
    die("Erro na conexão com o banco de dados: " . $conexao->lastErrorMsg());
}

// Cria uma tabela de usuários (exemplo)
$queryCriarTabela = "
    CREATE TABLE IF NOT EXISTS usuarios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        email TEXT NOT NULL,
        senha TEXT NOT NULL
    )
";

// Executa a query para criar a tabela
$resultado = $conexao->exec($queryCriarTabela);

// Verifica se houve erro na execução da query
if (!$resultado) {
    die("Erro ao criar tabela: " . $conexao->lastErrorMsg());
}

echo "Banco de dados e tabela criados com sucesso.";

// Fecha a conexão com o banco de dados
$conexao->close();
?>

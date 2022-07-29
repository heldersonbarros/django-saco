CREATE DATABASE saco;

CREATE TABLE Pessoa(
    id BIGSERIAL PRIMARY KEY,
    nome VARCHAR(120) NOT NULL,
    cpf VARCHAR(20) UNIQUE NOT NULL,
    rg VARCHAR(20) UNIQUE NOT NULL,
    telefone VARCHAR(20) NOT NULL
);

CREATE TABLE Endereco(
    id BIGSERIAL PRIMARY KEY,
    bairro VARCHAR(20) NOT NULL,
    rua VARCHAR(20) NOT NULL,
    numero VARCHAR(10) NOT NULL
);

CREATE TABLE Funcionario(
    data_admissao DATE NOT NULL,
    salario FLOAT NOT NULL,
    especialidade VARCHAR(20),
    pessoa_id BIGINT PRIMARY KEY NOT NULL REFERENCES Pessoa (id) ON DELETE CASCADE
);

CREATE TABLE Cliente(
    tipo VARCHAR(20) NOT NULL,
    celular VARCHAR(20) NOT NULL,
    pessoa_id BIGINT PRIMARY KEY NOT NULL REFERENCES Pessoa (id) ON DELETE CASCADE,
    endereco_id BIGINT NOT NULL REFERENCES Endereco (id) ON DELETE CASCADE
);

CREATE TABLE Veiculo(
    id BIGSERIAL PRIMARY KEY,
    placa VARCHAR(20) UNIQUE NOT NULL,
    marca VARCHAR(20) NOT NULL,
    modelo VARCHAR(20) NOT NULL,
    cliente_id BIGINT NOT NULL REFERENCES Cliente (pessoa_id) ON DELETE CASCADE
);

CREATE TABLE Servico(
    id BIGSERIAL PRIMARY KEY,
    descricao VARCHAR(50) NOT NULL,
    valor FLOAT NOT NULL
); 

CREATE TABLE ItemServico(
    id BIGSERIAL PRIMARY KEY,
    descricao VARCHAR(50) NOT NULL
);

CREATE TABLE Servico_Item_Servico(
    id BIGSERIAL PRIMARY KEY,
    servico_id BIGINT NOT NULL REFERENCES Servico (id) ON DELETE CASCADE, 
    itemservico_id BIGINT NOT NULL REFERENCES ItemServico (id) ON DELETE CASCADE
);

CREATE TABLE OrdemServico(
    id BIGSERIAL PRIMARY KEY,
    data_conclusao DATE,
    data_entrada DATE NOT NULL,
    data_saida DATE,
    cliente_id BIGINT NOT NULL REFERENCES Cliente (pessoa_id) ON DELETE CASCADE,
    responsavel_id BIGINT NOT NULL REFERENCES Funcionario (pessoa_id)
);

CREATE TABLE Ordem_Servico_Servico(
    id BIGSERIAL PRIMARY KEY,
    ordemservico_id BIGINT NOT NULL REFERENCES OrdemServico (id),
    servico_id BIGINT NOT NULL REFERENCES Servico (id) ON DELETE CASCADE
);

CREATE TABLE RealizacaoServico(
    id BIGSERIAL PRIMARY KEY,
    itemservico_id BIGINT NOT NULL REFERENCES ItemServico (id) ON DELETE CASCADE,
    ordem_servico_servico_id BIGINT NOT NULL REFERENCES Ordem_Servico_Servico (id) ON DELETE CASCADE,
    funcionario_id BIGINT NOT NULL REFERENCES Funcionario (pessoa_id) ON DELETE CASCADE,
    realizado BOOLEAN DEFAULT FALSE
);

CREATE TABLE Empresa(
    id BIGSERIAL PRIMARY KEY,
    cnpj VARCHAR(20) UNIQUE NOT NULL,
    endereco_id BIGINT NOT NULL REFERENCES Endereco (id)
);

CREATE TABLE NotaFiscal(
    id BIGSERIAL PRIMARY KEY,
    ordemservico_id BIGINT NOT NULL REFERENCES OrdemServico (id) ON DELETE CASCADE,
    empresa_id BIGINT NOT NULL REFERENCES Empresa (id) ON DELETE CASCADE
);

CREATE TABLE Parcela(
    id BIGSERIAL PRIMARY KEY,
    valor FLOAT,
    data_pagamento DATE NOT NULL,
    pago BOOLEAN DEFAULT FALSE,
    notafiscal_id BIGINT NOT NULL REFERENCES NotaFiscal (id) ON DELETE CASCADE
);
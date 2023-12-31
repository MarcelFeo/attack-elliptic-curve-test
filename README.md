# Experimento do artigo A Small Subgroup Attack on Bitcoin Address Generation

## Importação de Bibliotecas:

Este código inicia importando duas bibliotecas, hashlib e base58. A biblioteca hashlib é utilizada para calcular hashes SHA-256 e RIPEMD-160, enquanto a biblioteca base58 é empregada para codificar os dados em formato Base58.

## Definição do Subgrupo de Chaves Privadas Fictícias:

Em seguida, o código define uma lista denominada subgroup_private_keys, que contém chaves privadas fictícias representadas por números inteiros. Estas chaves privadas formam um subgrupo fictício para fins de demonstração.

## Função generate_address:

A função generate_address é implementada com o objetivo de criar endereços Bitcoin fictícios a partir das chaves privadas fictícias. Aqui está o processo detalhado:

Converte a chave privada em bytes usando o método to_bytes.

Calcula o hash SHA-256 da chave privada e converte o resultado em formato hexadecimal, representando a chave pública fictícia.

Em seguida, calcula o hash RIPEMD-160 da chave pública e a converte em formato hexadecimal, representando o endereço público fictício.

Adiciona o prefixo '1' ao endereço público e codifica o resultado em Base58 para obter o endereço Bitcoin fictício.

## Geração de Endereços no Subgrupo:

O código utiliza um loop para gerar endereços fictícios a partir das chaves privadas fictícias no subgrupo e armazena esses endereços na lista addresses_in_subgroup.

## Lista de Endereços na Blockchain Fictícia:

Uma lista fictícia chamada blockchain_addresses é criada, contendo endereços fictícios da blockchain, que servem como referência.

## Verificação de Correspondência:

O código emprega uma compreensão de lista para verificar quais dos endereços gerados a partir das chaves privadas fictícias no subgrupo correspondem a endereços na blockchain fictícia. Os endereços correspondentes são armazenados na lista matched_addresses.

## Impressão dos Resultados:

Por fim, o código imprime os endereços gerados no subgrupo e os endereços correspondentes na blockchain fictícia para fins de verificação e análise.

Esta documentação fornece uma visão geral abrangente do código, explicando seu propósito e funcionamento em detalhes.

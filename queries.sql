/* g1 */

SELECT * FROM Pessoa
JOIN Funcionario on Pessoa.id = Funcionario.pessoa_id;

/* g2 */

SELECT * FROM Funcionario
JOIN Cliente ON Funcionario.pessoa_id = Cliente.pessoa_id
JOIN Pessoa ON Funcionario.pessoa_id = Pessoa.id;

/* g3 */

SELECT * FROM Funcionario AS f1
WHERE f1.salario > (SELECT AVG(f2.salario) FROM FUNCIONARIO AS f2 
					WHERE EXTRACT(YEAR FROM f2.data_admissao) >= 2020);

/* g4 */

SELECT marca, COUNT(*) FROM Veiculo
GROUP BY marca
ORDER BY COUNT(*) DESC;

SELECT modelo, COUNT(*) FROM Veiculo
GROUP BY modelo
ORDER BY COUNT(*) DESC;

/* g5 */

SELECT * FROM ItemServico
JOIN Servico_Item_Servico ON ItemServico.id = Servico_Item_Servico.itemservico_id
JOIN Servico ON Servico_Item_Servico.servico_id = Servico.id;

/* g6 */

SELECT *, 
(COALESCE(OrdemServico.data_saida, CURRENT_DATE) - OrdemServico.data_entrada) AS Days 
FROM Cliente
JOIN OrdemServico ON cliente.pessoa_id = OrdemServico.cliente_id
ORDER BY Days DESC
LIMIT 10;

/* g7 */

SELECT * FROM OrdemServico
JOIN Cliente ON OrdemServico.cliente_id = Cliente.pessoa_id
WHERE OrdemServico.data_saida IS null;

/* g8 */

SELECT * FROM Pessoa
JOIN (
SELECT pessoa_id FROM Funcionario
JOIN RealizacaoServico ON RealizacaoServico.funcionario_id = Funcionario.pessoa_id
JOIN Ordem_Servico_Servico ON Ordem_Servico_Servico.id = RealizacaoServico.ordem_servico_servico_id
GROUP BY pessoa_id
HAVING COUNT(*) = (SELECT Count(*) FROM OrdemServico)) func
ON Pessoa.id = func.pessoa_id;

/* g9 */

SELECT SUM(valor) FROM Parcela
WHERE pago = false OR data_pagamento > CURRENT_DATE;

/* g10 */

SELECT salario, 
	(SELECT string_agg(pessoa.nome, ',') FROM Funcionario 
	JOIN Pessoa ON funcionario.pessoa_id = pessoa.id) 
FROM Funcionario
GROUP BY salario
HAVING COUNT(*) > 1;
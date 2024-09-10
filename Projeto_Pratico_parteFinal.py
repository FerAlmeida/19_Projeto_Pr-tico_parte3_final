# PROJETO PRÁTICO DE AULA EMPOWERDATA - PYTHON EXPRESS

import pandas as pd

dados = pd.read_excel("base_dados.xlsx")

dados.head(5)

dados.tail(5)

dados.shape

dados.info()

colunas = ["quantidade_itens", "valor_pedido", "dias_ate_entrega"]           # temos abaixo a "medidas resumo"
dados[colunas].describe()

dados["estado_destino"].value_counts()

dados["estado_destino"].value_counts().plot(kind="bar")

dados["cliente"].value_counts()

dados["cliente"].value_counts().plot(kind="bar")

dados["motorista"].value_counts()

dados["motorista"].value_counts().plot(kind="bar")

dados["motivo_devolucao"].value_counts()

filtro = dados["motivo_devolucao"] != "S/ Devolu."  # Com essa linha excluimos o "S/ Ddevolução", apresentando apenas os demais motivos
dados_com_devolucao = dados.loc[filtro]

colunas = ["cliente", "motivo_devolucao"]           # apresentação do cliente e o motivo da devoleção
dados_com_devolucao.groupby(colunas)["numero_pedido"].count().to_frame()

dados_com_devolucao

# Agrupando os dados solicitados
colunas = ["cliente","motivo_devolucao"]
dados_com_devolucao.groupby(colunas)["valor_pedido"].sum().to_excel("Prejuízo por motivo de devolução.xlsx")

filtro = dados["motivo_devolucao"] == "S/ Devolu."
dados.loc[filtro]

filtro = dados["motivo_devolucao"] == "S/ Devolu."
dados_sem_devolucao = dados.loc[filtro]

dados_sem_devolucao ["status"].value_counts()

# Agrupando nossas informações
colunas = ["cliente", "motorista", "status"]
dados_sem_devolucao.groupby(colunas)["numero_pedido"].count().to_frame()

# Exportando os dados para o Excel
colunas = ["cliente", "motorista", "status"]
dados_sem_devolucao.groupby(colunas)["numero_pedido"].count().to_excel("Status de entrega por motoristas e clientes.xlsx")
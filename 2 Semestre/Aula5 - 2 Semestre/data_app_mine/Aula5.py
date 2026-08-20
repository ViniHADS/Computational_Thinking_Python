import streamlit as st
import pandas as pd
import io
import os


# ============================================================
# CONFIGURAÇÃO DA PÁGINA
# ============================================================

st.set_page_config(
    page_title="Conversor Universal de Arquivos",
    page_icon="ð",
    layout="wide"
)


# ============================================================
# CONFIGURAÇÕES
# ============================================================

FORMATOS_ENTRADA = [
    "csv",
    "json",
    "xml",
    "xlsx",
    "txt",
    "parquet"
]

FORMATOS_SAIDA = [
    "csv",
    "json",
    "xml",
    "txt",
    "parquet",
    "xlsx"
]


# ============================================================
# FUNÇÃO DE LEITURA
# ============================================================

@st.cache_data
def ler_arquivo(conteudo, nome_arquivo, formato):
    """
    Lê o arquivo enviado e transforma seu conteúdo em um
    DataFrame Pandas.

    Parâmetros:
        conteudo: bytes do arquivo enviado.
        nome_arquivo: nome original do arquivo.
        formato: extensão do arquivo sem o ponto.

    Retorna:
        pandas.DataFrame
    """

    try:

        # ----------------------------------------------------
        # CSV
        # ----------------------------------------------------

        if formato == "csv":

            return pd.read_csv(
                io.BytesIO(conteudo)
            )


        # ----------------------------------------------------
        # JSON
        # ----------------------------------------------------

        elif formato == "json":

            return pd.read_json(
                io.BytesIO(conteudo)
            )


        # ----------------------------------------------------
        # XML
        # ----------------------------------------------------

        elif formato == "xml":

            return pd.read_xml(
                io.BytesIO(conteudo)
            )


        # ----------------------------------------------------
        # EXCEL XLSX
        # ----------------------------------------------------

        elif formato == "xlsx":

            return pd.read_excel(
                io.BytesIO(conteudo),
                engine="openpyxl"
            )


        # ----------------------------------------------------
        # TXT
        # ----------------------------------------------------

        elif formato == "txt":

            # O TXT será tratado como arquivo tabular.
            # As colunas devem estar separadas por TAB.
            return pd.read_csv(
                io.BytesIO(conteudo),
                sep="\t"
            )


        # ----------------------------------------------------
        # PARQUET
        # ----------------------------------------------------

        elif formato == "parquet":

            return pd.read_parquet(
                io.BytesIO(conteudo),
                engine="pyarrow"
            )


        # ----------------------------------------------------
        # FORMATO INVÁLIDO
        # ----------------------------------------------------

        else:

            raise ValueError(
                f"Formato de entrada não suportado: .{formato}"
            )


    except Exception as erro:

        raise ValueError(
            f"Não foi possível ler o arquivo "
            f"'{nome_arquivo}'. Detalhes: {erro}"
        )


# ============================================================
# FUNÇÃO DE CONVERSÃO
# ============================================================

def converter_dataframe(df, formato_saida):
    """
    Converte um DataFrame Pandas para o formato escolhido.

    Retorna:
        bytes do arquivo convertido.
    """

    try:

        # ----------------------------------------------------
        # CSV
        # ----------------------------------------------------

        if formato_saida == "csv":

            return df.to_csv(
                index=False
            ).encode("utf-8")


        # ----------------------------------------------------
        # JSON
        # ----------------------------------------------------

        elif formato_saida == "json":

            return df.to_json(
                orient="records",
                indent=4,
                force_ascii=False
            ).encode("utf-8")


        # ----------------------------------------------------
        # XML
        # ----------------------------------------------------

        elif formato_saida == "xml":

            xml_string = df.to_xml(
                index=False,
                root_name="dados",
                row_name="registro"
            )

            return xml_string.encode("utf-8")


        # ----------------------------------------------------
        # TXT
        # ----------------------------------------------------

        elif formato_saida == "txt":

            # TXT tabular separado por TAB.
            return df.to_csv(
                index=False,
                sep="\t"
            ).encode("utf-8")


        # ----------------------------------------------------
        # PARQUET
        # ----------------------------------------------------

        elif formato_saida == "parquet":

            # Parquet Ã© um formato binÃ¡rio.
            # Por isso utilizamos BytesIO para armazenar
            # o arquivo na memÃ³ria.
            buffer = io.BytesIO()

            df.to_parquet(
                buffer,
                index=False,
                engine="pyarrow"
            )

            # Retorna o conteÃºdo binÃ¡rio.
            return buffer.getvalue()


        # ----------------------------------------------------
        # EXCEL XLSX
        # ----------------------------------------------------

        elif formato_saida == "xlsx":

            # XLSX tambÃ©m Ã© um arquivo binÃ¡rio.
            # Utilizamos BytesIO para mantÃª-lo em memÃ³ria.
            buffer = io.BytesIO()

            with pd.ExcelWriter(
                buffer,
                engine="openpyxl"
            ) as writer:

                df.to_excel(
                    writer,
                    index=False,
                    sheet_name="Dados"
                )

            # Retorna o conteÃºdo binÃ¡rio.
            return buffer.getvalue()


        # ----------------------------------------------------
        # FORMATO INVÁLIDO
        # ----------------------------------------------------

        else:

            raise ValueError(
                f"Formato de saída não suportado: .{formato_saida}"
            )


    except Exception as erro:

        raise ValueError(
            f"Erro durante a conversÃ£o para "
            f".{formato_saida}: {erro}"
        )


# ============================================================
# FUNÇÃO PARA PREVIEW
# ============================================================

def mostrar_preview(conteudo_convertido, formato_saida):
    """
    Exibe uma prévia do arquivo convertido.

    Para formatos de texto:
        Exibe o conteúdo usando st.code().

    Para formatos binários:
        Exibe uma mensagem informando que o arquivo foi
        convertido e disponibiliza algumas informações.
    """

    try:

        # ----------------------------------------------------
        # FORMATOS DE TEXTO
        # ----------------------------------------------------

        if formato_saida in [
            "csv",
            "json",
            "xml",
            "txt"
        ]:

            texto = conteudo_convertido.decode("utf-8")

            linguagem = "text"

            if formato_saida == "json":
                linguagem = "json"

            elif formato_saida == "xml":
                linguagem = "xml"

            st.code(
                texto[:5000],
                language=linguagem
            )


        # ----------------------------------------------------
        # PARQUET
        # ----------------------------------------------------

        elif formato_saida == "parquet":

            tamanho_kb = (
                len(conteudo_convertido) / 1024
            )

            st.info(
                f"ð¦ Arquivo Parquet convertido com sucesso. "
                f"Tamanho: {tamanho_kb:.2f} KB."
            )

            st.caption(
                "Parquet é um formato binário, portanto "
                "não pode ser exibido diretamente como texto."
            )


        # ----------------------------------------------------
        # XLSX
        # ----------------------------------------------------

        elif formato_saida == "xlsx":

            tamanho_kb = (
                len(conteudo_convertido) / 1024
            )

            st.info(
                f"ð Arquivo Excel convertido com sucesso. "
                f"Tamanho: {tamanho_kb:.2f} KB."
            )

            st.caption(
                "O arquivo XLSX é binário e será disponibilizado "
                "através do botão de download."
            )


    except Exception as erro:

        st.error(
            f"Não foi possível gerar o preview: {erro}"
        )


# ============================================================
# TIPOS MIME
# ============================================================

MIME_TYPES = {

    "csv":
        "text/csv",

    "json":
        "application/json",

    "xml":
        "application/xml",

    "txt":
        "text/plain",

    "xlsx":
        "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",

    "parquet":
        "application/octet-stream"
}


# ============================================================
# INTERFACE
# ============================================================

st.title("ð Conversor Universal de Arquivos")

st.markdown(
    """
    Converta arquivos entre diferentes formatos utilizando
    **Python + Streamlit + Pandas**.

    **Formatos de entrada:**
    CSV, JSON, XML, XLSX, TXT e Parquet.

    **Formatos de saÃ­da:**
    CSV, JSON, XML, TXT, XLSX e Parquet.
    """
)

st.divider()


# ============================================================
# UPLOAD
# ============================================================

arquivo = st.file_uploader(
    "ð Selecione o arquivo que deseja converter",
    type=FORMATOS_ENTRADA
)


if arquivo is not None:

    # --------------------------------------------------------
    # INFORMAÇÕES DO ARQUIVO
    # --------------------------------------------------------

    nome_original = arquivo.name

    extensao_entrada = os.path.splitext(
        nome_original
    )[1].lower().replace(".", "")


    col1, col2 = st.columns(2)

    with col1:

        st.info(
            f"**Arquivo:** {nome_original}"
        )

    with col2:

        st.info(
            f"**Formato de entrada:** "
            f".{extensao_entrada.upper()}"
        )


    st.divider()


    # ========================================================
    # LEITURA
    # ========================================================

    try:

        conteudo = arquivo.getvalue()

        df = ler_arquivo(
            conteudo,
            nome_original,
            extensao_entrada
        )

        st.success(
            "✅ Arquivo carregado e interpretado "
            "com sucesso!"
        )


    except Exception as erro:

        st.error(
            f"❌ {erro}"
        )

        st.stop()


    # ========================================================
    # PREVIEW DOS DADOS
    # ========================================================

    st.subheader("ð Preview dos dados")

    st.dataframe(
        df,
        use_container_width=True,
        height=300
    )


    # ========================================================
    # INFORMAÃÃES DO DATAFRAME
    # ========================================================

    col1, col2, col3 = st.columns(3)

    with col1:

        st.metric(
            "Linhas",
            df.shape[0]
        )

    with col2:

        st.metric(
            "Colunas",
            df.shape[1]
        )

    with col3:

        st.metric(
            "CÃ©lulas",
            df.shape[0] * df.shape[1]
        )


    st.divider()


    # ========================================================
    # FORMATO DE SAÃDA
    # ========================================================

    st.subheader("âï¸ Escolha o formato de saÃ­da")

    formato_saida = st.selectbox(
        "Formato desejado:",
        FORMATOS_SAIDA,
        format_func=lambda formato:
            f".{formato.upper()}"
    )


    # ========================================================
    # CONVERSÃO
    # ========================================================

    try:

        arquivo_convertido = converter_dataframe(
            df,
            formato_saida
        )

        st.success(
            f"✅ Conversão para "
            f".{formato_saida.upper()} realizada "
            f"com sucesso!"
        )


    except Exception as erro:

        st.error(
            f"❌ Erro na conversão: {erro}"
        )

        st.stop()


    # ========================================================
    # PREVIEW DO ARQUIVO CONVERTIDO
    # ========================================================

    st.subheader(
        f"📄 Preview do arquivo "
        f".{formato_saida.upper()}"
    )

    mostrar_preview(
        arquivo_convertido,
        formato_saida
    )


    st.divider()


    # ========================================================
    # NOME DO ARQUIVO DE SAÍDA
    # ========================================================

    nome_sem_extensao = os.path.splitext(
        nome_original
    )[0]

    nome_saida = (
        f"{nome_sem_extensao}.{formato_saida}"
    )


    # ========================================================
    # DOWNLOAD
    # ========================================================

    st.subheader("⬇️ Baixar arquivo")

    st.download_button(
        label=f"📥 Baixar {nome_saida}",
        data=arquivo_convertido,
        file_name=nome_saida,
        mime=MIME_TYPES[formato_saida],
        use_container_width=True
    )


else:

    # ========================================================
    # ESTADO INICIAL
    # ========================================================

    st.info(
        "👆 Envie um arquivo acima para começar."
    )


# ============================================================
# RODAPÉ
# ============================================================

st.divider()

st.caption(
    "Conversor Universal de Arquivos • "
    "Python + Streamlit + Pandas"
    "Vinicius Araujo © 2026 • Projeto Prático de Eng. de Software."
)
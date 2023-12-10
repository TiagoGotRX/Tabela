from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import sqlite3

def gerar_pdf():
    # Conectar ao banco de dados
    conn = sqlite3.connect('cadastros.db')
    cursor = conn.cursor()

    # Executar a consulta para obter os dados
    cursor.execute('SELECT * FROM cadastros')
    dados = cursor.fetchall()

    # Fechar a conexão com o banco de dados
    conn.close()

    # Criar um documento PDF com tamanho personalizado
    largura_personalizada = 800  # Ajuste a largura conforme necessário
    altura_personalizada = 1000  # Ajuste a altura conforme necessário
    nome_arquivo = 'relatorio_cadastros.pdf'
    pdf = canvas.Canvas(nome_arquivo, pagesize=(largura_personalizada, altura_personalizada))
    
    # Adicionar cabeçalho
    pdf.setFont("Helvetica-Bold", 12)
    pdf.drawCentredString(largura_personalizada / 2, altura_personalizada - 30, "Relatório de Cadastros")

    # Adicionar dados ao PDF com linhas divisórias
    pdf.setFont("Helvetica", 10)
    y_inicial = altura_personalizada - 70  # Ajuste a posição inicial
    espacamento_entre_linhas = 15
    for cliente in dados:
        # Adicionar dados
        pdf.drawString(100, y_inicial, f"ID: {cliente[0]}")
        pdf.drawString(200, y_inicial, f"Nome: {cliente[1]}")
        pdf.drawString(400, y_inicial, f"CPF: {cliente[2]}")
        pdf.drawString(500, y_inicial, f"Endereço: {cliente[3]}")

        # Adicionar linha divisória
        pdf.line(100, y_inicial - espacamento_entre_linhas, largura_personalizada - 100, y_inicial - espacamento_entre_linhas)

        y_inicial -= espacamento_entre_linhas  # Ajuste a posição para a próxima linha

    # Salvar o arquivo PDF
    pdf.save()
    print(f'PDF gerado com sucesso: {nome_arquivo}')

# Chamar a função para gerar o PDF
gerar_pdf()

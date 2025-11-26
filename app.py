import qrcode
from PIL import Image, ImageDraw

# 📌 1. Defina o URL na constante
URL_PARA_QR = "https://g.page/r/CcLWs52CJQQ9EBM/review"
# 🖼️ 2. Defina o nome do arquivo de saída
NOME_DO_ARQUIVO = "qr_code.png"

# 🎨 3. Defina a cor do QR Code
COR_PREENCHIMENTO = "black"
COR_FUNDO = "white"

# 🖼️ 4. Defina o caminho para o ícone
ICON_QR = "marca-ceot.png"  # Substitua pelo nome do seu arquivo de ícone

# --- Configurações do QR Code ---
TAMANHO_CAIXA = 10
TAMANHO_BORDA = 4
TAMANHO_PERCENTUAL_ICONE = 0.25  # Ícone ocupará 25% do tamanho do QR

# -----------------------------------------------------------
# NOVA FUNÇÃO: Cria um espaço branco no centro antes de colar o ícone
# -----------------------------------------------------------


def centralizar_icone_com_fundo(img_qr, img_icon):
    """Cria um fundo branco no centro do QR code e cola o ícone."""

    # 1. Calcula o tamanho e posição do ícone no QR Code
    qr_w, qr_h = img_qr.size
    icon_w, icon_h = img_icon.size

    # 2. Define a posição de onde o ícone será colado
    pos = ((qr_w - icon_w) // 2, (qr_h - icon_h) // 2)

    # 3. Cria uma área de desenho na imagem do QR
    draw = ImageDraw.Draw(img_qr)

    # 4. Calcula as coordenadas do retângulo de fundo branco
    # Adicionamos uma pequena margem (ex: 10 pixels) ao redor do ícone
    margem = 10

    x1 = pos[0] - margem
    y1 = pos[1] - margem
    x2 = pos[0] + icon_w + margem
    y2 = pos[1] + icon_h + margem

    # 5. Desenha o retângulo branco sólido
    # Isso garante o espaço livre antes de colar o logo
    draw.rectangle([x1, y1, x2, y2], fill=COR_FUNDO)

    # 6. Cola o ícone sobre o fundo branco
    # O img_icon deve ter fundo transparente (máscara) para colar corretamente
    img_qr.paste(img_icon, pos, img_icon)

    return img_qr

# -----------------------------------------------------------
# INÍCIO DO PROCESSO
# -----------------------------------------------------------


# 🛠️ Criação da Instância do QR Code
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,  # Nível H é crucial para logos
    box_size=TAMANHO_CAIXA,
    border=TAMANHO_BORDA,
)

# ➕ Adiciona o dado
qr.add_data(URL_PARA_QR)
qr.make(fit=True)

# 🎨 Cria a imagem do QR Code
# Convertemos para RGBA para garantir que a transparência do ícone funcione corretamente
img_qr = qr.make_image(fill_color=COR_PREENCHIMENTO,
                       back_color=COR_FUNDO).convert("RGBA")

# 🖼️ Abre e redimensiona o ícone
try:
    img_icon = Image.open(ICON_QR).convert("RGBA")

    # Calcula o tamanho do ícone baseado no percentual definido
    basewidth = int(img_qr.size[0] * TAMANHO_PERCENTUAL_ICONE)
    wpercent = (basewidth / float(img_icon.size[0]))
    hsize = int((float(img_icon.size[1]) * float(wpercent)))

    # Redimensiona o ícone
    img_icon = img_icon.resize((basewidth, hsize), Image.Resampling.LANCZOS)

    # 🖼️ Chama a função para adicionar o fundo branco e colar o ícone
    img_final = centralizar_icone_com_fundo(img_qr, img_icon)

except FileNotFoundError:
    print(f"⚠️ Erro: O arquivo do ícone '{ICON_QR}' não foi encontrado.")
    img_final = img_qr  # Salva sem o ícone

except Exception as e:
    print(f"⚠️ Ocorreu um erro ao processar o ícone: {e}")
    img_final = img_qr  # Salva sem o ícone

# 💾 Salva a imagem final
img_final.save(NOME_DO_ARQUIVO)

print(f"✅ QR Code gerado com sucesso!")
print(f"URL codificado: {URL_PARA_QR}")
print(f"Salvo como: {NOME_DO_ARQUIVO}")

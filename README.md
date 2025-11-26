# 📷 QR Code Generator com Logo Personalizado

Um script em Python simples e eficaz para gerar QR Codes a partir de um URL, permitindo a personalização da cor e a incorporação de um logo centralizado com fundo branco para garantir a escaneabilidade.

---

## ✨ Funcionalidades

* **Geração de QR Code:** Converte qualquer string ou URL em um QR Code.
* **Personalização de Cor:** Permite definir a cor dos módulos (`fill_color`) e do fundo (`back_color`).
* **Incorporação de Logo:** Centraliza uma imagem `.png` (logo) no QR Code.
* **Correção de Fundo:** Cria um quadrado branco no centro do código (usando a cor de fundo) antes de colar o logo, garantindo que o logo não se misture com os dados do código e mantendo a alta escaneabilidade.
* **Alta Tolerância a Erros:** Utiliza o nível de correção de erro **H (High)**, o mais alto disponível, que é essencial para códigos que contêm logos.

---

## 🛠️ Instalação

O projeto requer Python e duas bibliotecas principais: `qrcode` para a geração do código e `Pillow` (PIL) para manipulação de imagens (redimensionamento e colagem do logo).

1.  **Clone o repositório:**
    ```bash
    git clone [https://github.com/SeuUsuario/NomeDoSeuRepositorio.git](https://github.com/SeuUsuario/NomeDoSeuRepositorio.git)
    cd NomeDoSeuRepositorio
    ```

2.  **Instale as dependências:**
    ```bash
    pip install qrcode Pillow
    ```

---

## ⚙️ Uso

Para gerar seu QR Code personalizado, siga estes passos:

1.  **Configure o Script:**
    Abra o arquivo Python (`gerador_qr.py` ou o nome que você usou) e edite as constantes no início do arquivo:

    * `URL_PARA_QR`: O URL que será codificado.
    * `ICON_QR`: O nome do arquivo do seu logo (`.png` recomendado).
    * `COR_PREENCHIMENTO`: A cor dos módulos do QR Code (ex: `"black"`, `"blue"`).

2.  **Posicione o Ícone:**
    Coloque seu arquivo de logo (ex: `icone.png`) na mesma pasta do script Python.

3.  **Execute o Script:**
    Execute o script no seu terminal:
    ```bash
    python seu_script_de_qr_code.py
    ```

4.  **Resultado:**
    O arquivo de imagem do QR Code finalizado (definido em `NOME_DO_ARQUIVO`) será salvo na mesma pasta.

---

## 📜 Exemplo de Código (Trecho Chave)

O trecho abaixo demonstra como o fundo branco é criado no centro do QR Code usando a biblioteca `Pillow` (`ImageDraw`):

```python
# Cria a área de desenho
draw = ImageDraw.Draw(img_qr)

# Desenha o retângulo branco sólido para limpar o fundo
draw.rectangle([x1, y1, x2, y2], fill=COR_FUNDO)

# Cola o ícone sobre o fundo limpo
img_qr.paste(img_icon, pos, img_icon)

# 1. Base image
FROM python:3.12-slim

# 2. Definir diretório de trabalho
WORKDIR /app

# 3. Copiar requirements e instalar dependências
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 4. Copiar o código do projeto
COPY . .

# 5. Expor porta
EXPOSE 8000

# 6. Comando para rodar o Django
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
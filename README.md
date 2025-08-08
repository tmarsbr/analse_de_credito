# Análise de Crédito

Projeto inicial para experimentos de análise de crédito.

## Estrutura (inicial)
- `data/` (crie para armazenar dados – evite subir dados sensíveis)
- `notebooks/` (explorações Jupyter, se usar)
- `src/` (código fonte principal)

## Próximos Passos
1. Definir objetivo (score, prob. default, etc.)
2. Coletar e limpar dados
3. Engenharia de atributos
4. Modelagem e validação
5. Deploy / Monitoramento

## Requisitos (exemplo futuramente)
Crie um `requirements.txt` ou `pyproject.toml` quando definir dependências.

## Ambiente Python / PySpark

ATENÇÃO: PySpark 3.5.1 ainda não suporta Python 3.13. Use Python 3.12 (ou 3.11/3.10) para evitar erros como:
`SparkException: Python worker exited unexpectedly (crashed)`.

### Instalar Python 3.12 no Windows (winget)
```powershell
winget install -e --id Python.Python.3.12
```

### Criar (ou recriar) o ambiente virtual
Apague o atual se foi criado com 3.13:
```powershell
Remove-Item -Recurse -Force .venv
```
Crie novamente com 3.12 (ajuste o caminho conforme instalação):
```powershell
"C:/Users/tiago/AppData/Local/Programs/Python/Python312/python.exe" -m venv .venv
. .venv/Scripts/Activate.ps1
pip install --upgrade pip
pip install -r requirements.txt
```

### Teste rápido do PySpark
```powershell
. .venv/Scripts/Activate.ps1
python test_pyspark.py
```

Se ocorrer erro de socket/worker, confirme:
- `python -V` mostra 3.12.x
- JAVA (JDK 8, 11 ou 17) instalado e `JAVA_HOME` configurado (opcional, mas recomendado)

### Variáveis de ambiente úteis
```powershell
$env:JAVA_HOME = 'C:/Program Files/Java/jdk-17'
$env:PATH = "$env:JAVA_HOME/bin;$env:PATH"
```

## Git / Push (SSH)
Se aparecer `Permission denied (publickey)`:
```powershell
Start-Service ssh-agent
Get-Service ssh-agent
ssh-add $env:USERPROFILE/.ssh/id_rsa
```
Ou troque para HTTPS:
```powershell
git remote set-url origin https://github.com/tmarsbr/analse_de_credito.git
```

---
Gerado automaticamente para o primeiro commit.

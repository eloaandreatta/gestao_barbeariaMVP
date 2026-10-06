# Sistema de Gestão para Barbearia — MVP
MVP acadêmico em Python 3.12 + Django 5.2, arquitetura monolítica em camadas, com autenticação, registro de atendimentos, histórico, testes automatizados e CI no GitHub Actions.

## Rodar localmente
```bash
python -m venv .venv
# Windows: .venv\\Scripts\\activate
# Linux/macOS: source .venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```
Acesse `http://127.0.0.1:8000/admin/` para cadastrar Clientes, Profissionais e Serviços e depois use a aplicação principal.

## PostgreSQL
Sem variáveis `POSTGRES_*`, o projeto usa SQLite apenas para facilitar desenvolvimento/testes. Para seguir a arquitetura planejada, configure as variáveis do `.env.example` em seu ambiente/hospedagem e execute `python manage.py migrate`.

## Testes
```bash
pytest -q
```

## GitHub / PR / CI
1. Crie o repositório e envie a branch `main`.
2. Para cada alteração, crie uma branch (`feature/...`), faça commits e abra Pull Request.
3. O workflow `.github/workflows/ci.yml` executa `manage.py check` e `pytest` em push/PR.

Sugestões de commits convencionais: `feat: adiciona registro de atendimento`, `test: cobre validação de valor`, `fix: melhora mensagem de erro`.

## Segurança
- Autenticação nativa Django e hash de senha do framework.
- CSRF nos formulários.
- ORM para consultas parametrizadas.
- Autoescape dos templates.
- Segredos via variáveis de ambiente.
- Em produção: `DEBUG=False`, HTTPS e cookies seguros.

## Observação acadêmica
As duas rodadas de validação em campo, feedbacks e ajustes devem ser registrados com evidências reais do representante externo; não estão simulados neste repositório.

## Revisão técnica do MVP

Durante a revisão técnica foram avaliados aspectos de arquitetura,
legibilidade, segurança e manutenção do sistema.

O projeto utiliza uma arquitetura monolítica em camadas com Django,
mantendo separadas as responsabilidades de apresentação, regras de
negócio e persistência de dados.

Também foram revisadas as validações dos formulários, autenticação,
proteção das rotas e organização do código, buscando manter o MVP
simples, seguro e de fácil manutenção.

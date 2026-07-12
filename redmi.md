mkdir backend, frontend ,app  создали папки 
git init                   подключили гид

python -m venv venv        создали окружение

.\venv\Scripts\activate.ps1  активируем среду

pip install sqlalchemy fastapi uvicorn pydantic python-dotenv pydantic-settings 

pip freeze > requirements.txt

app> mkdir models,schemas,repositories,services,routes 


конфиг состовляем по шаблону практически одинаков везде

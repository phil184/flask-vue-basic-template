@echo off
echo Crate venv...
python -m venv venv

echo Activate venv and install depen...
call venv\Scripts\activate
pip install -r requirements.txt

echo Install Vue...
cd frontend
npm install
cd ..

echo ✅ Setup finished!
pause
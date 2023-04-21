echo " BUILD START "
python3.9 -m python install -r requirements.txt
python3.9 manage.py collectstatic --noinput --clear
echo " BUILD END "

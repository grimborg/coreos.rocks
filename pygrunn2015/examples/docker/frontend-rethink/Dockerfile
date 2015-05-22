FROM library/python:2
EXPOSE 5000
ADD "requirements.txt" "requirements.txt"
ADD "web.py" "web.py"
RUN pip install -r requirements.txt
CMD ["python", "web.py"]

#use an offical python
FROM python:3.9-slim

#set the working folder in the continer
WORKDIR /usr/src/app

#COPY requirements.txt .

#RUN pip install --no-cache-dir -r requirements.txt

# Install Selenium using pip
RUN pip install --no-cache-dir selenium

#copy the app file to the contienr
COPY Test.login_test.py .

#run command
CMD ["python", "./login_test.py"]
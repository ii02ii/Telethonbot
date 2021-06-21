FROM ii02ii/f:latest

#clonning repo 
RUN git clone https://github.com/ii02ii/f.git /root/userbot
#working directory 
WORKDIR /root/userbot

# Install requirements
RUN pip3 install -U -r ments.txt

ENV PATH="/home/userbot/bin:$PATH"

CMD ["python3","-m","userbot"]

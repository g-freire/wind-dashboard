FROM microsoft/mssql-server-linux

ENV ACCEPT_EULA=Y
ENV MSSQL_SA_PASSWORD=1q2w3e%&!

COPY . . 

EXPOSE 1433

RUN apt-get -y update
RUN apt-get -y install curl
RUN curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add -
RUN curl https://packages.microsoft.com/config/ubuntu/16.04/prod.list | tee /etc/apt/sources.list.d/msprod.list
RUN apt-get -y install mssql-tools unixodbc-dev
RUN echo 'export PATH="$PATH:/opt/mssql-tools/bin"' >> ~/.bashrc
RUN . ~/.bashrc
RUN sqlcmd -S localhost -U SA -P '1q2w3e%&!' -i seed.sql


# RUN gnome-shell --replace
# RUN sqlcmd -S 127.0.0.1,1433 –U SA –P 1q2w3e%&!
# RUN sqlcmd -S localhost -U SA -P '1q2w3e%&!'
# wget -qO- https://packages.microsoft.com/keys/microsoft.asc | apt-key add -

# docker run -e 'ACCEPT_EULA=Y' -e 'SA_PASSWORD=1q2w3e%&!' -p 1433:1433 --name sql1 -d mcr.microsoft.com/mssql/server:2017-latest
# docker exec -it sql1 "bash"
# /opt/mssql-tools/bin/sqlcmd -S localhost -U SA -P '1q2w3e%&!'
# /opt/mssql-tools/bin/sqlcmd -S localhost -U SA -P '1q2w3e%&!' -i seed.sql
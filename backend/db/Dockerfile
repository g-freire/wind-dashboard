FROM microsoft/mssql-server-linux

ENV ACCEPT_EULA=Y
ENV MSSQL_SA_PASSWORD=1q2w3e%&!
# ENV LD_PRELOAD=/nodirect_open.so

COPY . . 

EXPOSE 1433

RUN apt-get -y update
RUN apt-get -y install curl
RUN curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add -
RUN curl https://packages.microsoft.com/config/ubuntu/16.04/prod.list | tee /etc/apt/sources.list.d/msprod.list
RUN apt-get -y install mssql-tools unixodbc-dev
RUN echo 'export PATH="$PATH:/opt/mssql-tools/bin"' >> ~/.bashrc
RUN /bin/bash -c ". ~/.bashrc"

RUN ( /opt/mssql/bin/sqlservr --accept-eula & ) | grep -q "Service Broker manager has started" \
    && /opt/mssql-tools/bin/sqlcmd -S localhost -U SA -P '1q2w3e%&!' -i seed.sql \
    && pkill sqlservr 


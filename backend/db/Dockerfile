FROM microsoft/mssql-server-linux
ENV ACCEPT_EULA=Y
ENV MSSQL_PID='Developer'
ENV MSSQL_SA_PASSWORD=1q2w3e%&!
ENV MSSQL_TCP_PORT=$PORT

EXPOSE $PORT

# ENV LD_PRELOAD=/nodirect_open.so
# EXPOSE 1433

# COPY . . 

# RUN apt-get -y update
# RUN apt-get -y install curl
# RUN curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add -
# RUN curl https://packages.microsoft.com/config/ubuntu/16.04/prod.list | tee /etc/apt/sources.list.d/msprod.list
# RUN apt-get -y install mssql-tools unixodbc-dev
# # this command will run the sqlcmd shell tool, connect to db instance and execute the seed SQL script
# RUN ( /opt/mssql/bin/sqlservr --accept-eula & ) | grep -q "Service Broker manager has started" \
#     && /opt/mssql-tools/bin/sqlcmd -S localhost -U SA -P '1q2w3e%&!' -i seed.sql \
#     && pkill sqlservr 

# sourcing the session not working properly
# RUN echo 'export PATH="$PATH:/opt/mssql-tools/bin"' >> ~/.bashrc
# RUN /bin/bash -c ". ~/.bashrc"

# Docker commands to run the container locally
# docker build -t db001 .
# docker run -p 1434:1433 -d db001


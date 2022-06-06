FROM redhat/ubi8:8.5

USER root

COPY /requirements.txt ./tmp
COPY /StaticMetrics/ ./tmp
COPY /StaticMetrics/entrypoint.sh ./

# Install Python and PowerShell
RUN dnf -y install python39 && \
    curl https://packages.microsoft.com/config/rhel/8/prod.repo | tee /etc/yum.repos.d/microsoft.repo && \
    dnf -y install powershell && \
    dnf clean all && \
    cd /tmp && Y | pip3 install -r requirements.txt

WORKDIR /tmp

EXPOSE 9200
ENTRYPOINT ["/entrypoint.sh"]
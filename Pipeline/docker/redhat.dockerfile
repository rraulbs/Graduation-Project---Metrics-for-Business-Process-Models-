FROM redhat/ubi8:8.5

USER root

COPY /requirements.txt ./tmp

# Install Python and PowerShell
RUN mkdir ./processes && \
    # chown nobody /tmp && \
    # chown nobody /processes && \
    dnf -y install python39 && \
    curl https://packages.microsoft.com/config/rhel/8/prod.repo | tee /etc/yum.repos.d/microsoft.repo && \
    dnf -y install powershell && \
    dnf clean all && \
    cd /tmp && Y | pip3 install -r requirements.txt

COPY Processes/* ./processes
COPY Scripts/* ./tmp

WORKDIR /tmp

# USER nobody
EXPOSE 9200
ENTRYPOINT ["/tmp/entrypoint.sh"]
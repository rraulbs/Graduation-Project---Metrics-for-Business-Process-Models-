FROM redhat/ubi8:8.5

USER root

# Install PowerShell
RUN curl https://packages.microsoft.com/config/rhel/8/prod.repo | tee /etc/yum.repos.d/microsoft.repo && \
    dnf -y install powershell && \
    dnf clean all
    
WORKDIR /tmp

EXPOSE 9200
ENTRYPOINT ["/tmp/entrypoint.sh"]
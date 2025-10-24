FROM debian:latest 
RUN apt-get update && apt-get install -y openssh-server iproute2 
RUN mkdir -p /root/.ssh 
COPY authorized_keys /root/.ssh/ 
RUN chmod 700 /root/.ssh  
RUN sed 's@session\s*required\s*pam_loginuid.so@session optional pam_loginuid.so@g' -i /etc/pam.d/sshd 
EXPOSE 22
CMD /usr/sbin/sshd -D

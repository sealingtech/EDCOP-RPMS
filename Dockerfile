FROM centos

RUN yum -y install rpm-build

COPY . /root/

RUN chmod +x /root/image_build_script.sh;/root/./image_build_script.sh


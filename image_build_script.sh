#!/bin/bash

rpmbuild -bb /root/rpmbuild/SPECS/edcop-repo.spec


cat <<EOF > /etc/yum.repos.d/kubernetes.repo
[kubernetes]
name=Kubernetes
baseurl=https://packages.cloud.google.com/yum/repos/kubernetes-el7-x86_64
enabled=1
gpgcheck=1
repo_gpgcheck=1
gpgkey=https://packages.cloud.google.com/yum/doc/yum-key.gpg https://packages.cloud.google.com/yum/doc/rpm-package-key.gpg
EOF

mkdir /root/extra-packages 

yumdownloader -y --destdir=/root/extra-packages kubeadm kubectl kubelet kubernetes-cni cri-tools
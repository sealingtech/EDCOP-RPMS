SHELL := /bin/bash

rpms:
	docker build -t edcop_rpm .
	id=$$(docker create edcop_rpm);docker cp $$id:/root/rpmbuild/RPMS/noarch .;docker cp $$id:/root/extra-packages .;docker rm -v $$id
	docker rmi edcop_rpm
	mv noarch edcop-packages


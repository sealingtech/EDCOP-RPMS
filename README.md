# EDCOP-RPMS


Builds RPM files needed for EDCOP.

Requires:
Docker
make

Run the command

```
make rpms
```

Two directories will be created, edcop-packages and extra-packages.  These packages are not signed and will need to be signed manually with a valid GPG key.

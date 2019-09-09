Name:           edcop-repo
Version:        1
Release:        1
Summary:        Expandable DCO Platform YUM Repository

Group:          System Environment/Base
License:        Apache

URL:            http://repos.sealingtech.org/edcop/1.0
Source0:        http://repos.sealingtech.org/edcop/RPM-GPG-KEY-EDCOP
Source1:        edcop.repo

BuildArch:     noarch

%description
This package contains the Expandable DCO Platform (EDCOP) repository
GPG key as well as configuration for yum.

%prep
%setup -q  -c -T
install -pm 644 %{SOURCE0} .

%build


%install
rm -rf $RPM_BUILD_ROOT

#GPG Key
install -Dpm 644 %{SOURCE0} \
    $RPM_BUILD_ROOT%{_sysconfdir}/pki/rpm-gpg/RPM-GPG-KEY-EDCOP

# yum
install -dm 755 $RPM_BUILD_ROOT%{_sysconfdir}/yum.repos.d
install -pm 644 %{SOURCE1}  \
    $RPM_BUILD_ROOT%{_sysconfdir}/yum.repos.d

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%config(noreplace) /etc/yum.repos.d/*
/etc/pki/rpm-gpg/*

%changelog
* Sun Dec 10 2017 Ed Sealing <ed.sealing@sealingtech.org> - 11-20
- Initial Commit

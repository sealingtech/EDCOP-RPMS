Name:           epel-release
Version:        7
Release:        11
Summary:        Extra Packages for Enterprise Linux repository configuration

Group:          System Environment/Base
License:        GPLv2

# This is a EPEL maintained package which is specific to
# our distribution.  Thus the source is only available from
# within this srpm.
URL:            http://download.fedoraproject.org/pub/epel
Source0:        http://download.fedoraproject.org/pub/epel/RPM-GPG-KEY-EPEL-7
Source1:        GPL
Source2:        epel.repo
Source3:        epel-testing.repo
# EPEL default preset policy (borrowed from fedora's 90-default.preset)
Source4:        90-epel.preset

BuildArch:     noarch
Requires:      redhat-release >=  %{version}
# epel-release is only for enterprise linux, not fedora
Conflicts:     fedora-release

%description
This package contains the Extra Packages for Enterprise Linux (EPEL) repository
GPG key as well as configuration for yum.

%prep
%setup -q  -c -T
install -pm 644 %{SOURCE0} .
install -pm 644 %{SOURCE1} .

%build


%install
rm -rf $RPM_BUILD_ROOT

#GPG Key
install -Dpm 644 %{SOURCE0} \
    $RPM_BUILD_ROOT%{_sysconfdir}/pki/rpm-gpg/RPM-GPG-KEY-EPEL-7

# yum
install -dm 755 $RPM_BUILD_ROOT%{_sysconfdir}/yum.repos.d
install -pm 644 %{SOURCE2} %{SOURCE3}  \
    $RPM_BUILD_ROOT%{_sysconfdir}/yum.repos.d
install -pm 644 -D %{SOURCE4} $RPM_BUILD_ROOT%{_prefix}/lib/systemd/system-preset/90-epel.preset

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc GPL
%config(noreplace) /etc/yum.repos.d/*
/etc/pki/rpm-gpg/*
%{_prefix}/lib/systemd/system-preset/90-epel.preset

%changelog
* Mon Oct 02 2017 Kevin Fenzi <kevin@scrye.com> - 7-11
- Add Conflicts on fedora-release to prevent people from installing on Fedora systems. Fixes bug #1497702

* Sat Jun 24 2017 Kevin Fenzi <kevin@scrye.com> - 7-10
- Change mirrorlist= in repo files to be metalink= (as thats what they are). Fixes bug #1451212

* Tue Dec 27 2016 Kevin Fenzi <kevin@scrye.com> - 7-9
- Add preset for drbdlinks package. Fixes bug #1405744

* Sat Jul 23 2016 Kevin Fenzi <kevin@scrye.com> - 7-8
- Drop duplicate libstoragemgmt from presets. Fixes bug #1358971

* Fri Jun 03 2016 Kevin Fenzi <kevin@scrye.com> - 7-7
- Drop initial-setup from presets. Fixes bug #1342511

* Wed Mar 30 2016 Jason L Tibbitts III <tibbs@math.uh.edu> - 7-6
- Remove macros.epel; let epel-rpm-macros handle it instead.

* Tue Nov 25 2014 Rex Dieter <rdieter@fedoraproject.org> 7-5
- fix typo in macros.epel

* Fri Nov 21 2014 Rex Dieter <rdieter@fedoraproject.org> 7-4
- add systemd 90-epel.preset

* Fri Nov 21 2014 Rex Dieter <rdieter@fedoraproject.org> 7-3
- implement %%epel macro

* Tue Sep 02 2014 Kevin Fenzi <kevin@scrye.com> 7-2
- Make repo files config(noreplace). Fixes bug #1135576

* Thu Aug 28 2014 Dennis Gilmore <dennis@ausil.us> - 7-1
- enable gpg checking now we are out of beta

* Wed Jun 18 2014 Kevin Fenzi <kevin@scrye.com> 7-0.2
- Drop unneeded up2date post/postun
- Fixed up description.
- Fixes bugs #1052434 and #1093918

* Mon Dec 16 2013 Dennis Gilmore <dennis@ausil.us> - 7-0.1
- initial epel 7 build. gpg cheking is disabled


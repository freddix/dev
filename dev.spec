Summary:	Set of basic /dev entries for passive environments
Name:		dev
Version:	1.0
Release:	1
License:	GPL v2
Group:		Applications/System
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_enable_debug_packages	0

%description
Set of basic /dev entries for chroot environments.

%prep
%build

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT/dev/{pts,shm}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%dir %attr(755,root,root) /dev/pts
%dir %attr(777,root,root) /dev/shm
%dev(c,1,3) %attr(666,root,root) /dev/null
%dev(c,1,5) %attr(666,root,root) /dev/zero
%dev(c,1,7) %attr(666,root,root) /dev/full
%dev(c,1,8) %attr(666,root,root) /dev/random
%dev(c,1,9) %attr(666,root,root) /dev/urandom
%dev(c,5,0) %attr(666,root,root) /dev/tty
%dev(c,5,1) %attr(600,root,root) /dev/console


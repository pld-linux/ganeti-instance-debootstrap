Summary:	Debian/Ubuntu guest OS definition for Ganeti
Name:		ganeti-instance-debootstrap
Version:	0.14
Release:	0.4
License:	GPL v2
Group:		Applications/System
Source0:	https://ganeti.googlecode.com/files/%{name}-%{version}.tar.gz
# Source0-md5:	318039b68d63453ac115a6987e31c6f0
Patch0:		kpartx-sync.patch
URL:		https://code.google.com/p/ganeti/
BuildRequires:	rpmbuild(macros) >= 1.647
Requires:	blockdev
Requires:	coreutils
Requires:	debootstrap
Requires:	dpkg
Requires:	dump
Requires:	e2fsprogs
Requires:	ganeti
Requires:	kpartx
Requires:	losetup
Requires:	mount
Requires:	sed
Requires:	tar
Requires:	util-linux
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a guest OS definition for Ganeti.  It will install a minimal
version of Debian or Ubuntu via debootstrap (thus it requires network
access).

%prep
%setup -q
%patch0 -p1

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_sysconfdir}/ganeti/instance-debootstrap/hooks \
	$RPM_BUILD_ROOT/var/cache/ganeti-instance-debootstrap

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__mv} $RPM_BUILD_ROOT%{_datadir}/ganeti/os/debootstrap/variants.list $RPM_BUILD_ROOT%{_sysconfdir}/ganeti/instance-debootstrap
ln -s %{_sysconfdir}/ganeti/instance-debootstrap/variants.list $RPM_BUILD_ROOT%{_datadir}/ganeti/os/debootstrap/variants.list

%{__rm} -r $RPM_BUILD_ROOT/%{_docdir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc NEWS README examples
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/default/ganeti-instance-debootstrap
%dir %{_sysconfdir}/ganeti/instance-debootstrap
%dir %{_sysconfdir}/ganeti/instance-debootstrap/hooks
%dir %{_sysconfdir}/ganeti/instance-debootstrap/variants
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/ganeti/instance-debootstrap/variants/default.conf
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/ganeti/instance-debootstrap/variants.list
%dir %{_datadir}/ganeti/os/debootstrap
%{_datadir}/ganeti/os/debootstrap/common.sh
%attr(755,root,root) %{_datadir}/ganeti/os/debootstrap/create
%attr(755,root,root) %{_datadir}/ganeti/os/debootstrap/export
%{_datadir}/ganeti/os/debootstrap/ganeti_api_version
%attr(755,root,root) %{_datadir}/ganeti/os/debootstrap/import
%{_datadir}/ganeti/os/debootstrap/parameters.list
%attr(755,root,root) %{_datadir}/ganeti/os/debootstrap/rename
%{_datadir}/ganeti/os/debootstrap/variants.list
%attr(755,root,root) %{_datadir}/ganeti/os/debootstrap/verify
/var/cache/ganeti-instance-debootstrap

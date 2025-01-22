#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cpan
# autospec version: v21
# autospec commit: 94c6be0
#
Name     : perl-SMTP-Server
Version  : 1.1
Release  : 28
URL      : https://cpan.metacpan.org/authors/id/M/MA/MACGYVER/SMTP-Server-1.1.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/M/MA/MACGYVER/SMTP-Server-1.1.tar.gz
Source1  : http://http.debian.net/debian/pool/main/libn/libnet-smtp-server-perl/libnet-smtp-server-perl_1.1-6.debian.tar.xz
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0
Requires: perl-SMTP-Server-license = %{version}-%{release}
Requires: perl-SMTP-Server-perl = %{version}-%{release}
BuildRequires : buildreq-cpan
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
SMTP::Server
------------
This module is a complete, RFC 821 compliant, SMTP server implementation
written entirely in Perl.  It has powerful extensively and customization
facilities that allow for a variety of potential uses.

%package dev
Summary: dev components for the perl-SMTP-Server package.
Group: Development
Provides: perl-SMTP-Server-devel = %{version}-%{release}
Requires: perl-SMTP-Server = %{version}-%{release}

%description dev
dev components for the perl-SMTP-Server package.


%package license
Summary: license components for the perl-SMTP-Server package.
Group: Default

%description license
license components for the perl-SMTP-Server package.


%package perl
Summary: perl components for the perl-SMTP-Server package.
Group: Default
Requires: perl-SMTP-Server = %{version}-%{release}

%description perl
perl components for the perl-SMTP-Server package.


%prep
%setup -q -n SMTP-Server-1.1
cd %{_builddir}
tar xf %{_sourcedir}/libnet-smtp-server-perl_1.1-6.debian.tar.xz
cd %{_builddir}/SMTP-Server-1.1
mkdir -p deblicense/
cp -r %{_builddir}/debian/* %{_builddir}/SMTP-Server-1.1/deblicense/

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} -I. Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-SMTP-Server
cp %{_builddir}/SMTP-Server-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/perl-SMTP-Server/74a8a6531a42e124df07ab5599aad63870fa0bd4 || :
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Net::SMTP::Server.3
/usr/share/man/man3/Net::SMTP::Server::Client.3
/usr/share/man/man3/Net::SMTP::Server::Relay.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-SMTP-Server/74a8a6531a42e124df07ab5599aad63870fa0bd4

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/*

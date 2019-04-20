#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-SMTP-Server
Version  : 1.1
Release  : 8
URL      : https://cpan.metacpan.org/authors/id/M/MA/MACGYVER/SMTP-Server-1.1.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/M/MA/MACGYVER/SMTP-Server-1.1.tar.gz
Source1  : http://http.debian.net/debian/pool/main/libn/libnet-smtp-server-perl/libnet-smtp-server-perl_1.1-6.debian.tar.xz
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0
Requires: perl-SMTP-Server-license = %{version}-%{release}
BuildRequires : buildreq-cpan

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

%description dev
dev components for the perl-SMTP-Server package.


%package license
Summary: license components for the perl-SMTP-Server package.
Group: Default

%description license
license components for the perl-SMTP-Server package.


%prep
%setup -q -n SMTP-Server-1.1
cd ..
%setup -q -T -D -n SMTP-Server-1.1 -b 1
mkdir -p deblicense/
mv %{_topdir}/BUILD/debian/* %{_topdir}/BUILD/SMTP-Server-1.1/deblicense/

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-SMTP-Server
cp LICENSE %{buildroot}/usr/share/package-licenses/perl-SMTP-Server/LICENSE
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
/usr/lib/perl5/vendor_perl/5.28.2/Net/SMTP/Server.pm
/usr/lib/perl5/vendor_perl/5.28.2/Net/SMTP/Server/Client.pm
/usr/lib/perl5/vendor_perl/5.28.2/Net/SMTP/Server/Relay.pm
/usr/lib/perl5/vendor_perl/5.28.2/auto/Net/SMTP/Server/Client/autosplit.ix
/usr/lib/perl5/vendor_perl/5.28.2/auto/Net/SMTP/Server/Relay/autosplit.ix
/usr/lib/perl5/vendor_perl/5.28.2/auto/Net/SMTP/Server/autosplit.ix

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Net::SMTP::Server.3
/usr/share/man/man3/Net::SMTP::Server::Client.3
/usr/share/man/man3/Net::SMTP::Server::Relay.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-SMTP-Server/LICENSE

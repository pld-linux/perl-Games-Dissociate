%define		perl_sitelib	%(eval "`perl -V:installsitelib`"; echo $installsitelib)
Summary:	Games-Dissociate perl module
Summary(pl):	Modu³ perla Games-Dissociate
Name:		perl-Games-Dissociate
Version:	0.12
Release:	3
Copyright:	GPL
Group:		Development/Languages/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Source:		ftp://ftp.perl.org/pub/CPAN/modules/by-module/Games/Games-Dissociate-%{version}.tar.gz
BuildRequires:	perl >= 5.005_03-10
%requires_eq	perl
Requires:	%{perl_sitearch}
BuildRoot:	/tmp/%{name}-%{version}-root

%description
Games-Dissociate module provides the function dissociate, which implements
a Dissociated Press algorithm well known to Emacs users as "meta-x dissociate".

%description -l pl
Modu³ perla Games-Dissociate.

%prep
%setup -q -n Games-Dissociate-%{version}

%build
perl Makefile.PL
make

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

(
  cd $RPM_BUILD_ROOT%{perl_sitearch}/auto/Games/Dissociate
  sed -e "s#$RPM_BUILD_ROOT##" .packlist >.packlist.new
  mv .packlist.new .packlist
)

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man3/* \
        ChangeLog README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {ChangeLog,README}.gz

%{perl_sitelib}/Games/Dissociate.pm
%{perl_sitearch}/auto/Games/Dissociate

%{_mandir}/man3/*

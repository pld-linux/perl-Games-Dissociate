#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Games
%define		pnam	Dissociate
Summary:	Games::Dissociate - a Dissociated Press algorithm and filter
Summary(pl.UTF-8):	Games::Dissociate - algorytm i filtr "Dissociated Press"
Name:		perl-Games-Dissociate
Version:	0.19
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Games/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	91ddf6a33e2dbe437c03af5b93397210
URL:		http://search.cpan.org/dist/Games-Dissociate/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Games::Dissociate Perl module provides the function dissociate, which
implements a Dissociated Press algorithm well known to Emacs users as
"meta-x dissociate".

%description -l pl.UTF-8
Moduł Perla Games::Dissociate udostępnia funkcję "dissociate", która
implementuje algorytm "Dissociated Press", dobrze znany użytkownikom
Emacsa jako "meta-x dissociate".

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README
%{perl_vendorlib}/Games/Dissociate.pm
%{_mandir}/man3/*

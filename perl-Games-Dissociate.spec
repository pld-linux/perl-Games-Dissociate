#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Games
%define	pnam	Dissociate
Summary:	Games::Dissociate - a Dissociated Press algorithm and filter
Summary(pl):	Games::Dissociate - algorytm i filtr "Dissociated Press"
Name:		perl-Games-Dissociate
Version:	0.14
Release:	6
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	a4d71db43a0f401a7da6aad4e843759c
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	perl-devel >= 5.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Games::Dissociate Perl module provides the function dissociate, which
implements a Dissociated Press algorithm well known to Emacs users as
"meta-x dissociate".

%description -l pl
Modu³ Perla Games::Dissociate udostêpnia funkcjê "dissociate", która
implementuje algorytm "Dissociated Press", dobrze znany u¿ytkownikom
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

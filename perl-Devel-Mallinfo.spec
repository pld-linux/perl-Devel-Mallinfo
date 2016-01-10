#
# Conditional build:
%bcond_without	tests	# do perform "make test"

%define		pdir	Devel
%define		pnam	Mallinfo
%include	/usr/lib/rpm/macros.perl
Summary:	Devel::Mallinfo - mallinfo() memory statistics and more
Summary(pl.UTF-8):	Devel::Mallinfo - statystyki pamięci mallinfo()
Name:		perl-%{pdir}-%{pnam}
Version:	14
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	eaf6d39b94ba1637ba38b7db74013d7d
URL:		http://search.cpan.org/dist/Devel-Mallinfo/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Devel::Mallinfo is an interface to the C library mallinfo function
giving various totals for memory used by malloc. It's meant for
development use, to give you an idea how much memory your program and
libraries are using. Interfaces to some GNU C Library specific malloc
information are provided too, when available.

%description -l pl.UTF-8
Devel::Mallinfo jest interfejsem do funkcji mallinfo w bibliotece C,
służącej do tworzenia statystyk zajętości pamięci alokowane przez
malloc. Przeznaczony jest dla programistów, do zobrazowania ile
pamięci zajmuje program i biblioteki. Dostarczany jest również
interfejs do różnych informacji o zajętości pamięci specyficznych dla
biblioteki GNU C.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make} \
	CC="%{__cc}" \
	OPTIMIZE="%{rpmcflags}"

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -a examples $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%{perl_vendorarch}/%{pdir}/%{pnam}.pm
%dir %{perl_vendorarch}/auto/%{pdir}/%{pnam}
%attr(755,root,root) %{perl_vendorarch}/auto/%{pdir}/%{pnam}/%{pnam}.so
%{_mandir}/man3/*
%dir %{_examplesdir}/%{name}-%{version}/
%attr(755,root,root) %{_examplesdir}/%{name}-%{version}/*

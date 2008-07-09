%define	module	Readonly
%define	name	perl-%{module}
%define version 1.03
%define release %mkrel 4

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	Facility for creating read-only scalars, arrays, hashes
License:	GPL or Artistic
Group:		Development/Perl
Source:		ftp://ftp.perl.org/pub/CPAN/modules/by-module/Readonly/%{module}-%{version}.tar.bz2
Url:		http://search.cpan.org/dist/%{module}
%if %{mdkversion} < 1010
Buildrequires:	perl-devel
%endif
Buildarch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
This is a facility for creating non-modifiable variables. This is useful for
configuration files, headers, etc. It can also be useful as a development and
debugging tool, for catching updates to variables that should not be changed.

If any of the values you pass to Scalar, Array, or Hash are references, then
those functions recurse over the data structures, marking everything as
Readonly. Usually, this is what you want: the entire structure nonmodifiable.
If you want only the top level to be Readonly, use the alternate Scalar1,
Array1 and Hash1 functions.

Please note that most users of Readonly will also want to install a companion
module Readonly::XS. See the "CONS" section below for more details.

%prep
%setup -q -n %{module}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%{__make} test

%install
rm -rf %{buildroot}
%makeinstall_std


%clean 
rm -rf %{buildroot}

%files 
%defattr(-,root,root)
%doc Changes README
%{perl_vendorlib}/Readonly.pm
%{perl_vendorlib}/benchmark.pl
%{_mandir}/*/*


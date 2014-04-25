%define	modname	Readonly
%define modver 1.04

Summary:	Facility for creating read-only scalars, arrays, hashes

Name:		perl-%{modname}
Version:	%perl_convert_version %{modver}
Release:	1
License:	GPLv2+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{modname}
Source0:	ftp://ftp.perl.org:21/pub/CPAN/modules/by-module/%{modname}/%{modname}-%{modver}.tar.gz
BuildArch:	noarch
BuildRequires:	perl-devel
BuildRequires: perl(Module::Build)

%description
This is a facility for creating non-modifiable variables. This is useful for
configuration files, headers, etc. It can also be useful as a development and
debugging tool, for catching updates to variables that should not be changed.

If any of the values you pass to Scalar, Array, or Hash are references, then
those functions recurse over the data structures, marking everything as
Readonly. Usually, this is what you want:	the entire structure nonmodifiable.
If you want only the top level to be Readonly, use the alternate Scalar1,
Array1 and Hash1 functions.

Please note that most users of Readonly will also want to install a companion
module Readonly::XS. See the "CONS" section below for more details.

%prep
%setup -qn %{modname}-%{modver}

%build
%__perl Build.PL installdirs=vendor
./Build

%check
./Build test

%install
./Build install destdir=%{buildroot}

%files 
%doc Changes 
%{perl_vendorlib}/Readonly.pm
%{perl_vendorlib}/benchmark.pl
%{_mandir}/man3/*
%{perl_vendorlib}Readonly/Array.pm
%{perl_vendorlib}Readonly/Hash.pm
%{perl_vendorlib}Readonly/Scalar.pm



%define	modname	Readonly

Summary:	Facility for creating read-only scalars, arrays, hashes
Name:		perl-%{modname}
Version:	2.05
Release:	2
License:	GPLv2+ or Artistic
Group:		Development/Perl
Url:		https://search.cpan.org/dist/%{modname}
Source0:	ftp://ftp.perl.org:21/pub/CPAN/modules/by-module/%{modname}/%{modname}-%{version}.tar.gz
BuildArch:	noarch
BuildRequires:	perl(CPAN::Meta)
BuildRequires:	perl-devel
BuildRequires:	perl(Module::Build)
BuildRequires:	perl(Module::Build::Tiny)
BuildRequires:	perl(ExtUtils::CBuilder)
BuildRequires:	perl(Test::More)

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
%setup -qn %{modname}-%{version}
perl Build.PL --installdirs=vendor

%build
./Build

%check
./Build test

%install
./Build install --destdir=%{buildroot}

%files 
%doc Changes 
%{perl_vendorlib}/Readonly.pm
%{_mandir}/man3/*
# %{perl_vendorlib}/Readonly/Array.pm
# %{perl_vendorlib}/Readonly/Hash.pm
# %{perl_vendorlib}/Readonly/Scalar.pm

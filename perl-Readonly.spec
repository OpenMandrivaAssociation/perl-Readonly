%define	upstream_name	 Readonly
%define upstream_version 1.03

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	7

Summary:	Facility for creating read-only scalars, arrays, hashes
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Readonly/%{upstream_name}-%{upstream_version}.tar.bz2

BuildRequires:	perl-devel
BuildArch:	noarch

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
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files 
%doc Changes README
%{perl_vendorlib}/Readonly.pm
%{perl_vendorlib}/benchmark.pl
%{_mandir}/*/*


%changelog
* Sun Jan 22 2012 Oden Eriksson <oeriksson@mandriva.com> 1.30.0-4mdv2012.0
+ Revision: 765629
- rebuilt for perl-5.14.2

* Sat Jan 21 2012 Oden Eriksson <oeriksson@mandriva.com> 1.30.0-3
+ Revision: 764139
- rebuilt for perl-5.14.x

* Sat May 21 2011 Oden Eriksson <oeriksson@mandriva.com> 1.30.0-2
+ Revision: 676732
- rebuild

* Wed Jul 29 2009 Jérôme Quelin <jquelin@mandriva.org> 1.30.0-1mdv2010.0
+ Revision: 404352
- rebuild using %%perl_convert_version

* Wed Jul 09 2008 Oden Eriksson <oeriksson@mandriva.com> 1.03-4mdv2009.0
+ Revision: 232969
- rebuild

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Sat Sep 15 2007 Guillaume Rousse <guillomovitch@mandriva.org> 1.03-3mdv2008.0
+ Revision: 86820
- rebuild


* Thu Aug 31 2006 Guillaume Rousse <guillomovitch@mandriva.org> 1.03-2mdv2007.0
- Rebuild

* Sun Apr 23 2006 Guillaume Rousse <guillomovitch@mandriva.org> 1.03-1mdk
- first mdk release


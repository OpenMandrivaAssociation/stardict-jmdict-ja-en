%define	version	2.4.2
%define release	6
%define dict_format_version	2.4.2

Summary:	JMDICT (Japanese -> English dictionary) converted to StarDict 2
Name:		stardict-jmdict-ja-en
Version:	%{version}
Release:	%{release}
License:	General Dictionary Licence
Group:		Databases
URL:		https://stardict.sourceforge.net/
Buildroot:	%{_tmppath}/%{name}-%{version}-buildroot
BuildArch:	noarch

Source0:	http://prdownloads.sourceforge.net/stardict/%{name}-%{version}.tar.bz2
Source1:	general-dictionary-licence.html.bz2

Provides:	stardict-dictionary = %{dict_format_version}
Requires:	stardict >= %{dict_format_version}

%description
The JMdict (Japanese-Multilingual Dictionary) project began in 1999 as an
offshoot of the EDICT Japanese-English Electronic Dictionary project. It
involved a major rebuild of the main files, with a more complex structure
using XML.
This package contains JMDICT database (Japanese -> English) converted
into StarDict 2 format.

Please refer to http://www.csse.monash.edu.au/~jwb/j_jmdict.html
for more info.

%prep
%setup -q
bzip2 -dc %SOURCE1 > general-dictionary-licence.html

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_datadir}/stardict/dic
install -m 0644 * %{buildroot}%{_datadir}/stardict/dic

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc general-dictionary-licence.html
%{_datadir}/stardict/dic/*



%changelog
* Wed Jul 23 2008 Thierry Vignaud <tvignaud@mandriva.com> 2.4.2-5mdv2009.0
+ Revision: 242736
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Mon Aug 20 2007 Thierry Vignaud <tvignaud@mandriva.com> 2.4.2-3mdv2008.0
+ Revision: 67663
- use %%mkrel


* Sat Oct 01 2005 Abel Cheung <deaddog@mandriva.org> 2.4.2-3mdk
- first Mandriva package


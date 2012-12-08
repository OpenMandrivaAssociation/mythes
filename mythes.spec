%define	api		1.2
%define	major	0
%define	libname	%mklibname %{name} %api %{major}
%define	develname	%mklibname %{name} -d

Name:		mythes
Summary:	A thesaurus library
Version:	1.2.2
Release:	1
Group:		System/Libraries
License:	BSD
URL:		http://hunspell.sourceforge.net/
Source0:	http://downloads.sourceforge.net/hunspell/%{name}-%{version}.tar.gz

BuildRequires: gettext-devel
BuildRequires: pkgconfig(hunspell)

%description
MyThes is a simple thesaurus that uses a structured text data file and an
index file with binary search to look up words and phrases and return 
information on part of speech, meanings, and synonyms.

%package -n %{libname}
Summary:	Libraries for %{name}
Group:		System/Libraries

%description -n %{libname}
This package contains libraries used by %{name}.

%package -n %{develname}
Summary:	Files for developing with mythes
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n %{develname}
Includes and definitions for developing with mythes

%prep
%setup -q

%build
%configure2_5x \
	--disable-static

%make

%check
./example th_en_US_new.idx th_en_US_new.dat checkme.lst
./example morph.idx morph.dat morph.lst morph.aff morph.dic

%install
rm -rf %{buildroot}
%makeinstall_std

mkdir -p %{buildroot}/%{_datadir}/mythes

%files -n %{libname}
%{_libdir}/*%{api}.so.%{major}*

%files -n %{develname}
%doc README COPYING AUTHORS
%doc data_layout.txt
%{_bindir}/th_gen_idx.pl
%{_includedir}/mythes.hxx
%{_libdir}/*.so
%{_libdir}/pkgconfig/mythes.pc
%{_datadir}/mythes





%changelog
* Sat Jan 07 2012 Matthew Dawkins <mattydaw@mandriva.org> 1.2.2-1
+ Revision: 758611
- imported package mythes


* Sat Jan 07 2012 Matthew Dawkins <mdawkins@unity-linux.org> 1.2.2-1-unity2011
- new version 1.2.2

* Wed Mar 09 2011 mdawkins <mattydaw@gmail.com> 1.2.1-1-unity2011
- import for Unity

* Sun Jan 23 2011 dmorgan <dmorgan> 1.2.1-1.mga1
+ Revision: 35239
- Add gettext-devel as buildrequires
- Adapt to mageia
- imported package mythes


* Mon Jun 21 2010 Caolán McNamara <caolanm@redhat.com> - 1.2.1-1
- latest version

* Thu Mar 11 2010 Caolán McNamara <caolanm@redhat.com> - 1.2.0-1
- initial version

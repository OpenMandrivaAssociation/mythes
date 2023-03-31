%define	api	1.2
%define	major	0
%define	libname	%mklibname %{name} %{api} %{major}
%define	devname	%mklibname %{name} -d

Summary:	A thesaurus library
Name:		mythes
Version:	1.2.4
Release:	8
Group:		System/Libraries
License:	BSD
Url:		http://hunspell.sourceforge.net/
Source0:	http://downloads.sourceforge.net/hunspell/%{name}-%{version}.tar.gz

BuildRequires:	gettext-devel
BuildRequires:	pkgconfig(hunspell)

%description
MyThes is a simple thesaurus that uses a structured text data file and an
index file with binary search to look up words and phrases and return 
information on part of speech, meanings, and synonyms.

%package -n %{libname}
Summary:	Libraries for %{name}
Group:		System/Libraries

%description -n %{libname}
This package contains libraries used by %{name}.

%package -n %{devname}
Summary:	Files for developing with mythes
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n %{devname}
Includes and definitions for developing with mythes

%prep
%setup -q

%build
%configure

%make

%check
./example th_en_US_new.idx th_en_US_new.dat checkme.lst
./example morph.idx morph.dat morph.lst morph.aff morph.dic

%install
%makeinstall_std

mkdir -p %{buildroot}/%{_datadir}/mythes

%files -n %{libname}
%{_libdir}/libmythes-%{api}.so.%{major}*

%files -n %{devname}
%doc README COPYING AUTHORS
%doc data_layout.txt
%{_bindir}/th_gen_idx.pl
%{_includedir}/mythes.hxx
%{_libdir}/*.so
%{_libdir}/pkgconfig/mythes.pc
%{_datadir}/mythes


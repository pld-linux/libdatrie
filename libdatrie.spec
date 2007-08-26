Summary:	Double-Array Trie library
Summary(pl.UTF-8):	Biblioteka dwutablicowego trie
Name:		libdatrie
Version:	0.1.2
Release:	1
License:	LGPL v2.1
Group:		Libraries
Source0:	http://linux.thai.net/pub/thailinux/software/libthai/%{name}-%{version}.tar.gz
# Source0-md5:	3eaedd5452149e11547a0dc74ee3fcfd
URL:		http://linux.thai.net/projects/datrie
BuildRequires:	doxygen
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
datrie is an implementation of double-array structure for representing
trie, as proposed by Junichi Aoe.

Trie is a kind of digital search tree, an efficient indexing method
with O(1) time complexity for searching. Comparably as efficient as
hashing, trie also provides flexibility on incremental matching and
key spelling manipulation. This makes it ideal for lexical analyzers,
as well as spelling dictionaries.

%description -l pl.UTF-8
datrie to implementacja struktury dwutablicowej do reprezentowania
trie, zaproponowanej przez Junichi Aoe.

Trie to rodzaj binarnego drzewa wyszukiwań, czyli wydajnej metody
indeksowania ze złożonością czasową wyszukiwania O(1). Porównując trie
jest tak wydajne jak haszowanie, ale zapewnia też elastyczność
przyrostowego dopasowywania i manipulacji pisownią klucza. To czyni je
idealnym dla analizatorów leksykalnych, a także sprawdzania pisowni.

%package devel
Summary:	Header files for datrie library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki datrie
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for datrie library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki datrie.

%package static
Summary:	Static datrie library
Summary(pl.UTF-8):	Statyczna biblioteka datrie
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static datrie library.

%description static -l pl.UTF-8
Statyczna biblioteka datrie.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/trietool
%attr(755,root,root) %{_libdir}/libdatrie.so.*.*.*
%{_mandir}/man1/trietool.1*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libdatrie.so
%{_libdir}/libdatrie.la
%{_includedir}/datrie
%{_pkgconfigdir}/datrie.pc
# only public API
%{_mandir}/man3/sb-trie.h.3*
%{_mandir}/man3/trie.h.3*
%{_mandir}/man3/triedefs.h.3*
%{_mandir}/man3/SB*.3*
%{_mandir}/man3/sb_trie_*.3*
%{_mandir}/man3/TRIE_*.3*
%{_mandir}/man3/Trie*.3*
%{_mandir}/man3/trie_*.3*

%files static
%defattr(644,root,root,755)
%{_libdir}/libdatrie.a

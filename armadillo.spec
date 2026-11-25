Summary:	C++ linear algebra library
Summary(pl.UTF-8):	Biblioteka C++ do algebry liniowej
Name:		armadillo
Version:	15.8.0
Release:	1
License:	MPL v2.0
Group:		Libraries
Source0:	https://downloads.sourceforge.net/arma/%{name}-%{version}.tar.xz
# Source0-md5:	d07a86855aed20fda004824f38b3777c
URL:		https://arma.sourceforge.net/
BuildRequires:	SuperLU-devel >= 5
BuildRequires:	arpack-devel
BuildRequires:	blas-devel
BuildRequires:	cmake >= 3.10
BuildRequires:	hdf5-devel
BuildRequires:	lapack-devel
BuildRequires:	libstdc++-devel >= 6:8.1
BuildRequires:	pkgconfig
BuildRequires:	rpm-build >= 4.6
BuildRequires:	rpmbuild(macros) >= 1.752
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Armadillo is a C++ linear algebra library (matrix maths) aiming
towards a good balance between speed and ease of use. The syntax is
deliberately similar to Matlab.

%description -l pl.UTF-8
Armadillo to biblioteka C++ do algebry liniowej (obliczeń na
macierzach), której celem jest dobry kompromis między szybkością a
łatwością użycia. Składnia jest celowo podobna do Matlaba.

%package devel
Summary:	Header files for Armadillo library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki Armadillo
Group:		Development/Libraries
Requires:	%{name}%{?_isa} = %{version}-%{release}
Requires:	SuperLU-devel%{?_isa} >= 5
Requires:	arpack-devel
Requires:	blas-devel%{?_isa}
Requires:	hdf5-devel%{?_isa}
Requires:	lapack-devel%{?_isa}
Requires:	libstdc++-devel%{?_isa} >= 6:8.1
Obsoletes:	armadillo-static < 6

%description devel
Header files for Armadillo library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki Armadillo.

%package apidocs
Summary:	Armadillo API documentation
Summary(pl.UTF-8):	Dokumentacja API biblioteki Armadillo
Group:		Documentation
BuildArch:	noarch

%description apidocs
API and internal documentation for Armadillo library.

%description apidocs -l pl.UTF-8
Dokumentacja API biblioteki Armadillo.

%prep
%setup -q

%build
install -d build
cd build
%cmake .. \
	-DDETECT_HDF5=ON \
	-DINSTALL_LIB_DIR=%{_libdir}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc LICENSE.txt README.md docs.html
%{_libdir}/libarmadillo.so.*.*.*
%ghost %{_libdir}/libarmadillo.so.15

%files devel
%defattr(644,root,root,755)
%{_libdir}/libarmadillo.so
%{_includedir}/armadillo
%{_includedir}/armadillo_bits
%{_pkgconfigdir}/armadillo.pc
%dir %{_datadir}/Armadillo
%{_datadir}/Armadillo/CMake

%files apidocs
%defattr(644,root,root,755)
%doc docs.html armadillo_*.pdf

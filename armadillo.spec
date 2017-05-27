Summary:	C++ linear algebra library
Summary(pl.UTF-8):	Biblioteka C++ do algebry liniowej
Name:		armadillo
Version:	7.900.1
Release:	1
License:	MPL v2.0
Group:		Libraries
Source0:	http://downloads.sourceforge.net/arma/%{name}-%{version}.tar.xz
# Source0-md5:	5ef71763bd429a3d481499878351f3be
URL:		http://arma.sourceforge.net/
BuildRequires:	SuperLU-devel >= 5
BuildRequires:	arpack-devel
BuildRequires:	blas-devel
BuildRequires:	cmake >= 2.8.12
BuildRequires:	hdf5-devel
BuildRequires:	lapack-devel
BuildRequires:	libstdc++-devel
BuildRequires:	pkgconfig
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
Requires:	%{name} = %{version}-%{release}
Requires:	SuperLU-devel >= 5
Requires:	arpack-devel
Requires:	blas-devel
Requires:	hdf5-devel
Requires:	lapack-devel
Requires:	libstdc++-devel
Obsoletes:	armadillo-static

%description devel
Header files for Armadillo library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki Armadillo.

%package apidocs
Summary:	Armadillo API documentation
Summary(pl.UTF-8):	Dokumentacja API biblioteki Armadillo
Group:		Documentation
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

%description apidocs
API and internal documentation for Armadillo library.

%description apidocs -l pl.UTF-8
Dokumentacja API biblioteki Armadillo.

%prep
%setup -q

%build
%cmake . \
	-DDETECT_HDF5=ON \
	-DINSTALL_LIB_DIR=%{_libdir}

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
%doc LICENSE.txt README.txt docs.html
%attr(755,root,root) %{_libdir}/libarmadillo.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libarmadillo.so.7

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libarmadillo.so
%{_includedir}/armadillo
%{_includedir}/armadillo_bits
%{_pkgconfigdir}/armadillo.pc
%dir %{_datadir}/Armadillo
%{_datadir}/Armadillo/CMake

%files apidocs
%defattr(644,root,root,755)
%doc docs.html armadillo_icon.png armadillo_nicta_2010.pdf rcpp_armadillo_csda_2014.pdf

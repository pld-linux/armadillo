Summary:	C++ linear algebra library
Summary(pl.UTF-8):	Biblioteka C++ do algebry liniowej
Name:		armadillo
Version:	3.920.2
Release:	1
License:	MPL v2.0
Group:		Libraries
Source0:	http://downloads.sourceforge.net/arma/%{name}-%{version}.tar.gz
# Source0-md5:	3d0396513e2802c08152f50e18b4a1cd
URL:		http://arma.sourceforge.net/
BuildRequires:	blas-devel
BuildRequires:	boost-devel >= 1.34
BuildRequires:	cmake >= 2.6
BuildRequires:	lapack-devel
BuildRequires:	libstdc++-devel
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
Requires:	blas-devel
Requires:	boost-devel >= 1.34
Requires:	lapack-devel
Requires:	libstdc++-devel

%description devel
Header files for Armadillo library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki Armadillo.

%package static
Summary:	Static Armadillo library
Summary(pl.UTF-8):	Statyczna biblioteka Armadillo
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static Armadillo library.

%description static -l pl.UTF-8
Statyczna biblioteka Armadillo.

%package apidocs
Summary:	Armadillo API documentation
Summary(pl.UTF-8):	Dokumentacja API biblioteki Armadillo
Group:		Documentation

%description apidocs
API and internal documentation for Armadillo library.

%description apidocs -l pl.UTF-8
Dokumentacja API biblioteki Armadillo.

%prep
%setup -q

%build
%cmake .

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
%doc LICENSE.txt README.txt
%attr(755,root,root) %{_libdir}/libarmadillo.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libarmadillo.so.3

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libarmadillo.so
%{_includedir}/armadillo
%{_includedir}/armadillo_bits
%dir %{_datadir}/Armadillo
%{_datadir}/Armadillo/CMake

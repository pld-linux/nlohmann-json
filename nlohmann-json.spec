Summary:	JSON for Modern C++ by Niels Lohmann
Summary(pl.UTF-8):	JSON dla współczesnego C++ autorstwa Nielsa Lohmanna
Name:		nlohmann-json
Version:	3.11.3
Release:	1
License:	MIT
Group:		Libraries
#Source0Download: https://github.com/nlohmann/json/releases
Source0:	https://github.com/nlohmann/json/archive/v%{version}/json-%{version}.tar.gz
# Source0-md5:	d603041cbc6051edbaa02ebb82cf0aa9
URL:		https://json.nlohmann.me/
BuildRequires:	cmake >= 3.1
BuildRequires:	libstdc++-devel >= 6:4.7
BuildRequires:	rpmbuild(macros) >= 1.605
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
JSON for Modern C++ by Niels Lohmann.

%description -l pl.UTF-8
JSON dla współczesnego C++ autorstwa Nielsa Lohmanna.

%package devel
Summary:	JSON for Modern C++ by Niels Lohmann
Summary(pl.UTF-8):	JSON dla współczesnego C++ autorstwa Nielsa Lohmanna
Group:		Development/Libraries
Requires:	libstdc++-devel >= 6:4.7

%description devel
JSON for Modern C++ by Niels Lohmann.

%description devel -l pl.UTF-8
JSON dla współczesnego C++ autorstwa Nielsa Lohmanna.

%prep
%setup -q -n json-%{version}

%build
install -d build
cd build
# force noarch libdir
%cmake .. \
	-DCMAKE_INSTALL_LIBDIR=share \
	-DJSON_MultipleHeaders=ON

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files devel
%defattr(644,root,root,755)
%doc ChangeLog.md LICENSE.MIT README.md
%dir %{_includedir}/nlohmann
%{_includedir}/nlohmann/adl_serializer.hpp
%{_includedir}/nlohmann/byte_container_with_subtype.hpp
%{_includedir}/nlohmann/json.hpp
%{_includedir}/nlohmann/json_fwd.hpp
%{_includedir}/nlohmann/ordered_map.hpp
%{_includedir}/nlohmann/detail
%{_includedir}/nlohmann/thirdparty
%{_npkgconfigdir}/nlohmann_json.pc
%{_datadir}/cmake/nlohmann_json

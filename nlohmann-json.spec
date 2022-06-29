Summary:	JSON for Modern C++ by Niels Lohmann
Summary(pl.UTF-8):	JSON dla współczesnego C++ autorstwa Nielsa Lohmanna
Name:		nlohmann-json
Version:	3.10.5
Release:	1
License:	MIT
Group:		Libraries
#Source0Download: https://github.com/nlohmann/json/releases
Source0:	https://github.com/nlohmann/json/archive/v%{version}/json-%{version}.tar.gz
# Source0-md5:	5b946f7d892fa55eabec45e76a20286b
URL:		https://json.nlohmann.me/
BuildRequires:	cmake >= 3.1
BuildRequires:	libstdc++-devel >= 6:4.7
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
%cmake ..

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
%{_includedir}/nlohmann/json.hpp
%{_pkgconfigdir}/nlohmann_json.pc
%{_libdir}/cmake/nlohmann_json

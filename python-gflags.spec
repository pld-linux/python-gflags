%define		module gflags
Summary:	Commandline flags module for Python
Summary(pl.UTF-8):	Moduł flag linii poleceń dla Pythona
Name:		python-%{module}
Version:	2.0
Release:	6
License:	BSD
Group:		Development/Languages/Python
#Source0:	https://github.com/gflags/python-gflags/archive/%{name}-%{version}.tar.gz
Source0:	http://python-gflags.googlecode.com/files/%{name}-%{version}.tar.gz
# Source0-md5:	c3ab70218dbf945cc32c0cd64c51d162
URL:		https://github.com/gflags/python-gflags
BuildRequires:	python-devel
BuildRequires:	python-distribute
BuildRequires:	rpmbuild(macros) >= 1.710
BuildRequires:	sed >= 4.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This project is the Python equivalent of google-gflags, a Google
commandline flag implementation for C++. It is intended to be used in
situations where a project wants to mimic the command-line flag
handling of a C++ app that uses google-gflags, or for a Python app
that, via swig or some other means, is linked with a C++ app that uses
google-gflags.

The gflags package contains a library that implements commandline
flags processing. As such it's a replacement for getopt(). It has
increased flexibility, including built-in support for Python types,
and the ability to define flags in the source file in which they're
used. (This last is its major difference from OptParse.)

%description -l pl.UTF-8
Ten projekt jest pythonowym odpowiednikiem google-gflags -
implementacji C++ flag linii poleceń autorstwa Google. Jego
zastosowaniem są projekty, które mają naśladować obsługę flag linii
poleceń aplikacji C++ wykorzystujących google-gflags oraz aplikacje
Pythona, które poprzez swig lub w inny sposób są zlinkowane z
aplikacją C++ wykorzystującą google-gflags.

Pakiet gflags zawiera bibliotekę implementującą przetwarzanie flag
linii poleceń. Jako taka jest zamiennikiem getopt(). Ma większą
elastyczność, w tym wbudowaną obsługę typów pythonowych oraz możliwość
definiowania flag w plikach źródłowych, w których są używane (to
ostatnie to główna różnica względem OptParse).

%prep
%setup -q
# Fix non-executable-script error
%{__sed} -i '/^#!\/usr\/bin\/env python$/,+1 d' %{module}.py

%{__sed} -i '1s,/usr/bin/env python,%{_bindir}/python2,' gflags2man.py

%build
%py_build

%install
rm -rf $RPM_BUILD_ROOT
%py_install

%py_postclean

# Remove ext from name
%{__mv} $RPM_BUILD_ROOT%{_bindir}/gflags2man{.py,}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog COPYING README
%attr(755,root,root) %{_bindir}/gflags2man
%{py_sitescriptdir}/gflags.py[co]
%{py_sitescriptdir}/gflags_validators.py[co]
%{py_sitescriptdir}/python_gflags-%{version}-py*.egg-info

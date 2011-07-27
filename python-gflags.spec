%define		module gflags
Summary:	Commandline flags module for Python
Name:		python-%{module}
Version:	1.5.1
Release:	1
License:	BSD
Group:		Development/Languages/Python
URL:		http://code.google.com/p/python-gflags/
Source0:	http://python-gflags.googlecode.com/files/python-gflags-%{version}.tar.gz
# Source0-md5:	467717cdcf65f11b3edd1cc99debb244
BuildRequires:	python-devel
BuildRequires:	python-distribute
BuildRequires:	rpmbuild(macros) >= 1.219
BuildRequires:	sed >= 4.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This project is the python equivalent of google-gflags, a Google
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

%prep
%setup -q
# Fix non-executable-script error
sed -i '/^#!\%{_prefix}\/bin\/env python$/,+1 d' %{module}.py

%build
%{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install \
	--skip-build \
	--optimize=2 \
	--root=$RPM_BUILD_ROOT

%py_postclean

# Remove ext from name
mv $RPM_BUILD_ROOT%{_bindir}/gflags2man.py  $RPM_BUILD_ROOT%{_bindir}/gflags2man

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog COPYING README
%attr(755,root,root) %{_bindir}/gflags2man
%{py_sitescriptdir}/%{module}.py[co]
%{py_sitescriptdir}/%{module}_validators.py[co]
%{py_sitescriptdir}/python_gflags-%{version}-py*.egg-info

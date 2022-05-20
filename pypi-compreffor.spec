#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-compreffor
Version  : 0.5.1.post1
Release  : 2
URL      : https://files.pythonhosted.org/packages/2a/12/c1343a811d996bed09464367e6090555d1be34af506453f3bd5af8c9f8a8/compreffor-0.5.1.post1.tar.gz
Source0  : https://files.pythonhosted.org/packages/2a/12/c1343a811d996bed09464367e6090555d1be34af506453f3bd5af8c9f8a8/compreffor-0.5.1.post1.tar.gz
Summary  : A CFF subroutinizer for fontTools.
Group    : Development/Tools
License  : Apache-2.0 BSD-2-Clause
Requires: pypi-compreffor-bin = %{version}-%{release}
Requires: pypi-compreffor-filemap = %{version}-%{release}
Requires: pypi-compreffor-lib = %{version}-%{release}
Requires: pypi-compreffor-license = %{version}-%{release}
Requires: pypi-compreffor-python = %{version}-%{release}
Requires: pypi-compreffor-python3 = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-distutils3
BuildRequires : pypi(cython)
BuildRequires : pypi(fonttools)
BuildRequires : pypi(py)
BuildRequires : pypi(setuptools)
BuildRequires : pypi(setuptools_git_ls_files)
BuildRequires : pypi(setuptools_scm)
BuildRequires : pypi(wheel)
BuildRequires : pypi-pluggy
BuildRequires : pypi-pytest
BuildRequires : pypi-tox
BuildRequires : pypi-virtualenv

%description
|CI Build Status|
A CFF table subroutinizer for FontTools.
.. |CI Build Status| image:: https://github.com/googlefonts/compreffor/workflows/Build%20+%20Deploy/badge.svg
:target: https://github.com/googlefonts/compreffor/actions?query=workflow%3A%22Build+%2B+Deploy%22

%package bin
Summary: bin components for the pypi-compreffor package.
Group: Binaries
Requires: pypi-compreffor-license = %{version}-%{release}
Requires: pypi-compreffor-filemap = %{version}-%{release}

%description bin
bin components for the pypi-compreffor package.


%package filemap
Summary: filemap components for the pypi-compreffor package.
Group: Default

%description filemap
filemap components for the pypi-compreffor package.


%package lib
Summary: lib components for the pypi-compreffor package.
Group: Libraries
Requires: pypi-compreffor-license = %{version}-%{release}
Requires: pypi-compreffor-filemap = %{version}-%{release}

%description lib
lib components for the pypi-compreffor package.


%package license
Summary: license components for the pypi-compreffor package.
Group: Default

%description license
license components for the pypi-compreffor package.


%package python
Summary: python components for the pypi-compreffor package.
Group: Default
Requires: pypi-compreffor-python3 = %{version}-%{release}

%description python
python components for the pypi-compreffor package.


%package python3
Summary: python3 components for the pypi-compreffor package.
Group: Default
Requires: pypi-compreffor-filemap = %{version}-%{release}
Requires: python3-core
Provides: pypi(compreffor)
Requires: pypi(fonttools)

%description python3
python3 components for the pypi-compreffor package.


%prep
%setup -q -n compreffor-0.5.1.post1
cd %{_builddir}/compreffor-0.5.1.post1
pushd ..
cp -a compreffor-0.5.1.post1 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1653010306
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
python3 -m build --wheel --skip-dependency-check --no-isolation
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -m build --wheel --skip-dependency-check --no-isolation

popd

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-compreffor
cp %{_builddir}/compreffor-0.5.1.post1/LICENSE %{buildroot}/usr/share/package-licenses/pypi-compreffor/2b8b815229aa8a61e483fb4ba0588b8b6c491890
cp %{_builddir}/compreffor-0.5.1.post1/src/cxx/mingw-std-threads/LICENSE %{buildroot}/usr/share/package-licenses/pypi-compreffor/dd7d2e4f4bde0bf9e83138927fc7df466377a015
pip install --root=%{buildroot} --no-deps --ignore-installed dist/*.whl
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
pip install --root=%{buildroot}-v3 --no-deps --ignore-installed dist/*.whl
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot}/usr/share/clear/optimized-elf/ %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/compreffor

%files filemap
%defattr(-,root,root,-)
/usr/share/clear/filemap/filemap-pypi-compreffor

%files lib
%defattr(-,root,root,-)
/usr/share/clear/optimized-elf/other*

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-compreffor/2b8b815229aa8a61e483fb4ba0588b8b6c491890
/usr/share/package-licenses/pypi-compreffor/dd7d2e4f4bde0bf9e83138927fc7df466377a015

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*

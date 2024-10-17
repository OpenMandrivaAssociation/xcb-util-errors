%define major 0
%define libname %mklibname xcb-util-errors %{major}
%define devname %mklibname -d xcb-util-errors

%global optflags %{optflags} -O3

Summary:	XCB errors library
Name:		xcb-util-errors
Version:	1.0.1
Release:	2
License:	MIT
Group:		Development/Libraries/C and C++
Url:		https://xcb.freedesktop.org/
Source0:	http://xcb.freedesktop.org/dist/%name-%version.tar.xz
BuildRequires:	pkgconfig(xcb) >= 1.4
BuildRequires:	pkgconfig(xcb-proto) >= 1.6
BuildRequires:	pkgconfig(xorg-macros) >= 1.6

%description
The XCB util modules provide a number of libraries which sit on top
of libxcb, the core X protocol library, and some of the extension
libraries.

Included in this package is:

- errors: utility library that gives human readable names to error
  codes and event codes and also to major and minor numbers

%package -n %{libname}
Summary: XCB errors library
Group: System/Libraries

%description -n %{libname}
The XCB util modules provide a number of libraries which sit on top
of libxcb, the core X protocol library, and some of the extension
libraries.

Included in this package is:

- errors: port of utility library that gives human readable names to error
  codes and event codes and also to major and minor numbers

%package -n %{devname}
Summary:	Development files for the XCB errors library
Group:		Development/Libraries/C and C++
Requires:	%{libname} = %{EVRD}

%description -n %{devname}
The XCB util modules provide a number of libraries which sit on top
of libxcb, the core X protocol library, and some of the extension
libraries.

This package contains the development headers for the library found
in %lname.

%prep
%autosetup -p1
%config_update

%build
./autogen.sh
%configure --disable-static
%make_build

%install
%make_install

%files -n %{libname}
%{_libdir}/libxcb-errors.so.%{major}*

%files -n %{devname}
%doc COPYING
%{_includedir}/xcb
%{_libdir}/libxcb-errors.so
%{_libdir}/pkgconfig/xcb-errors.pc
